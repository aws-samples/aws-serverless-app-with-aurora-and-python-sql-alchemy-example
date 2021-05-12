from bookstore_orm_objects import create_db_schema, Book, Review, Inventory
from bookstore_utils import create_db_session, create_db_engine

if __name__ == '__main__':

    db_conn_string = 'sqlite:///:memory:'
    engine = create_db_engine(db_conn_string)
    session = create_db_session(engine)
    create_db_schema(engine)

    book = Book(
        title='AWS Certified Solutions Architect Associate Training Notes 2020: '
              'Fast-track your exam success with the ultimate cheat sheet for '
              'the SAA-C02 exam',
        author='Neal Davis',
        publisher='Amazon.com Services LLC',
        year=2019)
    book.reviews = [
        Review(
            reviewer='John Smith',
            rate=5,
            review='Loved this book. I passed the exam on the first attempt!'
        ),
        Review(
            reviewer='Mary Smith',
            rate=5,
            review='I really enjoyed the examples provided.'
        )
    ]
    book.inventory = [
        Inventory(
            warehouse_id=100,
            quantity=10
        ),
        Inventory(
            warehouse_id=200,
            quantity=5
        ),
    ]
    session.add_all([book])

    books = session.query(Book)
    for book in books:
        print(book)
        for r in book.reviews:
            print('\t review: %s' % r)
        for i in book.inventory:
            print('\t inventory: %s' % i)
