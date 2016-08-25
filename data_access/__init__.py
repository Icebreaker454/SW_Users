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

    def format_users(self, raw_data):
        return [{
            'id': x[0],
            'name': x[1],
            'email': x[2],
            'active': x[3]} for x in raw_data]

    def get_all_users(self):
        self._cur.callproc('getallusers')
        return self.format_users(self._cur.fetchall())

    def get_users_by_name(self, name):
        self._cur.callproc('getusersbyname', (name, ))
        return self.format_users(self._cur.fetchall())

    def __del__(self):
        self._conn.close()
