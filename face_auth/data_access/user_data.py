from face_auth.config.database import MongodbClient
from face_auth.constant.database_constants import USER_COLLECTION_NAME
from face_auth.entity.user import User

class UserData:
    """This class will have all the mongo db operations for user data
    like get_user and save_user
    """

    def __init__(self) -> None:
        self.client = MongodbClient()
        self.collection_name = USER_COLLECTION_NAME
        self.collection = self.client.database[self.collection_name]

    def save_user(self, user: User) -> None:
        self.collection.insert_one(user)

    def get_user(self, query: dict):
        user = self.collection.find_one(query)
        return user

    def get_all_users(self):
        users = list(self.collection.find())
        return users

    def delete_user(self, user_id: str) -> None:
        self.collection.delete_one({"_id": user_id})


    def delete_all_users(self) -> None:
        self.collection.delete_many({})
        result = self.collection.delete_many({})
        print(f'This many no of records got deleted {result.deleted_count}')
