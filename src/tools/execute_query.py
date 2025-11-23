from langchain_core.tools import tool, StructuredTool
from src.utils import db


def create_query_tool(engine) -> StructuredTool:
    """Create a tool for executing read-only SQL queries.
    
    Args:
        engine: SQLAlchemy engine instance
        
    Returns:
        StructuredTool for query execution
    """
    @tool
    def execute_query(query: str) -> str:
        """Execute a read-only SQL query (SELECT only).
        
        Use this to answer questions about the data. Only SELECT statements are allowed.
        
        Args:
            query: SQL SELECT query to execute
            
        Returns:
            Query results formatted as a markdown table, or error message if query fails.
        """
        result, error = db.run_query(engine, query)
        if error:
            return f"Error executing query: {error}"
        return result.to_markdown(index=False)
    return execute_query
