from .base_api import BaseAPI


class UsersAPI(BaseAPI):
    def get_users(self):
        """Retrieve list of users."""
        return self.get("/users")

    def get_user_by_id(self, user_id):
        """Retrieve details of a specific user."""
        return self.get(f"/users/{user_id}")

    def create_user(self, user_data):
        """Create a new user."""
        return self.post("/users", user_data)
