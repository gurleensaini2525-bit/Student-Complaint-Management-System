import customtkinter as ctk
from tkinter import messagebox
import database


class UpdateComplaintWindow(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Update Complaint")
        self.geometry("1200x850")
        self.resizable(True,True)
        self.state("zoomed")
        self.transient(parent)
        self.grab_set()
        self.lift()
        self.focus_force()
        self.configure(fg_color="#F5F9FF")
        self.create_header()
        self.scroll_frame=ctk.CTkScrollableFrame(self,fg_color="#F5F9FF") 
        self.scroll_frame.pack(fill="both",expand=True)
        self.create_complaint_selection()
        self.create_complaint_information()
        self.create_edit_section()

#HEADER/TITLE/SUBTITLE

    def create_header(self):
        header = ctk.CTkFrame(self,height=120,corner_radius=0,fg_color="#1F4E79")
        header.pack(fill="x")
        header.pack_propagate(False)
        title = ctk.CTkLabel(header,text="✏️  Update Complaint",font=("Segoe UI", 28, "bold"),text_color="white")
        title.pack(pady=(22, 3))
        subtitle = ctk.CTkLabel(header,text="Modify your submitted complaint",font=("Segoe UI", 14),text_color="#D9EAF7")
        subtitle.pack() 

#COMPLAINT SELECTION CARD

    def create_complaint_selection(self):
        selection_card = ctk.CTkFrame(self.scroll_frame,corner_radius=15,fg_color="white")
        selection_card.pack(fill="x",padx=35,pady=(25, 15))
        heading = ctk.CTkLabel(selection_card,text="🔎  Find Your Complaint",font=("Segoe UI", 18, "bold"),text_color="#123B72")
        heading.pack(anchor="w",padx=25,pady=(18, 12))
        self.complaint_id_entry = ctk.CTkEntry(selection_card,placeholder_text="Enter Complaint ID (e.g. CMS-1024)",height=42,font=("Segoe UI", 14),border_color="#B8CBE0",fg_color="#F8FBFF")
        self.complaint_id_entry.pack(side="left",fill="x",expand=True,padx=(25, 10),pady=(0, 20))
        search_button = ctk.CTkButton(selection_card,text="🔍  Search",width=130,height=42,corner_radius=8,fg_color="#1F4E79",hover_color="#163A5C",font=("Segoe UI", 14, "bold"),command=self.search_complaint)
        search_button.pack(side="right",padx=(10, 25),pady=(0, 20)) 

#COMPLAINT INFORMATION 

    def create_complaint_information(self):
        info_card = ctk.CTkFrame(self.scroll_frame,corner_radius=15,fg_color="white")
        info_card.pack(fill="x",padx=35,pady=15)
        heading = ctk.CTkLabel(info_card,text="📋  Complaint Information",font=("Segoe UI", 18, "bold"),text_color="#123B72")
        heading.pack(anchor="w",padx=25,pady=(18, 15))
        details_frame = ctk.CTkFrame(info_card,fg_color="transparent")
        details_frame.pack(fill="x",padx=25,pady=(0, 20))

# Complaint ID
        ctk.CTkLabel(details_frame,text="Complaint ID",font=("Segoe UI", 13, "bold"),text_color="#34506F").grid(row=0, column=0, sticky="w", padx=(0, 20))
        self.complaint_id_value = ctk.CTkEntry(details_frame,height=40,font=("Segoe UI", 13),fg_color="#EEF3F8",border_color="#D2DEE9")
        self.complaint_id_value.grid(row=1, column=0, sticky="ew", padx=(0, 20))
# Student Name
        ctk.CTkLabel(details_frame,text="Student Name",font=("Segoe UI", 13, "bold"),text_color="#34506F").grid(row=0, column=1, sticky="w", padx=20)
        self.student_name_value = ctk.CTkEntry(details_frame,height=40,font=("Segoe UI", 13),fg_color="#EEF3F8",border_color="#D2DEE9")
        self.student_name_value.grid(row=1, column=1, sticky="ew", padx=20)
# Roll No.
        ctk.CTkLabel(details_frame,text="Roll No.",font=("Segoe UI", 13, "bold"),text_color="#34506F").grid(row=0, column=2, sticky="w", padx=(20, 0))
        self.roll_no_value = ctk.CTkEntry(details_frame,height=40,font=("Segoe UI", 13),fg_color="#EEF3F8",border_color="#D2DEE9")
        self.roll_no_value.grid(row=1, column=2, sticky="ew", padx=(20, 0))
        details_frame.grid_columnconfigure(0, weight=1)
        details_frame.grid_columnconfigure(1, weight=1)
        details_frame.grid_columnconfigure(2, weight=1)
# Department
        ctk.CTkLabel(details_frame,text="Department",font=("Segoe UI", 13, "bold"),text_color="#34506F").grid(row=2, column=0, sticky="w", padx=(0, 20), pady=(18, 5))
        self.department_value = ctk.CTkEntry(details_frame,height=40,font=("Segoe UI", 13),fg_color="#EEF3F8",border_color="#D2DEE9")
        self.department_value.grid(row=3, column=0, sticky="ew", padx=(0, 20))
# Course
        ctk.CTkLabel(details_frame,text="Course",font=("Segoe UI", 13, "bold"),text_color="#34506F").grid(row=2, column=1, sticky="w", padx=20, pady=(18, 5))
        self.course_value = ctk.CTkEntry(details_frame,height=40,font=("Segoe UI", 13),fg_color="#EEF3F8",border_color="#D2DEE9")
        self.course_value.grid(row=3, column=1, sticky="ew", padx=20)
# Current Status
        ctk.CTkLabel(details_frame,text="Current Status",font=("Segoe UI", 13, "bold"),text_color="#34506F").grid(row=2, column=2, sticky="w", padx=(20, 0), pady=(18, 5))
        self.status_value = ctk.CTkEntry(details_frame,height=40,font=("Segoe UI", 13),fg_color="#EEF3F8",border_color="#D2DEE9")
        self.status_value.grid(row=3, column=2, sticky="ew", padx=(20, 0))

        # Make complaint information read-only

        self.complaint_id_value.configure(state="readonly")
        self.student_name_value.configure(state="readonly")
        self.roll_no_value.configure(state="readonly")
        self.department_value.configure(state="readonly")
        self.course_value.configure(state="readonly")
        self.status_value.configure(state="readonly")

#EDIT SECTION 
    def create_edit_section(self):
        edit_card = ctk.CTkFrame(self.scroll_frame,corner_radius=15,fg_color="white")
        edit_card.pack(fill="x",padx=35,pady=15)
        heading = ctk.CTkLabel(edit_card,text="✏️  Complaint Details",font=("Segoe UI", 18, "bold"),text_color="#123B72")
        heading.pack(anchor="w",padx=25,pady=(18, 15))

# Category
        ctk.CTkLabel(edit_card,text="Category",font=("Segoe UI", 13, "bold"),text_color="#34506F").pack(anchor="w",padx=25,pady=(0, 5))
        self.category_menu = ctk.CTkOptionMenu(edit_card,values=["Academic Related","Infrastructure","Faculty / Staff","Examination","Fees / Finance","Other"],height=40,font=("Segoe UI", 13),fg_color="#F8FBFF",text_color="white",button_color="#1F4E79",button_hover_color="#163A5C",dropdown_fg_color="white",dropdown_hover_color="#EAF2F8")
        self.category_menu.pack(fill="x",padx=25,pady=(0, 15))
# Urgency
        ctk.CTkLabel(edit_card,text="Urgency",font=("Segoe UI", 13, "bold"),text_color="#34506F").pack(anchor="w",padx=25,pady=(0, 5))
        self.urgency_menu = ctk.CTkOptionMenu(edit_card,values=["Low","Medium","High"],height=40,font=("Segoe UI", 13),fg_color="#F8FBFF",text_color="white",button_color="#1F4E79",button_hover_color="#163A5C",dropdown_fg_color="white",dropdown_hover_color="#EAF2F8")
        self.urgency_menu.pack(fill="x",padx=25,pady=(0, 20))
# Subject
        ctk.CTkLabel(edit_card,text="Subject",font=("Segoe UI", 13, "bold"),text_color="#34506F").pack(anchor="w",padx=25,pady=(0, 5))
        self.subject_entry = ctk.CTkEntry(edit_card,height=40,placeholder_text="Enter complaint subject",font=("Segoe UI", 13),fg_color="#F8FBFF",border_color="#B8CBE0")
        self.subject_entry.pack(fill="x",padx=25,pady=(0, 15))
# Description
        ctk.CTkLabel(edit_card,text="Description",font=("Segoe UI", 13, "bold"),text_color="#34506F").pack(anchor="w",padx=25,pady=(0, 5))
        self.description_text = ctk.CTkTextbox(edit_card,height=130,font=("Segoe UI", 13),fg_color="#F8FBFF",border_color="#B8CBE0",border_width=1)
        self.description_text.pack(fill="x",padx=25,pady=(0, 20))

# Buttons
        button_frame = ctk.CTkFrame(edit_card,fg_color="transparent")
        button_frame.pack(fill="x",padx=25,pady=(0, 20))
        update_button = ctk.CTkButton(button_frame,text="✓  Update Complaint",height=44,width=180,corner_radius=8,fg_color="#1F4E79",hover_color="#163A5C",font=("Segoe UI", 14, "bold"),command=self.update_complaint)
        update_button.pack(side="left")
        clear_button = ctk.CTkButton(button_frame,text="↻  Clear",height=44,width=120,corner_radius=8,fg_color="#E8EEF5",hover_color="#D5E0EB",text_color="#34506F",font=("Segoe UI", 14, "bold"),command=self.clear_fields)
        clear_button.pack(side="left",padx=(12, 0))
        ctk.CTkFrame(edit_card,height=40,fg_color="transparent").pack()
    def search_complaint(self):
        complaint_id = self.complaint_id_entry.get().strip()
        if not complaint_id:
            messagebox.showwarning("Missing Complaint ID","Please enter a Complaint ID.")
            return
        # Remove CMS- prefix if entered
        if complaint_id.upper().startswith("CMS-"):
            complaint_id = complaint_id[4:]
        try:
            complaint_id = int(complaint_id)
        except ValueError:
            messagebox.showerror("Invalid Complaint ID","Please enter a valid Complaint ID.")
            return
        complaint = database.get_complaint_by_id(complaint_id)
        if not complaint:
            messagebox.showerror("Complaint Not Found","No complaint was found with this Complaint ID.")
            return
        # Fill Complaint Information
        self.complaint_id_value.configure(state="normal")
        self.complaint_id_value.delete(0, "end")
        self.complaint_id_value.insert(0, f"CMS-{complaint[0]}")
        self.complaint_id_value.configure(state="readonly")
        self.student_name_value.configure(state="normal")
        self.student_name_value.delete(0, "end")
        self.student_name_value.insert(0, complaint[1])
        self.student_name_value.configure(state="readonly")
        self.roll_no_value.configure(state="normal")
        self.roll_no_value.delete(0, "end")
        self.roll_no_value.insert(0, complaint[2])
        self.roll_no_value.configure(state="readonly")
        self.department_value.configure(state="normal")
        self.department_value.delete(0, "end")
        self.department_value.insert(0, complaint[3])
        self.department_value.configure(state="readonly")
        self.course_value.configure(state="normal")
        self.course_value.delete(0, "end")
        self.course_value.insert(0, complaint[4])
        self.course_value.configure(state="readonly")
        self.status_value.configure(state="normal")
        self.status_value.delete(0, "end")
        self.status_value.insert(0, complaint[10])
        self.status_value.configure(state="readonly")
        # Fill editable complaint details
        self.category_menu.set(complaint[5])
        self.urgency_menu.set(complaint[6])
        self.subject_entry.delete(0, "end")
        self.subject_entry.insert(0, complaint[7])
        self.description_text.delete("1.0", "end")
        self.description_text.insert("1.0", complaint[8])

    def clear_fields(self):
        self.category_menu.set("Academic Related")
        self.urgency_menu.set("Medium")
        self.subject_entry.delete(0, "end")
        self.description_text.delete("1.0", "end")

    def update_complaint(self):

        complaint_id = self.complaint_id_entry.get().strip()
        if not complaint_id:
            messagebox.showwarning("No Complaint Selected","Please search for a complaint first.")
            return
        if complaint_id.upper().startswith("CMS-"):
            complaint_id = complaint_id[4:]
        try:
            complaint_id = int(complaint_id)
        except ValueError:
            messagebox.showerror("Invalid Complaint ID","Please search for a valid Complaint ID.")
            return
        category = self.category_menu.get()
        urgency = self.urgency_menu.get()
        subject = self.subject_entry.get().strip()
        description = self.description_text.get("1.0", "end").strip()
        if not subject:
            messagebox.showwarning("Missing Subject","Please enter a complaint subject.")
            return
        if not description:
            messagebox.showwarning("Missing Description","Please enter a complaint description.")
            return
        database.update_student_complaint(complaint_id,category,urgency,subject,description)
        messagebox.showinfo("Complaint Updated","Your complaint has been updated successfully.")   