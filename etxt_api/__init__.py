"""
    To use API on etxt.biz you have to:
        sign up at https://etxt.biz/users/register/
        go to account/settings
        checkbox 'Work with this profile by API'
        get API key (token)
        define API password (api_pass)
        press 'Save'

    Use call_api() for calling API-function
        Required parameters:
            method - name of called method (See specification at https://www.etxt.biz/api/)
            token - API key of current user
            api_pass - API password of current user
        Auxiliary parameters for certain method (See specification at https://www.etxt.biz/api/)

    call_api returns json of http-response or error message in json format - {'error': 'error message'}

"""

import requests
from hashlib import md5

ETXT_BASE_URL = "https://www.etxt.ru/api/json/"
POST_METHODS = [
    "aricles.buy",
    "bwgroups.saveGroup",
    "bwgroups.deleteGroup",
    "bwgroups.updateGroup",
    "correction.add",
    "correction.import",
    "folders.addFolder",
    "folders.moveToFolder",
    "messages.setRead",
    "messages.setDelete",
    "messages.writePrivate",
    "tasks.setClientComment",
    "tasks.setNote",
    "tasks.unsetNote",
    "tasks.paidTask",
    "tasks.cancelTask",
    "tasks.deleteTask",
    "tasks.extraPaid",
    "tasks.saveTask",
    "tasks.failTask",
    "tasks.copyTask",
    "tasks.setDeadline",
    "tasks.saveComment",
    "tasks.sendNoteFail",
    "users.setNote",
    "users.setReport",
    "users.setUserBW",
]


def query_params(method: str, token: str, api_pass: str, **aux_params) -> str:
    """
     Create string with query parameters: required - method, token, sign and auxiliary - aux_params
    """

    param_list = ["method=" + method, "token=" + token]
    param_list += [key + "=" + str(val) for key, val in aux_params.items()]
    param_list.sort()
    params = ""
    for i in param_list:
        params += i
    a_p = api_pass + "api-pass"
    params += md5(a_p.encode()).hexdigest()
    param_list.append("sign=" + md5(params.encode()).hexdigest())
    return "&".join(param_list)


def call_api(method: str, token: str, api_pass: str, **aux_params):
    """
     Call etxt.biz API-function named method with aux_params. Return json response
    """

    if method in POST_METHODS:
        params = query_params(method=method, token=token, api_pass=api_pass)
        resp = requests.post(url=ETXT_BASE_URL, params=params, data=aux_params)
    else:
        params = query_params(method=method, token=token, api_pass=api_pass, **aux_params)
        resp = requests.get(url=ETXT_BASE_URL, params=params)
    if resp.status_code == 200:
        try:
            json = resp.json()
        except:
            json = {"error": resp.text}
        return json
    else:
        return {"error": f"Server error - {resp.status_code}"}
