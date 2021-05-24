import sqlite3           
class Contact:
        def __init__(self,first_name,last_name,number,db,id):
               self.first_name =str(first_name)
               self.last_name =str(last_name)
               self.number =int(number)
               self.db =db
               self.id = id
        def insert(self):
                self.db.execute(f"INSERT INTO mahiroi VALUES ('{self.id+1}','{self.first_name}','{self.last_name}','{self.number}');")
                print("Inserted Success fully")
        #to update the database
        def update(self,OPTION,ITEM,ID):
                self.db.execute(f"UPDATE mahiroi set '{OPTION}' = '{ITEM}' WHERE ID ='{ID};'")
                print("Updated Successfuly")
        def delete(self,ID):
                self.db.execute(f"DELETE mahiroi WHERE ID = '{ID}';")
                print("deleted successfuly")
        def view(self):
                cur = self.db.execute("SELECT ID, FIRSTNAME,LASTNAME,NUMBER FROM mahiroi;")
                for item in cur:
                        print(f""" YOUR SAVED Contacts
                                 
                                 ID: '{item[0]}'
                                 FIRSTNAME:'{item[1]}'
                                 LASTNAME:'{item[2]}'
                                 NUMBER:'{item[3]}'

                                   """)                

def create_database():
        
        app  = sqlite3.connect("CONTACTBOOK.db")
        print("DATABASE connected success fully") 
        db =app.execute("""             CREATE TABLE mahiroi
                                        (ID INT PRIMARY KEY NOT NULL,
                                        FIRSTNAME TEXT NOT NULL,
                                        LASTNAME TEXT NOT NULL,
                                        NUMBER INT NOT NULL);""")
        return db

id =  0
print("HI WELCOME TO THE CONTACT BOOK")
print("We are happy to have you!!")


val = create_database()

while(True):
        NAME = input("ENTER YOUR NAME:")
        FIRST,LAST =NAME.split(" ")
        NUM = input("ENTER YOUR NUMBER")
        contact = Contact(FIRST,LAST,NUM,val,id)
        choice = input("IF YOU ARE GONNANA TO [U]PDATE | [D]ELETE | [C]REATE | [I]NSERT | [E]xit | [V]iew")
        if choice != None:
                if choice.lower() == 'i':
                        contact.insert()
                        id = id+1  
                elif choice.lower() == "u":
                        opt = input("What to do you wnat to update: ")
                        item = input("Item that you Wnat To change: ")
                        id1 = input("Enter YouR id")
                        contact.update(opt,item,int(id1))
                elif choice.lower() == 'd':
                        id2 = input("Enter The Id")
                        contact.delete(int(id2)) 
                elif choice.lower == 'v':
                        contact.view()
                elif choice.lower == "e":
                        break 