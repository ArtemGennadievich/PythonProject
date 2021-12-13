class Book:
    name = 'name'
    data_facture = 'data_facture'
    author_book = 'author_book'
    book_publisher = 'book_publisher'
    price = "price"
    genre = 'genre'

    def out_write(self):
        print('Book legend'.center(40))
        print('*' * 55)
        print(f' Перед вами книга "{self.name}", {self.data_facture} года выпуска.\n Выпущеная издателем "'
              f'{self.book_publisher}".\n Автор этой книги {self.author_book} использовал жанр - {self.genre}.\n '
              f'На данный момент эта книга оценивается в {self.price} рублей.'.center(40))
        print('*' * 55)

    def save_value(self, name, data_facture, author_book, book_publisher, price, genre):
        self.name = name
        self.data_facture = data_facture
        self.author_book = author_book
        self.book_publisher = book_publisher
        self.price = price
        self.genre = genre

    def set_value_name(self):
        return f'Название книги: {self.name}'

    def set_value_data_facture(self):
        return f"Даты выпуска книги: {self.data_facture} год"

    def set_value_author_book(self):
        return f"Автор книги: {self.author_book}"

    def set_value_book_publisher(self):
        return f"Издатель книги: {self.book_publisher}"

    def set_value_price(self):
        return f"Стоимость книги: {self.price} рублей"

    def set_value_genre(self):
        return f"Жанр книги: {self.genre}"


book = Book()
book.out_write()
book.save_value('Вокруг света за 80 дней', '1872', 'Жюль Верн', 'Пьер-Жюль Этцель', '5000', 'приключенческий роман')
book.out_write()
print(book.set_value_name())
print(book.set_value_data_facture())
print(book.set_value_book_publisher())
print(book.set_value_genre())
print(book.set_value_author_book())
print(book.set_value_price())

