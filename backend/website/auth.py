from flask import Response
from flask_restful import Resource
from flask import request, make_response
from website.service import (
    create_user,
    reset_password_email_send,
    login_user,
    reset_password,
    create_social_user,
    verify_email_send,
    verify_code_sent,
    update_password_verified,
)


class SignUpApi(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = create_user(request, input_data)
        return make_response(response, status)


class SocialSignUpApi(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = create_social_user(request, input_data)
        return make_response(response, status)


class VerifyEmailApi(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = verify_email_send(request, input_data)
        return make_response(response, status)


class VerifyCodeApi(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = verify_code_sent(request, input_data)
        return make_response(response, status)


class UpdatePasswordApi(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = update_password_verified(request, input_data)
        return make_response(response, status)


class LoginApi(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = login_user(request, input_data)
        return make_response(response, status)


class ForgotPassword(Resource):
    @staticmethod
    def post() -> Response:
        input_data = request.get_json()
        response, status = reset_password_email_send(request, input_data)
        return make_response(response, status)


class ResetPassword(Resource):
    @staticmethod
    def post(token) -> Response:
        input_data = request.get_json()
        response, status = reset_password(request, input_data, token)
        return make_response(response, status)
