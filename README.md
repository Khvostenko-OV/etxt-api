## ETXT.biz API-client

To use API on etxt.biz you need:
* sign up at https://etxt.biz/users/register/
* go to account/settings
* checkbox **Work with this profile by API**
* get API key (*token*)
* define API password (*api_pass*)
* press **Save**

--------------

Use **call_api()** for calling API-function
* Required parameters:
  * *method* - name of called method (See specification at https://www.etxt.biz/api/)
  * *token* - API key of current user
  * *api_pass* - API password of current user
* Auxiliary parameters (*aux_params*) for certain method (See specification at https://www.etxt.biz/api/)

**call_api** makes GET/POST http-request (depends on *method*) by defining signature of request (*sign*), 
transfering *method*, *token*, *sign* and *aux_params* to http-request.
Returns json of http-response or error message in json format - {'error': 'error message'}

More information about implemented API methods look at https://www.etxt.biz/api/