# Azure Function App Setup

## Setup Azure Function App

Within Azure Portal, access lab1 resource group and hit create button.
Search: azure function (hit enter)

![azfuncimg1](assets/azfunc1.jpg)

Select Create, Function App
_ Resource Group: lab1
_ Function App Name: (give it a unique name)
_ Runtime Stack: Python
_ Version: 3.9

![azfuncimg2](assets/azfunc2.jpg)

    * Leave remaining options on initial page as default.
    * click the button, Next : Storage

Note: You will need a storage account so can leave the default new one Azure creates or manually create your own.

![azfuncimg3](assets/azfunc3.jpg)

    * Click button: Next: Networking
    * Leave options as default
    * click the button: Next: Monitoring
    * Set Enable Application Insights to no.

![azfuncimg4](assets/azfunc4.jpg)

    * Click button Review + Create

Verify the setup on the summary page and hit create button to provision function app

I now have the following Azure Components Setup within my lab1 resource group

![azfuncimg5](assets/azfunc5.jpg)

## Enable Managed Identity for Function App

    * Within Azure Function App, click Identity on the left.
    * Under System Assigned, change status to On and click save
    * Select Yes to the prompt

![azfuncimg6](assets/azfunc6.jpg)
