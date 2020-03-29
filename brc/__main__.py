import sys
import pandas as pd
import requests
from bs4 import BeautifulSoup

try:
    req = requests.get('https://www.brawlhalla.com/rankings/2v2/brz/')
except requests.exceptions.ConnectionError as err:
    print('Connection Error: ', err)
    sys.exit(1)

if req.status_code != 200:
    print('Request failed with status code:', req.status_code)
    sys.exit(1)

content = req.content
soup = BeautifulSoup(content, 'html.parser')
table = soup.find(name='table')
table_str = str(table)
df = pd.read_html(table_str, skiprows=4)

header = df[0].iloc[0]
df = df[0][1:]
header[0] = 'Clear'
header[4] = 'Clear'
header[6] = 'Clear'
df.columns = header

df[['Win', 'Loss']] = df['Win-Loss'].str.split('-', expand=True)

df = df.drop(columns=['Clear', 'Win-Loss'])

print(df)
