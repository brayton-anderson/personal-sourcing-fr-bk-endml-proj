import requests
import json

# GitHub API
def get_github_info(username):
    api_endpoint = "https://api.github.com/users/"
    access_token = "<your_access_token>"

    headers = {
        "Authorization": "Token " + access_token,
        "Accept": "application/vnd.github+json",
    }
    url = api_endpoint + username
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        username = data["login"]
        location = data["location"]
        email = data["email"]
        bio = data["bio"]
        followers = data["followers"]
        following = data["following"]
        created_at = data["created_at"]
        return {
            "Name": name,
            "Username": username,
            "Location": location,
            "Email": email,
            "Bio": bio,
            "Followers": followers,
            "Following": following,
            "Created at": created_at
        }