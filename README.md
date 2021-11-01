# Simple Receipt API

This exercise focuses on using fully-managed cloud services.

If you want more details about this exercise, please refer to `exercize.md`.

#### TL;DR;
This is a Serverless project on AWS. You can deploy the stack with the following command:

    sls deploy

Looking for a CD pipeline? Give a look at section [Pipeline](#pipeline).

## The solution
The solution has been implemented as a HTTP JSON API with a single resource which takes as input a list of products (title, price, category, quantity, imported) and responds with the receipt, which takes in account applied taxes.

**Want to have fun?** This API exposes a public endpoint: `https://qudnfgaqrl.execute-api.eu-west-1.amazonaws.com/receipt`. 

### Usage example

Let's make a POST request with your favourite client. Remember to set `"Content-Type": "application/json"` in the header!
    
     POST https://qudnfgaqrl.execute-api.eu-west-1.amazonaws.com/receipt
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

Field "imported" is not mandatory. It is *false* by default.
Valid values for "category" are `food`, `book`, `medical`, `cosmetic`, `entertainment`, and `other`.

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

If you want to test data defined in `exercise.md`, please refer to `exercise_payloads.md`


## Architecture

The solution is hosted in the **AWS** cloud and leverages serverless services.
The API is exposed through API Gateway, which is backed by Lambda functions. Some advantages of this configuration are:
 * no server to manage;
 * high scalability;
 * high availability;
 * pay-per-use;

*Note*: it sounds great, but serverless and Lambda are not a silver bullet, so I'm just focusing on the good part of the whole story here ☺

The application belongs to a CloudFormation stack, which is described *as code*. **Serverless Framework** has been chosen as IaC tool, because of its simplicity in configuring this type of applications.

Other services are used, but they're very marginal to understand the big picture. An **IAM** role has been assigned to the Lambda function just for giving permissions for logging to **CloudWatch**. Moreover, **S3** is used by Serverless Framework for deploying the code.

### <a name="pipeline"></a> Pipeline
A **continuous development pipeline** has been implemented as code, in a separated project built on top of CDK.

It could be versioned in a separated git project, we're all aware of the fact that the this project is just a demo ☺.   

For implmentation details, please refer to `/pipeline/README.md`.

### Security
Fully managed services have been chosen, therefore many responsibilities lie outside our duties.

IAM roles used by the application and the pipeline have beed designed to respect the **principle of least privileges**.

Secrets have been stored in AWS Secrets Manager. 

## Project structure

#### Needs
The application is a HTTP API which takes some input data and returns other data. It's enough for detecting several duties, like:

* validating input data;
* applying the business logic, which is relatively complex;
* in case of errors, collecting sufficient information for the client to explain what happened;
* building the response for the client;

#### Code Organization
The project is organized through several directories in order to give an immediate overview of the components which the application is made of.
Anyway, the hierarchy of these components is quite *flat*. Indeed these components are independent each other and are exploited in series by the client, i.e the Lambda handler, which acts as a driver.

The Lambda handler `/handler/create_receipt.py` invokes several functions in order to:
* retrieve items from event, i.e the payload;
* validate retrieved items;
* build the basket, which contains the items;
* build the receipt using the basket's information;
* build the response for the remote client;
* ...and in the meanwhile this happens, it is ready to catch different kind of exceptions, in order to produce different "reason of failure" for the client;

**OOP** has been used mainly for addressing problems closer to the application domain:
   * classes in `/entity` are used for modeling;
   * classes in `/factory`, given a basket, allow to build the receipt;
   * classes in `/validator` parse some data and, if something is not correct, raise an exception with a custom message;
   * classes in `/exception` contain the definition of custom exceptions;

Some procedural-style functions have been defined to accomplish general tasks:
* `/api` contains some functions for building the API response;
* `/common` contains some general purpose functions;
 
 #### Principles
Data arrive in JSON format, so could be handled like Python dictionaries and also the receipt could be treated this way, resulting in nested structures. Imagine how difficult it could be for a new developer facing this project for the first time to understand the entire data structure. It is not immediate and would be a mess!
 
**OOP** has been used in order to avoid handling nesting dictionaries. We can take advantage of the intrinsic solidity of objects and visibility of members, implement SoC and understand faster how the application works. The developer can take a peek and understand quickly how data is organized. Furthermore, a lot of weight has been given to **SRP**, so each class is responsible for only one thing.
 
In the current implementation there is a single class for all the products, named **Product**. Taxes are calculated differently on the basis of the value of the field **category** in Product.
Another possible implementation is the use of **inheritance**. In that case, Product would be abstract and extended by concrete classes Book, Food, Medical, and so on. The tax calculation would work based on the instance type of objects. This solution would be longer to code and there would be a distinct class for each kind of product. Above all, it brings no additional value. This phylosophy of avoiding uneuseful complexity and focusing only on satisfying requested features is the basis of the **KISS** principle.