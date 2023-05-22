import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.data.tables import TableServiceClient

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ServiceRequestError,
    ResourceNotFoundError,
    AzureError
)


# load up env variables specified in my .ev file
result = load_dotenv(".env")

try:
    # authenticate and get access token which represents service principle
    token_credential = DefaultAzureCredential()

except ClientAuthenticationError as e:
    print(e)

except HttpResponseError as e:
    print(e)

except AzureError as e:
    print(e)

except Exception as e:
    print(e)

# get tableservice client
service = TableServiceClient(
    endpoint="https://<storageaccountname>.table.core.windows.net", credential=token_credential)


# This will create a table if it doesn't already exists
table_client = service.create_table_if_not_exists("testTable")


# print all tables
tblresults = service.list_tables()


for tbl in tblresults:
    print(tbl.name)


# create an entry
my_entity = {
    u'PartitionKey': u'Teams',
    u'RowKey': u'002',
    u'Car': u'Pathfinder',
    u'Color': u'Black',
    u'Mileage': 34223
}


try:
    # add entry to table
    table_client.create_entity(entity=my_entity)
    print("Completed")

except AzureError as e:
    print(e)

except Exception as e:
    print(e)


# list the entries in a table
entities = table_client.list_entities()

for ent in entities:
    print(ent)
