# File in order to get the database from different file

from credentials import DATABASE_USER, DATABASE_PASSWORD
from Base_file import Kishan

QUERY_3 = f"""
select  distinct right(mobile,10) FROM medisage2.mtalks_delivery_report
where campaignName like "%NTS%" or campaignName like "%NCF%" or campaignName like "%_NOS_%"  
and campaignName not like "%Sanosan%" and created_at >= '2021-07-01'
    """
with Kishan(DATABASE_USER, DATABASE_PASSWORD) as db:
    data_3 = (db.table_by_sql_query(QUERY_3))

print(data_3)

