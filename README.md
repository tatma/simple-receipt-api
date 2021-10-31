# Simple Receipt API

This exercise focuses on using fully-managed cloud services.

If you want more details about this exercise, please refer to `exercize.md`.

## The solution
The solution has been implemented as a HTTP JSON API with a single endpoint which takes as input a list of products (title, price, category, quantity, imported) and responds with the receipt, which takes in account applied taxes.

**Want to have fun?** This API exposes a public endpoint: `https://41q21i0d50.execute-api.eu-west-1.amazonaws.com/receipt`. 

### Usage example

Let's make a HTTP request with your favourite client.
    
     POST https://41q21i0d50.execute-api.eu-west-1.amazonaws.com/receipt
        {
            "items": [
                {
                    "title": "Alleycat by Nucleus", 
                    "price": 12.49, 
                    "category": "entertainment", 
                    "quantity": 1,
                    "imported": true
                }, 
                {
                    "title": "Gentleman by Fela Kuti", 
                    "price": 9.85,
                    "category": "entertainment",
                    "quantity": 1
                }
            ]
        }

The API *should* respond with HTTP status **201**:

    {
        "items": [
            {
                "product": "Alleycat by Nucleus",
                "quantity": 1,
                "amount": 14.39
            },
            {
                "product": "Gentleman by Fela Kuti",
                "quantity": 1,
                "amount": 10.85
            }
        ],
        "sales_taxes": 2.9,
        "total": 25.24
    }

Valid values for categories are `food`, `book`, `medical`, `cosmetic`, `entertainment`, and `other`. 


## Architecture

The solution is hosted in the **AWS** cloud and leverages serverless services.
The API is exposed through API Gateway, which is backed by Lambda functions. Some advantages of this configuration are:
 * no server to manage;
 * high scalability;
 * high availability;
 * pay-per-use;

*Note*: it sounds great, but serverless and Lambda are not a silver bullet, so I'm just focusing on the good part of the whole story here ☺

The application belongs to a CloudFormation stack, which is described *as code*. **Serverless Framework** has been chosen as IaC tool, because of its simplicity in configuring this type of applications.

Other services are used, but they're very marginal to understand the big picture. An **IAM** role has been assigned to the Lambda function just for giving permissions for logging to **CloudWatch** (anyway, it is important to respect the minimum privileges principle). Moreover, **S3** is used by Serverless Framework for deploying the code.

### Project structure

#### Needs
The application is a HTTP API which takes some input data and returns other data. It's enough for detecting several duties, like:

* validating input data;
* applying the business logic, which is relatively complex;
* in case of errors, collecting sufficient information for the client to explain what happened;
* building the response for the client;

#### Code Organization
The project is organized through several directories in order to give an immediate overview of the components which the application is made of.
Anyway, the hierarchy of these components is quite *flat*. Indeed these components are independent each other and are exploited in series by the client, which is the Lambda handler.

The Lambda handler `/handler/create_receipt.py` invokes several functions in order to:
* retrieve items from event, i.e the payload;
* build the structure for the basket (which contains the items);
* build the receipt;
* build the response for the remote client;
* ...and in the meanwhile this happens, it is ready to catch different kind of exceptions, in order to produce different "reason of failure" for the client;

The application uses **OOP**, in order to avoid handling nested dicts which in this case would be a mess. Instead we can leverage the intrinsic solidity of objects, visibility of members, and understand faster how the application works. To further facilitate general understanding, I have given a lot of weight to **SRP**, so each class is responsible for only one thing.

OOP has been used mainly for addressing problems closer to the application domain:
   * classes in `/entity` are used for modeling;
   * classes in `/factory`, given a basket, allow to build the receipt;
   * classes in `/validator` parses some data and if something is not correct, raise an Exception with a custom message;
   * classes in `/exception` contain the definition of custom exceptions;

Some procedural-style functions have been defined to accomplish general tasks:
* `/api` contains some functions for building the response for the API;
* `/common` contains some general purpose functions;
 