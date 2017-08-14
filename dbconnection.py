"""
module to handle the database query for the authentification
"""
try:
    import MySQLdb
except ImportError:
    print "Installing MySql API"
    import pip
    pip.main(args=["install", "-r", "requirements.txt"])
    import MySQLdb


def check_user(RFID=[]):
    """
    checks if the user is in the data base
    :return: True if the user is in the database False if not
    """
    """
    host
      string, host to connect

    user
      string, user to connect as

    passwd
      string, password to use

    db
      string, database to use

    port
      integer, TCP/IP port to connect to

    unix_socket
      string, location of unix_s
      """
    try:
        con = MySQLdb.connect(host="127.0.0.1", user="pi", db="tuer", passwd='raspberry')
        cur = con.cursor()
    except MySQLdb.Error,e:
        print(e.message)
        return False
    try:
        query = str()
        query_elements = list()
        if not (isinstance(RFID, list)):
            return False
        # bring the rfid into a string form
        query = "SELECT * FROM tuer WHERE rfid=%s"
        cur.execute(query, query_elements)
        result = cur.fetchall()
        if result is not None:
            return True
        # todo make string magik here
    except MySQLdb.Error, e:
        print(e.message)
        return False
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    print("Checking database Connection")
    v = check_user([0,0,0,0])
    print(v)
