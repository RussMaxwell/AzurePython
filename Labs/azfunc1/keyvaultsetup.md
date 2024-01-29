# Azure Key Vault Setup

## Key Vault Setup and Grant Key Vault Admin Role

Within Azure Portal, access lab1 resource group and hit create button.
Search: azure key vault (hit enter)

![kvimg1](assets/kv1.jpg)

    * Click Create, Key Vault
    * Give it a unique name.  Mine is labakv
    * Left remaining options default and clicked review + create button.
    * Click create button

Accessing lab1 resource group looks like this

![kvimg2](assets/kv2.jpg)

Since I'm using RBAC model, I'll grant my admin account Key Vault Administrator role.

    * Within the newly created Azure Key Vault, select Access control (IAM)
    * click Add role assignment.
    * Select Key Vault Administrator and select next button
    * Add my user account and click next

![kvimg3](assets/kv3.jpg)

Click Review + Assign button

## Key Vault and Generate Secrets

Next, create two secrets that represent SQL Authentication account credentials. One secret represents the user and second secret represents the password.

Create First Secret
_ Within Key Vault, click Secrets
_ click Generate/Import button  
 _ Upload options: manual
_ Name: sqlusr
_ Secret Value: funcusr
_ remaining options leave default

![kvimg4](assets/kv4.jpg)

    * click Create button

![kvimg5](assets/kv5.jpg)

Create Second Secret
_ Within Key Vault, click Secrets
_ click Generate/Import button  
 _ Upload options: manual
_ Name: sqlpasswrd
_ Secret Value: yourpasswordhere
_ remaining options leave default

![kvimg6](assets/kv6.jpg)

    * click Create Button

![kvimg7](assets/kv7.jpg)

## Grant Azure Function Managed Identity access to read secrets

    * within Azure Key Vault, select Access Control (IAM)
    * click Add role assignment button
    * select Key Vault Secrets User
    * click Next
    * under members tab
        * Assign Access To: Managed Identity
        * Members: click to select members
        * use drop downs and locate your managed identity

![kvimg8](assets/kv8.jpg)

        * click select button

![kvimg9](assets/kv9.jpg)

        * click review + Assign button
