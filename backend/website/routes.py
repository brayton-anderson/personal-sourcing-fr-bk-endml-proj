from flask_restful import Api
from website.auth import (
    LoginApi,
    ForgotPassword,
    SignUpApi,
    ResetPassword,
    SocialSignUpApi,
    VerifyCodeApi,
    VerifyEmailApi,
    UpdatePasswordApi,
)
from website.views import (
    GetLinkedInProfileData,
    UpdateGoogleSearchRelevance,
    MakeGogleSearchRequest,
    GetGithubUserSingleRepoData,
    GetGithubUserReposData,
    GetGithubProfileData,
)


def create_authentication_routes(api: Api):
    api.add_resource(SignUpApi, "/api/auth/register/")
    api.add_resource(SocialSignUpApi, "/api/auth/register-social/")
    api.add_resource(LoginApi, "/api/auth/login/")
    api.add_resource(UpdatePasswordApi, "/api/auth/update-password/")
    api.add_resource(ForgotPassword, "/api/auth/forgot-password/")
    api.add_resource(ResetPassword, "/api/auth/reset-password/<token>")
    api.add_resource(VerifyEmailApi, "/api/auth/verify-email/")
    api.add_resource(VerifyCodeApi, "/api/auth/verify-code/")


def create_view_routes(api: Api):
    api.add_resource(GetLinkedInProfileData, "/api/views/linkeduser-profile/")
    api.add_resource(GetGithubProfileData, "/api/views/gituser-profile/")
    api.add_resource(GetGithubUserReposData, "/api/views/gituser-repos/")
    api.add_resource(GetGithubUserSingleRepoData, "/api/views/gituser-single-repo/")
    api.add_resource(UpdateGoogleSearchRelevance, "/api/views/update-relevace/")
    api.add_resource(MakeGogleSearchRequest, "/api/views/search-web/")
