#!/usr/bin/python3
""" task 1 """


if __name__ == "__main__":
    import sys
    import MySQLdb


    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[0][1] == N:
            print(row)

    cur.close()
    con.close()
