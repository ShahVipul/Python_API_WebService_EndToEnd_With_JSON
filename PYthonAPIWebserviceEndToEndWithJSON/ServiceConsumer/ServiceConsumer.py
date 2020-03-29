import urllib.request, json
import time
import pandas as pd
time.sleep(5)
with urllib.request.urlopen("http://127.0.0.1:5000/api/vipul/exchangerates/curr/all") as url: #Calling json api url of provider
    ex_rates = json.loads(url.read().decode()) #reading exchange rate
    print(ex_rates)
    ex_rates = json.loads(json.dumps(ex_rates, sort_keys=False, indent=4))
    with open('ex_rates.json', 'w') as outfile:
        json.dump(ex_rates, outfile, sort_keys=False, indent=4)
    df = pd.read_json (r'C:\Users\asus\Desktop\PYTHONAPI\ServiceConsumer\ex_rates.json')
    export_csv = df.to_csv (r'C:\Users\asus\Desktop\PYTHONAPI\ServiceConsumer\exchange_rates.csv', index = None, header=False)
   
