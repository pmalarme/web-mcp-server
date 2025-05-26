# server.py
from mcp.server.fastmcp import FastMCP
from markitdown import MarkItDown
from dotenv import load_dotenv
import os
import requests

load_dotenv()

google_seach_api_key = os.getenv("GOOGLE_SEARCH_API_KEY")
google_search_api_cse_id = os.getenv("GOOGLE_SEARCH_API_CSE_ID")
google_search_url = "https://www.googleapis.com/customsearch/v1"

# Create an MCP server
mcp = FastMCP("Website Content Fetcher")
# mcp = FastMCP("Website Content Fetcher", port=3000)

@mcp.tool()
def get_website_content(website_url: str) -> str:
    """Get a website content for a given URL
    
    Args:
        website_url (str): The URL of the website to fetch content from.
    """
    md = MarkItDown()
    result = md.convert(website_url)
    return result
    # return f"Website content for {website_url}"

@mcp.tool()
def google_search(query: str, num_results: int = 5) -> str:
    """Perform a Google search for a given query and return the results.
    
    Args:
        query (str): The search query.
        num_results (int): The number of results to return.
    """
    params = {
        "key": google_seach_api_key,
        "cx": google_search_api_cse_id,
        "q": query,
        "num": num_results
    }
    response = requests.get(google_search_url, params=params)
    data = response.json()
    return data.get("items", [])

@mcp.tool()
def get_contents(query: str, num_results: int = 5) -> str:
    """Get the content of each website for a given query to Google Search.
    
    Args:
        query (str): The search query.
        num_results (int): The number of results to return.
    """
    search_results = google_search(query, num_results)
    if not search_results:
        return []
    
    for search_result in search_results:
        website_url = search_result.get("link")
        if website_url:
            content = get_website_content(website_url)
            search_result["content"] = content
            
    return search_results

# if __name__ == "__main__":
#     mcp.run(transport='sse')