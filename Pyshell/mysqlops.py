import MySQLdb as db


class BD_MANAGEMENT():
    def __init__(self, db_host, db_user, db_pass, db_name):
        self.__db_host = db_host
        self.__db_user = db_user
        self.__db_pass = db_pass
        self.__db_name = db_name
        self.__fetchone_count = 0
        self.__con, self.__cursor = self.__getConnection()

    def __getConnection(self):
        try:
            con = db.connect(
                host=self.__db_host,
                user=self.__db_user,
                passwd=self.__db_pass,
                db=self.__db_name,
                charset='utf8'
            )
            cursor = con.cursor()
            return con, cursor
        except Exception as db_connect_error:
            return db_connect_error

    def closeConnection(self):
        try:
            self.__cursor.close()
            self.__con.close()
        except Exception as close_connection_error:
            return close_connection_error

    def fetchResult(self, sql_string, fetch_method):
        try:
            # cursor = self.con.cursor()
            if fetch_method == 'fetchone':
                if self.__fetchone_count == 0:
                    self.__cursor.execute(sql_string)
                result = self.__cursor.fetchone()
                self.__fetchone_count += 1
                if result is None:
                    self.__fetchone_count = 0
            elif fetch_method == 'fetchall':
                self.__cursor.execute(sql_string)
                result = self.__cursor.fetchall()
            else:
                raise SyntaxError('''
                                Fetch method error:
                                fetch method should be set 'fetchone' or 'fetchall'
                                but you give me: %s
                                ''' % fetch_method)
            return result
        except Exception as fetch_result_error:
            return fetch_result_error

    def updateRow(self, sql_string):
        try:
            self.__cursor.execute(sql_string)
            self.__con.commit()
        except Exception as update_row_error:
            return update_row_error

    def countRows(self, table_name):
        sql_string = 'select count(*) from %s' % table_name
        count = self.fetchResult(sql_string, 'fetchone')[0]
        return count