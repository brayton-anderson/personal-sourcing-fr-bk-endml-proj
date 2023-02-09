# Facebook API
def get_facebook_info(facebook_id):
    api_endpoint = "https://graph.facebook.com/"
    access_token = "<your_access_token>"

    # Formulate the API request
    headers = {
        "Authorization": "Bearer " + access_token,
    }
    url = api_endpoint + facebook_id + "?fields=id,name,email,birthday,location,education,work"
    response = requests.get(url, headers=headers)

    # Parse the API response
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        email = data["email"]
        birthday = data["birthday"]
        location = data["location"]["name"]
        education = data["education"][0]["school"]["name"]
        work = data["work"][0]["employer"]["name"]
        return {
            "Name": name,
            "Email": email,
            "Birthday": birthday,
            "Location": location,
            "Education": education,
            "Work": work
        }