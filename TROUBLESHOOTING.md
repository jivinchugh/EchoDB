# Troubleshooting: Table Formatting

## Issue: Query Results Not Showing as Tables

If you're seeing query results as plain text lists instead of formatted tables, here's what's happening and how to fix it.

## Why This Happens

MCP prompts are **user-controlled** features - they're designed to be explicitly invoked by users, not automatically used by Claude. However, Claude should still format tabular data as tables automatically based on the tool description.

## Solutions

### Option 1: Automatic Formatting (Recommended)

The `execute_query` tool now includes explicit instructions in its description to format results as markdown tables. Claude should automatically format query results as tables when you run queries.

**What changed:**
- Tool description now explicitly instructs table formatting
- Response includes formatting hints
- Row count is included for better context

**Try it:**
```
echodb, help me find top 10 actors w most sales
```

Claude should now automatically format the results as a table.

### Option 2: Explicitly Use Prompts

If automatic formatting still doesn't work, you can explicitly invoke the formatting prompts:

1. **After running a query**, you can use the prompts feature:
   - Look for prompts in Claude Desktop's interface (often as slash commands like `/format_table`)
   - Or explicitly ask: "Use the format_table prompt to format those results"

2. **Available prompts:**
   - `format_table` - Basic table formatting
   - `format_summary_table` - For aggregated/summary data
   - `format_comparison_table` - For comparison data

### Option 3: Ask Claude Directly

You can also just ask Claude to format the results:
```
"Please format those results as a markdown table"
```

## Verification

To verify prompts are working:

1. Check that prompts are registered - restart Claude Desktop after code changes
2. Look for prompts in Claude Desktop's prompt menu
3. Try explicitly invoking a prompt after a query

## If Issues Persist

1. **Restart Claude Desktop** - MCP servers are loaded on startup
2. **Check MCP server logs** - Look for "Registered prompts" messages
3. **Verify MCP config** - Ensure `mcp_config.json` points to `src/main.py`
4. **Try the alternative implementation** - Use `src/main_prompts.py` if FastMCP doesn't support prompts

## Expected Behavior

When working correctly, you should see:
- Query results automatically formatted as markdown tables
- Proper column alignment (text left, numbers right)
- Appropriate number formatting (currency, decimals)
- Clear column headers

Example output:
```
| Actor Name | Total Sales | Rentals |
|------------|-------------|---------|
| GINA DEGENERES | $5,008.94 | 749 |
| MATTHEW CARREY | $4,114.84 | 676 |
...
```

