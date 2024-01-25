# TODO Найдите количество книг, которое можно разместить на дискете

bytes_for_sym = 4
pages = 100
lines = 50
symbols = 25

disk_size = 1.44 * 1024 * 1024

number_of_books = int(disk_size // (bytes_for_sym * symbols * lines * pages))

print("Количество книг, помещающихся на дискету:", number_of_books)


