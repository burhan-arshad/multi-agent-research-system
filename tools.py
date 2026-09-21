from langchain.tools import tool 
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os 
from dotenv import load_dotenv
from rich import print
load_dotenv()

tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def fetch_news(query: str) -> str:
    """
    A tool that is use to get Recent news from Tavily API.
    """
    result=tavily.search(query=query, max_results=3)
    out=[]
    for r in result['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nsnippet: {r['content'][:100]}\n"
        )

    return "\n----------------------------------------------\n".join(out)


@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"