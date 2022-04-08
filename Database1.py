# Redoing the Database file in order to practice the use of the SQLite3 module

import pandas as pd
import MySQLdb
import credentials as cred

# Creating a class in order to connect to the API


class MedisageDB(object):

    HOSTNAME = "production-medisage.cpwmy4x3jsiq.ap-south-1.rds.amazonaws.com"
    DATABASE = "medisage2"

    def __init__(self, username, password):
        assert isinstance(username, str)
        assert isinstance(password, str)
        self.username = username
        self.password = password

    def __enter__(self):

        try:
            self.conn = MySQLdb.connect(host=self.HOSTNAME,
                                        user=self.username,
                                        passwd=self.password,
                                        db=self.DATABASE)
            return self
        except MySQLdb.Error:
            print("Could not connect to database. Please check Connectivity "
                  "or Credential information.")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def get_data(self, query):
        """
        Put a query inside and get the required data as per the need

        """
        df = pd.read_sql(query, self.conn)   # Reading the data from the database
        return df


if __name__ == "__main__":

    with MedisageDB(cred.DATABASE_USER, cred.DATABASE_PASSWORD) as db:
        query = f"""
                select l.link_id,count(lm.mobile_number) as user from live_event_members lm
                left join live_events l on lm.link_id = l.id
                group by l.title
                order by user desc
                """
        df = db.get_data(query)
        print(df)










