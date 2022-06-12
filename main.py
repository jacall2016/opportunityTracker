import json

import requests

from pandas.io.json import json_normalize

url = 'https://api.sam.gov/prod/opportunities/v2/search?limit=10&api_key=FGTJQrYpZfifUA65pNNstMFwAjifNDFQLzWkGo6O&postedFrom=01/01/2022&postedTo=05/10/2022&ptype=a&deptname=general'

#url = 'https://api.sam.gov/prod/opportunities/v2/search?limit=1&api_key=Q6Sgtaf4kiZS77RajWOn5O6ylRfluoF8tQNpsUXZ&postedFrom=01/01/2021&postedTo=05/10/2021&ptype=a&deptname=general'

resp = requests.get(url=url)

print(resp.json)

jsonObject = json_normalize(resp.json())

print(jsonObject)
jsonString = json.dumps(resp.json)
jsonFile = open("data.json","w")
jsonFile.write(jsonString)
jsonFile.close()

#df.to_csv('data_files\oppurtunityTracker.csv')

#df_json = pd.read_json('https://api.sam.gov/prod/opportunities/v2/search?limit=1&api_key=Q6Sgtaf4kiZS77RajWOn5O6ylRfluoF8tQNpsUXZ&postedFrom=01/01/2021&postedTo=05/10/2021&ptype=a&deptname=general')



#response = requests.get('https://api.sam.gov/prod/opportunities/v2/search?limit=1&api_key=Q6Sgtaf4kiZS77RajWOn5O6ylRfluoF8tQNpsUXZ&postedFrom=01/01/2021&postedTo=05/10/2021&ptype=a&deptname=general')
#response_info = json.loads(response)
#print(response)

#print(df_json)