from langchain_core.tools import tool, StructuredTool
from src.utils import db


def create_schema_tool(engine) -> StructuredTool:
    """Create a tool for retrieving database schema.
    
    Args:
        engine: SQLAlchemy engine instance
        
    Returns:
        StructuredTool for schema retrieval
    """
    @tool
    def get_schema() -> dict:
        """Get the database schema including tables, columns, types, primary keys, and foreign keys.
        
        Always call this first to understand the database structure before executing queries.
        
        Returns:
            Dictionary containing schema information for all tables.
        """
        return db.get_schema(engine)
    return get_schema
