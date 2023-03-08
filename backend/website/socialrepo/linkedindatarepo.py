import os
from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
api_data = Linkedin(os.environ.get("LINKUSER_MAIL"), os.environ.get("LINKUSER_PASS"))


class Linkdata:
    def get_the_profile(name: str):
        # GET a profile
        profile = api_data.get_profile(name)
        return profile

    def get_the_contact_info(name: str):
        # GET a profiles contact info
        contact_info = api_data.get_profile_contact_info(name)
        return contact_info

    def get_the_connections(name: str):
        # GET 1st degree connections of a given profile
        connections = api_data.get_profile_connections(name)
        return connections

    def get_the_school(name: str):
        schools = api_data.get_school(name)
        return schools
