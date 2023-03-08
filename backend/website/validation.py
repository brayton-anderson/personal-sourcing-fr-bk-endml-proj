from marshmallow import Schema, fields, validate


class CreateSignupInputSchema(Schema):
    username = fields.Str(required=False)
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))
    phone = fields.Str(required=False, validate=validate.Length(min=8))
    name = fields.Str(required=True)
    suid = fields.Str(required=False)
    picture = fields.Str(required=False)
    tenant_id = fields.Str(required=False)
    is_social = fields.Boolean(required=True)
    verified = fields.Boolean(required=True)
    agreement = fields.Boolean(required=True)
    userlen = fields.Number(required=True)
    created_at = fields.Number(required=True)


class CreateSocialSignupInputSchema(Schema):
    username = fields.Str(required=False)
    email = fields.Email(required=True)
    phone = fields.Str(required=False, validate=validate.Length(min=8))
    name = fields.Str(required=True)
    suid = fields.Str(required=False)
    picture = fields.Str(required=False)
    tenant_id = fields.Str(required=False)
    is_social = fields.Boolean(required=True)
    verified = fields.Boolean(required=True)
    agreement = fields.Boolean(required=True)
    userlen = fields.Number(required=True)
    created_at = fields.Number(required=True)


class CreateLoginInputSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))


class CreateVerifyCodeInputSchema(Schema):
    code = fields.Str(required=True)
    token = fields.Str(required=True)
    created_at = fields.Number(required=True)


class CreateLinkedinUserProfileDataSchema(Schema):
    name = fields.Str(required=True)
    token = fields.Str(required=True)


class CreateGoogleSearchQueryDataSchema(Schema):
    name = fields.Str(required=True)
    token = fields.Str(required=True)


class CreateGithubSearchUserProfileDataSchema(Schema):
    name = fields.Str(required=True)
    token = fields.Str(required=True)


class CreateGithubSearchUserSingleRepoDataSchema(Schema):
    name = fields.Str(required=True)
    reponame = fields.Str(required=True)
    token = fields.Str(required=True)


class CreateUpdateGoogleResultsRelevanceDataSchema(Schema):
    name = fields.Str(required=True)
    link = fields.Str(required=True)
    relevance = fields.Number(required=True)
    token = fields.Str(required=True)


class CreateVerifyEmailInputSchema(Schema):
    email = fields.Email(required=True)
    created_at = fields.Number(required=True)


class UpdateVerifiedPasswordInputSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))


class CreateResetPasswordEmailSendInputSchema(Schema):
    email = fields.Email(required=True)


class ResetPasswordInputSchema(Schema):
    password = fields.Str(required=True, validate=validate.Length(min=6))
