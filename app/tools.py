from smolagents import tool, Tool
from duckduckgo_search import DDGS
import requests
from markdownify import markdownify
import re

@tool
def web_search(query: str) -> str:
    """Search the web using DuckDuckGo.
    
    Args:
        query (str): The search query.
    
    Returns:
        str: The top search results as a formatted string.
    """
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=5))
        return str(results)
class VisitWebpageTool(Tool):
    name = "visit_webpage"
    description = "Reads webpage content from a given URL and returns markdown text."

    inputs = {
        "url": {
            "type": "string",
            "description": "Full webpage URL to visit"
        }
    }

    output_type = "string"

    def forward(self, url: str) -> str:
        try:
            response = requests.get(url, timeout=20)
            response.raise_for_status()

            markdown_content = markdownify(response.text)
            markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)

            return markdown_content[:40000]

        except Exception as e:
            return str(e)