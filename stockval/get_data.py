import pandas as pd
import time
import requests


Ticker = "CSCO"
API_key = "29IORL2ZB7ZP8CIE"
function = "BALANCE_SHEET"


API_url = f'https://www.alphavantage.co/query?function={function}&symbol={Ticker}&apikey={API_key}'
data = requests.get(API_url).json()

bq = prs.Persist()
bq.append_json("sec", "metadata", [{"CIK":str(CIK), "efiled": eFiled, "timestamp_processed" : timestamp_processed}])



 bq = prs.Persist()
    for key in company_facts["facts"]["us-gaap"].keys():
        if not isAvailable(CIK, key):
            logging.info("process fact: " + key)
            currency = list(company_facts["facts"]["us-gaap"][key]["units"].keys())[0]
            df = pd.DataFrame(company_facts["facts"]["us-gaap"][key]["units"][currency])
            df["cik"] = CIK
            df['entityName'] = company_facts["entityName"]
            df['unit'] = currency
            try: 
                bq.append_df("sec", key, df)
            except Exception as e:
                logging.error(CIK + ", " + key + ": " + e)

# https://stockanalysis.com/ipos/
# https://www.alphavantage.co/documentation/
