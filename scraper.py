import requests
from bs4 import BeautifulSoup

# Specify the URL of the website
url = "https://fcainfoweb.nic.in/reports/report_menu_web.aspx"

# Make a GET request to the website
response = requests.get(url)

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Locate the table containing the daily prices data
table = soup.find("table", id="dvData")

# Extract the data from the table
rows = table.find_all("tr")
data = []
for row in rows:
    columns = row.find_all("td")
    data_row = [column.text for column in columns]
    data.append(data_row)

# Export the data to an Excel file
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

for row in data:
    ws.append(row)

wb.save("daily_prices_2020_02_03_04.xlsx")
