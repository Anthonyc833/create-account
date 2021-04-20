import os
class back_frame_program ():
    def account(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        
        

    def create_text_editor ():
       
        name = input("enter in the name here: ")
        username = input("enter username here: ")
        password = input(" put in password here: ")
        Cpassword = input("confirm the password here: ")
        with open("passwords.txt", "w") as p:
            if password == Cpassword :
                os.system("notepad passwords.txt")
                w = p.write(name )
                x = p.write(username )
                y = p.write(password )
                print(p)
                p.close()
            else:
                print("error the passwords do not match")
            
        
        
    def view_password ():
        with open("passwords.txt", "r") as r:
            try:
                print(r.read())
            except FileNotFoundError:
                print("file isn't there")
            finally:
                r.close()

x = back_frame_program()
back_frame_program.create_text_editor()
back_frame_program.view_password()

