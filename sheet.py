import os
import google.auth
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Path to the service account JSON key
SERVICE_ACCOUNT_FILE = 'Credentials.json'

# Scopes required by the Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Authenticate with Google Sheets API using the service account
def authenticate_google_sheets():
    creds = None

    # Use the service account to authenticate
    creds, _ = google.auth.load_credentials_from_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # If we don't have valid credentials, request new ones
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

    return creds

# Access Google Sheets
def access_google_sheet():
    creds = authenticate_google_sheets()
    service = build('sheets', 'v4', credentials=creds)
    SPREADSHEET_ID = '1teh_eb14FPwAtXMp1bafI473s7ZL13K2_BxQJK7fB9A'  # Replace with your sheet ID
    RANGE_NAME = 'Sheet1!A1:D10'  # Replace with your desired range

    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    return values

# Write filtered data to Google Sheets
def write_to_google_sheet(dataframe):
    creds = authenticate_google_sheets()
    service = build('sheets', 'v4', credentials=creds)
    SPREADSHEET_ID = '1teh_eb14FPwAtXMp1bafI473s7ZL13K2_BxQJK7fB9A'  # Replace with your sheet ID
    RANGE_NAME = 'Sheet1!A1'  # Starting cell for data output

    # Convert the DataFrame to a list of lists for Sheets API
    values = [dataframe.columns.tolist()] + dataframe.values.tolist()

    # Write the data to the specified range in Google Sheets
    body = {
        'values': values
    }
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption='RAW',
        body=body
    ).execute()
