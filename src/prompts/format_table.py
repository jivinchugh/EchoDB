"""Prompt templates for formatting query results as tables."""
import json
from typing import Any, Dict, List


def get_table_formatting_prompt() -> Dict[str, Any]:
    """Get the prompt for formatting query results as a table."""
    return {
        "name": "format_table",
        "title": "Format Query Results as Table",
        "description": (
            "Formats database query results as a well-structured markdown table. "
            "Use this prompt to ensure data is presented in a clear, tabular format "
            "with proper alignment and headers."
        ),
        "arguments": [
            {
                "name": "query_results",
                "description": "The JSON data from execute_query containing rows of data",
                "required": True,
            },
            {
                "name": "table_title",
                "description": "Optional title for the table",
                "required": False,
            },
        ],
    }


def get_table_formatting_messages(
    query_results: Dict[str, Any],
    table_title: str | None = None,
) -> List[Dict[str, Any]]:
    """Generate prompt messages for table formatting."""
    rows = query_results.get("rows", [])
    
    if not rows:
        text_content = "No data to format. The query returned empty results."
    else:
        # Create structured instructions for table formatting
        instructions = [
            "Format the following database query results as a well-structured markdown table.",
            "",
            "Requirements:",
            "1. Create a table with proper headers (use column names from the data)",
            "2. Align columns appropriately (text left, numbers right)",
            "3. Format numbers with appropriate precision (avoid unnecessary decimals)",
            "4. Truncate very long text values appropriately",
            "5. Include a summary row if applicable (totals, averages, etc.)",
            "",
        ]
        
        if table_title:
            instructions.append(f"Table Title: {table_title}")
            instructions.append("")
        
        instructions.extend([
            "Data to format:",
            "```json",
            json.dumps(query_results, indent=2, default=str),
            "```",
            "",
            "Please format this data as a markdown table with proper alignment and formatting.",
        ])
        
        text_content = "\n".join(instructions)
    
    return [
        {
            "role": "user",
            "content": {
                "type": "text",
                "text": text_content,
            },
        }
    ]


def get_summary_table_prompt() -> Dict[str, Any]:
    """Get the prompt for creating summary tables with statistics."""
    return {
        "name": "format_summary_table",
        "title": "Format Summary Statistics Table",
        "description": (
            "Creates a summary table with statistics (counts, sums, averages, etc.) "
            "from query results. Use this for aggregated data analysis."
        ),
        "arguments": [
            {
                "name": "query_results",
                "description": "The JSON data from execute_query containing aggregated data",
                "required": True,
            },
            {
                "name": "summary_type",
                "description": "Type of summary (e.g., 'sales', 'users', 'products')",
                "required": False,
            },
        ],
    }


def get_summary_table_messages(
    query_results: Dict[str, Any],
    summary_type: str | None = None,
) -> List[Dict[str, Any]]:
    """Generate prompt messages for summary table formatting."""
    rows = query_results.get("rows", [])
    
    if not rows:
        text_content = "No data to format. The query returned empty results."
    else:
        instructions = [
            "Format the following aggregated query results as a summary statistics table.",
            "",
            "Requirements:",
            "1. Create a clear table with metric names as rows and values as columns (or vice versa)",
            "2. Highlight key metrics (totals, averages, percentages)",
            "3. Format numbers appropriately (currency, percentages, decimals)",
            "4. Add brief insights or highlights if significant patterns are present",
            "5. Include a title describing the summary",
            "",
        ]
        
        if summary_type:
            instructions.append(f"Summary Type: {summary_type}")
            instructions.append("")
        
        instructions.extend([
            "Data to format:",
            "```json",
            json.dumps(query_results, indent=2, default=str),
            "```",
            "",
            "Please format this as a summary table with proper numeric formatting and insights.",
        ])
        
        text_content = "\n".join(instructions)
    
    return [
        {
            "role": "user",
            "content": {
                "type": "text",
                "text": text_content,
            },
        }
    ]


def get_comparison_table_prompt() -> Dict[str, Any]:
    """Get the prompt for creating comparison tables."""
    return {
        "name": "format_comparison_table",
        "title": "Format Comparison Table",
        "description": (
            "Creates a comparison table showing differences between data sets, "
            "time periods, or categories. Use this for side-by-side comparisons."
        ),
        "arguments": [
            {
                "name": "query_results",
                "description": "The JSON data from execute_query containing comparison data",
                "required": True,
            },
            {
                "name": "comparison_dimension",
                "description": "What is being compared (e.g., 'time_periods', 'categories', 'regions')",
                "required": False,
            },
        ],
    }


def get_comparison_table_messages(
    query_results: Dict[str, Any],
    comparison_dimension: str | None = None,
) -> List[Dict[str, Any]]:
    """Generate prompt messages for comparison table formatting."""
    rows = query_results.get("rows", [])
    
    if not rows:
        text_content = "No data to format. The query returned empty results."
    else:
        instructions = [
            "Format the following query results as a comparison table.",
            "",
            "Requirements:",
            "1. Create a table that clearly shows comparisons between items",
            "2. Highlight differences or changes (use indicators like ↑, ↓, or % change)",
            "3. Format numbers consistently for easy comparison",
            "4. Add a column or row showing percentage changes if applicable",
            "5. Include a title describing what is being compared",
            "",
        ]
        
        if comparison_dimension:
            instructions.append(f"Comparison Dimension: {comparison_dimension}")
            instructions.append("")
        
        instructions.extend([
            "Data to format:",
            "```json",
            json.dumps(query_results, indent=2, default=str),
            "```",
            "",
            "Please format this as a comparison table with clear visual indicators of differences.",
        ])
        
        text_content = "\n".join(instructions)
    
    return [
        {
            "role": "user",
            "content": {
                "type": "text",
                "text": text_content,
            },
        }
    ]

