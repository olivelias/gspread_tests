#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

# https://github.com/burnash/gspread
# http://gspread.readthedocs.io/en/latest/ doc

import gspread # yaourt gspread
from oauth2client.service_account import ServiceAccountCredentials # yaourt oauth2client

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Gspread-9149778487d9.json', scope)
client = gspread.authorize(credentials)

# Open file
sheet = client.open("Gspreadtest").sheet1

# Print file records
records = sheet.get_all_records()
print (records)

# Add record
sheet.update_acell('B1', 'Toto')

# Import csv file
