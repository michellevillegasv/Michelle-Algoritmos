#Se desea implementar un sistema para el manejo de los libros de una librería, en donde cada
#libro tiene un título, un autor, número de páginas, número de capítulos, una editorial, número
#de edición, precio y cantidad disponible. En el caso de los autores, cada uno tendrá nombre,
#apellido, edad, cédula y nacionalidad. Para las editoriales, se maneja su nombre y dirección.
libros={}
autores = {}
def books_editorial_author():
    name = input("Enter the name of the book:")
    key_diccionary_book = name
    book = { 
        "Pages": int(input("Enter the number of pages: ")),
        "Chapters": int(input("Enter the number of chapters: ")),
        "Author":{
            "Author's Name": input("Enter the autor's name: "),
            "Last name": input("Enter the autor's last name: "),
            "Age": input("Enter the autors age: "),
            "ID number": input("Enter the authors ID number: "),
            "Nationality": input("Enther the author's nationality: ")
        },
        "Editorial": {
            "Editorial's Name": input("Enter the editorial: "),
            "Editorial Direction": input("Enter the direction of the editorial: ")
        },
        "Number of edition": input("Enter the number of the edition: "),
        "Price": input("Enter the price of the book: "),
        "Amount avaible": input("Enter the amount avaible:")
    }
    libros[key_diccionary_book]=book
def main():
    while True: 
        menu = input("Choose an option: \n1. Register a book \n2. Search a book \n3. Exit \n->")
        if menu == "1":
            book_register = books()
        if menu == "2":
            search = input("Enter the book you want to search: ")
            search.lower()
            for keys, values in libros.items():
                keys=str(keys).lower()
                if search == keys:
                    print(f"{search.upper()}:")
                    for keys2,values2 in values.items():
                        for name,data in values2:
                            print(f"{name}:{data}")
                else:
                    print("Not found")
        if menu=="3":
            break
main()
        
