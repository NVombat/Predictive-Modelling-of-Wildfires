from dotenv import load_dotenv
import pymongo
import random
import string
import os

from core.settings import DATABASE
from .errors import (
    UserDoesNotExistError,
    InvalidArgumentError,
    ResultUpdationError,
    InvalidDataIDError,
)

load_dotenv()


class DataEntry:
    def __init__(self) -> None:
        """
        Connect to MongoDB
        """
        client = pymongo.MongoClient(DATABASE["mongo_uri"])
        self.db = client[DATABASE["db"]][os.getenv("DATA_COLLECTION")]

    def generate_data_id(self) -> str:
        """Generates a unique data id

        Args:
            None

        Returns:
            str
        """
        data_id = "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(16)
        )

        if self.db.find_one({"Data.data_id": data_id}):
        # if self.db.find({"Data": {"$in": [data_id]}}):
            data_id = self.generate_data_id()
        return data_id

    def get_data_id(self, email: str) -> list:
        """Fetches all data ids for particular user

        Args:
            email: User Email ID

        Returns:
            list
        """
        if value := self.db.find_one({"Email": email}):
            res = []
            for element in value["Data"]:
                res.append(element["data_id"])
            return res

        raise UserDoesNotExistError(f"User {email} Does Not Exist")

    def validate_data_id(self, data_id: str) -> bool:
        """Validates user id for particular user

        Args:
            data_id: Data ID

        Returns:
            bool
        """
        if self.db.find_one({"Data.data_id": data_id}):
        # if self.db.find({"Data": {"$in": [data_id]}}):
            return True

        raise InvalidDataIDError(f"Data With ID {data_id} NOT Found")

    def insert_data(self, name: str, email: str, date: str, feature_list: list) -> None:
        """Inserts data into collection

        Args:
            name: User Name
            email: User Email ID
            date: Date of prediction request
            feature_list: List of Features

        Returns:
            None: inserts user data into db
        """
        pred_data = {
            "data_id": self.generate_data_id(),
            "Date": date,
            "Features": feature_list,
        }

        db_data = {"Data": pred_data}

        if self.db.find_one({"Email": email}):
            self.db.update_one(
                {"Email": email},
                {"$push": db_data},
            )
        else:
            rec = {"Name": name, "Email": email, "Data": [pred_data]}
            self.db.insert_one(rec)

    def fetch_feature_data(self, d=False, e=False, **kwargs) -> list:
        """Fetches features from collection

        Args:
            d: representative of data_id argument present (False)
            e: representative of email argument present (False)
            **kwargs: Contains data_id and email

        Returns:
            list
        """
        if d == True and e == False:
            try:
                data_id = kwargs["data_id"]
                print("data_id:", data_id)

                # Get Data with ID = data_id
                if value := self.db.find_one({"Data.data_id": data_id}):
                # if value := self.db.find({"Data": {"$in": [data_id]}}):
                    data = value["Data"]
                    return data["Features"]

                raise InvalidDataIDError(f"Data with ID {data} DOES NOT Exist")

            except Exception:
                raise InvalidArgumentError(
                    "Kwargs Has Invalid Argument - Missing Argument 'data_id'"
                )

        elif e == True and d == False:
            try:
                email = kwargs["Email"]
                print("Email:", email)

                # Get All Data for email ID = email
                if value := self.db.find_one({"Email": email}):
                    feature_list = []
                    data = value["Data"]
                    for element in data:
                        feature = data["Features"]
                        feature_list.append(feature)

                    return feature_list

                raise UserDoesNotExistError(f"User with Email {email} DOES NOT Exist")

            except Exception:
                raise InvalidArgumentError(
                    "Kwargs Has Invalid Argument - Missing Argument 'Email'"
                )

        elif e == True and d == True:
            try:
                data_id = kwargs["data_id"]
                email = kwargs["Email"]
                print(email, data_id)

                if value := self.db.find({"Email": email, "Data": {"$in": [data_id]}}):
                    data = value["Data"]
                    return data["Features"]

                raise InvalidArgumentError(f"User with Email {email} And Data with ID {data} DOES NOT Exist")

            except Exception:
                raise InvalidArgumentError(
                    "Kwargs Has Invalid Argument - Missing Argument 'Email'"
                )

    def add_prediction_result(self, email: str, data_id: str, res: int) -> None:
        """Inserts prediction result into collection

        Args:
            email: User Email ID
            data_id: Data ID
            res: Result of Prediction

        Returns:
            None: inserts result into db
        """
        if self.db.find_one({"Email": email}):
            if self.db.find({"Data": {"$in": [data_id]}}):
                try:
                    self.db.update_one(
                        {"Email": email, "Data.data_id": data_id},
                        {
                            "$set": {
                                "Data.Result": res,
                            }
                        },
                    )
                except Exception:
                    raise ResultUpdationError(
                        f"Unable to Update Data With ID {data_id}"
                    )
            else:
                raise InvalidDataIDError(f"Data With ID {data_id} NOT Found")
        else:
            raise UserDoesNotExistError(f"User with Email {email} DOES NOT Exist")

    def fetch_prediction_result(self, email: str, data_id: str) -> int:
        """Fetches prediction result from collection

        Args:
            email: User Email ID
            data_id: Data ID

        Returns:
            int: prediction result
        """
        if value := self.db.find_one({"Email": email, "Data": {"$in": [data_id]}}):
            data = value["Data"]
            res = data["Result"]

            return res
        raise InvalidArgumentError(f"User with Email {email} And Data with ID {data} DOES NOT Exist")
