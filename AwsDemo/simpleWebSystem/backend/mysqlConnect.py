import pymysql
import os

tbname = os.getenv("TB_NAME")
dbname = os.getenv("DB_NAME")
mysqlUser = os.getenv("MYSQL_USER_NAME")
mysqlUserPass = os.getenv("MYSQL_USER_PASSWORD")
mysqlEndpoint = os.getenv("MYSQL_ENDPOINT")

def viewDB():
    sql = "select * from {0}".format(tbname)
    return queryDB(sql)

def regDB(skillType,certName):
    sql = "insert into {0}(skillType,certName) VALUE ('{1}','{2}')".format(tbname,skillType,certName)
    queryDB(sql)
    
def queryDB(sql):    
    print("tbname:{0},dbname:{1},mysqlUser:{2},mysqlUserPass:{3},mysqlEnd:{4}".format(tbname,dbname,mysqlUser,mysqlUserPass,mysqlEndpoint))
    connection=pymysql.connect(host=mysqlEndpoint, port=3306, user=mysqlUser, password=mysqlUserPass, db=dbname, cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
            result = cursor.fetchall()
            return result
    finally:
        connection.close()