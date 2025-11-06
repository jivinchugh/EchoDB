"""Utilities for formatting query results."""
from typing import Any, Dict, List


def format_rows(rows: List[Dict[str, Any]]) -> str:
    """Format rows as a markdown table if multiple rows, or plain text if single row.
    
    This function ensures consistent formatting. The AI is instructed via tool descriptions
    to preserve this format when presenting results to users.
    
    Args:
        rows: List of dictionaries representing rows
        
    Returns:
        Formatted string - markdown table for multiple rows (2+), plain text for single row
    """
    if not rows:
        return "No results found."
    
    # Single row - format as plain text
    if len(rows) == 1:
        row = rows[0]
        parts = []
        for key, value in row.items():
            # Format None as empty string
            display_value = "" if value is None else str(value)
            parts.append(f"{key}: {display_value}")
        return "\n".join(parts)
    
    # Multiple rows (2+) - format as markdown table
    
    # Get all column names from all rows (handles cases where rows have different keys)
    all_keys = set()
    for row in rows:
        all_keys.update(row.keys())
    columns = sorted(all_keys)  # Sort for consistency
    
    # Build markdown table
    lines = []
    
    # Header row
    header = "| " + " | ".join(str(col) for col in columns) + " |"
    lines.append(header)
    
    # Separator row
    separator = "| " + " | ".join("---" for _ in columns) + " |"
    lines.append(separator)
    
    # Data rows - ALL rows must be in the table
    for row in rows:
        values = []
        for col in columns:
            value = row.get(col)
            # Format None as empty string, escape pipes and newlines in values
            if value is None:
                display_value = ""
            else:
                display_value = str(value).replace("|", "\\|").replace("\n", " ").replace("\r", "")
            values.append(display_value)
        row_line = "| " + " | ".join(values) + " |"
        lines.append(row_line)
    
    return "\n".join(lines)

