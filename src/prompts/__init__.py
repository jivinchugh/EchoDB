"""MCP prompts for tabular data formatting.

This module provides prompt templates and handlers for formatting database
query results as well-structured markdown tables.
"""

from src.prompts.handlers import (
    get_prompt,
    get_prompt_handler,
    list_prompts,
    list_prompts_handler,
)

__all__ = [
    "get_prompt",
    "get_prompt_handler",
    "list_prompts",
    "list_prompts_handler",
]
