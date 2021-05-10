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

import json
import logging
import db_connection
from bookstore_orm_objects import Book

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

session = db_connection.get_db_session()

def get_books():
    try:
        books = session.query(Book)
        results = [
            { "id": book.id,
              "title": book.title,
              "author": book.author,
              "publisher": book.publisher,
              "year": book.year }
            for book in books
        ]

        return {
            "statusCode": 200,
            "body": json.dumps({
                "books": results
            })
        }
    except Exception as e:
        logger.debug(e)
        return {
            "statusCode": 500,
            "error": f"Error: {e}"
        }


def put_book(event):
    try:
        req = json.loads(event['body'])
        book = Book(
            title=req['title'],
            author=req['author'],
            publisher=req['publisher'],
            year=int(req['year'])
        ) 
        logger.debug(f"Inserting: {book}")
        session.add(book)
        session.commit()

        return {
            "statusCode": 200
        }
    except Exception as e:
        logger.debug(e)
        return {
            "statusCode": 500,
            "error": f"Error: {e}"
        }

def lambda_handler(event, context):
    
    logger.debug(event)

    if (event['httpMethod'] == 'PUT'):
        response = put_book(event)
    elif (event['httpMethod'] == 'GET'):
        response = get_books();
    else:
        logger.debug(f"No handler for http verb: {event['httpMethod']}")
        raise Exception(f"No handler for http verb: {event['httpMethod']}")
        
    return response