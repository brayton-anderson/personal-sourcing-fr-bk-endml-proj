from . import db
import json
from website.utils.utilities import Utilities
from website.models import (
    Cirtificaton,
    Usereducation,
    Cirtexperience,
    Companyworked,
    Companyexperience,
    Profile,
)


class Insertsocialdata:
    def insert_company_experience_data(usrid: int, data: json):
        # data_pro = json.load(data)
        orders_entries = []
        orders_entries2 = []
        for experiences in data["experience"]:
            if (
                "description" in experiences
                and "region" in experiences
                and "company" in experiences
            ):
                company = Companyworked(
                    industries=experiences["company"]["industries"][0],
                    company_name=experiences["companyName"],
                    company_region=experiences["region"],
                    description=experiences["description"],
                    entity_urn=(experiences["entityUrn"]),
                    geo_location_name=experiences["geoLocationName"],
                    location_name=experiences["locationName"],
                    title=experiences["title"],
                    user_id=usrid,
                    owner=usrid,
                )
            elif "description" in experiences and "company" in experiences:
                company = Companyworked(
                    industries=experiences["company"]["industries"][0],
                    company_name=experiences["companyName"],
                    description=experiences["description"],
                    entity_urn=(experiences["entityUrn"]),
                    geo_location_name=experiences["geoLocationName"],
                    location_name=experiences["locationName"],
                    title=experiences["title"],
                    user_id=usrid,
                    owner=usrid,
                )
            elif "region" in experiences and "company" in experiences:
                company = Companyworked(
                    industries=experiences["company"]["industries"][0],
                    company_name=experiences["companyName"],
                    company_region=experiences["region"],
                    entity_urn=(experiences["entityUrn"]),
                    geo_location_name=experiences["geoLocationName"],
                    location_name=experiences["locationName"],
                    title=experiences["title"],
                    user_id=usrid,
                    owner=usrid,
                )
            elif "region" in experiences and "description" in experiences:
                company = Companyworked(
                    company_name=experiences["companyName"],
                    entity_urn=(experiences["entityUrn"]),
                    company_region=experiences["region"],
                    description=experiences["description"],
                    geo_location_name=experiences["geoLocationName"],
                    location_name=experiences["locationName"],
                    title=experiences["title"],
                    user_id=usrid,
                    owner=usrid,
                )
            elif "region" in experiences:
                company = Companyworked(
                    company_name=experiences["companyName"],
                    entity_urn=(experiences["entityUrn"]),
                    company_region=experiences["region"],
                    geo_location_name=experiences["geoLocationName"],
                    location_name=experiences["locationName"],
                    title=experiences["title"],
                    user_id=usrid,
                    owner=usrid,
                )
            elif "description" in experiences:
                company = Companyworked(
                    company_name=experiences["companyName"],
                    entity_urn=(experiences["entityUrn"]),
                    description=experiences["description"],
                    geo_location_name=experiences["geoLocationName"],
                    location_name=experiences["locationName"],
                    title=experiences["title"],
                    user_id=usrid,
                    owner=usrid,
                )
            else:
                company = Companyworked(
                    company_name=experiences["companyName"],
                    entity_urn=(experiences["entityUrn"]),
                    geo_location_name=experiences["geoLocationName"],
                    location_name=experiences["locationName"],
                    title=experiences["title"],
                    user_id=usrid,
                    owner=usrid,
                )

            orders_entries.append(company)
            if "timePeriod" in experiences:
                experience_data = experiences["timePeriod"]["startDate"]
                if (
                    "endDate" in experiences["timePeriod"]
                    and "companyUrn" in experiences
                ):
                    experience_data2 = experiences["timePeriod"]["endDate"]
                    experience = Companyexperience(
                        company_name=experiences["companyName"],
                        company_urn=experiences["companyUrn"],
                        start_month=experience_data["month"],
                        start_year=experience_data["year"],
                        end_month=experience_data2["month"],
                        end_year=experience_data2["year"],
                    )
                elif "companyUrn" in experiences:
                    experience = Companyexperience(
                        company_name=experiences["companyName"],
                        company_urn=experiences["companyUrn"],
                        start_month=experience_data["month"],
                        start_year=experience_data["year"],
                    )
                elif "endDate" in experiences["timePeriod"]:
                    experience_data2 = experiences["timePeriod"]["endDate"]
                    experience = Companyexperience(
                        company_name=experiences["companyName"],
                        start_month=experience_data["month"],
                        start_year=experience_data["year"],
                        end_month=experience_data2["month"],
                        end_year=experience_data2["year"],
                    )
                else:
                    experience = Companyexperience(
                        company_name=experiences["companyName"],
                        company_urn="data",
                        start_month=experience_data["month"],
                        start_year=experience_data["year"],
                    )

            orders_entries2.append(experience)

        db.session.bulk_save_objects(orders_entries)
        db.session.bulk_save_objects(orders_entries2)

        db.session.commit()
        return "done"

    def insert_certification_data(usrid: int, data: json):
        # data_pro = json.load(data)
        orders_entries = []
        orders_entries2 = []
        for experience in data["certifications"]:
            company_data = experience["company"]
            company = Cirtificaton(
                active=company_data["active"],
                user_id=usrid,
                dash_company_urn=company_data["dashCompanyUrn"],
                entity_urn=company_data["entityUrn"],
                logo=json.dumps(company_data["logo"]),
                name=company_data["name"],
                object_urn=company_data["objectUrn"],
                showcase=company_data["showcase"],
                tracking_id=company_data["trackingId"],
                universal_name=company_data["universalName"],
                owner=usrid,
            )

            orders_entries.append(company)
            if "timePeriod" in experience:
                experience_data = experience["timePeriod"]["startDate"]
                experience = Cirtexperience(
                    authority=experience["authority"],
                    company_urn=company_data["entityUrn"],
                    name=experience["name"],
                    start_month=experience_data["month"],
                    start_year=experience_data["year"],
                    company=company,
                )

                orders_entries2.append(experience)

        db.session.bulk_save_objects(orders_entries)
        db.session.bulk_save_objects(orders_entries2)

        db.session.commit()
        return "done"

    def insert_educational_data(usrid: int, data: json):
        orders_entries = []
        for education in data["education"]:
            fsid = Utilities.contains_word(words=education["degreeName"])
            ed = Usereducation(
                user_id=usrid,
                degree_name=education["degreeName"],
                entity_urn=education["entityUrn"],
                field_of_study=education["fieldOfStudy"],
                field_of_study_urn=education["fieldOfStudyUrn"],
                field_of_study_id=fsid,
                school_name=education.get("school", {}).get(
                    "schoolName", education.get("schoolName", None)
                ),
                school_urn=education.get("school", {}).get("entityUrn", None),
                active=education.get("school", {}).get("active", None),
                logo_url=education.get("school", {}).get("logoUrl", None),
                object_urn=education.get("school", {}).get("objectUrn", None),
                tracking_id=education.get("school", {}).get("trackingId", None),
                start_month=education.get("timePeriod", {})
                .get("startDate", {})
                .get("month", None),
                start_year=education.get("timePeriod", {})
                .get("startDate", {})
                .get("year", None),
                end_month=education.get("timePeriod", {})
                .get("endDate", {})
                .get("month", None),
                end_year=education.get("timePeriod", {})
                .get("endDate", {})
                .get("year", None),
                owner=usrid,
            )
            orders_entries.append(ed)
            # print(orders_entries)
        db.session.bulk_save_objects(orders_entries)
        db.session.commit()
        return "done"

    def insert_linkedin_prof_data(usrid: int, data: json, lname: str):
        if "displayPictureUrl" in data:
            lprp = data["displayPictureUrl"]
        else:
            lprp = ""
        if "firstName" in data:
            lfname = data["firstName"]
        else:
            lfname = ""
        if "lastName" in data:
            llname = data["lastName"]
        else:
            llname = ""
        if "geoCountryName" in data:
            lgeocname = data["geoCountryName"]
        else:
            lgeocname = ""

        if "headline" in data:
            lhdln = data["headline"]
        else:
            lhdln = ""
        if "locationName" in data:
            lllname = data["locationName"]
        else:
            lllname = ""
        if "profile_id" in data:
            lprofid = data["profile_id"]
        else:
            lprofid = ""
        if "student" in data:
            lstnt = data["student"]
        else:
            lstnt = ""
        if "summary" in data:
            lsumry = data["summary"]
        else:
            lsumry = ""
        prof = Profile(
            user_id=usrid,
            profile_picture=lprp,
            profile_summary=lsumry,
            linked_fname=lfname,
            linked_lname=llname,
            geo_country_name=lgeocname,
            linked_headline=lhdln,
            location_name=lllname,
            linked_profile_name=lprofid,
            is_student=lstnt,
            linkedin_profile=lname,
            country=lgeocname,
            owner=usrid,
        )
        db.session.add(prof)
        db.session.commit()
        return "done"
