#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import MySQLdb

    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities as c, states as s\
    WHERE s.id = c.state_id ORDER BY c.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    con.close()
