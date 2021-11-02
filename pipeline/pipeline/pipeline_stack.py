from aws_cdk import (
    core,
    aws_codebuild as codebuild,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_iam as iam)


class PipelineStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, params, **kwargs) -> None:

        super().__init__(scope, construct_id, **kwargs)

        account_id = self.account
        region = self.region

        #
        # CodePipeline definition
        #
        pipeline = codepipeline.Pipeline(
            self,
            "SimpleReceiptApi",
            pipeline_name='simple-receipt-api-cicd',
            cross_account_keys=False
        )

        #
        # Stage 1: Source
        #
        source_output = codepipeline.Artifact()
        source_action = codepipeline_actions.GitHubSourceAction(
            action_name="Source",
            owner=params['owner'],
            repo=params['repo'],
            branch=params['branch'],
            oauth_token=core.SecretValue.secrets_manager('simple-receipt-api/github-token'),
            output=source_output,
            variables_namespace="simple-receipt-api"
        )
        pipeline.add_stage(stage_name="Source", actions=[source_action])


        #
        # Stage 2: Build
        #
        build_role = self.__build_project_role(account_id=account_id, region=region)
        build_action = codepipeline_actions.CodeBuildAction(
            action_name="Build",
            project=codebuild.PipelineProject(
                self,
                "BuildSimpleReceiptApi",
                role=build_role),
            input=source_output,
            # role=codebuild_role,
            environment_variables={
                "COMMIT_URL": {
                    "value": source_action.variables.commit_url
                }
            }
        )
        pipeline.add_stage(stage_name="Build", actions=[build_action])


    def __build_project_role(self, account_id, region):
        return iam.Role(
            self,
            'BuildProjectRole',
            role_name='simple-receipt-api-project',
            description='Used by CodeCommit in CI/CD pipeline',
            assumed_by=iam.CompositePrincipal(
                iam.ServicePrincipal("codebuild.amazonaws.com"),
                iam.AccountPrincipal(account_id)
            ),
            inline_policies={
                'deploy-on-cloudformation': iam.PolicyDocument(
                    statements=[
                        iam.PolicyStatement(
                            resources=['*'],
                            actions=[
                                "cloudformation:CreateStack",
                                "cloudformation:DescribeStacks",
                                "cloudformation:DescribeStackResource",
                                "cloudformation:DescribeStackEvents",
                                "cloudformation:UpdateStack",
                                "cloudformation:ListStacks",
                                "cloudformation:ListStackResources",
                                "cloudformation:ValidateTemplate",
                            ]),
                        iam.PolicyStatement(
                            resources=['*'],
                            actions=[
                                "iam:GetRole",
                                "iam:CreateRole",
                                "iam:PutRolePolicy",
                                "iam:PassRole"
                            ]),
                        iam.PolicyStatement(
                            resources=['*'],
                            actions=[
                                "lambda:CreateFunction",
                                "lambda:GetFunction",
                                "lambda:UpdateFunctionCode",
                                "lambda:UpdateFunctionConfig",
                                "lambda:UpdateFunctionConfiguration",
                                "lambda:GetFunctionConfiguration",
                                "lambda:ListVersionsByFunction",
                                "lambda:PublishVersion",
                                "lambda:AddPermission",
                                "lambda:GetFunctionCodeSigningConfig"
                            ]),
                        iam.PolicyStatement(
                            resources=['*'],
                            actions=[
                                "apigateway:POST"
                            ]),
                        iam.PolicyStatement(
                            resources=['*'],
                            actions=[
                                "s3:DeleteObject",
                                "s3:GetObject",
                                "s3:ListBucket",
                                "s3:PutObject",
                                "s3:CreateBucket",
                                "s3:SetBucketEncryption",
                                "s3:GetEncryptionConfiguration",
                                "s3:PutEncryptionConfiguration",
                                "s3:PutBucketPolicy",
                                "s3:PutBucketPolicy",
                                "s3:PutBucketTagging",
                                "kms:Decrypt",
                                "kms:GenerateDatakey",
                                "kms:Encrypt",
                                "kms:ReEncrypt*",
                                "kms:GenerateDataKey*"
                            ]),
                        iam.PolicyStatement(
                            resources=[f'arn:aws:logs:{region}:{account_id}:log-group:/*'],
                            actions=[
                                "logs:CreateLogGroup",
                                "logs:CreateLogStream",
                                "logs:PutLogEvents"
                            ])
                    ]
                )
            }
        )