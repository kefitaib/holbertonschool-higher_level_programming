#!/usr/bin/python3
""" task 3 """


if __name__ == "__main__":
    import sys
    import MySQLdb

    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (sys.argv[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    con.close()
