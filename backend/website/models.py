import datetime
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from . import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    phone = db.Column(db.String(25), nullable=True)
    name = db.Column(db.String(50))
    suid = db.Column(db.String(50), unique=True)
    picture = db.Column(db.String(50))
    tenant_id = db.Column(db.String(150))
    is_social = db.Column(db.Boolean)
    verified = db.Column(db.Boolean)
    agreement = db.Column(db.Boolean)
    userlen = db.Column(db.Integer)
    created_at = db.Column(db.Integer)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    profiles = db.relationship("Profile", backref="users", passive_deletes=True)
    verify = db.relationship("Verify", backref="users", passive_deletes=True)
    experiences = db.relationship("Experience", backref="users", passive_deletes=True)
    earningroles = db.relationship("Earningrole", backref="users", passive_deletes=True)
    userskills = db.relationship("Userskill", backref="users", passive_deletes=True)
    usereducations = db.relationship(
        "Usereducation", backref="users", passive_deletes=True
    )
    userprojects = db.relationship("Userproject", backref="users", passive_deletes=True)
    cirtificatons = db.relationship(
        "Cirtificaton", backref="users", passive_deletes=True
    )
    companiesworked = db.relationship(
        "Companyworked", backref="users", passive_deletes=True
    )
    userawards = db.relationship("Useraward", backref="users", passive_deletes=True)
    availabilities = db.relationship(
        "Availability", backref="users", passive_deletes=True
    )
    comments = db.relationship("Comment", backref="users", passive_deletes=True)
    likes = db.relationship("Like", backref="users", passive_deletes=True)

    def __init__(self, **kwargs):
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")
        self.phone = kwargs.get("phone")
        self.name = kwargs.get("name")
        self.suid = kwargs.get("suid")
        self.picture = kwargs.get("picture")
        self.tenant_id = kwargs.get("tenant_id")
        self.is_social = kwargs.get("is_social")
        self.verified = kwargs.get("verified")
        self.agreement = kwargs.get("agreement")
        self.userlen = kwargs.get("userlen")
        self.created_at = kwargs.get("created_at")

    def __repr__(self):
        return "<User {}>".format(self.username)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Verify(db.Model):
    __tablename__ = "verifyer"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(80))
    user_id = db.Column(db.Integer)
    code = db.Column(db.String(7))
    token = db.Column(db.String(150))
    verified = db.Column(db.Boolean)
    expired = db.Column(db.Boolean)
    created_at = db.Column(db.Integer)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    owner = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.code = kwargs.get("code")
        self.token = kwargs.get("token")
        self.verified = kwargs.get("verified")
        self.created_at = kwargs.get("created_at")
        self.expired = kwargs.get("expired")

    def __repr__(self):
        return "<Verify {}>".format(self.username)

    def hash_code(self):
        self.code = generate_password_hash(self.code).decode("utf8")

    def check_code(self, code):
        return check_password_hash(self.code, code)


class Profile(db.Model):
    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    profile_picture = db.Column(db.String(150))
    profile_summary = db.Column(db.Text, nullable=False)
    linked_fname = db.Column(db.String(20))
    linked_lname = db.Column(db.String(20))
    geo_country_name = db.Column(db.String(20))
    linked_headline = db.Column(db.String(20))
    location_name = db.Column(db.String(20))
    street_name = db.Column(db.String(90))
    state_name = db.Column(db.String(20))
    address_name = db.Column(db.String(20))
    county_name = db.Column(db.String(20))
    linked_profile_name = db.Column(db.String(20))
    is_student = db.Column(db.Boolean)
    is_developer = db.Column(db.Boolean)
    gender = db.Column(db.String(20))
    github_profile = db.Column(db.String(150))
    linkedin_profile = db.Column(db.String(150))
    facebook_profile = db.Column(db.String(150))
    twitter_profile = db.Column(db.String(150))
    app_theme = db.Column(db.String(10))
    country = db.Column(db.String(30))
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    owner = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    comments = db.relationship("Comment", backref="profiles", passive_deletes=True)
    likes = db.relationship("Like", backref="profiles", passive_deletes=True)

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.profile_picture = kwargs.get("profile_picture")
        self.profile_summary = kwargs.get("profile_summary")
        self.linked_fname = kwargs.get("linked_fname")
        self.linked_lname = kwargs.get("linked_lname")
        self.geo_country_name = kwargs.get("geo_country_name")
        self.linked_headline = kwargs.get("linked_headline")
        self.location_name = kwargs.get("location_name")
        self.street_name = kwargs.get("street_name")
        self.state_name = kwargs.get("state_name")
        self.address_name = kwargs.get("address_name")
        self.county_name = kwargs.get("county_name")
        self.linked_profile_name = kwargs.get("linked_profile_name")
        self.is_student = kwargs.get("is_student")
        self.is_developer = kwargs.get("is_developer")
        self.gender = kwargs.get("gender")
        self.github_profile = kwargs.get("github_profile")
        self.linkedin_profile = kwargs.get("linkedin_profile")
        self.facebook_profile = kwargs.get("facebook_profile")
        self.twitter_profile = kwargs.get("twitter_profile")
        self.app_theme = kwargs.get("app_theme")
        self.country = kwargs.get("country")
        self.owner = kwargs.get("owner")

    def __repr__(self):
        return "<Profile %r>" % self.id


class Experience(db.Model):
    __tablename__ = "experiences"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    years_experienced = db.Column(db.Integer)
    years_remote_experienced = db.Column(db.Integer)
    lannguage_pro = db.Column(db.Integer)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    owner = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )


class Userproject(db.Model):
    __tablename__ = "userprojects"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    proj_name = db.Column(db.String(80))
    proj_type = db.Column(db.String(80))
    proj_summary = db.Column(db.Text, nullable=False)
    proj_stars = db.Column(db.Integer)
    proj_forked = db.Column(db.String(80))
    proj_link = db.Column(db.String(180))
    proj_grade = db.Column(db.Integer)
    proj_marks = db.Column(db.Integer)
    is_proj_cheked = db.Column(db.Boolean)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    owner = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    comments = db.relationship("Comment", backref="userprojects", passive_deletes=True)
    likes = db.relationship("Like", backref="userprojects", passive_deletes=True)


class Availability(db.Model):
    __tablename__ = "availabilities"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    avail_state = db.Column(db.Integer)
    work_hours = db.Column(db.Integer)
    notice_period = db.Column(db.Integer)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    owner = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )


class Googlesearchresl(db.Model):
    __tablename__ = "googlesearchreslts"
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(200))
    rank = db.Column(db.Integer)
    link = db.Column(db.String(200))
    title = db.Column(db.String(200))
    snippet = db.Column(db.Text)
    html = db.Column(db.Text)
    relevance = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )

    def __init__(self, **kwargs):
        self.query = (kwargs.get("query"),)
        self.rank = (kwargs.get("rank"),)
        self.link = (kwargs.get("link"),)
        self.title = (kwargs.get("title"),)
        self.snippet = (kwargs.get("snippet"),)
        self.html = (kwargs.get("html"),)
        self.relevance = (kwargs.get("relevance"),)
        self.created = (kwargs.get("created"),)

    def __repr__(self):
        return "<Googlesearchresl %r>" % self.id


class Cirtificaton(db.Model):
    __tablename__ = "cirtificatons"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    active = db.Column(db.Boolean)
    dash_company_urn = db.Column(db.String(200))
    entity_urn = db.Column(db.String(200))
    logo = db.Column(db.String(200))
    name = db.Column(db.String(200))
    object_urn = db.Column(db.String(200))
    showcase = db.Column(db.String(200))
    tracking_id = db.Column(db.String(200))
    universal_name = db.Column(db.String(200))
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    cirtxperiences = db.relationship("Cirtexperience", back_populates="cirtificaton")
    owner = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.active = kwargs.get("active")
        self.dash_company_urn = kwargs.get("dash_company_urn")
        self.entity_urn = kwargs.get("entity_urn")
        self.logo = kwargs.get("logo")
        self.name = kwargs.get("name")
        self.object_urn = kwargs.get("object_urn")
        self.showcase = kwargs.get("showcase")
        self.tracking_id = kwargs.get("tracking_id")
        self.universal_name = kwargs.get("universal_name")
        self.experiences = kwargs.get("experiences")
        self.owner = kwargs.get("owner")

    def __repr__(self):
        return "<Cirtificaton %r>" % self.id


class Cirtexperience(db.Model):
    __tablename__ = "cirtxperiences"

    id = db.Column(db.Integer, primary_key=True)
    authority = db.Column(db.String(200))
    company_urn = db.Column(db.String(200), db.ForeignKey("cirtificatons.entity_urn"))
    name = db.Column(db.String(200))
    start_month = db.Column(db.Integer)
    start_year = db.Column(db.Integer)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    cirtificaton = db.relationship("Cirtificaton", back_populates="cirtxperiences")

    def __init__(self, **kwargs):
        self.authority = kwargs.get("authority")
        self.company_urn = kwargs.get("company_urn")
        self.name = kwargs.get("name")
        self.start_month = kwargs.get("start_month")
        self.start_year = kwargs.get("start_year")
        self.company = kwargs.get("company")

    def __repr__(self):
        return "<Cirtexperience %r>" % self.id


class Companyworked(db.Model):
    __tablename__ = "companiesworked"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    industries = db.Column(db.String(200))
    company_name = db.Column(db.String(200))
    description = db.Column(db.Text)
    entity_urn = db.Column(db.String(200))
    geo_location_name = db.Column(db.String(200))
    geo_urn = db.Column(db.String(200))
    location_name = db.Column(db.String(200))
    company_region = db.Column(db.String(200))
    title = db.Column(db.String(200))
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    companyexperiences = db.relationship(
        "Companyexperience", back_populates="companyworked"
    )
    owner = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.industries = kwargs.get("industries")
        self.company_name = kwargs.get("company_name")
        self.description = kwargs.get("description")
        self.entity_urn = kwargs.get("entity_urn")
        self.geo_location_name = kwargs.get("geo_location_name")
        self.geo_urn = kwargs.get("geo_urn")
        self.location_name = kwargs.get("location_name")
        self.company_region = kwargs.get("company_region")
        self.title = kwargs.get("title")
        self.owner = kwargs.get("owner")

    def __repr__(self):
        return "<Companyworked %r>" % self.id


class Companyexperience(db.Model):
    __tablename__ = "companyexperiences"

    id = db.Column(db.Integer, primary_key=True)
    company_urn = db.Column(db.String(200), db.ForeignKey("companiesworked.entity_urn"))
    company_name = db.Column(db.String(200))
    company_region = db.Column(db.String(200))
    start_month = db.Column(db.Integer)
    start_year = db.Column(db.Integer)
    end_month = db.Column(db.Integer)
    end_year = db.Column(db.Integer)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    companyworked = db.relationship(
        "Companyworked", back_populates="companyexperiences"
    )

    def __init__(self, **kwargs):
        self.company_name = kwargs.get("company_name")
        self.company_urn = kwargs.get("company_urn")
        self.company_region = kwargs.get("company_region")
        self.start_month = kwargs.get("start_month")
        self.start_year = kwargs.get("start_year")
        self.end_month = kwargs.get("end_month")
        self.end_year = kwargs.get("end_year")

    def __repr__(self):
        return "<Companyexperience %r>" % self.id


class Usereducation(db.Model):
    __tablename__ = "usereducations"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    degree_name = db.Column(db.String(255))
    entity_urn = db.Column(db.String(255))
    field_of_study = db.Column(db.String(255))
    field_of_study_urn = db.Column(db.String(255))
    field_of_study_id = db.Column(db.Integer)
    school_name = db.Column(db.String(255))
    school_urn = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    logo_url = db.Column(db.String(255))
    object_urn = db.Column(db.String(255))
    tracking_id = db.Column(db.String(255))
    start_month = db.Column(db.Integer)
    start_year = db.Column(db.Integer)
    end_month = db.Column(db.Integer)
    end_year = db.Column(db.Integer)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    owner = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.degree_name = kwargs.get("degree_name")
        self.entity_urn = kwargs.get("entity_urn")
        self.field_of_study = kwargs.get("field_of_study")
        self.field_of_study_urn = kwargs.get("field_of_study_urn")
        self.field_of_study_id = kwargs.get("field_of_study_id")
        self.school_name = kwargs.get("school_name")
        self.school_urn = kwargs.get("school_urn")
        self.active = kwargs.get("active")
        self.logo_url = kwargs.get("logo_url")
        self.object_urn = kwargs.get("object_urn")
        self.tracking_id = kwargs.get("tracking_id")
        self.start_month = kwargs.get("start_month")
        self.start_year = kwargs.get("start_year")
        self.end_month = kwargs.get("end_month")
        self.end_year = kwargs.get("end_year")
        self.owner = kwargs.get("owner")

    def __repr__(self):
        return "<Usereducation %r>" % self.id


class Useraward(db.Model):
    __tablename__ = "userawards"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    award = db.Column(db.String(120))
    organisation = db.Column(db.String(100))
    cirt_id = db.Column(db.String(80))
    date_started = db.Column(db.DateTime, nullable=True)
    date_expired = db.Column(db.DateTime, nullable=True)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    owner = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )


class Earningrole(db.Model):
    __tablename__ = "earningroles"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    preffered_role = db.Column(db.Integer)
    cur_annual_earning = db.Column(db.Integer)
    exp_annual_earning = db.Column(db.Integer)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    owner = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )


class Userskill(db.Model):
    __tablename__ = "userskills"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    skill = db.Column(db.Integer)
    years_experienced = db.Column(db.Integer)
    competency = db.Column(db.Integer)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    owner = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )


class Languagepro(db.Model):
    __tablename__ = "languagepros"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    details = db.Column(db.Text, nullable=False)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )


class Competency(db.Model):
    __tablename__ = "competencies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    details = db.Column(db.Text, nullable=False)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )


class Educationlevel(db.Model):
    __tablename__ = "educationlevels"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    details = db.Column(db.Text, nullable=False)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )


class Skill(db.Model):
    __tablename__ = "skills"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    category = db.Column(db.String(30))
    details = db.Column(db.Text, nullable=False)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )


class Programinglanguage(db.Model):
    __tablename__ = "programinglanguages"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    category = db.Column(db.String(30))
    details = db.Column(db.Text, nullable=False)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )


class Framework(db.Model):
    __tablename__ = "frameworks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    category = db.Column(db.String(30))
    pl_id = db.Column(db.Integer)
    details = db.Column(db.Text, nullable=False)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )


class Roles(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    details = db.Column(db.Text, nullable=True)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )


class Workavailability(db.Model):
    __tablename__ = "workavailabilities"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    details = db.Column(db.Text, nullable=False)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    author = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    profile_id = db.Column(
        db.Integer, db.ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False
    )
    userprojects_id = db.Column(
        db.Integer, db.ForeignKey("userprojects.id", ondelete="CASCADE"), nullable=False
    )


class Like(db.Model):
    __tablename__ = "likes"
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=True
    )
    author = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    profile_id = db.Column(
        db.Integer, db.ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False
    )
    userprojects_id = db.Column(
        db.Integer, db.ForeignKey("userprojects.id", ondelete="CASCADE"), nullable=False
    )
