from etxt_api import ApiClient
from pprint import pprint
from decouple import config

TOKEN = config("TOKEN", "my_token")
API_PASS = config("API_PASS", "my_api_pass")

if __name__ == "__main__":

    api = ApiClient(TOKEN, API_PASS)

    # Existing orders of current user
    print("Order list:")
    resp = api.order_list()
    pprint(resp)
    print()
    print("Orders count:", len(resp))

    # Deleting order
    print()
    num = input("Input order id to delete: ")
    if num:
        print()
        print("Deleted order: ", api.order_delete(num))
