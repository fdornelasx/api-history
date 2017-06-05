import json
from functools import wraps
from time import strftime, localtime
import requests
import pytz
import datetime
import time

def send_message(script_code, params=None,reason=None, comment=None,ip=None,machine_nickname=None):
    data = """{"script_code":"%d", "params":"%s","reason":"%s","comment":"%s","ip":"%s","machine_nickname":"%s"}""" % (script_code, params, reason, comment, ip, machine_nickname)
    insert = requests.post('http://0.0.0.0:7007/push', data=data)
    status = json.loads(insert.content)['result']['status']
    token = json.loads(insert.content)['result']['token']
    
    tz = pytz.timezone('America/Sao_Paulo')
    timestamptz = datetime.datetime.now(tz=tz)
    
    def send_message_decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            URL_update = "http://0.0.0.0:7007/update"
            try:
                f = func(*args, **kwargs)
            except Exception, e:
                status = "error"
                reason = e
                data_error = """{"token":"%s","finished_at":"%s", "status":"%s", "reason": "%s"}""" % (token, timestamptz, status, reason)
                requests.post(URL_update, data=data_error)
                raise
            else:
                status = "OK"
                reason = f
                data_sucess = """{"token":"%s","finished_at":"%s", "status":"%s", "reason": "%s"}""" % (token, timestamptz, status, reason)
                requests.post(URL_update,data=data_sucess)
            return f
        return decorated
    return send_message_decorator
