import os
import json
import requests
import pytz
import datetime
import time

from functools import wraps
from time import strftime, localtime

API_ENDPOINT = os.environ["API_ENDPOINT"]
push_url = "{API_ENDPOINT}{action}".format(API_ENDPOINT=API_ENDPOINT, action='/push')
update_url = "{API_ENDPOINT}{action}".format(API_ENDPOINT=API_ENDPOINT, action='/update')

def send_message(script_code, params=None,reason=None, comment=None,ip=None,machine_nickname=None):
    data = """{"script_code":"%s", "params":"%s","reason":"%s","comment":"%s","ip":"%s","machine_nickname":"%s"}""" % (script_code, params, reason, comment, ip, machine_nickname)
    insert = requests.post(push_url, data=data)
    status = json.loads(insert.content)['result']['status']
    token = json.loads(insert.content)['result']['token']
    
    
    def send_message_decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            tz = pytz.timezone('America/Sao_Paulo')
            timestamptz = datetime.datetime.now(tz=tz)
            
            try:
                f = func(*args, **kwargs)
            except Exception, e:
                status = "error"
                reason = e
                data_error = """{"token":"%s","finished_at":"%s", "status":"%s", "reason": "%s"}""" % (token, timestamptz, status, reason)
                requests.post(update_url, data=data_error)
                raise
            else:
                status = "OK"
                reason = f
                data_sucess = """{"token":"%s","finished_at":"%s", "status":"%s", "reason": "%s"}""" % (token, timestamptz, status, reason)
                requests.post(update_url,data=data_sucess)
            return f
        return decorated
    return send_message_decorator
