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

from sqlalchemy import Column, Integer, String, SmallInteger
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


def create_db_schema(engine):
    Base.metadata.create_all(engine)


class Book(Base):
    """
    Our Book class
    """
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    publisher = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Book(title='%s', author='%s', publisher='%s', year='%d')>" % (
            self.title, self.author, self.publisher, self.year)

    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

class Review(Base):
    """
    Our Review class
    """
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    reviewer = Column(String(100), nullable=False)
    rate = Column(SmallInteger, nullable=False)  # 1-5 stars
    review = Column(String(500), nullable=True)
    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship("Book", back_populates="reviews")

    def __repr__(self):
        return "<Review(reviewer='%s', rate='%d', review='%s', book_id='%s')>" % (
            self.reviewer, self.rate, self.review, self.book_id)


# 1 Book <-> 0 or more Reviews
Book.reviews = relationship("Review", order_by=Review.id, back_populates="book")
