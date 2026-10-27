import customtkinter as ctK
import os
from tkinter import messagebox
import add_complaint
import update_complaint
import delete_complaint
from view_complaint import ViewComplaintWindow
user_type = os.environ.get("CMS_USER_TYPE","Student")
ctK.set_appearance_mode("System")
ctK.set_default_color_theme("blue")
app=ctK.CTk()
app.configure(fg_color="#EAF2F8")
app.title("Complaint Management System")
app.geometry("900x600")
label=ctK.CTkLabel(app,text="Complaint Management System",font=ctK.CTkFont(size=28,weight="bold"),text_color="#2563EB")
label.grid(row=0,column=0,columnspan=2,padx=20,pady=(15,5))
accent_line=ctK.CTkFrame(app,height=3,width=80,fg_color="#0F766E",corner_radius=5)
accent_line.grid(row=1,column=0,columnspan=2,pady=(0,5))
subtitle=ctK.CTkLabel(app,text="Student Complaint Portal",font=ctK.CTkFont(size=14),text_color="#0F766E")
subtitle.grid(row=2,column=0,columnspan=2,padx=20,pady=(0,15))

frame=ctK.CTkFrame(app,fg_color="#F8FAFC",corner_radius=20,border_width=1,border_color="#B8C7D9")
frame.grid_columnconfigure(1,weight=1)
frame.grid_columnconfigure(0,weight=0,minsize=150)
frame.grid(row=3,column=0,columnspan=2,padx=80,pady=20,sticky="nsew")
section_label=ctK.CTkLabel(frame,text="Student Information",font=ctK.CTkFont(size=16,weight="bold"),text_color="#1E3A5F",fg_color="#E8F1FB",corner_radius=8,height=35,anchor="w")
section_label.grid(row=0,column=0,columnspan=2,padx=20,pady=(15,5),sticky="w")
app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)


#STUDENT NAME 

name_label=ctK.CTkLabel(frame,text="Student Name:",font=ctK.CTkFont(size=14,weight="bold"),text_color="#334155")
name_label.grid(row=1,column=0,padx=20,pady=15)
name_entry=ctK.CTkEntry(frame,placeholder_text="Enter your Name",fg_color="#FFFFFF",border_color="#B8C7D9",border_width=1,corner_radius=8,height=35)
name_entry.grid(row=1,column=1,padx=20,pady=10,sticky="ew")

#ROLL NUMBER

roll_label=ctK.CTkLabel(frame,text="Roll Number:",font=ctK.CTkFont(size=14,weight="bold"),text_color="#334155")
roll_label.grid(row=2,column=0,padx=20,pady=15)
roll_entry=ctK.CTkEntry(frame,placeholder_text="Enter your Roll number",fg_color="#FFFFFF",border_color="#B8C7D9",border_width=1,corner_radius=8,height=35)
roll_entry.grid(row=2,column=1,padx=20,pady=10,sticky="ew")

#DEPARTMENT

department_label=ctK.CTkLabel(frame,text="Department:",font=ctK.CTkFont(size=14,weight="bold"),text_color="#334155")
department_label.grid(row=3,column=0,padx=20,pady=15)
department_combo=ctK.CTkComboBox(frame,values=["Physics","Mathematics","Computer Science","Chemistry","Other"],fg_color="#FFFFFF",border_color="#B8C7D9",border_width=1,corner_radius=8,height=35,button_color="#2563EB",button_hover_color="#1D4ED8",dropdown_fg_color="#FFFFFF",dropdown_hover_color="#E8F1FB")
department_combo.set("Select Department")
department_combo.grid(row=3,column=1,padx=20,pady=10,sticky="ew")

#COURSE

course_label=ctK.CTkLabel(frame,text="Course:",font=ctK.CTkFont(size=14,weight="bold"),text_color="#334155")
course_label.grid(row=4,column=0,padx=20,pady=15)
course_entry=ctK.CTkEntry(frame,placeholder_text="Enter your Course",fg_color="#FFFFFF",border_color="#B8C7D9",border_width=1,corner_radius=8,height=35)
course_entry.grid(row=4,column=1,padx=20,pady=10,sticky="ew")

## YEAR

year_label = ctK.CTkLabel(frame,text="Year:",font=ctK.CTkFont(size=14, weight="bold"),text_color="#334155")
year_label.grid(row=5, column=0, padx=20, pady=15)
year_combo = ctK.CTkComboBox(frame,values=["1st Year", "2nd Year", "3rd Year","4th Year"],fg_color="#FFFFFF",border_color="#B8C7D9",border_width=1,corner_radius=8,height=35,button_color="#2563EB",button_hover_color="#1D4ED8",dropdown_fg_color="#FFFFFF",dropdown_hover_color="#E8F1FB",state="readonly")
year_combo.set("Select Year")
year_combo.grid(row=5, column=1,padx=20, pady=10,sticky="ew")

#CONTACT

contact_label=ctK.CTkLabel(frame,text="Contact Number:",font=ctK.CTkFont(size=14,weight="bold"),text_color="#334155")
contact_label.grid(row=6,column=0,padx=20,pady=15)
contact_entry=ctK.CTkEntry(frame,placeholder_text="Enter your Contact number",fg_color="#FFFFFF",border_color="#B8C7D9",border_width=1,corner_radius=8,height=35)
contact_entry.grid(row=6,column=1,padx=20,pady=10,sticky="ew")

#EMAIL

email_label=ctK.CTkLabel(frame,text="Email:",font=ctK.CTkFont(size=14,weight="bold"),text_color="#334155")
email_label.grid(row=7,column=0,padx=20,pady=15)
email_entry=ctK.CTkEntry(frame,placeholder_text="Enter your Email",fg_color="#FFFFFF",border_color="#B8C7D9",border_width=1,corner_radius=8,height=38)
email_entry.grid(row=7,column=1,padx=20,pady=10,sticky="ew")

# VALIDATE REQUIRED STUDENT DETAILS

def validate_student_details():
    student_name = name_entry.get().strip()
    roll_number = roll_entry.get().strip()
    department = department_combo.get().strip()
    course = course_entry.get().strip()
    year = year_combo.get().strip()
    if not student_name:
        messagebox.showwarning("Required Field","Please enter your Student Name.",parent=app)
        name_entry.focus()
        return False
    if not roll_number:
        messagebox.showwarning("Required Field","Please enter your Roll Number.",parent=app)
        roll_entry.focus()
        return False
    if department not in ["Physics","Mathematics","Computer Science","Chemistry","Other"]:
        messagebox.showwarning("Required Field","Please select your Department.",parent=app)
        return False
    if not course:
        messagebox.showwarning("Required Field","Please enter your Course.",parent=app)
        course_entry.focus()
        return False
    if year not in ["1st Year", "2nd Year", "3rd Year"]:
        messagebox.showwarning("Required Field","Please select your Year.",parent=app)
        return False
    return True

#BUTTON FRAME

button_frame=ctK.CTkFrame(frame)
button_frame.grid(row=8,column=0,columnspan=4,pady=15)

## ADD COMPLAINT BUTTON

def open_add_complaint():
    if not validate_student_details():
        return
    add_complaint.open_add_complaint(app,name_entry.get().strip(),roll_entry.get().strip(),department_combo.get(),course_entry.get().strip())
add_button = ctK.CTkButton(button_frame,text="ADD COMPLAINT",fg_color="#2563EB",hover_color="#1D4ED8",width=200,height=40,corner_radius=10,font=ctK.CTkFont(size=13, weight="bold"),command=open_add_complaint)
add_button.grid(row=0, column=0, padx=5)

#VIEW COMPLAINT BUTTON
def open_view_window():
    if not validate_student_details():
        return 
    app.view_window=ViewComplaintWindow(app)
view_complaints_button=ctK.CTkButton(button_frame,text="View Complaints",fg_color="#2563EB",hover_color="#1D4ED8",width=200,height=40,corner_radius=10,font=ctK.CTkFont(size=13,weight="bold"),command=open_view_window)
view_complaints_button.grid(row=0,column=3,padx=5)

#DELETE COMPLAINT BUTTON 
def open_delete_complaint():
    if not validate_student_details():
        return 
    app.delete_window = delete_complaint.DeleteComplaintWindow(app,name_entry.get(),roll_entry.get())
delete_button=ctK.CTkButton(button_frame,text="Delete Complaint",fg_color="#2563EB",hover_color="#1D4ED8",width=200,height=40,corner_radius=10,font=ctK.CTkFont(size=13,weight="bold"),command=open_delete_complaint)
delete_button.grid(row=0,column=2,padx=5)


#UPDATE COMPLAINT BUTTON
def open_update_complaint():
    if not validate_student_details():
        return 
    app.update_window = update_complaint.UpdateComplaintWindow(app)
update_button=ctK.CTkButton(button_frame,text="Update Complaint",fg_color="#2563EB",hover_color="#1D4ED8",width=200,height=40,corner_radius=10,font=ctK.CTkFont(size=13,weight="bold"), command=open_update_complaint)
update_button.grid(row=0,column=1,padx=5)

# LOGOUT
def logout():
    confirm = messagebox.askyesno("Logout","Are you sure you want to logout?",parent=app)
    if confirm:
        app.destroy()
        os.system('python login_page.py')
logout_button = ctK.CTkButton(frame,text="Logout",width=150,height=38,corner_radius=8,fg_color="#0F766E",hover_color="#115E59",command=logout)
logout_button.grid(row=9,column=0,columnspan=4,pady=15)















app.mainloop()