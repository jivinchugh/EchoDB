# EchoDB

Natural Language Database Interface via MCP (Model Context Protocol)

## Project Structure

```
EchoDB/
├── src/
│   ├── __init__.py
│   ├── main.py                    # Main MCP server entry point
│   ├── main_prompts.py            # Alternative implementation using standard MCP server
│   │
│   ├── prompts/                   # MCP prompts for tabular data formatting
│   │   ├── __init__.py           # Module exports
│   │   ├── format_table.py       # Prompt templates (format_table, format_summary_table, format_comparison_table)
│   │   └── handlers.py           # Prompt handlers and MCP protocol integration
│   │
│   ├── tools/                     # MCP tools for database operations
│   │   ├── __init__.py
│   │   ├── connect_database.py   # Database connection tool
│   │   ├── execute_query.py      # SQL query execution tool
│   │   ├── get_schema.py         # Schema introspection tool
│   │   └── get_table_sample.py   # Table sampling tool
│   │
│   └── utils/                     # Utility functions
│       ├── __init__.py
│       └── db.py                 # Database connection and utility functions
│
├── mcp_config.json               # MCP server configuration
├── pyproject.toml                 # Project dependencies
├── README.md                     # Main project documentation
├── PROMPTS_README.md             # Prompts feature documentation
└── PROJECT_PLAN.md               # Project planning document
```

## Overview

EchoDB is an MCP server that provides natural language database querying capabilities. It exposes database operations as MCP tools that can be used by AI assistants like Claude Desktop.

### Core Components

- **`src/main.py`**: Entry point that initializes the MCP server and registers all tools
- **`src/tools/`**: Contains all MCP tools for database operations
- **`src/utils/db.py`**: Centralized database connection and utility functions

### MCP Tools

1. **`connect_database`**: Connect to a database using a SQLAlchemy URI
2. **`get_schema`**: Retrieve database schema (tables, columns, keys, indexes)
3. **`execute_query`**: Execute read-only SELECT queries
4. **`get_table_sample`**: Get sample rows from a table

### MCP Prompts

EchoDB includes MCP prompts for formatting query results as well-structured markdown tables:

1. **`format_table`**: Format query results as a markdown table with proper alignment
2. **`format_summary_table`**: Create summary tables with statistics and aggregations
3. **`format_comparison_table`**: Create comparison tables showing differences between data sets

See [PROMPTS_README.md](PROMPTS_README.md) for detailed usage instructions.

## Installation

```bash
# Install dependencies using uv
uv sync
```

## Configuration

Configure the MCP server in your Claude Desktop `mcp_config.json`:

```json
{
  "mcpServers": {
    "echodb": {
      "command": "${uvcommand}",
      "args": [
        "run",
        "--directory",
        "/path/to/EchoDB",
        "src/main.py"
      ],
      "env": {
        "DATABASE_URI": "postgresql+psycopg2://user:pass@host:port/db"
      }
    }
  }
}
```

## Usage

Once configured, you can interact with your database through Claude Desktop using natural language queries. The AI will automatically:
- Connect to your database
- Understand the schema
- Generate and execute SQL queries
- Format and present results as markdown tables

### Example Queries

```
"Show me the top 10 customers by total sales"
"What are the average prices by product category?"
"Compare sales between Q1 and Q2"
```

Results are automatically formatted as well-structured markdown tables for easy readability.

## Features

- 🔒 **Secure**: Read-only queries, SQL injection protection
- 🗄️ **Multi-Database**: Supports PostgreSQL, MySQL, SQLite
- 🤖 **AI-Powered**: Natural language query interface
- 📊 **Schema-Aware**: Automatic schema introspection
- 🔍 **Safe**: Only SELECT statements allowed
- 📋 **Table Formatting**: MCP prompts for beautiful markdown tables
- 🎨 **Flexible Presentation**: Summary tables, comparison tables, and more

## Documentation

- **[PROMPTS_README.md](PROMPTS_README.md)**: Detailed guide to table formatting prompts
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)**: Solutions for common table formatting issues
- **[PROJECT_PLAN.md](PROJECT_PLAN.md)**: Project architecture and planning
- **[CODE_ORGANIZATION.md](CODE_ORGANIZATION.md)**: Code structure and organization



