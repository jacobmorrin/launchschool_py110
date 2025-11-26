"""
PROBLEM:
How would you sort the following list of dictionaries based 
on the year of publication of each book, from the earliest 
to the most recent?

EXAMPLE:

"""
def get_year(book):
    return int(book['published'])

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

books_sorted = sorted(books, key=get_year)
print(books_sorted)