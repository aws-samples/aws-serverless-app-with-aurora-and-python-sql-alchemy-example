"""
Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
This script orchestrates the enablement and centralization of SecurityHub
across an enterprise of AWS accounts.
It takes in a list of AWS Account Numbers, iterates through each account and
region to enable SecurityHub.
It creates each account as a Member in the SecurityHub Master account.
It invites and accepts the invite for each Member account.
The Security Hub automation is based on the scripts published at
https://github.com/awslabs/aws-securityhub-multiaccount-scripts
"""

from bookstore_utils import create_db_engine, create_db_session
import boto3
import json
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
db_secret_name = os.getenv('AURORA_DB_SECRET_NAME')
db_proxy_endpoint = os.getenv('AURORA_DB_PROXY_ENDPOINT')
secrets_client = boto3.client('secretsmanager')

# Get DB credentials from AWS Secrets Manager
def get_db_secrets():
    """
    Return the secret string as a dictionary for secret name SECRET_NAME.
    """
    secret_response = secrets_client.get_secret_value(SecretId=db_secret_name)
    secrets = json.loads(secret_response['SecretString'])
    return secrets

# Get SQLAlchemy Session
def get_db_session():
    logger.info(f'Retrieving database access information from Secrets Manager\'s secret: "{db_secret_name}"')
    secrets = get_db_secrets()
    db_name = secrets['dbname']
    db_conn_string = f"postgresql://{secrets['username']}:{secrets['password']}@{db_proxy_endpoint}:{secrets['port']}/{db_name}?sslmode=require"
    
    logger.info(f'Creating SQLAlchemy database engine for database: "{db_name}"')
    engine = create_db_engine(db_conn_string)
    session = create_db_session(engine)
    return session