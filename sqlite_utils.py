import sqlite3


def create_table(commend):
    # connect to db
    conn = sqlite3.connect('stuff.db')
    print("数据库打开成功")
    c = conn.cursor()

    c.execute(commend)
    print("Success to create the table.")
    conn.commit()
    conn.close()


def insert_data(commend, data):
    # connect to db
    conn = sqlite3.connect('stuff.db')
    print("数据库打开成功")
    c = conn.cursor()

    c.execute(commend, data)
    conn.commit()
    print('Success to insert data.')
    conn.close()


def count_lines():
    # connect to db
    conn = sqlite3.connect('stuff.db')
    print("数据库打开成功")
    c = conn.cursor()

    cursor = c.execute("SELECT COUNT(*) FROM STUFF")
    result = cursor.fetchone()
    conn.close()
    return result[0]
