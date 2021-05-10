
# Intro

This project is companion source code to the AWS Database blog post: [Using Python SQL Alchemy ORM to Interact with an Amazon Aurora Database from a Serverless Application](TODO). Please read the blog post for details.

Below, we depict the AWS architecture discussed in the blog as a reference. The various components depicted in the architecture can be deployed using the code in this repository.

![Alt text](docs/blog-sql-alchemy-solution-diagram.png?raw=true "Python SQLAlchemy in an AWS Bookstore Serverless Application")

# Requirements

In order to deploy the solution in this repository you'll need the following:

* Access to an AWS account
* [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
* [AWS SAM Command Line Interface](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Python 3.7.x installed

# Installing the required libraries in the Lambda Layer

This project uses Lambda functions that depend on libraries deployed to a Lambda layer. So, the first step is to make sure these libraries are installed properly in the Lambda layer.

Run the commands below in a sandbox environment similar to your Lambda function's environment. This is required as package `psycopg2-binary` is OS-dependent. If you prefer, you can use a Docker image for that (e.g., https://hub.docker.com/r/lambci/lambda/).

```
cd db_schema/db_schema_lambda_layer/
python -m pip install -r requirements.txt -t "python/"
```

# Deploying the solution
Please check this [blog post](TODO) for details.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

