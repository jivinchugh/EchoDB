"""Tool for connecting to a database."""
from typing import Any, Dict

from src.utils.db import ensure_engine


def connect_database() -> Dict[str, Any]:
    """
    Connect to a database using the provided SQLAlchemy URI.
    """
    engine = ensure_engine()
    # Test connection
    with engine.connect() as conn:
        conn.exec_driver_sql("SELECT 1")
  
    return {"status": "connected"}

