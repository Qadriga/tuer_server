"""
module to handle the database query for the authentification
"""

from configLoader import ProjectConfiguration
try:
    import MySQLdb
except ImportError:
    print("Installing MySql API")
    import pip
    pip.main(args=["install", "-r", "requirements.txt"])
    import MySQLdb

import MySQLdb.cursors


SQLPASSWRD = ProjectConfiguration().getLocalDatabasePassword()
USERNAME = ProjectConfiguration().getLocalDatabaseUsername()
DATABASENAME = ProjectConfiguration().getLocalDatabaseName()
DOORID = ProjectConfiguration().getDOORID()

def append_rfid(RFID=[]):
    """

    :param RFID: list of byte thats represents the RFID tag number
    :return: a int or long value to
    """
    res = int()
    if not isinstance(RFID, (tuple, list)):
        return 0
    RFID.reverse()
    for elem in RFID:
        res = res | (elem << (RFID.index(elem)*8))
    return res

def validate_schema():
    con = MySQLdb.Connect(user=USERNAME,
                          passwd=SQLPASSWRD,
                          db=DATABASENAME,
                          cursorclass=MySQLdb.cursors.DictCursor)
    cur = con.cursor()
    query = "SELECT * FROM information_schema.tables WHERE table_name=%s"
    cur.execute(query)
    res = cur.fetchone()
    if res is None:
        with open('setuplocaldb.sql', 'r') as f:
            query += f.read()
        cur.execute(query) # create the database with the schema in seruplocaldb.sql file 
    con.close()

def check_user(rfid=list()):
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
    

    unix_socket
      string, location of unix_s
      """
    try:
        con = MySQLdb.connect(host="127.0.0.1",
                              user=USERNAME,
                              db=DATABASENAME,
                              passwd=SQLPASSWRD,                              
                              cursorclass=MySQLdb.cursors.DictCursor)
        cur = con.cursor()
    except MySQLdb.Error, e:
        print(e)
        return False
    try:
        query_elements = list(("tag_id",str(DOORID)))
        if not (isinstance(rfid, list)):
            return False
        tag = append_rfid(rfid)
        query_elements.append(str(tag))

        # bring the rfid into a string form
        query = "SELECT %s FROM authorisations WHERE door_id=%s AND tag_id=%s" #
        own_build = query % tuple(query_elements)
        print own_build
        cur.execute(own_build)
        result = cur.fetchall()

        print result
        if result is not None:
            if not isinstance(result, (tuple, dict)):
                return False
            if long(tag) == result[0]['tag_id']:
                return True
            else:
                return False
        # todo make string magik here
    except MySQLdb.Error, e:
        print(e)
        return False
    finally:
        if con:
            con.close()




if __name__ == '__main__':
    print("Checking database Connection")
    read_conf()
    from time import time
    start = time()
    v = append_rfid([0xff, 0xfe, 0x02, 0x5, 0x1])
    # v = check_user(['123','456','789','000'])
    end = time()
    print end - start
    print(v)
