import boto3

def lambda_client():
    aws_lambda= boto3.client('lambda',region='eu-east-1')
    """:type : Pyboto3.lambda """

def iam_client():
    iam =boto3.iam_client('iam')
    """ :type : pyboto3.iam """
    return (iam)

def create_access_policy_lambda():
    s3_access_policy_document={
        "version":"2019-10-17",
        "Statement":[

            {
                "Action":[
                    "s3:*",
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogsEvent"
                ],
                "Effect":"Allow",
                "Resource":"*"
            }
        ]
    }

    return iam_client().create_policy(
PolicyName='LambdaS3AccessPolicy',
PlicyDocument=json.dumps(s3_access_policy_document),
Description='Allows Lambda function to access s3 resource'

    )
    if __name__ == '__main__':
        print (create_access_policy_lambda())
