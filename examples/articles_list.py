from etxt_api import ApiClient
from pprint import pprint
from decouple import config

TOKEN = config("TOKEN", "my_token")
API_PASS = config("API_PASS", "my_api_pass")

if __name__ == "__main__":

    api = ApiClient(TOKEN, API_PASS)
    # Show 5 existing articles
    pprint(api.article_list(count=5))
    print()

    # Show 20 existing articles with specified string in title/description/keywords
    search = input("Input searching string: ")
    print()
    pprint(api.article_list(text=search))
