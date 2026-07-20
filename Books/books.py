import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Title getter & setter
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, new_title):
        if not new_title:
            raise ValueError("Error: Title Can Not Be Empty")
        self.__title = new_title

    # Author getter & setter
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, new_author):
        if not new_author:
            new_author = "Unknown"
        self.__author = new_author

    # Year getter & setter
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if new_year == "Unknown" or not new_year:
            self.__year = "Unknown"
            return

        if new_year < 0 or new_year > 2026:
            raise ValueError("Error: Year must be between 0 and 2026")

        self.__year = new_year


class BookManager:
    def __init__(self, filename="Books/books_db.json"):
        self.filename = filename
        self.books = []  # აქ შეინახება Book კლასის ობიექტები
        self.load_books()  # პროგრამის ჩართვისას ავტომატურად ვკითხულობთ JSON-ს

    # ფაილიდან წაკითხვა და ობიექტებად გადაქცევა
    def load_books(self):

        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                book_obj = Book(item["title"], item["author"], item["year"])
                self.books.append(book_obj)


    # ფაილში შენახვა
    def save_books(self):
        # რადგან JSON-ში პირდაპირ Book ობიექტს ვერ ჩავწერთ, მათ ისევ ლექსიკონებად ვაქცევთ
        json_data = []
        for book in self.books:
            json_data.append({
                "title": book.title,
                "author": book.author,
                "year": book.year
            })
        
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2, ensure_ascii=False)

    # წიგნის დამატება
    def add_book(self, book_obj):
        self.books.append(book_obj)
        self.save_books()
        print(f"\nBook '{book_obj.title}' successfully added and saved!")

    # ყველა წიგნის ნახვა
    def see_books(self):
        if not self.books:
            print("\nNo books found in the library.")
            return

        print("\n" + "=" * 20, "Library Books", "=" * 20)
        for index, book in enumerate(self.books, 1):
            print(f"{index}. Title: '{book.title}' | Author: {book.author} | Year: {book.year}")
        print("=" * 55)

    # წიგნის ძებნა სათაურით
    def search_book(self, search_title):
        search_title = search_title.strip().lower()
        found_books = []

        for book in self.books:
            if search_title in book.title.lower():
                found_books.append(book)

        if found_books:
            print(f"\nFound {len(found_books)} match(es):")
            for book in found_books:
                print(f"Title: '{book.title}' | Author: {book.author} | Year: {book.year}")
        else:
            print(f"\nNo book found with the title containing '{search_title}'.")


# ვალიდაციები
def get_choice(prompt: str) -> int:
    while True:
        try:
            choice = int(input(prompt))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Error, Choose (1, 2, 3 or 4)!")
        except ValueError:
            print("Error, Input Must Be a Number Only!")



def get_year(prompt: str):
    while True:
        year_input = input(prompt).strip()

        if not year_input:
            year_input = "Unknown"
            return year_input

        if not year_input.isdigit():
            print("Error: Year must contain digits only!")
            continue

        if len(year_input) != 4:
            print("Error: Year must be exactly a 4-digit number!")
            continue

        if int(year_input) < 0 or int(year_input) > 2026:
            print("Error: Year Is In Wrong Range (Max allowed 2026)!")
            continue

        return year_input
    


def get_author(prompt: str) -> str:
    while True:
        name = input(prompt).strip()

        if not name:
            name = "Unknown"

        return name

def get_title(prompt: str) -> str:
    while True:
        name = input(prompt).strip()

        if not name:
            print("Error: Author name cannot be empty!")
            continue

        return name


# --- მთავარი პროგრამა ---

manager = BookManager()

while True:
    print("\n" + "=" * 10, "Book Manager", "=" * 10)
    print("1. Add Book")
    print("2. See All Books")
    print("3. Search For a Book")
    print("4. Exit")

    user_choice = get_choice("Type (1, 2, 3 or 4): ")

    if user_choice == 1:
        print("\n--- Add a New Book ---")

        title = get_title("Enter Title: ")
        author = get_author("Enter Author: ")
        year = get_year("Enter Year: ")           

        new_book = Book(title, author, year)
        manager.add_book(new_book)
        

    elif user_choice == 2:
        manager.see_books()

    elif user_choice == 3:
        print("\n--- Search Book ---")
        title_to_search = get_title("Enter the title to search for: ")
        manager.search_book(title_to_search)

    elif user_choice == 4:
        print("\nGoodbye! Library manager closed.")
        break