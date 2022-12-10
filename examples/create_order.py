from etxt_api import ApiClient
from decouple import config

TOKEN = config("TOKEN", "my_token")
API_PASS = config("API_PASS", "my_api_pass")

if __name__ == "__main__":

    api = ApiClient(TOKEN, API_PASS)

    # Creating non-public order with given parameters
    title = input("Article title: ")
    descr = input("Order description: ")
    size = input("Text size: ")
    price = input("Total price: ")
    date = input("Deadline (dd.mm.yyyy): ")
    print()
    resp = api.order_create(
        public=0,   # non-public
        title=title,
        description=descr,
        size=size,
        price=price,
        price_type=2,   # total price
        deadline=date,
        id_category=1911    # category undefined
    )
    print("Created order:", resp)
    print()

    # Deleting last created order
    if not "error" in resp:
        if input(f"Delete order {resp['id_task']} (y/n)? ").lower() in ["y", "д"]:
            print()
            print("Deleted order: ", api.order_delete(resp["id_task"]))
