import pymysql
from . import DBUtils


class DBOpera():

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db = pymysql.connect(
            host="localhost", user=user, password=password, database=db_name)

    def insert(self, table_name, data_list):
        status = False
        err = None
        cursor = self.db.cursor()
        parse = "insert into %s values (%s)" % (
            table_name, DBUtils.listToString(data_list))
        try:
            print(parse)
            cursor.execute(parse)
            self.db.commit()
            status = True
            err = None
        except Exception as e:
            status = False
            err = e
        return (status, err)

    def delete(self, table_name, attr_list, data_list):
        status = False
        err = None
        cursor = self.db.cursor()
        parse = "delete from %s where %s" % (
            table_name, DBUtils.twoListToCond(attr_list, data_list))
        try:
            print(parse)
            cursor.execute(parse)
            self.db.commit()
            status = True
            err = None
        except Exception as e:
            status = False
            err = e
        return (status, err)

    def query(self, table_name, attr_list, data_list):
        status = False
        err = None
        res = None
        cursor = self.db.cursor()
        parse = "SELECT * FROM %s" % (table_name,)
        if(len(attr_list) != 0):
            parse = "SELECT * FROM %s where %s" % (
                table_name, DBUtils.twoListToCond(attr_list, data_list))
        try:
            print(parse)
            cursor.execute(parse)
            self.db.commit()
            status = True
            err = None
            res = cursor.fetchall()
        except Exception as e:
            status = False
            err = e
            res = None
        return (status, err, res)

    def update(self, table_name, sel_attr, sel_value, set_attr, set_value):
        status = False
        err = None
        res = None
        cursor = self.db.cursor()
        parse = "update %s set " % (table_name,)

        for i in range(len(set_attr)-1):
            parse += "%s = '%s' ," % (set_attr[i], set_value[i])
        parse += "%s = '%s'" % (set_attr[-1], set_value[-1])
        parse += " where "
        for i in range(len(sel_attr)-1):
            parse += "%s = '%s' AND " % (sel_attr[i], sel_value[i])
        parse += "%s = '%s'" % (sel_attr[-1], sel_value[-1])
        try:
            print(parse)
            cursor.execute(parse)
            self.db.commit()
            status = True
            err = None
            res = cursor.fetchall()
        except Exception as e:
            status = False
            err = e
            res = None
        return (status, err, res)

    def __del__(self):
        self.db.close()
