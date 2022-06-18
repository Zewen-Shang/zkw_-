from flask import request
import json


from DB import *
from DB import mysql_user,mysql_password
from Utils import getHash


def QueryComUser():
    dbo = DBOpera.DBOpera(mysql_user,mysql_password,"se_project") 
    json_data = json.loads(request.data.decode("utf-8"))
    all_attr = ("user_name","password","phone_number","user_state","user_type")
    attr_list = []
    data_list = []
    for x in all_attr:
        tmp = json_data.get(x) 
        if(tmp != None): 
            attr_list.append(x)
            data_list.append(tmp)
    (status,err,res) = dbo.query("com_user",attr_list,data_list)
    return json.dumps({"status":status,"err":err.args[1] if err != None else err,"res":res})  