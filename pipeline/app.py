#!/usr/bin/env python3
import os

from aws_cdk import core
from dotenv import load_dotenv

from pipeline.pipeline_stack import PipelineStack

load_dotenv(dotenv_path='./.env')

app = core.App()
PipelineStack(app, "simple-receipt-cicd",
              env=core.Environment(
                  account=os.environ['CDK_DEFAULT_ACCOUNT'],
                  region=os.environ['CDK_DEFAULT_REGION']),
              params={
                  'owner': os.environ['SIMPLE_RECEIPT_GITHUB_OWNER'],
                  'repo': os.environ['SIMPLE_RECEIPT_GITHUB_REPO'],
                  'branch': os.environ['SIMPLE_RECEIPT_GITHUB_BRANCH']})

app.synth()
