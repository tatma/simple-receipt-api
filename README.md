# Simple Receipt API

This exercise focuses on using fully-managed cloud services.

If you want more details about this exercise, please refer to [`exercise.md`](./exercise.md).

#### TL;DR;
This is a Serverless project on AWS. You can deploy the stack with the following command:

    sls deploy

**But hey!** Why don't you use a CD pipeline? Give a look at section [Pipeline](#pipeline).

If you want to run unit tests:

    python -m pytest tests

*Note*: you have to be in a virtual environment.

## Overview
The solution has been implemented as a HTTP JSON API with a single resource which takes as input a list of products (described by fields title, price, category, quantity, imported) and responds with the receipt, which takes in account sales taxes.

**Want to have fun?** This API exposes a public endpoint: `https://ia1z6dfv4c.execute-api.eu-west-1.amazonaws.com/receipt`. 

### Usage example

Let's make a POST request with your favourite client. Remember to set `"Content-Type": "application/json"` in the header!
    
     POST https://ia1z6dfv4c.execute-api.eu-west-1.amazonaws.com/receipt
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

Field *imported* is not mandatory. It is *false* by default.
Valid values for *category* are `food`, `book`, `medical`, `cosmetic`, `entertainment`, and `other`.

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

If you want to test data defined in `exercise.md`, please refer to [`exercise_payloads.md`](./exercise_payloads.md)


## Architecture

The solution is hosted in the **AWS** cloud and leverages serverless services.
The API is exposed through API Gateway, which is backed by Lambda functions. Some advantages of this configuration are:
 * no server to manage;
 * high scalability;
 * high availability;
 * pay-per-use;

*Note*: it sounds great, but serverless and Lambda are not a silver bullet, so I'm just focusing on the good part of the whole story ☺

The application belongs to a CloudFormation stack, which is described *as code*. **Serverless Framework** has been chosen as IaC tool, because of its simplicity in configuring this type of applications.

Other services are used, but they're very marginal to understand the big picture. An **IAM** role has been assigned to the Lambda function just for giving permissions for logging to **CloudWatch**. Moreover, **S3** is used by Serverless Framework for deploying the code.

### <a name="pipeline"></a> Pipeline
A **continuous deployment pipeline** has been described as code, in a separated project built on top of CDK.

It should be versioned in a separated git project, but we're all aware that this is just a demo ☺.   

For implementation details, please refer to [`/pipeline/README.md`](./pipeline/README.md).

### Security
Fully-managed services have been chosen, therefore many responsibilities lie outside our duties.

IAM role attached to the components of the pipeline have fine graned permissions, for accomplishing the **principle of least privileges**.

Secrets have been stored in AWS Secrets Manager. 

## Project structure

### Needs
Let's make a very short analysis: the application is a HTTP API which takes some input data and returns other data. It's enough for detecting several duties, like:

* validating input data;
* applying the business logic, which is relatively complex;
* in case of errors, collecting sufficient information for the client to explain what happened;
* building the response for the client;

Software licensed under [GNU General Public License v3](./LICENSE.md).