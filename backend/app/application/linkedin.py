import requests
import json

# Google Search API
def get_google_search_info(query):
    
    api_endpoint = "https://www.googleapis.com/customsearch/v1"
    access_token = "<your_access_token>"
    cx = "<your_cx>"
    
    headers = {
        "Authorization": "Bearer " + access_token,
    }
    params = {
        "q": query,
        "cx": cx,
        "num": 10,
    }
    response = requests.get(api_endpoint, headers=headers, params=params)

    # Parse the API response
    if response.status_code == 200:
        data = response.json()
        items = data["items"]
        search_results = []
        for item in items:
            title = item["title"]
            link = item["link"]
            snippet = item["snippet"]
            search_results.append({
                "Title": title,
                "Link": link,
                "Snippet": snippet,
            })
        return search_results
