from flask import request
import json

from DB import *
from Utils import *
from DB import mysql_user,mysql_password

def DeleteBoardMessage():
    attr_list = ["user_name","phone_number","content"]
    data_list = []
    dbo = DBOpera.DBOpera(mysql_user,mysql_password,"se_project") 
    json_data = json.loads(request.data.decode("utf-8"))
    for x in attr_list:
        tmp = json_data.get(x)
        if(tmp != None):
            data_list.append(tmp)

    (status,err) = dbo.delete("board_message",attr_list,data_list)
    return json.dumps({"status":status,"err":err.args[1] if err != None else err})