# Simple Receipt CD

This is a CDK project which handles the continuous deployment of project [Simple Receipt API](../README.md).

It is based on **CodePipeline** and consists of only two *stages*, each one made of a single *action*. The first one uses downloads the git project from GitHub. The second one uses **CodeBuild** to run unit tests and deploy the application on CloudFormation.

It is very simple and a lot more could be made! Integration tests, a recovery plan from CloudFormation failures, are missing

## Usage

### Warm up!

First of all you need to setup a *personal access token* within your GitHub account and store the value of the token in a secret named **simple-receipt-api/github-token** in AWS SecretsManager.

Then you need to create a file `.env` containing some environment variable about the GitHub repository. Example:

    SIMPLE_RECEIPT_GITHUB_OWNER=tatma
    SIMPLE_RECEIPT_GITHUB_REPO=simple-receipt-api
    SIMPLE_RECEIPT_GITHUB_BRANCH=master
 

The stack is region and account agnostic, so you need also to setup config and credentials.

### Deploy the pipeline

    cdk deploy simple-receipt-cicd

*Note*: you have to be in a virtual environment.

Software licensed under [GNU General Public License v3](./LICENSE.md).