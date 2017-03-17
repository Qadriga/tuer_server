"""
module to handle the database query for the authentification
"""
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
    con = MySQLdb.connect(host="127.0.0.1", user="pi" , db="tuer", passwd='raspberry')
    cur = con.cursor()
    try:
        query = str()
        query_elements = list()
        if not (isinstance(RFID,list)):
            return False
        # cur.execute()
        # todo make string magik here
    except MySQLdb.Error, e:
        print(e.message)
    finally:
        if con:
            con.close()



if __name__ == '__main__':
    print("Checking database Connection")
    v = check_user([0,0,0,0])
    print(v)