from etxt_api import call_api
from decouple import config

TOKEN = config("TOKEN", "my_token")
API_PASS = config("API_PASS", "my_api_pass")

if __name__ == "__main__":

    # Creating non-public order with given parameters
    title = input("Article title: ")
    descr = input("Order description: ")
    size = input("Text size: ")
    price = input("Total price: ")
    date = input("Deadline (dd.mm.yyyy): ")
    resp = call_api(
        "tasks.saveTask", TOKEN, API_PASS,
        public=0,   # non-public
        title=title,
        description=descr,
        size=size,
        price=price,
        price_type=2,   # total price
        deadline=date,
        id_category=1911    # category undefined
    )
    print()
    print(resp)
