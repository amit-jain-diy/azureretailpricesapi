import requests
import json
import pandas as pd
import os

# region variable: CHnage this to get price by region
zRegion = 'northeurope'

# Set your file location and filename to save your json and excel file
#change path 
filelocation = "C:/temp/azureretailpricesapi"
filename = zRegion 

# URL
url = "https://prices.azure.com/api/retail/prices?$filter=armRegionName eq " + "'"+ zRegion +"'"

# url = "https://prices.azure.com/api/retail/prices?$filter=contains(productName,'SSD Managed Disks') and armRegionName eq " + zRegion 
#url = "https://prices.azure.com/api/retail/prices?$filter=armSkuName eq 'Standard_A2'"


print ("Processing url : " + url)
# Call the Azure Retail Prices API
response = requests.get(url)


# Create an array to store price list
priceitems= []

#Add the retail prices returned in the API response to a list
for i in response.json()['Items']:
    priceitems.append(i) 

print(response.json()["NextPageLink"])

# Retrieve price list from all available pages until there is a 'NextPageLink' available to retrieve prices
while response.json()["NextPageLink"] != None:   
    for i in response.json()['Items']:
        priceitems.append(i) 
    response = requests.get(response.json()["NextPageLink"])
    print(response.json()["NextPageLink"])

# Retrieve price list from the last page when there is no "NextPageLink" available to retrieve prices
if response.json()["NextPageLink"] == None:
    for i in response.json()['Items']:
        priceitems.append(i) 

# Write the price list to a json file
with open(os.path.join(filelocation,filename) + '.json', 'w') as f:
    json.dump(priceitems, f)

# Open the price list json file and load into a variable
with open(os.path.join(filelocation,filename) + '.json', encoding='utf-8') as f:
    raw = json.loads(f.read())

# Convert the price list into a data frame
df = pd.json_normalize(raw)

# Save the data frame as an excel file
df.to_excel(os.path.join(filelocation,filename) + '.xlsx', sheet_name='RetailPrices', index=False)