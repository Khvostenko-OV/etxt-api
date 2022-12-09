from etxt_api import call_api
from pprint import pprint
from decouple import config

TOKEN = config("TOKEN", "my_token")
API_PASS = config("API_PASS", "my_api_pass")

if __name__ == "__main__":

    # Show 5 existing articles
    resp = call_api("articles.getList", TOKEN, API_PASS, count=5)
    pprint(resp)

    # Show 20 existing articles with specified string in title/description/keywords
    search = input("Input searching string: ")
    resp = call_api("articles.getList", TOKEN, API_PASS, text=search)
    print()
    pprint(resp)
