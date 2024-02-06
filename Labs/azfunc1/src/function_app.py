import azure.functions as func
import logging
import pyodbc
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="lab1func")
def lab1func(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

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
            key_vault_url = "https://{yourkeyvaultname}.vault.azure.net"
            credential = DefaultAzureCredential()

            client = SecretClient(vault_url=key_vault_url,
                                  credential=credential)

            sqlusername = client.get_secret("sqlusr").value
            sqlpassword = client.get_secret("sqlpasswrd").value

        except:
            logging.info("exception caught attempting to get secrets from AKV")
            return func.HttpResponse("exception caught attempting to get secrets from AKV", status_code=500)

        # connecting to SQL DB
        server = '{yoursqlserver}.database.windows.net'
        database = 'autos'
        driver = '{ODBC Driver 17 for SQL Server}'

        try:
            cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                                  ';PORT=1433;DATABASE='+database+';UID='+sqlusername+';PWD=' + sqlpassword)

        except pyodbc.Error as ex:
            logging.info("exception caught attempting to connect to SQL DB")
            logging.info(ex)
            return func.HttpResponse("exception caught attempting to connect to SQL DB", status_code=500)

        # executing SQL query
        allrecordsqry = "select * from inventory"
        car_models = []

        try:
            with cnxn.cursor() as cursor:
                cursor.execute(allrecordsqry)
                rows = cursor.fetchall()

                for row in rows:
                    logging.info(row)
                    car_models.append(row[2])

            return func.HttpResponse(f"{car_models}")

        except pyodbc.Error as ex:
            logging.info("exception caught attempting to execute SQL query")
            logging.info(ex)
            return func.HttpResponse("exception caught attempting to execute SQL query", status_code=500)

    else:
        return func.HttpResponse("This http triggered function executed successfully.  You didn't pass the correct name though, try again.", status_code=200)
