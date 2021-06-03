
# Intro

This project is companion source code to the AWS Database blog post: [Use Python SQLAlchemy ORM to interact with an Amazon Aurora database from a serverless application](https://aws.amazon.com/blogs/database/use-python-sqlalchemy-orm-to-interact-with-an-amazon-aurora-database-from-a-serverless-application/). Please read the blog post for details.

In the diagram below, we depict the AWS architecture discussed in the blog as a reference. The various components depicted in the architecture can be deployed using the code in this repository. 

![Alt text](docs/blog-sql-alchemy-solution-diagram.png?raw=true "Python SQLAlchemy in an AWS Bookstore Serverless Application")

# Prerequisites

In order to deploy the solution in this repository you'll need the following:

* An AWS account
* The latest version of the AWS Command Line Interface ([AWS CLI](https://aws.amazon.com/cli/)) configured and with permissions to deploy to the AWS account
* The [AWS Serverless Model (SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) CLI
* Python 3.8
* Clone this repository into your local environment

# Installing the required libraries in the Lambda Layer

This project uses Lambda functions that depend on libraries deployed to a Lambda layer. So, the first step is to make sure these libraries are installed properly in the Lambda layer.

Run the commands below in a sandbox environment similar to your Lambda function's environment. This is required as package `psycopg2-binary` is OS-dependent. If you prefer, you can use a Docker image for that (e.g., https://hub.docker.com/r/lambci/lambda/).

```
cd db_schema/db_schema_lambda_layer/
python -m pip install -r requirements.txt -t "python/"
```

# Deploying the solution
Please check our [blog post](TODO) for details.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

