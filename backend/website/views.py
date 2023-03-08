from flask import Response
from flask_restful import Resource
from flask import request, make_response
from website.repository import (
    get_linkedin_profile_data,
    mark_ggle_results_relevant,
    run_ggle_search,
    getgithub_user_single_repo,
    getgithub_user_repos,
    getgithub_user_profile,
)


class GetLinkedInProfileData(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = get_linkedin_profile_data(request, input_data)
        return make_response(response, status)


class GetGithubProfileData(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = getgithub_user_profile(request, input_data)
        return make_response(response, status)


class GetGithubUserReposData(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = getgithub_user_repos(request, input_data)
        return make_response(response, status)


class GetGithubUserSingleRepoData(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = getgithub_user_single_repo(request, input_data)
        return make_response(response, status)


class MakeGogleSearchRequest(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = run_ggle_search(request, input_data)
        return make_response(response, status)


class UpdateGoogleSearchRelevance(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = mark_ggle_results_relevant(request, input_data)
        return make_response(response, status)
