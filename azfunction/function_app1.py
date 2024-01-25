import logging
import azure.functions as func
import pyodbc
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


app = func.FunctionApp()


@app.schedule(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False)
def myazfunction(myTimer: func.TimerRequest) -> None:

    logging.info('Python timer trigger function starting.')

    # get keyvault username and password
    try:

        key_vault_uri = "https://youkeyvaultcluster.vault.azure.net/"

        credential = DefaultAzureCredential()

        client = SecretClient(vault_url=key_vault_uri,
                              credential=credential)

        sqlusername = client.get_secret("sql-username").value
        sqlpassword = client.get_secret("sql-password").value

    except:
        print("exception caught")
        print("key vault URI not found")

    # SQL Connect and query
    server = 'dcrsql.database.windows.net'
    database = 'sip'
    driver = '{ODBC Driver 17 for SQL Server}'

    try:
        # establish connection#
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                              ';PORT=1433;DATABASE='+database+';UID='+sqlusername+';PWD=' + sqlpassword)

    except pyodbc.Error as ex:
        print("exception caught establishing connection to SQL Server")
        print(ex)

    allrecordsqry = 'select * from yourtablename with (NOLOCK)'

    try:
        with cnxn.cursor() as cursor:
            cursor.execute(allrecordsqry)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    except pyodbc.Error as ex:
        sqlstate = ex.args[1]
        print("exception caught executing SQL query")
        print(f"SQL state: {sqlstate}")
