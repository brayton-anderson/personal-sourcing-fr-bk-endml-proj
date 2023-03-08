import os
from github import Github

# Authenticate using any Github account credentials
api_data = Github(os.environ.get("LINKUSER_MAIL"), os.environ.get("LINKUSER_PASS"))


class Gitdata:
    def get_gituser_profile(name: str):
        # GET a profile
        profile = api_data.search_users(name)
        return profile

    def get_gituser_repos(name: str):
        # GET a user repositories contact info
        user = api_data.get_user(name)
        for repos in user.get_repos():
            return repos

    def get_gituser_single_repo(name: str, repo_name: str):
        # GET a single repo by repo name or id
        user = api_data.get_user(name)
        repo = user.get_repo(repo_name)
        return repo
