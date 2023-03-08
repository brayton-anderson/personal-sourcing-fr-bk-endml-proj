import json
import jwt
import datetime
from . import db
from os import environ
from website.helper import send_forgot_password_email
from website.models import User, Verify
from flask_bcrypt import generate_password_hash
from website.utils.common import generate_response, TokenGenerator
from website.utils.utilities import Utilities
from website.validation import (
    CreateLoginInputSchema,
    CreateResetPasswordEmailSendInputSchema,
    CreateSignupInputSchema,
    ResetPasswordInputSchema,
    CreateSocialSignupInputSchema,
    CreateVerifyEmailInputSchema,
    CreateVerifyCodeInputSchema,
    UpdateVerifiedPasswordInputSchema,
)
from website.utils.http_code import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST


def create_user(request, input_data):
    create_validation_schema = CreateSignupInputSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    check_username_exist = User.query.filter_by(
        username=input_data.get("username")
    ).first()
    check_email_exist = User.query.filter_by(email=input_data.get("email")).first()
    if check_username_exist:
        return generate_response(
            message="Username already exist", status=HTTP_400_BAD_REQUEST
        )
    elif check_email_exist:
        return generate_response(
            message="Email  already taken", status=HTTP_400_BAD_REQUEST
        )
    usrn = Utilities.generate_username(name=input_data.get("name"), n=7)
    print(usrn)
    input_data["username"] = usrn
    new_user = User(**input_data)  # Create an instance of the User class
    new_user.hash_password()
    token = jwt.encode(
        {
            "id": new_user.id,
            "email": new_user.email,
            "username": new_user.username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
        },
        environ.get("SECRET_KEY"),
    )
    db.session.add(new_user)  # Adds new User record to database
    db.session.commit()  # Comment
    del input_data["password"]
    input_data["token"] = token
    return generate_response(
        data=input_data, message="User Created", status=HTTP_201_CREATED
    )


def create_social_user(request, input_data):
    create_validation_schema = CreateSocialSignupInputSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    check_username_exist = User.query.filter_by(
        username=input_data.get("username")
    ).first()
    check_email_exist = User.query.filter_by(email=input_data.get("email")).first()
    if check_username_exist:
        return generate_response(
            message="Username already exist", status=HTTP_400_BAD_REQUEST
        )
    elif check_email_exist:
        return generate_response(
            message="Email  already taken", status=HTTP_400_BAD_REQUEST
        )
    usrn = Utilities.generate_username(name=input_data.get("name"), n=7)
    print(usrn)
    input_data["username"] = usrn
    new_user = User(**input_data)  # Create an instance of the User class
    token = jwt.encode(
        {
            "id": new_user.id,
            "email": new_user.email,
            "username": new_user.username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
        },
        environ.get("SECRET_KEY"),
    )
    db.session.add(new_user)  # Adds new User record to database
    db.session.commit()  # Comment
    input_data["token"] = token
    return generate_response(
        data=input_data, message="User Created", status=HTTP_201_CREATED
    )


def login_user(request, input_data):
    create_validation_schema = CreateLoginInputSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)

    get_user = User.query.filter_by(email=input_data.get("email")).first()
    if get_user is None:
        return generate_response(message="User not found", status=HTTP_400_BAD_REQUEST)
    if get_user.check_password(input_data.get("password")):
        token = jwt.encode(
            {
                "id": get_user.id,
                "email": get_user.email,
                "username": get_user.username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            },
            environ.get("SECRET_KEY"),
        )
        input_data["token"] = token
        input_data["phone"] = get_user.phone
        input_data["username"] = get_user.username
        input_data["name"] = get_user.name
        input_data["suid"] = get_user.suid
        input_data["picture"] = get_user.picture
        input_data["tenant_id"] = get_user.tenant_id
        input_data["is_social"] = get_user.is_social
        input_data["verified"] = get_user.verified
        input_data["agreement"] = get_user.agreement
        del input_data["password"]
        return generate_response(
            data=input_data, message="User login successfully", status=HTTP_201_CREATED
        )
    else:
        return generate_response(
            message="Password is wrong", status=HTTP_400_BAD_REQUEST
        )


def verify_email_send(request, input_data):
    create_validation_schema = CreateVerifyEmailInputSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    user = User.query.filter_by(email=input_data.get("email")).first()
    if user is None:
        return generate_response(
            message="No record found with these credantials. please signup first.",
            status=HTTP_400_BAD_REQUEST,
        )
    token = TokenGenerator.encode_token(user)
    code = Utilities.generate_rand(n=7)
    input_data["token"] = token
    input_data["user_id"] = user.id
    input_data["username"] = user.username
    input_data["code"] = code
    input_data["verified"] = False
    input_data["expired"] = False
    ##delete if previous verify records exist##
    verify_data = Verify.query.filter_by(email=input_data.get("email")).first()
    if verify_data is None:
        send_forgot_password_email(
            request, user=input_data.get("email"), code=code, token=token
        )
        new_verification = Verify(**input_data)
        new_verification.hash_code()
        db.session.add(new_verification)  # Adds new User record to database
        db.session.commit()

        del input_data["expired"]
        del input_data["verified"]
        del input_data["code"]
        del input_data["username"]
        del input_data["user_id"]
        del input_data["email"]
        return generate_response(
            data=input_data,
            message="Link sent to the registered email address.",
            status=HTTP_200_OK,
        )
    else:
        db.session.delete(verify_data)
        db.session.commit()

        send_forgot_password_email(request, user=user, code=code, token=token)

        new_verification = Verify(**input_data)
        new_verification.hash_code()
        db.session.add(new_verification)  # Adds new User record to database
        db.session.commit()

        del input_data["expired"]
        del input_data["verified"]
        del input_data["code"]
        del input_data["username"]
        del input_data["user_id"]
        del input_data["email"]
        return generate_response(
            data=input_data,
            message="Link sent to the registered email address.",
            status=HTTP_200_OK,
        )


def verify_code_sent(request, input_data):
    create_validation_schema = CreateVerifyCodeInputSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    tk = input_data.get("token")
    if not tk:
        return generate_response(
            message="Token is required!",
            status=HTTP_400_BAD_REQUEST,
        )
    token = TokenGenerator.decode_token(tk)
    verify = Verify.query.filter_by(id=token.get("id")).first()
    if verify is None:
        return generate_response(
            message="No record found with these credantials. please signup first.",
            status=HTTP_400_BAD_REQUEST,
        )
    if verify.check_code(input_data.get("code")):
        expired = Utilities.compare_timestamp_data(
            dt1=verify.created_at, dt2=input_data.get("created_at")
        )
        if expired:
            db.session.delete(verify)  # Adds new User record to database
            db.session.commit()
            return generate_response(
                message="Verification period expied. please start the verification process.",
                status=HTTP_400_BAD_REQUEST,
            )
        else:
            input_data["verified"] = True
            input_data["expired"] = True
            del input_data["code"]
            del input_data["token"]
            del input_data["created_at"]
            new_verification = Verify(**input_data)
            new_verification.hash_code()

            db.session.update(new_verification)  # Adds new User record to database
            db.session.commit()
            input_data["email"] = verify.email
            input_data["user_id"] = verify.user_id
            del input_data["expired"]
            del input_data["verified"]
            return generate_response(
                data=input_data,
                message="Link sent to the registered email address.",
                status=HTTP_200_OK,
            )
    else:
        return generate_response(
            message="Verification code does not match. please start the verification process.",
            status=HTTP_400_BAD_REQUEST,
        )


def update_password_verified(request, input_data):
    create_validation_schema = UpdateVerifiedPasswordInputSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    user = User.query.filter_by(email=input_data.get("email")).first()
    if user is None:
        return generate_response(
            message="No record found with these credantials. please signup first.",
            status=HTTP_400_BAD_REQUEST,
        )
    user.hash_password()
    db.session.update(user)  # Adds new User record to database
    db.session.commit()
    token = jwt.encode(
        {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
        },
        environ.get("SECRET_KEY"),
    )
    input_data["token"] = token
    input_data["phone"] = user.phone
    input_data["username"] = user.username
    input_data["name"] = user.name
    input_data["suid"] = user.suid
    input_data["picture"] = user.picture
    input_data["tenant_id"] = user.tenant_id
    input_data["is_social"] = user.is_social
    input_data["verified"] = user.verified
    input_data["agreement"] = user.agreement
    del input_data["password"]
    return generate_response(
        data=input_data, message="Password has been updated.", status=HTTP_200_OK
    )


def reset_password_email_send(request, input_data):
    create_validation_schema = CreateResetPasswordEmailSendInputSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    user = User.query.filter_by(email=input_data.get("email")).first()
    if user is None:
        return generate_response(
            message="No record found with these credantials. please signup first.",
            status=HTTP_400_BAD_REQUEST,
        )
    send_forgot_password_email(request, user)
    return generate_response(
        message="Link sent to the registered email address.", status=HTTP_200_OK
    )


def reset_password(request, input_data, token):
    create_validation_schema = ResetPasswordInputSchema()
    errors = create_validation_schema.validate(input_data)
    if errors:
        return generate_response(message=errors)
    if not token:
        return generate_response(
            message="Token is required!",
            status=HTTP_400_BAD_REQUEST,
        )
    token = TokenGenerator.decode_token(token)
    user = User.query.filter_by(id=token.get("id")).first()
    if user is None:
        return generate_response(
            message="No record found with these credantials. please signup first.",
            status=HTTP_400_BAD_REQUEST,
        )
    user = User.query.filter_by(id=token["id"]).first()
    user.password = generate_password_hash(input_data.get("password")).decode("utf8")
    db.session.commit()
    return generate_response(
        message="New password SuccessFully set.", status=HTTP_200_OK
    )
