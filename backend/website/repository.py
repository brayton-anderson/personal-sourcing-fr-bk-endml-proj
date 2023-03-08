from flask import jsonify
import json
import jwt
import datetime
from . import db
from os import environ
from website.insertslinkedindata import Insertsocialdata
from website.models import User
from website.googlesearchresstorage import DBStorage
from website.searchgoogleapidata.search import Searchgoogle
from website.searchgoogleapidata.filter import Filter
from website.utils.common import generate_response
from website.socialrepo.linkedindatarepo import Linkdata
from website.socialrepo.githubdatarepo import Gitdata
from website.validation import (
    CreateLinkedinUserProfileDataSchema,
    CreateGoogleSearchQueryDataSchema,
    CreateUpdateGoogleResultsRelevanceDataSchema,
    CreateGithubSearchUserProfileDataSchema,
    CreateGithubSearchUserSingleRepoDataSchema,
)
from website.utils.http_code import HTTP_200_OK, HTTP_400_BAD_REQUEST


def get_linkedin_profile_data(request, input_data):
    create_validation_schema = CreateLinkedinUserProfileDataSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    tk = input_data.get("token")
    if not tk:
        return generate_response(
            message="Token is required!",
            status=HTTP_400_BAD_REQUEST,
        )
    token = jwt.decode(tk, environ.get("SECRET_KEY"), algorithms=["HS256"])
    user = User.query.filter_by(email=token.get("email")).first()
    if user is None:
        return generate_response(
            message="No record found with these credantials. please signup first.",
            status=HTTP_400_BAD_REQUEST,
        )
    linkuser_data = Linkdata.get_the_profile(name=input_data.get("name"))
    Insertsocialdata.insert_linkedin_prof_data(
        usrid=user.id, data=linkuser_data, lname=input_data.get("name")
    )
    if len(linkuser_data["experience"]) >= 1:
        Insertsocialdata.insert_company_experience_data(
            usrid=user.id, data=linkuser_data
        )
    if len(linkuser_data["certifications"]) >= 1:
        Insertsocialdata.insert_certification_data(usrid=user.id, data=linkuser_data)
    if len(linkuser_data["education"]) >= 1:
        Insertsocialdata.insert_educational_data(usrid=user.id, data=linkuser_data)
    linkuser_data["user"] = user.name
    return generate_response(
        data=linkuser_data["experience"],
        message="Likedin profile retrved",
        status=HTTP_200_OK,
    )


def run_ggle_search(request, input_data):
    create_validation_schema = CreateGoogleSearchQueryDataSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    tk = input_data.get("token")
    if not tk:
        return generate_response(
            message="Token is required!",
            status=HTTP_400_BAD_REQUEST,
        )
    token = jwt.decode(tk, environ.get("SECRET_KEY"), algorithms=["HS256"])
    user = User.query.filter_by(email=token.get("email")).first()
    if user is None:
        return generate_response(
            message="No record found with these credantials. please signup first.",
            status=HTTP_400_BAD_REQUEST,
        )
    results = Searchgoogle.search(input_data.get("name"))
    fi = Filter(results)
    filtered = fi.filter()

    return generate_response(
        data=filtered, message="Likedin profile retrved", status=HTTP_200_OK
    )


def mark_ggle_results_relevant(request, input_data):
    create_validation_schema = CreateUpdateGoogleResultsRelevanceDataSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    tk = input_data.get("token")
    if not tk:
        return generate_response(
            message="Token is required!",
            status=HTTP_400_BAD_REQUEST,
        )
    token = jwt.decode(tk, environ.get("SECRET_KEY"), algorithms=["HS256"])
    user = User.query.filter_by(email=token.get("email")).first()
    if user is None:
        return generate_response(
            message="No record found with these credantials. please signup first.",
            status=HTTP_400_BAD_REQUEST,
        )
    DBStorage.update_relevance(
        input_data.get("name"), input_data.get("link"), input_data.get("relevance")
    )
    return generate_response(message="Update Posted", status=HTTP_200_OK)


def getgithub_user_profile(request, input_data):
    create_validation_schema = CreateGithubSearchUserProfileDataSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    tk = input_data.get("token")
    if not tk:
        return generate_response(
            message="Token is required!",
            status=HTTP_400_BAD_REQUEST,
        )
    token = jwt.decode(tk, environ.get("SECRET_KEY"), algorithms=["HS256"])
    user = User.query.filter_by(email=token.get("email")).first()
    if user is None:
        return generate_response(
            message="No record found with these credantials. please signup first.",
            status=HTTP_400_BAD_REQUEST,
        )
    gituser_profile = Gitdata.get_gituser_profile(name=input_data.get("name"))
    return generate_response(
        data=gituser_profile, message="Update Posted", status=HTTP_200_OK
    )


def getgithub_user_repos(request, input_data):
    create_validation_schema = CreateGithubSearchUserProfileDataSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    tk = input_data.get("token")
    if not tk:
        return generate_response(
            message="Token is required!",
            status=HTTP_400_BAD_REQUEST,
        )
    token = jwt.decode(tk, environ.get("SECRET_KEY"), algorithms=["HS256"])
    user = User.query.filter_by(email=token.get("email")).first()
    if user is None:
        return generate_response(
            message="No record found with these credantials. please signup first.",
            status=HTTP_400_BAD_REQUEST,
        )
    gituser_profile = Gitdata.get_gituser_repos(name=input_data.get("name"))
    return generate_response(
        data=gituser_profile, message="Update Posted", status=HTTP_200_OK
    )


def getgithub_user_single_repo(request, input_data):
    create_validation_schema = CreateGithubSearchUserSingleRepoDataSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    tk = input_data.get("token")
    if not tk:
        return generate_response(
            message="Token is required!",
            status=HTTP_400_BAD_REQUEST,
        )
    token = jwt.decode(tk, environ.get("SECRET_KEY"), algorithms=["HS256"])
    user = User.query.filter_by(email=token.get("email")).first()
    if user is None:
        return generate_response(
            message="No record found with these credantials. please signup first.",
            status=HTTP_400_BAD_REQUEST,
        )
    gituser_profile = Gitdata.get_gituser_single_repo(
        name=input_data.get("name"), repo_name=input_data.get("reponame")
    )
    return generate_response(
        data=gituser_profile, message="Update Posted", status=HTTP_200_OK
    )
