#%%
import pandas as pd
import time
import requests

Ticker = "CSCO"
API_key = "29IORL2ZB7ZP8CIE"
function = "BALANCE_SHEET"


API_url = f'https://www.alphavantage.co/query?function={function}&symbol={Ticker}&apikey={API_key}'
data = requests.get(API_url).json()
df = pd.DataFrame(data["annualReports"]).set_index("fiscalDateEnding")
print(df.head())
# %%
