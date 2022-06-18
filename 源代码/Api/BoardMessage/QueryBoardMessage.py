from flask import request
import json

from DB import *
from Utils import *
from DB import mysql_user,mysql_password

def QueryBoardMessage():
    all_attr=("user_name","phone_number","content")
    attr_list = []
    data_list=[]
    dbo = DBOpera.DBOpera(mysql_user,mysql_password,"se_project") 
    json_data = json.loads(request.data.decode("utf-8"))
    for x in all_attr:
        tmp = json_data.get(x)
        if(tmp != None):
            attr_list.append(x)
            data_list.append(tmp)
    (status,err,res) = dbo.query("board_message",attr_list,data_list)
    return json.dumps({"status":status,"err":err.args[1] if err != None else err,"res":res})