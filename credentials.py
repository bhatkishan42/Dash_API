import sys

sys.path.insert(0, './')

import pandas as pd
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# User Credentials File Details
LOGIN_CRED_FILENAME = Path(__file__).parent / "LoginCredentials.xlsx"
LOGIN_SHEET_NAME = "Sheet1"

# Database Credentials
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

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
