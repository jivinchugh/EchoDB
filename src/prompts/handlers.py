"""Prompt handlers for MCP server."""
import json
from typing import Any, Dict, List

from src.prompts.format_table import (
    get_comparison_table_messages,
    get_comparison_table_prompt,
    get_summary_table_messages,
    get_summary_table_prompt,
    get_table_formatting_messages,
    get_table_formatting_prompt,
)

# ============================================================================
# Prompt Registry
# ============================================================================

# Registry of all available prompts
_PROMPTS = {
    "format_table": get_table_formatting_prompt,
    "format_summary_table": get_summary_table_prompt,
    "format_comparison_table": get_comparison_table_prompt,
}

# Message generators for each prompt
_MESSAGE_GENERATORS = {
    "format_table": get_table_formatting_messages,
    "format_summary_table": get_summary_table_messages,
    "format_comparison_table": get_comparison_table_messages,
}

# ============================================================================
# Public API
# ============================================================================

def list_prompts() -> List[Dict[str, Any]]:
    """List all available prompts."""
    prompts = []
    for name, prompt_func in _PROMPTS.items():
        prompt_def = prompt_func()
        # Convert to dict format expected by MCP
        prompt_dict = {
            "name": prompt_def["name"],
            "title": prompt_def.get("title", ""),
            "description": prompt_def.get("description", ""),
            "arguments": [
                {
                    "name": arg["name"],
                    "description": arg["description"],
                    "required": arg.get("required", False),
                }
                for arg in prompt_def.get("arguments", [])
            ],
        }
        prompts.append(prompt_dict)
    return prompts


def get_prompt(name: str, arguments: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """Get a specific prompt with arguments applied.
    
    Args:
        name: The name of the prompt to retrieve
        arguments: Optional dictionary of arguments to pass to the prompt
        
    Returns:
        Dictionary containing the prompt description and messages
        
    Raises:
        ValueError: If prompt name is invalid or required arguments are missing
    """
    if name not in _PROMPTS:
        raise ValueError(f"Prompt '{name}' not found. Available prompts: {list(_PROMPTS.keys())}")
    
    if arguments is None:
        arguments = {}
    
    # Get the message generator for this prompt
    message_generator = _MESSAGE_GENERATORS.get(name)
    if not message_generator:
        raise ValueError(f"Message generator for prompt '{name}' not found")
    
    # Generate messages based on prompt type and arguments
    if name == "format_table":
        query_results = arguments.get("query_results")
        if query_results is None:
            raise ValueError("'query_results' argument is required for format_table prompt")
        # Parse JSON string if needed
        if isinstance(query_results, str):
            query_results = json.loads(query_results)
        table_title = arguments.get("table_title")
        messages = message_generator(query_results, table_title)
    
    elif name == "format_summary_table":
        query_results = arguments.get("query_results")
        if query_results is None:
            raise ValueError("'query_results' argument is required for format_summary_table prompt")
        # Parse JSON string if needed
        if isinstance(query_results, str):
            query_results = json.loads(query_results)
        summary_type = arguments.get("summary_type")
        messages = message_generator(query_results, summary_type)
    
    elif name == "format_comparison_table":
        query_results = arguments.get("query_results")
        if query_results is None:
            raise ValueError("'query_results' argument is required for format_comparison_table prompt")
        # Parse JSON string if needed
        if isinstance(query_results, str):
            query_results = json.loads(query_results)
        comparison_dimension = arguments.get("comparison_dimension")
        messages = message_generator(query_results, comparison_dimension)
    
    else:
        raise ValueError(f"Unknown prompt type: {name}")
    
    # Convert messages to dict format
    prompt_def = _PROMPTS[name]()
    result = {
        "description": prompt_def.get("description", ""),
        "messages": [
            {
                "role": msg["role"],
                "content": {
                    "type": msg["content"]["type"],
                    "text": msg["content"]["text"],
                },
            }
            for msg in messages
        ],
    }
    return result


# ============================================================================
# MCP Protocol Handlers
# ============================================================================

def list_prompts_handler(cursor: str | None = None) -> Dict[str, Any]:
    """MCP handler for listing prompts.
    
    MCP method: prompts/list
    """
    prompts = list_prompts()
    return {
        "prompts": prompts,
        "nextCursor": None,  # No pagination for now
    }


def get_prompt_handler(name: str, arguments: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """MCP handler for getting a specific prompt.
    
    MCP method: prompts/get
    """
    try:
        return get_prompt(name, arguments or {})
    except ValueError as e:
        raise ValueError(f"Invalid prompt request: {e}")
    except Exception as e:
        import logging
        logger = logging.getLogger("echodb")
        logger.error(f"Error getting prompt {name}: {e}", exc_info=True)
        raise

