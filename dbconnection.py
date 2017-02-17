"""
module to handle the database query for the authentification
"""
import MySQLdb
def check_user(RFID=[]):
    """
    checks if the user is in the data base
    :return: True if the user is in the database False if not
    """
    con = MySQLdb.connect('') # todo set connection string here
    cur = con.cursor()
    try:
        if not (isinstance(RFID,list)):
            return False
        # todo make string magik here
    except MySQLdb.Error, e:
        pass
    finally:
        if con:
            con.close()



