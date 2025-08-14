import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
import os, json

PF_SHEET_ID = "10kZrRYhLWbmyUmCVL_3OSu6QH2BFmwMb_WYyCh5ebjw"  # paste your PF_Data sheet ID

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
# For local test only: point to local JSON file named sa_key.json
creds = Credentials.from_service_account_file("sa_key.json", scopes=SCOPES)
gc = gspread.authorize(creds)

sh = gc.open_by_key(PF_SHEET_ID)
try:
    ws = sh.worksheet("pf_metrics_v2")
except gspread.WorksheetNotFound:
    ws = sh.add_worksheet(title="pf_metrics_v2", rows=1000, cols=20)

df = pd.DataFrame([{"month":"2025-03-01","income":3100,"expense":2000,"net":1100}])
ws.clear()
set_with_dataframe(ws, df, include_index=False, include_column_header=True)
print("✅ Local write OK")