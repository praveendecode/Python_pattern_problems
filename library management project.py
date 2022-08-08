class library:
    def __init__(self,list):


        self.full_books_list=list

        self.available_books_list=list[:]#copy of main list


        self.lent_book={}


    def display_available_books(self):
       ''' book=input("enter the name of the book u want:")
        if book in self.available_books_list:
            print('yes available...you can borrow')
            for i in 
        elif book not in self.available_books_list:
            print("not available, check full book list and give book name")
            return'''
       print("These books available:")
       print()
       for book in self.available_books_list:
           print(book)

        

    def display_fUll_book_list(self):
        
        print("These books available:")
        print()
        for book in self.full_books_list:
            print(book)
            
    def borrow_book(self,name,bookname):

        if bookname not in self.available_books_list:
            print("invalid book name")
            return
        elif bookname  in self.available_books_list:
            print("valid book name")
            self.lent_book.update({bookname:name})
            self.available_books_list.remove(bookname)
        
    def return_book(self,book):
        del self.lent_book[book]
        self.available_books_list.append(book)
        
    def quit(self):
        print("thank you you may go ......")

    def libmanagement(self):
        print('accessed person:',self.lent_book)


if __name__=='__main__':
    lib=library(['book1','book2','book3'])
    print("hi you are accesing lib books ......choice options below!!!")
    
    while True:

        print("*************list of options here************")
        print()
        print('1.display all books' )
        print()
        
        print('2.display available books' )
        print()

        print('3.Borrow a book')
        print()

        print('4.return books' )
        print()
        print('5.quit')
        print()
        print('6.access lib history')
        print()

        choice=input("enter the choice:")
        if choice=="1":
            lib.display_fUll_book_list()

        elif choice=="2":
            lib.display_available_books()

        elif choice=="3":
            name=input("enter your name:")
            bookname=input("enter your book name:")
            lib.borrow_book(name,bookname)
            

        elif choice=="4":
            book=input("enter book name:")
            
            lib.return_book(book)

        elif choice=="5":
            lib.quit()

        elif choice=="6":
            lib.libmanagement()
        else:
            print("choice invalid!!!!! enter valid choice from 1 to 5.....")





            
