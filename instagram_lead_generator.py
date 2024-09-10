import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Tavily API key
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def search_instagram_accounts(location, niche):
    url = "https://api.tavily.com/search"
    headers = {
        "content-type": "application/json"
    }
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": f"Instagram accounts in {location} for {niche}",
        "search_depth": "advanced",
        "include_domains": ["instagram.com"],
        "max_results": 10
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Request failed: {e}")
        return None

def parse_results(results):
    parsed_results = []
    if results and "results" in results:
        for result in results["results"]:
            parsed_results.append({
                "title": result.get("title", ""),
                "url": result.get("url", ""),
                "snippet": result.get("content", "")
            })
    return parsed_results
