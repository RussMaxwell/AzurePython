import azure.functions as func
import logging
from azure.identity import DefaultAzureCredential
from openai import AzureOpenAI

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="process_alert")
def process_alert(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name') 
    error_submitted = req.params.get('message')

    if name == "getinfo" and error_submitted:
        #error message submitted and passed to openAI
                
        try:            
            #vars to fill in#
            aiURI = "insert ai endpoint"
            aiKey = "insert ai Key"
            
            #prompts 
            sysprompt = """You will review error messages generated from a .Net core application and 
                            provide why the error is occurring and possible mitigation steps.  Please suggests a max of 2 
                            of the most likely causes and mitigation for those issues."""
            
            #open client connection to openAI service
            client = AzureOpenAI(azure_endpoint=aiURI, api_key=aiKey, api_version="2024-08-01-preview")
            response = client.chat.completions.create(
            model="boston-gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": f"{sysprompt}"
                },
                {
                    "role": "user", 
                    "content": f"{error_submitted}"
                }
            ]
            )
            resp = response.choices[0].message.content.strip()
            
            return func.HttpResponse(f"{resp}")
        
        except Exception as e:
            logging.info(f"Exception Caught! {e}")    
            return func.HttpResponse("Exception caught either during keyvault fetch or openai fetch!", status_code=500)
        
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
