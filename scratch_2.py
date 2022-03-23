import MySQLdb
import pandas as pd

import credentials as cred


# Data Base Class
class MediSageDB(object):

    HOSTNAME = "production-medisage.cpwmy4x3jsiq.ap-south-1.rds.amazonaws.com"
    DATABASE = "medisage2"

    def __init__(self, username, passwd):
        assert isinstance(username, str)
        assert isinstance(passwd, str)

        self.username = username
        self.passwd = passwd

    def __enter__(self):
        try:
            self.conn = MySQLdb.connect(host=self.HOSTNAME, user=self.username,
                                        passwd=self.passwd, db=self.DATABASE,
                                        charset="utf8")
            return self

        except MySQLdb.Error:
            print("Could not connect to database. Please check Connectivity "
                  "or Credential informations.")
            raise

    def __exit__(self, type_, value, traceback):
        self.conn.close()

    def table_by_sql_query(self, query):
        """
        Fetch Data by Custom Query. Returns pandas dataframe

        :param query str: SQL Query to be queried to the database
        """

        df = pd.read_sql_query(QUERY, self.conn)
        return df






if __name__ == "__main__":
    with MediSageDB(cred.DATABASE_USER, cred.DATABASE_PASSWORD) as db:
        #  df = db.get_table("videos")
        QUERY = f"""
                        SELECT * FROM live_event_members
                        """
        df = (db.table_by_sql_query(QUERY))
    print(df)
