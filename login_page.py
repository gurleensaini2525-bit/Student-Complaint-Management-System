import customtkinter as ctK
from tkinter import messagebox
import database 
import os
ctK.set_appearance_mode("System")
ctK.set_default_color_theme("blue")
app=ctK.CTk()
app.title("Student Login")
app.geometry("800x600")
app.configure(fg_color="#EAF4F5")
tittle=ctK.CTkLabel(app,text="Student Login",font=ctK.CTkFont(size=25,weight="bold"),text_color="#1F4E79")
tittle.pack(pady=30)

#USERNAME

username=ctK.CTkEntry(app,placeholder_text="Enter Username",width=350,height=45)
username.pack(pady=15)

#PASSWORD

password=ctK.CTkEntry(app,placeholder_text="Enter Password",show="*",width=350,height=45)
password.pack(pady=15)

#USER TYPE

user_type=ctK.CTkComboBox(app,values=["Student","Admin"],width=350,height=45)
user_type.pack(pady=15)
user_type.set("Select User Type")

#LOGIN BUTTON

def login():
    username_value = username.get()
    password_value = password.get()
    user_type_value = user_type.get()
    if user_type_value == "Select User Type":
        messagebox.showerror("Error", "Please select a user type.")
        return
    # Fixed Admin Login
    if user_type_value == "Admin":
        if username_value == "admin" and password_value == "admin123":
            messagebox.showinfo("Success", "Admin Login Successful!")
            os.environ["CMS_USER_TYPE"] = "Admin"
            app.destroy()
            import my_project
        else:
            messagebox.showerror("Error", "Invalid Admin username or password.")
        return
    # Student Login
    account = database.login_user(username_value,password_value,"Student")
    if account:
        messagebox.showinfo("Success", "Student Login Successful!")
        os.environ["CMS_USER_TYPE"] = "Student"
        app.destroy()
        import my_project
    else:
        messagebox.showerror("Error", "Invalid Student username or password.")

login_button=ctK.CTkButton(app,text="Login",width=350,height=45,fg_color="#1F4E79",hover_color="#163A5C",command=login)
login_button.pack(pady=20)

#SIGN UP 
signup_label=ctK.CTkLabel(app,text="Don't have an account?")
signup_label.pack(pady=5)

#SIGN UP WINDOW 

def create_account():
    signup_window=ctK.CTkToplevel(app)
    signup_window.title("Create Account")
    signup_window.geometry("600x650")
    signup_window.grab_set()

#YOUR FULL NAME,USERNAME,PASSWORD,CONFIRM PASSWORD AND USER TYPE
    
    title = ctK.CTkLabel(signup_window,text="Create Account",font=ctK.CTkFont(size=25, weight="bold"),text_color="#1F4E79")
    title.pack(pady=25) 

    name_entry = ctK.CTkEntry(signup_window,placeholder_text="Enter Full Name",width=350, height=45)
    name_entry.pack(pady=20)  

    username_entry = ctK.CTkEntry(signup_window,placeholder_text="Enter Username",width=350,height=45)
    username_entry.pack(pady=10) 

    password_entry = ctK.CTkEntry(signup_window,placeholder_text="Enter Password",width=350,height=45,show="*")
    password_entry.pack(pady=10)

    confirm_entry = ctK.CTkEntry(signup_window,placeholder_text="Confirm Password",width=350,height=45,show="*")
    confirm_entry.pack(pady=10)

    account_user_type=ctK.CTkComboBox(signup_window,values=["Student"],width=350,height=45)
    account_user_type.pack(pady=10)
    account_user_type.set("Student")



    #CHECK PASSWORD
    def check_password():
       if password_entry.get() == confirm_entry.get():
           database.create_user(name_entry.get(),username_entry.get(),password_entry.get(),account_user_type.get())
           messagebox.showinfo("Success","Account created successfully!")
           signup_window.destroy()
       else:      
          messagebox.showerror("Error","Password do not match.")   
                          
    create_button = ctK.CTkButton(signup_window,text="CREATE ACCOUNT",width=250,height=45,fg_color="#1F4E79",hover_color="#163A5C",command=check_password)
    create_button.pack(pady=20)

#SIGN UP BUTTON    

signup_button=ctK.CTkButton(app,text="SIGN UP",width=200,height=40,fg_color="#3498DB",hover_color="#217DBB",command=create_account)
signup_button.pack(pady=10)

app.mainloop()