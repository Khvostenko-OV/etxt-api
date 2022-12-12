## ETXT.biz API-client

To use API on etxt.biz you need:
* sign up at https://etxt.biz/users/register/
* go to account/settings
* checkbox **Work with this profile by API**
* get API key (*token*)
* define API password (*api_pass*)
* press **Save**

--------------

Create ApiClient object with your *token* and *api_pass*.

Use **ApiClient._request(*method*, *params*)** for calling API-function
* *method* - name of called method (required parameter)
* *params* - dictionary of auxiliary parameters for certain method (see https://www.etxt.biz/api/)

**Note:** if required transfer array of ids to the API-function use array=[id1, ...] parameter


**ApiClient._request** makes POST http-request by defining signature (*sign*), 
transfering *method*, *token*, *sign* and *params* to http-request.
Returns json of http-response or error message in json format - {'error': 'error message'}


More implemented ApiClient methods:
* **article_list** - returns the list of articles offered for sale
* **article_buy** - rerforms purchase of indicated article by current user
* **article_get** - returns texts of the requested purchased articles
* **category_list** - returns the list of subject categories of orders/articles, sorted by category name
* **order_list** - returns the list of orders of current user
* **order_create** - creating an order
* **order_update** - updating indicated order
* **order_delete** - deletion of orders that have status of waiting for author or from drafts
* **user_get** - returns detailed information of indicated user
* **user_balance** - returns balance of current user
* **query_params** - returns string with query parameters for http-request:

More information about implemented API methods look at https://www.etxt.biz/api/