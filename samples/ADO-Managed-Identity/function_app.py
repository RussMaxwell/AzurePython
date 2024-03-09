import azure.functions as func
import logging
import json
from azure.identity import DefaultAzureCredential
from azure.core.pipeline.policies import BearerTokenCredentialPolicy
from azure.core.pipeline import Pipeline
from azure.core.pipeline.transport import HttpRequest, RequestsTransport


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="adofun")
def adofun(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('adofun AZ Function is running.')

    try:
        credential = DefaultAzureCredential()

        # swap out your organization and project name
        organization_url = "https://yourado-orgname.visualstudio.com/yourado-projectname"

        # swap out your work item number
        url = f'{organization_url}/_apis/wit/workitems/157'

        policy = BearerTokenCredentialPolicy(
            credential, "499b84ac-1321-427f-aa17-267ca6975798/.default")
        pipeline = Pipeline(transport=RequestsTransport(), policies=[policy])
        request = HttpRequest("GET", url)
        response = pipeline.run(request)

        if response.http_response.status_code != 200:
            logging.debug(
                f'Teams ADO DCR Response Status Code: {response.http_response.status_code}')
            raise Exception("Failed to get work item")

        elif response:
            try:

                body_str = response.http_response.body().decode('utf-8')
                body = json.loads(body_str)
                logging.info(
                    f'ADO WorkItem #157 was successfully retrieved: {body}.')

                return func.HttpResponse(f"ADO WorkItem #157 was successfully retrieved: {body}.")

            except Exception as e:
                logging.error(f'Error: {str(e)}')
                return func.HttpResponse(f"HTTP Response back to ADO WI was {response.http_response.status_code}, not sure if soemthing else happened.")

    except Exception as e:
        logging.error(f'Error: {str(e)}')
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
