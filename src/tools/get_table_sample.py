from langchain_core.tools import tool, StructuredTool
from src.utils import db


def create_sample_tool(engine) -> StructuredTool:
    """Create a tool for retrieving table samples.
    
    Args:
        engine: SQLAlchemy engine instance
        
    Returns:
        StructuredTool for table sampling
    """
    @tool
    def get_table_sample(table_name: str, limit: int = 5) -> str:
        """Get a sample of rows from a specific table to understand the data format and content.
        
        Args:
            table_name: Name of the table to sample
            limit: Number of rows to retrieve (default: 5, max: 100)
            
        Returns:
            Sample rows formatted as a markdown table, or error message if operation fails.
        """
        # Validate limit
        if limit < 1:
            return "Error: limit must be at least 1"
        if limit > 100:
            return "Error: limit cannot exceed 100"
            
        result, error = db.get_table_sample(engine, table_name, limit)
        if error:
            return f"Error retrieving table sample: {error}"
        return result.to_markdown(index=False)
    return get_table_sample
