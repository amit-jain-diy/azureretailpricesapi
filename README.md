# azureretailpricesapi
Get Azure Retail pricing via API using Python


Hi All,

This python script will help to download Azure Retail price for services offered by Azure
This is based on Azure Retail API 

https://docs.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices

API Endpoint
https://prices.azure.com/api/retail/prices

If you execute this API, you will notice that one can download 100 rows at a time

Python Scripts
1. Azure_get_price_by_Region.py : Get prices for all services for a specific Region
2. Azure_get_price_Disks.py : Get prices for managed disks for all regions
3. Azure_get_price_VM.py : Get VM prices for a specific region



Installation 
1. Create a folder on C Drive "c:/temp/azureretailpricesapi"
2. Download the file and place in this folder
3. Software needed
    Python 3
    panda
    requests

How to Run 
- open the python file and change the region from the table below 
- Execute by calling <filename>.py


Regions
| armRegionName | location |
| - | - |
| westus | US West |
| ukwest | UK West |
| westus2 | US West 2 |
| australiacentral2 | AU Central 2 |
| southeastasia | AP Southeast |
| eastus | US East |
| uksouth2 | UK South 2 |
| southcentralus | US South Central |
| japanwest | JA West |
| canadaeast | CA East |
| chinanorth3 | CN North 3 |
| brazilsouth | BR South |
| australiasoutheast | AU Southeast |
| francecentral | FR Central |
| canadacentral | CA Central |
| australiacentral | AU Central |
| eastasia | AP East |
| uknorth | UK North |
| francesouth | FR South |
| westeurope | EU West |
| usgovvirginia | US Gov Virginia |
| japaneast | JA East |
| westindia | IN West |
| usgovarizona | US Gov AZ |
| chinaeast3 | CN East 3 |
| southindia | IN South |
| centralus | US Central |
| koreasouth | KR South |
| usgovtexas | US Gov TX |
| eastus2 | US East 2 |
| centralindia | IN Central |
| uksouth | UK South |
| northeurope | EU North |
| australiaeast | AU East |
| koreacentral | KR Central |
| westcentralus | US West Central |
| northcentralus | US North Central |
| Global | Global |
| swedencentral | SE Central |
| swedensouth | SE South |
| jioindiawest | IN West Jio |
