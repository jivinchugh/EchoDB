"""Tool for executing read-only SQL queries."""
from typing import Any, Dict

from sqlalchemy import text

from src.utils.db import ensure_engine, is_select_only, rows_to_dicts


def execute_query(sql: str) -> Dict[str, Any]:
    """Execute a read-only SELECT SQL query and return rows as JSON.
    
    IMPORTANT: When presenting query results to the user, always format them as a 
    well-structured markdown table with proper alignment. Use column headers from 
    the data, align text left and numbers right, and format numbers appropriately.
    
    Security: Only SELECT statements are allowed. Multiple statements are rejected.
    """
    if not is_select_only(sql):
        return {"error": "Only single SELECT statements are allowed."}

    engine = ensure_engine()
    with engine.connect() as conn:
        # Best-effort read-only enforcement (supported DBs like Postgres)
        try:
            conn.execute(text("SET TRANSACTION READ ONLY"))
        except Exception:
            # Some dialects (e.g., SQLite) won't support this; rely on validation
            pass
        sql_to_run = sql.rstrip()
        if sql_to_run.endswith(";"):
            sql_to_run = sql_to_run[:-1].rstrip()
        result = conn.execute(text(sql_to_run))
        rows = rows_to_dicts(result)
    
    # Return results - note: always format query results as markdown tables
    # when presenting to users for better readability
    return {
        "rows": rows,
        "row_count": len(rows),
        "note": (
            "Present these results as a markdown table with column headers. "
            "Align text left, numbers right. Format currency/decimal values appropriately."
        )
    }

