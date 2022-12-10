from etxt_api import ApiClient
from pprint import pprint
from decouple import config

TOKEN = config("TOKEN", "my_token")
API_PASS = config("API_PASS", "my_api_pass")

if __name__ == "__main__":

    api = ApiClient(TOKEN, API_PASS)

    # Current user information
    bal = api.user_balance()
    user = api.user_get(id=bal["id"])
    pprint(user)
    print("Money balance:", bal["balance"])

