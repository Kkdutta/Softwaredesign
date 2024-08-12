from datetime import datetime

book_data = [
        {
            'title': 'To Kill a Mockingbird',
            'author': 'Harper Lee',
            'publication_date': datetime.strptime('1960-07-11', '%Y-%m-%d'),
            'sales_data': '10 million copies sold'
        },
        {
            'title': 'The Lord of the Rings',
            'author': 'J.R.R. Tolkien',
            'publication_date': datetime.strptime('1954-07-29', '%Y-%m-%d'),
            'sales_data': '150 million copies sold'
        },
        {
            'title': 'The Hunger Games',
            'author': 'Suzanne Collins',
            'publication_date': datetime.strptime('2008-09-14', '%Y-%m-%d'),
            'sales_data': '100 million copies sold'
        },
        {
            'title': 'Pride and Prejudice',
            'author': 'Jane Austen',
            'publication_date': datetime.strptime('1813-01-28', '%Y-%m-%d'),
            'sales_data': '20 million copies sold'
        },
        {
            'title': 'The Lion, the Witch and the Wardrobe',
            'author': 'C.S. Lewis',
            'publication_date': datetime.strptime('1950-11-16', '%Y-%m-%d'),
            'sales_data': '85 million copies sold'
        },
        {
            'title': 'The Great Gatsby',
            'author': 'F SCOTT FITZGERALD',
            'publication_date': datetime.strptime('1925-04-10', '%Y-%m-%d'),
            'sales_data': '30 million copies sold'
        }
    ]
