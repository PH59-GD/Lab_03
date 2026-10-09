LBooks = []
LUser = []
LAuthor = []

class Book:
    def __init__(self):
        self.Book_ID = ""
        self.Book_title = ""
        self.Author_ID = ""
        self.Publisher = ""
        self.Year_of_publication = ""
        self.Checked_out = 0
    def Create_new_book(self):
        self.Book_ID = input("Book ID: ")
        self.Book_title = input("Book Title: ")
        self.Publisher = input("Book Publisher: ")
        self.Year_of_publication = input("Year of publication: ")
    def Assign_author(self):
        UC = input("Enter Author ID: ")
        for i in range(len(LAuthor)):
            if UC == LAuthor[i].AuthorID:
                self.Author_ID = LAuthor[i].AuthorID
                
                
    def Display_book(self):
        print("Book Title:", self.Book_title)
        print("Book ID:", self.Book_ID)
        print("Book Author ID:", self.Author_ID)
        print("Book Publisher:", self.Publisher)
        print("Book year of publication:", self.Year_of_publication)
class Author:
    def __init__(self):
        self.Author_ID = ""
        self.Author_Name = ""
        self.Affiliation = ""
        self.Country = ""
        self.Phone = ""
        self.Email_ID = ""
        self.AuthoredB = []
    def Create_new_author(self):
        self.Author_ID = input("Author ID: ")
        self.Author_Name = input("Author name: ")
        self.Affiliation = input("Author Affiliation: ")
        self.Country = input("Country: ")
        self.Phone = input("Phone: ")
        self.Email_ID = input("Email ID: ")
    def Display_author(self):
        print("Author ID",  self.Author_ID)
        print("Author Name", self.Author_Name)
        print("Author Affiliation", self.Affiliation)
        print("Country:", self.Country)
        print("Phone:", self.Phone)
        print("Email ID:", self.Email_ID)
    def Display_num_book_CO(self):
        print("Authored Books:", str(len(self.AuthoredB)))
        if len(self.AuthoredB) > 0:
            for i in range(len(self.AuthoredB)):
                for b in range(len(LBooks)):
                    if self.AuthoredB[i] == LBooks[i].Book_ID:
                        print("Title: "+LBooks[i].Book_title+" ID:"+ LBooks[i].Book_ID+ " Number Checked out: "+ str(LBooks[i].Checked_out))
class User:
    def __init__(self):
        self.User_ID = ""
        self.Name = ""
        self.Password = ""
        self.Address = ""
        self.Phone = ""
        self.Email_ID = ""
        self.Books_borrowed = []
    def Create_new_user(self):
        self.User_ID = input("User ID: ")
        self.Name = input("User's name: ")
        self.Password = input("Password: ")
        self.Phone = input("Phone: ")
        self.Email_ID = input("Email ID: ")
    def Display_user(self):
        print("User ID:", self.User_ID)
        print("User's Name:", self.Name)
        print("User's Password:", self.Password)
        print("Phone:", self.Phone)
        print("Email ID:", self.Email_ID)
        print("Books borrowed:", self.Books_borrowed)
    def Borrow_a_book(self):
        UC = input("Enter book ID: ")
        for i in range(len(LBooks)):
            if UC == LBooks[i].Book_ID:
                self.Books_borrowed.append(LBooks[i].Book_ID)

while True:
    print("")
    print("[1] Book")
    print("[2] User")
    print("[3] Author")
    print("")
    UC = input("Input: ")
    if UC == "1":
        print("")
        print("[1] Add book")
        print("[2] Assign Author")
        print("[3] Display book")
        print("")
        UC = input("Input: ")
        if UC == "1":
            Book = Book()
            Book.Create_new_book()
            LBooks.append(Book)
            print(LBooks)
        if UC == "2":
            UC = input("Book ID: ")
            OC = input("Enter Author's ID: ")
            for b in range(len(LAuthor)):
                if OC == LAuthor[b].Author_ID:
                    pass
                else:
                    break
            for i in range(len(LBooks)):
                if(UC == LBooks[i].Book_ID):
                    LBooks[i].Author_ID = OC
                    LAuthor[b].AuthoredB.append( LBooks[i].Book_ID)
        if UC == "3":
            UC = input("Book ID: ")
            for i in range(len(LBooks)):
                if (UC == LBooks[i].Book_ID):
                    LBooks[i].Display_book()
    if UC == "2":
        print("")
        print("[1] Add User")
        print("[2] Display User")
        print("[3] Borrow a book")
        print("")
        UC = input("Input: ")
        if UC == "1":
            User = User()
            User.Create_new_user()
            LUser.append(User)
            print(LUser)
        if UC == "2":
            UC = input("User ID: ")
            for i in range(len(LUser)):
                if (UC == LUser[i].User_ID):
                    LUser[i].Display_user()
        if UC == "3":
            CB = input("Enter book ID: ")
            CU = input("Enter User ID: ")
            for i in range(len(LBooks)):
                if CB == LBooks[i].Book_ID:
                    pass
            for a in range(len(LUser)):
                if CU == LUser[a].User_ID:
                    LUser[a].Books_borrowed.append(LBooks[i].Book_ID)
                    LBooks[i].Checked_out += 1
    if UC == "3":
        print("")
        print("[1] Add Author")
        print("[2] Display Author")
        print("[3] Display Checked out books")
        print("")
        UC = input("Input: ")
        if UC == "1":
            Author = Author()
            Author.Create_new_author()
            LAuthor.append(Author)
            print(LAuthor)
        if UC == "2":
            UC = input("Author ID: ")
            for i in range(len(LAuthor)):
                if (UC == LAuthor[i].Author_ID):
                    LAuthor[i].Display_author()
        if UC == "3":
            CA = input("Enter Author ID: ")
            for i in range(len(LAuthor)):
                if CA == LAuthor[i].Author_ID:
                    LAuthor[i].Display_num_book_CO()
                    