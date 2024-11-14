# lst = [10, 9, -6, 11, 7, -16, 50, 8]
# list2 = sorted(lst)
# list3 = sorted(lst, reverse=True)

# print(list2)
# print(list3)

# lst = [10, 9, -6, 11, 7, -16, 50, 8]
# list.sort(lst)
# print(lst)
# list.sort(lst, reverse=True)
# print(lst)

# How would you sort the following list of dictionaries based on the year of publication of each book, from the earliest to the most recent?
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
# def year_earliest_recent(book):
#     return int(book['published'])

# list1 = sorted(books, key=year_earliest_recent)
# print(list1)