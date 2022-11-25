from model.db import DB
import json

def insert(account, Tracecode, fb1q_type):
    print("this is po")
    typesql = "select 4b1q_id from `4b1q_type` where 4b1q = ?",(fb1q_type,)
    print(typesql)
    type = DB.execution(DB.select, typesql)
    sqlstr = "select Tracecode from 4b1q where Tracecode =? AND 4b1q_type=?", (Tracecode,type,)
    print(sqlstr)
    data = DB.execution(DB.select, sqlstr)
    if data is None:
        return "不存在"
    else:
        sqlstr = "select id from 4b1q where Tracecode =? AND 4b1q_type=?", (Tracecode,type,)
        print(sqlstr)
        id = DB.execution(DB.select, sqlstr)
        sqlstr = "insert into 4b1q_user (account,id) VALUES (\"%s\",\"%s\")" % (account, id)
        print(sqlstr)
        return DB.execution(DB.create, sqlstr)