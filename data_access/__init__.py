import psycopg2


class DBWrapper(object):
    _conn = None
    _cur = None

    def __init__(self, db_name, user, password, host='localhost'):
        connection_str = "host='%s' dbname='%s' user='%s' password='%s'" % (
            host, db_name, user, password)
        try:
            self._conn = psycopg2.connect(connection_str)
            self._cur = self._conn.cursor()
        except psycopg2.Error:
            if self._conn:
                self._conn.close()

    def list_users(self):
        self._cur.callproc('getallusers')
        return self._cur.fetchall()

    def get_users_by_name(self, name):
        self._cur.callproc('getusersbyname', (name, ))
        return self._cur.fetchall()

    def __del__(self):
        self._conn.close()
