"""
    To use API on etxt.biz you need:
        sign up at https://etxt.biz/users/register/
        go to account/settings
        checkbox 'Work with this profile by API'
        get API key (token)
        define API password (api_pass)
        press 'Save'

    Create ApiClient object with your token and api_pass.

    Use ApiClient._request(method, **params) for calling API-function
        method - name of called method (required parameter)
        params - dictionary of auxiliary parameters for certain method (see https://www.etxt.biz/api/)

    Note: if required transfer array of ids to the API-function use array=[id1, ...] parameter

    ApiClient._request returns json of http-response or error message in format - {'error': 'error message'}

    More implemented ApiClient methods:
        article_list(**params) - returns the list of articles offered for sale
        article_buy(article_id) - performs purchase of indicated article by current user
        article_get(article_ids) - returns texts of the requested purchased articles
        category_list() - returns the list of subject categories of orders/articles, sorted by category name
        order_list(**params) - returns the list of orders of current user
        order_create(**params) - creating an order
        order_update(order_id, **params) - updating indicated order
        order_delete(order_ids) - deletion of orders that have status of waiting for author or from drafts
        user_get(id, login) - returns detailed information of indicated user
        user_balance() - returns balance of current user
        query_params(method, **aux_params) - creates string with query parameters:
                                                required - method, token, sign
                                                auxiliary - aux_params

    More information about implemented API methods look at https://www.etxt.biz/api/
"""

import requests
from hashlib import md5

ETXT_URL = "https://www.etxt.ru/api/json/"


class ApiClient():

    def __init__(self, token, api_pass):
        self.token = token
        self.api_pass = api_pass


    def query_params(self, method: str, **aux_params) -> str:
        """
        Creates string with query parameters: required - method, token, sign and auxiliary - aux_params
        """
        param_list = ["method=" + method, "token=" + self.token]
        param_list += [key + "=" + str(val) for key, val in aux_params.items() if key != "array"]
        if "array" in aux_params:
            for i,j in enumerate(aux_params["array"]):
                param_list.append(f"id[{i}]=" + str(j))
        param_list.sort()
        params = "".join(param_list)
        a_p = self.api_pass + "api-pass"
        params += md5(a_p.encode()).hexdigest()
        param_list.append("sign=" + md5(params.encode()).hexdigest())
        return "&".join(param_list)

    def _request(self, method, **params):
        """ Calls etxt.biz API-function named method with params. Returns json response """
        array = params.pop("array", [])
        resp = requests.post(url=ETXT_URL, params=self.query_params(method=method, array=array), data=params)

        if resp.status_code == 200:
            try:
                json = resp.json()
            except requests.exceptions.JSONDecodeError:
                json = {"error": resp.text}
            return json
        else:
            return {"error": f"Server error - {resp.status_code}"}

    def article_list(self, **params):
        """ Returns the list of articles offered for sale """
        return self._request(method="articles.getList", **params)

    def article_buy(self, article_id):
        """ Performs purchase of indicated article by current user """
        return self._request(method="articles.buy", id=int(article_id))

    def article_get(self, article_ids: list):
        """" Returns texts of the requested purchased articles """
        return self._request(method="articles.getText", array=article_ids)

    def order_list(self, **params):
        """ Returns the list of orders of current user"""
        return self._request(method="tasks.listTasks", **params)

    def order_create(self, **params):
        """
         Creating an order
         Required parameters:
            title - order name, no more than 512 characters
            size - order size in characters
            price - order price
            price_type - order price type (1 - for 1000 characters, 2 - for the whole order)
            deadline - deadline in format dd.mm.yyyy, not more than 90 days
            id_category - identifier of order category (1911 - category undefined)
        """
        return self._request(method="tasks.saveTask", **params)

    def order_update(self, order_id, **params):
        """" Updating indicated order """
        return self._request(method="tasks.saveTask", id=int(order_id), **params)

    def order_delete(self, order_ids: list):
        """ Deletion of orders that have status of waiting for author or from drafts """
        return self._request(method="tasks.deleteTask", array=order_ids)

    def category_list(self):
        """ Returns the list of subject categories of orders/articles, sorted by category name """
        return self._request(method="categories.listCategories")

    def user_get(self, id=0, login=""):
        """ Returns detailed information on the indicated user """
        return self._request(method="users.getUser", id=int(id), login=login)

    def user_balance(self):
        """ Returns account balance of current user """
        return self._request(method="users.getBalance")
