#!/usr/bin/python3
""" task 5 """


if __name__ == "__main__":
    import sys
    import MySQLdb

    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT c.name FROM cities as c, states as s WHERE\
    s.id = c.state_id AND s.name = %s ORDER BY c.id ASC", (sys.argv[4], ))
    query_rows = cur.fetchall()
    l = []
    for row in query_rows:
        l.append(row[0])

    print(", ".join(l))
    cur.close()
    con.close()
