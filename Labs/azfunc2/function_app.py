import azure.functions as func
import logging
import pyodbc
import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="lab2func")
def lab2_func(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info("Attempting to retrieve secrets from Azure Key Vault")

    name = req.params.get('name')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name == "magic":
        # getting secrets from AKV
        try:

            logging.info("Attempting to retrieve secrets from Azure Key Vault")

            key_vault_url = os.getenv('KEYVAULT_URL')
            credential = DefaultAzureCredential()

            client = SecretClient(vault_url=key_vault_url,
                                  credential=credential)

            sqlusername = client.get_secret("sqlusr").value
            sqlpassword = client.get_secret("sqlpasswrd").value

            logging.debug(f'Retrieved the username {sqlusername} from AKV')

            logging.info("Successfully retrieved secrets from Azure Key Vault")

        except Exception as ex:
            logging.exception(
                f"Exception caught getting secrets from Keyvault: {ex}")
            return func.HttpResponse("Exception caught attempting to get secrets from AKV", status_code=500)

        # connecting to SQL DB
        try:

            logging.info('Connecting to SQL DB')
                 
            server = os.getenv('SQL_SRV')
            database = os.getenv('SQL_DB')
            driver = '{ODBC Driver 17 for SQL Server}'

            cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                                  ';PORT=1433;DATABASE='+database+';UID='+sqlusername+';PWD=' + sqlpassword)

            logging.info("Successfully Connected to SQL DB")

        except Exception as ex:
            logging.exception(f"Exception caught connecting to SQL: {ex}")
            return func.HttpResponse("exception caught attempting to connect to SQL DB", status_code=500)

        # executing SQL query
        try:
            # logging.debug('Attempting to execute SQL query')
            logging.info('Fetching results from SQL')
            allrecordsqry = "select * from inventory"
            car_models = []

            with cnxn.cursor() as cursor:
                cursor.execute(allrecordsqry)
                rows = cursor.fetchall()

                for row in rows:
                    # logging.info(row)
                    logging.info(row)
                    car_models.append(row[2])

            carscnt = str(len(rows))

            logging.info(
                f"Successfully retrieved and returned {carscnt} car models to the user")

            return func.HttpResponse(f"{car_models}")

        except pyodbc.Error as ex:
            logging.exception(
                f"exception caught attempting to execute SQL query: {ex}")
            return func.HttpResponse("exception caught attempting to execute SQL query", status_code=500)

    elif name != "magic":
        logging.info(
            "The function executed successfully however the user didn't specify the correct name parameter")
        return func.HttpResponse("This http triggered function executed successfully.  You didn't pass the correct name though, try again.", status_code=200)
