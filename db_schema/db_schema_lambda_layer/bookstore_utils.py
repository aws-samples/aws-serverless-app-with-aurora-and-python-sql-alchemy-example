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
This script creates the connection to the database using sqlalchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = None


def create_db_engine(db_conn_string, debug_mode=False):
    return create_engine(db_conn_string,
                         echo=debug_mode,
                         pool_size=1,
                         max_overflow=0,
                         pool_recycle=3600,
                         pool_pre_ping=True,
                         pool_use_lifo=True)


def create_db_session(engine):
    global Session
    if not Session:
        Session = sessionmaker(bind=engine)
        # todo: setup connection pooling properties
    return Session()
