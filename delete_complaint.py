import customtkinter as ctk
from tkinter import messagebox
import database
class DeleteComplaintWindow(ctk.CTkToplevel):
    def __init__(self, parent,student_name,student_roll_no):
        super().__init__(parent)
        self.student_name=student_name
        self.roll_no=student_roll_no
        self.transient(parent)
        self.grab_set()
        self.focus_force()
        self.lift()
# Window
        self.title("Delete Complaint")
        self.geometry("1200x850")
        self.resizable(True, True)
        self.state("zoomed")
        self.configure(fg_color="#F5F9FF")
#HEADER
        header = ctk.CTkFrame(self,height=145,corner_radius=0,fg_color="#123B72")
        header.pack(fill="x")
        header.pack_propagate(False)
        # Icon
        ctk.CTkLabel(header,text="🗑️",font=("Segoe UI Emoji", 45),text_color="white").place(x=45, y=35)
        # Title
        ctk.CTkLabel(header,text="Delete Complaint",font=("Segoe UI", 32, "bold"),text_color="white").place(x=120, y=30)
        # Subtitle
        ctk.CTkLabel(header,text="Remove a complaint you submitted",font=("Segoe UI", 17),text_color="#DCEBFA").place(x=123, y=82)
#STUDENT PORTAL
        ctk.CTkLabel(header,text="👤  Student Portal",font=("Segoe UI", 16, "bold"),text_color="white").place(relx=0.92,rely=0.5,anchor="center")
#SCROLLABLE CONTENT 
        content=ctk.CTkScrollableFrame(self,fg_color="#F5F9FF",corner_radius=0)
        content.pack(fill="both",expand="True")
#SELECT COMPLAINT
        select_card = ctk.CTkFrame(content,fg_color="white",corner_radius=15)
        select_card.pack(fill="x",padx=45,pady=(30, 15))
        # Section title
        ctk.CTkLabel(select_card,text="Select Complaint",font=("Segoe UI", 22, "bold"),text_color="#123B72").pack(anchor="w",padx=25,pady=(20, 5))
# Description
        ctk.CTkLabel(select_card,text="Select the complaint you want to delete.",font=("Segoe UI", 14),text_color="#6B7C93").pack(anchor="w",padx=25,pady=(0, 15))
# Complaint dropdown
        self.complaint_dropdown = ctk.CTkComboBox(select_card,width=500,height=45,values=["Select Complaint"],font=("Segoe UI", 15),dropdown_font=("Segoe UI", 14),fg_color="#F5F9FF",border_color="#B8C7D9",border_width=1,button_color="#123B72",button_hover_color="#0E315F",text_color="#34506F")
        self.complaint_dropdown.pack(anchor="w",padx=25,pady=(0, 25))
        self.complaint_dropdown.set("Select Complaint")
        self.complaints = {}
        self.load_student_complaints()
        self.complaint_dropdown.configure(command=self.show_selected_complaint)
#COMPLAINT DETAILS
        details_card = ctk.CTkFrame(content,fg_color="white",corner_radius=15)
        details_card.pack(fill="x",expand=True,padx=45,pady=15)
        # Section title
        ctk.CTkLabel(details_card,text="Complaint Details",font=("Segoe UI", 22, "bold"),text_color="#123B72").pack(anchor="w",padx=25,pady=(20, 15))
        # Details area
        details_frame = ctk.CTkFrame(details_card,fg_color="#F5F9FF",corner_radius=12)
        details_frame.pack(fill="both",expand=True,padx=25,pady=(0, 25))
        # Subject
        ctk.CTkLabel(details_frame,text="Subject",font=("Segoe UI", 14, "bold"),text_color="#34506F").grid(row=0,column=0,sticky="w",padx=20,pady=(20, 5))
        self.subject_value = ctk.CTkLabel(details_frame,text="—",font=("Segoe UI", 14),text_color="#6B7C93")
        self.subject_value.grid(row=1,column=0,sticky="w",padx=20)
        # Category
        ctk.CTkLabel(details_frame,text="Category",font=("Segoe UI", 14, "bold"),text_color="#34506F").grid(row=0,column=1,sticky="w",padx=20,pady=(20, 5))
        self.category_value = ctk.CTkLabel(details_frame,text="—",font=("Segoe UI", 14),text_color="#6B7C93")
        self.category_value.grid(row=1,column=1,sticky="w",padx=20)
        # Urgency
        ctk.CTkLabel(details_frame,text="Urgency",font=("Segoe UI", 14, "bold"),text_color="#34506F").grid(row=0,column=2,sticky="w",padx=20,pady=(20, 5))
        self.urgency_value = ctk.CTkLabel(details_frame,text="—",font=("Segoe UI", 14),text_color="#6B7C93")
        self.urgency_value.grid(row=1,column=2,sticky="w",padx=20)
        # Status
        ctk.CTkLabel(details_frame,text="Status",font=("Segoe UI", 14, "bold"),text_color="#34506F").grid(row=0,column=3,sticky="w",padx=20,pady=(20, 5))
        self.status_value = ctk.CTkLabel(details_frame,text="—",font=("Segoe UI", 14),text_color="#6B7C93")
        self.status_value.grid(row=1,column=3,sticky="w",padx=20)
        # Description
        ctk.CTkLabel(details_frame,text="Description",font=("Segoe UI", 14, "bold"),text_color="#34506F").grid(row=2,column=0,sticky="w",padx=20,pady=(25, 5))
        self.description_value = ctk.CTkLabel(details_frame,text="Select a complaint to view its details",font=("Segoe UI", 14),text_color="#8A9AAD",anchor="w",justify="left")
        self.description_value.grid(row=3,column=0,columnspan=4,sticky="w",padx=20,pady=(0, 20))
# Make columns expand evenly
        for column in range(4):details_frame.grid_columnconfigure(column,weight=1)

#STUDENT INFORMATION
        student_card = ctk.CTkFrame(content,fg_color="white",corner_radius=15)
        student_card.pack(fill="x",padx=45,pady=15)
# Section title
        ctk.CTkLabel(student_card,text="Student Information",font=("Segoe UI", 22, "bold"),text_color="#123B72").pack(anchor="w",padx=25,pady=(20, 15))
# Information frame
        student_info = ctk.CTkFrame(student_card,fg_color="#F5F9FF",corner_radius=12)
        student_info.pack(fill="x",padx=25,pady=(0, 25))
# Name
        ctk.CTkLabel(student_info,text="Name",font=("Segoe UI", 13, "bold"),text_color="#34506F").grid(row=0,column=0,sticky="w",padx=20,pady=(15, 3))
        self.name_value=ctk.CTkLabel(student_info,text="—",font=("Segoe UI", 14),text_color="#6B7C93")
        self.name_value.grid(row=1,column=0,sticky="w",padx=20,pady=(0, 15))
# Roll Number
        ctk.CTkLabel(student_info,text="Roll Number",font=("Segoe UI", 13, "bold"),text_color="#34506F").grid(row=0,column=1,sticky="w",padx=20,pady=(15, 3))
        self.roll_no_value=ctk.CTkLabel(student_info,text="—",font=("Segoe UI", 14),text_color="#6B7C93")
        self.roll_no_value.grid(row=1,column=1,sticky="w",padx=20,pady=(0, 15))
# Department
        ctk.CTkLabel(student_info,text="Department",font=("Segoe UI", 13, "bold"),text_color="#34506F").grid(row=0,column=2,sticky="w",padx=20,pady=(15, 3))
        self.department_value=ctk.CTkLabel(student_info,text="—",font=("Segoe UI", 14),text_color="#6B7C93")
        self.department_value.grid(row=1,column=2,sticky="w",padx=20,pady=(0, 15))
# Course
        ctk.CTkLabel(student_info,text="Course",font=("Segoe UI", 13, "bold"),text_color="#34506F").grid(row=0,column=3,sticky="w",padx=20,pady=(15, 3))
        self.course_value=ctk.CTkLabel(student_info,text="—",font=("Segoe UI", 14),text_color="#6B7C93")
        self.course_value.grid(row=1,column=3,sticky="w",padx=20,pady=(0, 15))
# Equal column widths
        for column in range(4):
            student_info.grid_columnconfigure(column,weight=1)
#DELETE WARNING
        warning_card = ctk.CTkFrame(content,fg_color="#FFF7E6",corner_radius=12,border_width=1,border_color="#F2C66D")
        warning_card.pack(fill="x",padx=45,pady=15)
        ctk.CTkLabel(warning_card,text="⚠️  Deleting a complaint is permanent.",font=("Segoe UI", 15, "bold"),text_color="#9A6700").pack(anchor="w",padx=20,pady=(15, 3))
        ctk.CTkLabel(warning_card,text="You will not be able to recover it after deletion.",font=("Segoe UI", 13),text_color="#7A5A16").pack(anchor="w",padx=20,pady=(0, 15))
#Bottom BUTTONS
        button_frame = ctk.CTkFrame(content,fg_color="transparent")
        button_frame.pack(fill="x",padx=45,pady=(10, 30))
# Back button
        ctk.CTkButton(button_frame,text="←  Back",width=150,height=45,corner_radius=10,fg_color="#E7EEF7",hover_color="#D6E2F0",text_color="#34506F",font=("Segoe UI", 15, "bold")).pack(side="left")
# Delete button
        self.delete_button = ctk.CTkButton(button_frame,text="🗑️  Delete Complaint",width=210,height=45,corner_radius=10,fg_color="#D1D5DB",hover_color="#D1D5DB",text_color="#6B7280",font=("Segoe UI", 15, "bold"),state="disabled", command=self.delete_selected_complaint)
        self.delete_button.pack(side="right")   
        ctk.CTkFrame(content,height=40,fg_color="transparent").pack(fill="x")

    def load_student_complaints(self):
        complaints = database.get_student_complaints(self.student_name,self.roll_no)
        self.complaints = {}
        if not complaints:
            self.complaint_dropdown.configure(values=["No Complaints Found"])
            self.complaint_dropdown.set("No Complaints Found")
            return
        complaint_list = []
        for complaint in complaints:
            complaint_id = complaint[0]
            subject = complaint[7]
            display_text = f"CMS-{complaint_id}  |  {subject}"
            complaint_list.append(display_text)
            self.complaints[display_text] = complaint
        self.complaint_dropdown.configure(values=complaint_list)
        self.complaint_dropdown.set("Select Complaint")

    def show_selected_complaint(self, selected_complaint):
        if selected_complaint not in self.complaints:
            return
        complaint = self.complaints[selected_complaint]
        self.subject_value.configure(text=complaint[7])
        self.category_value.configure(text=complaint[5])
        self.urgency_value.configure(text=complaint[6])
        self.status_value.configure(text=complaint[10])
        self.description_value.configure(text=complaint[8])   
        self.name_value.configure(text=complaint[1])
        self.roll_no_value.configure(text=complaint[2])
        self.department_value.configure(text=complaint[3])
        self.course_value.configure(text=complaint[4]) 
        self.selected_complaint_id = complaint[0]
        self.delete_button.configure(state="normal",fg_color="#DC2626",hover_color="#B91C1C",text_color="white")

    def delete_selected_complaint(self):
        if not hasattr(self, "selected_complaint_id"):
            return
        confirm = messagebox.askyesno("Confirm Deletion","Are you sure you want to delete this complaint?\n\n"
            "This action cannot be undone.")
        if not confirm:
            return
        deleted = database.delete_complaint(self.selected_complaint_id,self.student_name,self.roll_no)
        if deleted:
            messagebox.showinfo("Complaint Deleted","The complaint has been deleted successfully.")
            self.destroy()
        else:
            messagebox.showerror("Delete Failed","The complaint could not be deleted.")


