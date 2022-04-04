# creating Data Base Connection using python
import MySQLdb
import pandas as pd

import credentials as cred


# Creating a class for checking the connection
class Kishan(object):
    HOSTNAME = "production-medisage.cpwmy4x3jsiq.ap-south-1.rds.amazonaws.com"
    DATABASE = "medisage2"

    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd
        print('im here')

    def __enter__(self):
        print('im here at 2')
        self.conn = MySQLdb.connect(host=self.HOSTNAME,
                                    user=self.username,
                                    passwd=self.passwd,
                                    db=self.DATABASE,
                                    charset="utf8")
        return self

    def __exit__(self, type_, value, traceback):
        print('im here at 3')
        self.conn.close()

    def table_by_sql_query(self, query):
        """
        Fetch Data by Custom Query. Returns pandas dataframe

        : param query str: SQL Query to be queried to the database
        """
        df = pd.read_sql_query(query, self.conn)
        return df


if __name__ == "__main__":
    with Kishan(cred.DATABASE_USER, cred.DATABASE_PASSWORD) as db:
        QUERY = f"""
        SELECT * FROM live_event_members
"""
        df = (db.table_by_sql_query(QUERY))
    print(df)