import pymysql


def getResults(query):
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="ifootball")
    myCursor = conn.cursor()
    # query = "INSERT INTO `me`(name) VALUES('mohamed');"
    myCursor.execute(query)

    rows = myCursor.fetchall()
    # print(rows)
    conn.commit()
    conn.close()
    return rows

def addRow(query):
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="ifootball")
    myCursor = conn.cursor()
    myCursor.execute(query)
    # print("myCursor.lastrowid",myCursor.lastrowid)
    conn.commit()
    conn.close()
    return myCursor

def signup(query,email):
    if isEMailRepeated(email):
        return -1
    else:
        cursor = addRow(query)
        id = cursor.lastrowid if cursor.rowcount == 1 else 0
        return id



def isEMailRepeated(email):
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="ifootball")
    myCursor = conn.cursor()
    query = f"SELECT COUNT(*) From `user` WHERE `email` = '{email}'"
    myCursor.execute(query)
    result = myCursor.fetchone()
    conn.commit()
    conn.close()
    return False if result[0]==0 else True

