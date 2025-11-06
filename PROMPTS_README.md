# EchoDB MCP Prompts for Tabular Data Formatting

This document describes the MCP prompts feature integrated into EchoDB to ensure database query results are presented in a well-structured, tabular format rather than plain text.

## Overview

EchoDB now includes MCP (Model Context Protocol) prompts that guide the LLM to format query results as properly structured markdown tables. This ensures data is presented clearly and consistently, making it easier to read and understand.

## Available Prompts

### 1. `format_table`

Formats database query results as a well-structured markdown table.

**Arguments:**
- `query_results` (required): The JSON data from `execute_query` containing rows of data
- `table_title` (optional): Title for the table

**Usage Example:**
```python
# In Claude Desktop, after executing a query:
# Use prompt: format_table
# Arguments:
{
  "query_results": {"rows": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]},
  "table_title": "User List"
}
```

### 2. `format_summary_table`

Creates a summary table with statistics (counts, sums, averages, etc.) from aggregated query results.

**Arguments:**
- `query_results` (required): The JSON data from `execute_query` containing aggregated data
- `summary_type` (optional): Type of summary (e.g., 'sales', 'users', 'products')

**Usage Example:**
```python
# Use prompt: format_summary_table
# Arguments:
{
  "query_results": {"rows": [{"metric": "Total Sales", "value": 50000}]},
  "summary_type": "sales"
}
```

### 3. `format_comparison_table`

Creates a comparison table showing differences between data sets, time periods, or categories.

**Arguments:**
- `query_results` (required): The JSON data from `execute_query` containing comparison data
- `comparison_dimension` (optional): What is being compared (e.g., 'time_periods', 'categories', 'regions')

**Usage Example:**
```python
# Use prompt: format_comparison_table
# Arguments:
{
  "query_results": {"rows": [{"period": "Q1", "sales": 10000}, {"period": "Q2", "sales": 15000}]},
  "comparison_dimension": "time_periods"
}
```

## How It Works

1. **Query Execution**: Execute a database query using the `execute_query` tool
2. **Prompt Selection**: Select one of the formatting prompts based on your data type
3. **Formatting**: The prompt guides the LLM to format the raw JSON data as a markdown table
4. **Result**: You receive a beautifully formatted table with proper alignment and formatting

## Integration with Query Flow

The typical workflow:

1. User asks a question in natural language
2. Claude generates SQL and calls `execute_query()`
3. Raw JSON data is returned
4. User (or Claude) can use a formatting prompt to convert the data to a table
5. Result is displayed as a well-formatted markdown table

## Technical Details

### MCP Protocol Implementation

The prompts are implemented according to the [MCP Prompts Specification](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts):

- **Capability Declaration**: The server declares the `prompts` capability with `listChanged: true`
- **Prompt Listing**: `prompts/list` method returns all available prompts
- **Prompt Retrieval**: `prompts/get` method returns a specific prompt with arguments applied

### Prompt Message Structure

Each prompt generates messages with:
- **Role**: `user` (instructions to the LLM)
- **Content Type**: `text`
- **Content**: Structured instructions for table formatting, including:
  - Formatting requirements (alignment, number formatting, etc.)
  - The actual data to format (as JSON)
  - Specific formatting instructions based on prompt type

## Benefits

1. **Consistency**: All query results are formatted consistently
2. **Readability**: Tables are easier to read than raw JSON
3. **Professional**: Well-formatted tables look more professional
4. **Flexibility**: Different prompts for different data types (summary, comparison, etc.)
5. **User Control**: Users can explicitly choose when to format as tables

## Future Enhancements

Potential improvements:
- Additional formatting options (charts, graphs)
- Custom table styling options
- Automatic prompt selection based on data characteristics
- Export to various formats (CSV, Excel, etc.)

