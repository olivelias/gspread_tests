#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

# https://github.com/burnash/gspread
# http://gspread.readthedocs.io/en/latest/ doc

import gspread # yaourt gspread
from oauth2client.service_account import ServiceAccountCredentials # yaourt oauth2client

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Gspread-9149778487d9.json', scope)
client = gspread.authorize(credentials)

# Ouverture du fichier
sheet = client.open("Gspreadtest").sheet1

# Affichage du contenu de tout le fichier
records = sheet.get_all_records()
print (records)

#
