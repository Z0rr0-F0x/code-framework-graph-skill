#!/usr/bin/env python3
"""Graph JSON to Mermaid converter.

This script converts a JSON graph structure to Mermaid diagram syntax.

Usage:
    python graph_to_mermaid.py input.json > output.mmd
    python graph_to_mermaid.py input.json --output output.mmd
"""

import json
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from enum import Enum


class GraphLevel(str, Enum):
    HIGH_LEVEL = "high"
    MODULE_LEVEL = "module"
    DETAILED_LEVEL = "detailed"


class RelationshipType(str, Enum):
    IMPORT = "import"
    INHERITANCE = "inheritance"
    COMPOSITION = "composition"
    REFERENCE = "reference"
    CALL = "call"
    IMPLEMENTATION = "implementation"


def sanitize_id(id_str: str) -> str:
    """Convert string to valid Mermaid ID."""
    return "N" + "".join(c if c.isalnum() else "_" for c in id_str)


def get_edge_label(edge: Dict[str, Any]) -> str:
    """Generate label for an edge with semantic information."""
    metadata = edge.get("metadata", {})
    semantics = metadata.get("semantics", {})
    
    parts = []
    
    # Business description has highest priority
    if semantics.get("business_description"):
        label = semantics["business_description"]
        if semantics.get("call_type") == "async":
            label += " (async)"
        return label
    
    # Build combined label
    if semantics.get("is_data_flow"):
        parts.append("data")
    if semantics.get("is_control_flow"):
        parts.append("control")
    if semantics.get("call_type") == "async":
        parts.append("async")
    if semantics.get("direction") == "bidirectional":
        parts.append("bidirectional")
    
    relationship = semantics.get("relationship_type", edge.get("type", ""))
    
    if parts:
        combined = " ".join(parts)
        return f"{combined} {relationship}" if relationship else combined
    
    return edge.get("type", "relates")


def subgraph_to_mermaid(subgraph: Dict[str, Any], indent: int = 0) -> List[str]:
    """Convert a subgraph to Mermaid syntax lines."""
    lines = []
    indent_str = "    " * indent
    
    # Subgraph header
    label = subgraph.get("label", subgraph.get("id", "unnamed"))
    lines.append(f'{indent_str}subgraph "{label}"')
    
    # Add nodes
    for node in subgraph.get("nodes", []):
        node_id = sanitize_id(node["id"])
        node_label = node.get("label", node["id"]).replace('"', '\\"')
        lines.append(f'{indent_str}    {node_id}["{node_label}"]')
    
    # Add nested subgraphs
    for child in subgraph.get("children", []):
        lines.extend(subgraph_to_mermaid(child, indent + 1))
    
    # Close subgraph
    lines.append(f'{indent_str}end')
    
    # Add internal edges
    for edge in subgraph.get("edges", []):
        source_id = sanitize_id(edge["source"])
        target_id = sanitize_id(edge["target"])
        label = get_edge_label(edge)
        lines.append(f'{indent_str}    {source_id} -->|{label}| {target_id}')
    
    return lines


def graph_to_mermaid(graph: Dict[str, Any], level: str = "high") -> str:
    """Convert full graph structure to Mermaid diagram."""
    lines = ["graph TD"]
    
    # Render high-level view
    high_level = graph.get("high_level", {})
    
    # Render top-level nodes (not in subgraphs)
    for node in high_level.get("nodes", []):
        node_id = sanitize_id(node["id"])
        node_label = node.get("label", node["id"]).replace('"', '\\"')
        lines.append(f'    {node_id}["{node_label}"]')
    
    # Render subgraphs (children)
    for child in high_level.get("children", []):
        lines.extend(subgraph_to_mermaid(child, 1))
    
    # Render all edges from edge_index if present
    edge_index = graph.get("edge_index", [])
    if not edge_index:
        # Try to get edges from metadata or high_level
        edge_index = graph.get("metadata", {}).get("edges", [])
    
    for edge in edge_index:
        source_id = sanitize_id(edge["source"])
        target_id = sanitize_id(edge["target"])
        label = get_edge_label(edge)
        lines.append(f"    {source_id} -->|{label}| {target_id}")
    
    return "\n".join(lines)


def validate_graph(graph: Dict[str, Any]) -> List[str]:
    """Validate graph structure and return list of issues."""
    issues = []
    
    # Check required fields
    if "high_level" not in graph:
        issues.append("Missing 'high_level' field")
        return issues
    
    high_level = graph["high_level"]
    
    # Validate nodes
    node_ids = set()
    for node in high_level.get("nodes", []):
        if "id" not in node:
            issues.append(f"Node missing 'id': {node}")
        else:
            node_ids.add(node["id"])
    
    # Validate subgraph nodes
    def check_subgraph(subgraph: Dict[str, Any], path: str = ""):
        sg_id = subgraph.get("id", "unnamed")
        current_path = f"{path}/{sg_id}" if path else sg_id
        
        for node in subgraph.get("nodes", []):
            if "id" not in node:
                issues.append(f"Node in {current_path} missing 'id'")
            else:
                node_ids.add(node["id"])
        
        for child in subgraph.get("children", []):
            check_subgraph(child, current_path)
    
    for child in high_level.get("children", []):
        check_subgraph(child)
    
    # Validate edges reference existing nodes
    for edge in graph.get("edge_index", []):
        source = edge.get("source")
        target = edge.get("target")
        
        if source and source not in node_ids:
            issues.append(f"Edge source '{source}' not found in nodes")
        if target and target not in node_ids:
            issues.append(f"Edge target '{target}' not found in nodes")
        if "type" not in edge:
            issues.append(f"Edge {source} -> {target} missing 'type'")
    
    return issues


def main():
    parser = argparse.ArgumentParser(
        description="Convert graph JSON to Mermaid diagram"
    )
    parser.add_argument("input", help="Input JSON file path")
    parser.add_argument("--output", "-o", help="Output file path (default: stdout)")
    parser.add_argument(
        "--level", "-l",
        choices=["high", "module", "detailed"],
        default="high",
        help="Graph detail level (default: high)"
    )
    parser.add_argument(
        "--validate", "-v",
        action="store_true",
        help="Only validate input, don't convert"
    )
    
    args = parser.parse_args()
    
    # Read input
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)
    
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            graph = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Validate
    issues = validate_graph(graph)
    if issues:
        print("Validation issues:", file=sys.stderr)
        for issue in issues:
            print(f"  - {issue}", file=sys.stderr)
        if args.validate:
            sys.exit(1 if issues else 0)
    
    if args.validate:
        print("Validation passed!", file=sys.stderr)
        sys.exit(0)
    
    # Convert
    mermaid = graph_to_mermaid(graph, args.level)
    
    # Output
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(mermaid)
        print(f"Mermaid diagram written to: {args.output}", file=sys.stderr)
    else:
        print(mermaid)


if __name__ == "__main__":
    main()
