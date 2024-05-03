class Bookshop:
    def __init__(self,f):
        self.f = f
    def import_file(self): 
        try:
            with open("bookshop.txt", 'r') as fayl:
                royxat = fayl.readlines()
            return royxat
        except FileNotFoundError:
            print("Fayl topilmadi.")
            return []
        
    def remove_book(self,bookname):
        listt = self.import_file()
        if bookname in listt:
            listt.remove(bookname)
            
        with open("bookshop.txt", 'w') as fayl:
                for kitob in listt:
                    fayl.write(kitob)
        print(f"{bookname} nomli kitob ro'yxatdan o'chirildi.")
                  
    def add_book(self,bookname):
        with open("bookshop.txt", 'a') as fayl:
            fayl.write('\n'+bookname + '\n')
            print(f.read())

    def show_books(self):
        f = open("bookshop.txt", "r")
        print(f.read())
f = open("bookshop.txt","r")   
obj = Bookshop(f)
# obj.add_book(input("kiritmoqchi bo'lgan kitob nomi: "))
obj.remove_book(input("o'chirmoqchi bo'lgan kitob nomi: "))
# obj.show_books()