import sys

sys.path.insert(0, './')

import pandas as pd
from pathlib import Path

# User Credentials File Details
LOGIN_CRED_FILENAME = Path(__file__).parent / "LoginCredentials.xlsx"
LOGIN_SHEET_NAME = "Sheet1"

# Database Credentials
DATABASE_USER = "sanchalak_reader"
DATABASE_PASSWORD = "medprodreader_123"

# LOGIN DATABASE
flask_secret_key = 'Medisage@123'

df = pd.read_excel(LOGIN_CRED_FILENAME, sheet_name=LOGIN_SHEET_NAME)

users = {}
for i, row in df.iterrows():
    users[row['Username']] = {
        'Username': row['Username'],
        'Password': row['Password'],
        'PartnerId': row['PartnerId'],
        'PartnerDivisionId': row.get('PartnerDivisionId', '-1'),
        'StartDate': row.get('StartDate', -1),
        'Path': row['Path'],
        'Role': row['Role'],
    }
