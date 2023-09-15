import pyodbc
import pandas as pd
import textwrap

class sqlcl():

    def __init__(self):
        server = 'sqlsrvname.database.windows.net'
        database = 'dbname'
        username = 'username'
        password = 'password'
        driver = '{ODBC Driver 17 for SQL Server}'

        try:
            ## Establish Connection##
            self.cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server +
                                       ';PORT=1433;DATABASE='+database+';UID='+username+';PWD=' + password)

        except pyodbc.Error as ex:
            sqlstate = ex.args[1]
            sqlstate = sqlstate.split(".")
            print('Exception Caught!')
            print(sqlstate[-3])
            return None

    # get all records from a table and return a DF#
    def getRecords(self):

        allrecordsqry = textwrap.dedent('''
        SELECT * 
        from [tablename] with(NOLOCK);        
        ''')

        # Fetch all rows and return dataframe
        with self.cnxn:

            try:
                cursor = self.cnxn.cursor()
                cursor.execute(allrecordsqry)
                qryres = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                tmp_df = pd.DataFrame.from_records(
                    qryres, columns=columns)
                return tmp_df

            except pyodbc.Error as e:
                print(f"Error: {e}")


# get an instance of the above class
myobj = sqlcl()

try:
    if isinstance(myobj.cnxn, pyodbc.Connection):
        print("Connection Established!")
        print("Attempting to retrieve and display records")

        data = myobj.getRecords()

        try:
            if isinstance(data, pd.DataFrame):
                print("Records retrieved!")
                print("")
                print(data)

            else:
                print("unable to retreive records")

        except:
            print("exception occurred checking results")

    else:
        print("something went wrong establishing connection, try again")

except:
    print("problems establishing connection, try again")
