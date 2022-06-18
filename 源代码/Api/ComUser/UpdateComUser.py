from flask import request
import json

from DB import *
from Utils import *
from DB import mysql_user,mysql_password

def UpdateComUser():
    dbo = DBOpera.DBOpera(mysql_user,mysql_password,"se_project") 
    json_data = json.loads(request.data.decode("utf-8"))
    all_attr = ("user_name","password","phone_number","user_state","user_type")
    sel_attr = []
    sel_value = []
    set_attr = []
    set_value = []

    for x in all_attr:
        tmp = json_data[0].get(x)
        if(tmp != None):
            sel_attr.append(x)
            sel_value.append(tmp)
        tmp = json_data[1].get(x)
        if(tmp != None):
            set_attr.append(x)
            set_value.append(tmp)

    (status,err,res) = dbo.update("com_user",sel_attr,sel_value,set_attr,set_value)
    return json.dumps({"status":status,"err":err.args[1] if err != None else err,"res":res})