import customtkinter as ctk
import database
class ViewComplaintWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.selected_complaint_id=None
        # Sample complaint data
        self.complaint_data = {"id": "CMS-1024","date": "28-Sep-2026","subject": "Hostel Room Maintenance","student": "Gurleen Saini","roll": "22CS001","category": "Hostel","status": "Pending","description": "The fan in my hostel room is not working properly."}
        self.title("View Complaint Portal")
        self.geometry("1200x850")
        self.resizable(True,True)
        self.state("zoomed")
        self.transient(parent)
        self.lift()
        self.focus_force()
        self.minsize(1000,750)
        self.configure(fg_color="#F5F9FF")

        # Header
        self.header = ctk.CTkFrame(self,height=130,corner_radius=0,fg_color="#123B72")
        self.header.pack(fill="x")
        self.title_label = ctk.CTkLabel(self.header,text="📋  View Complaints",font=("Arial", 30, "bold"),text_color="white")
        self.title_label.pack(anchor="w", padx=40, pady=(25, 5))
        self.subtitle_label = ctk.CTkLabel(self.header,text="Search, filter and manage student complaints efficiently.",font=("Arial", 16),text_color="white")
        self.subtitle_label.pack(anchor="w", padx=45)

        # ---------------- SEARCH & FILTER ----------------
        self.filter_frame = ctk.CTkFrame(self,fg_color="white",corner_radius=12)
        self.filter_frame.pack(fill="x",padx=25,pady=(20,8))
        # Search Bar
        self.search_entry = ctk.CTkEntry(self.filter_frame,placeholder_text="Search by Complaint ID, Student Name or Subject...",height=45,font=("Arial", 14))
        self.search_entry.pack(side="left",fill="x",expand=True,padx=(15, 10),pady=15)
        # Status Filter
        self.status_frame = ctk.CTkFrame(self.filter_frame,fg_color="transparent")
        self.status_frame.pack(side="left",padx=10,pady=8)
        self.status_label = ctk.CTkLabel(self.status_frame,text="Status",font=("Arial", 14, "bold"),text_color="#123B72")
        self.status_label.pack(anchor="w")
        self.status_menu = ctk.CTkOptionMenu(self.status_frame,values=["All","Pending","In Progress","Resolved"],width=150,height=40,command=self.filter_complaints)
        self.status_menu.set("All")
        self.status_menu.pack()

        # Category Filter
        self.category_frame = ctk.CTkFrame(self.filter_frame,fg_color="transparent")
        self.category_frame.pack(side="left",padx=10,pady=8)
        self.category_label = ctk.CTkLabel(self.category_frame,text="Category",font=("Arial", 14, "bold"),text_color="#123B72")
        self.category_label.pack(anchor="w")
        self.category_menu = ctk.CTkOptionMenu(self.category_frame,values=["All","Academic Related","Examination","Faculty / Staff","Infrastructure","Fees / Finance","Other"],width=170,height=40,command=self.filter_category)
        self.category_menu.set("All")
        self.category_menu.pack()
        # Search Button
        self.search_button = ctk.CTkButton(self.filter_frame,text="🔍  Search",width=120,height=45,fg_color="#1769E0",hover_color="#1255B5",command=self.search_complaints)
        self.search_button.pack(side="left",padx=(10, 15))

        #MAIN AREA 
        self.main_scroll = ctk.CTkScrollableFrame(self,fg_color="transparent")
        self.main_scroll.pack(fill="both",expand=True,padx=25,pady=(0, 5))
        self.main_frame=ctk.CTkFrame(self.main_scroll,fg_color="transparent")
        self.main_frame.pack(fill="x",expand=False)

        #COMPLAINT LIST
        self.list_frame = ctk.CTkFrame(self.main_frame,fg_color="white",corner_radius=12)
        self.list_frame.pack(side="left",fill="both",expand=True,padx=(0, 8))
        self.list_frame.configure(height=550)
        self.list_frame.configure(width=780)

        # Complaint List Title
        self.list_title = ctk.CTkLabel(self.list_frame,text="☷  Complaint List",font=("Arial", 20, "bold"),text_color="#123B72")
        self.list_title.pack(anchor="w",padx=20,pady=15)

        # Scrollable area for complaints
        self.complaint_scroll = ctk.CTkScrollableFrame(self.list_frame,fg_color="#F8FBFF")
        self.complaint_scroll.pack(fill="both",expand=True,padx=15,pady=(0, 15))
        self.details_frame=ctk.CTkFrame(self.main_frame,fg_color="white",corner_radius=12)
        self.details_frame.pack(side="right",fill="both",expand=True,padx=(8,0))
        self.details_frame.configure(height=550)
        self.details_title=ctk.CTkLabel(self.details_frame,text="📄  Complaint Details",font=("Arial",20,"bold"),text_color="#123B72")
        self.details_title.pack(anchor="w",padx=20,pady=15)
        #COMPLAINT INFORMATION
        self.info_frame=ctk.CTkScrollableFrame(self.details_frame,fg_color="#F2F7FD",corner_radius=10)
        self.info_frame.pack(fill="x",padx=15,pady=(0,10))

        # BOTTOM ACTIONS AREA
        self.bottom_area = ctk.CTkFrame(self.details_frame,fg_color="transparent")
        self.bottom_area.pack(fill="x", padx=15, pady=(0, 10))
        self.bottom_area.grid_columnconfigure(0, weight=2)
        self.bottom_area.grid_columnconfigure(1, weight=1)

        # ADMIN ACTIONS 
        self.admin_frame = ctk.CTkFrame(self.bottom_area,fg_color="#F2F7FD",corner_radius=10)
        self.admin_frame.grid(row=0,column=0,sticky="nsew",pady=(0,8))
        
        # Admin Actions Title
        ctk.CTkLabel(self.admin_frame,text="⚙  Admin Actions",font=("Arial", 14, "bold"),text_color="#123B72").pack(anchor="w", padx=15, pady=(10,5))
        # Update Status
        ctk.CTkLabel(self.admin_frame,text="Update Status",font=("Arial", 12),text_color="#123B72").pack(anchor="w", padx=15, pady=(5,2))
        self.change_status_menu = ctk.CTkOptionMenu(self.admin_frame,values=["Pending", "In Progress", "Resolved"],width=180,height=35,command=self.update_selected_status)
        self.change_status_menu.set("Pending")
        self.change_status_menu.pack(anchor="w", padx=15, pady=(0,5))
        self.save_admin_button = ctk.CTkButton(self.admin_frame,text="💾 Save Admin Actions",width=170,height=35,font=("Arial", 12, "bold"),fg_color="#123B72",hover_color="#0D2F5C",command=self.save_admin_actions)
        self.save_admin_button.place(relx=0.98,y=45,anchor="ne")
        # Assign Officer
        ctk.CTkLabel(self.admin_frame,text="Assign Officer",font=("Arial", 12),text_color="#123B72").pack(anchor="w", padx=15, pady=(5,2))
        self.officer_menu = ctk.CTkOptionMenu(self.admin_frame,values=["Select Officer","Maintenance Team","Academic Department","Examination Department","Internal Complaint Committee","Hostel Department","Other"],width=180,height=35,command=self.update_assigned_officer)
        self.officer_menu.set("Select Officer")
        self.officer_menu.pack(anchor="w", padx=15, pady=(0,5))
        # Admin Remarks
        ctk.CTkLabel(self.admin_frame,text="Admin Remarks / Feedback",font=("Arial", 12),text_color="#123B72").pack(anchor="w", padx=15, pady=(5,2))
        self.remarks_box = ctk.CTkTextbox(self.admin_frame,height=70,font=("Arial", 13),fg_color="white",border_width=1,border_color="#C7DCF2")
        self.remarks_box.pack(fill="x", padx=15, pady=(0,10))
        
        # ADDITIONAL INFO
        self.additional_frame = ctk.CTkFrame(self.bottom_area,fg_color="#F2F7FD",corner_radius=10)
        self.additional_frame.grid(row=0,column=1,sticky="nsew",padx=(8, 0))
        ctk.CTkLabel(self.additional_frame,text="👤  Additional Info",font=("Arial", 14, "bold"),text_color="#123B72").pack(anchor="w", padx=15, pady=(10, 12))
        ctk.CTkLabel(self.additional_frame,text="Submitted On",font=("Arial", 12, "bold"),text_color="#123B72").pack(anchor="w", padx=15)
        self.submitted_on_label = ctk.CTkLabel(self.additional_frame,text="—",font=("Arial", 12),text_color="#555555")
        self.submitted_on_label.pack(anchor="w", padx=15, pady=(0, 8))
        ctk.CTkLabel(self.additional_frame,text="Last Updated",font=("Arial", 12, "bold"),text_color="#123B72").pack(anchor="w", padx=15)
        self.last_updated_label = ctk.CTkLabel(self.additional_frame,text="—",font=("Arial", 12),text_color="#555555")
        self.last_updated_label.pack(anchor="w", padx=15, pady=(0, 8))
        ctk.CTkLabel(self.additional_frame,text="Updated By",font=("Arial", 12, "bold"),text_color="#123B72").pack(anchor="w", padx=15)
        self.updated_by_label = ctk.CTkLabel(self.additional_frame,text="—",font=("Arial", 12),text_color="#555555")
        self.updated_by_label.pack(anchor="w", padx=15, pady=(0, 12))
        ctk.CTkLabel(self.additional_frame,text="Assigned Officer",font=("Arial", 12, "bold"),text_color="#123B72").pack(anchor="w", padx=15)
        self.assigned_officer_label = ctk.CTkLabel(self.additional_frame,text="—",font=("Arial", 12),text_color="#555555")
        self.assigned_officer_label.pack(anchor="w", padx=15, pady=(0, 12))

        #BOTTOM BUTTONS
        self.bottom_frame = ctk.CTkFrame(self.main_scroll,fg_color="white",corner_radius=12,height=65)
        self.bottom_frame.pack_propagate(False)
        self.bottom_frame.pack(fill="x",padx=25,pady=(10,15))
                
        # Refresh Button
        self.refresh_button = ctk.CTkButton(self.bottom_frame,text="🔄  Refresh",width=210,height=45,fg_color="#2563EB",hover_color="#1D4ED8",font=("Arial", 13, "bold"),command=self.refresh_complaints)
        self.refresh_button.pack(side="left",padx=(15,10),pady=10)
        # Export Data Button
        self.export_button = ctk.CTkButton(self.bottom_frame,text="📄  Export Data    ▼",width=230,height=45,fg_color="#22A05A",hover_color="#198A4A",font=("Arial", 13, "bold"),command=self.export_data)
        self.export_button.pack(side="left",padx=10,pady=10)
        # Back / Home Button
        self.back_button = ctk.CTkButton(self.bottom_frame,text="🏠  Back / Home",width=210,height=45,fg_color="#2563EB",hover_color="#1D4ED8",font=("Arial", 13, "bold"),command=self.go_back_home)
        self.back_button.pack(side="right",padx=(10,15),pady=10)
        self.bottom_space=ctk.CTkFrame(self.main_scroll,height=30,fg_color="transparent")
        self.bottom_space.pack(fill="x")

        self.load_complaints()

    def go_back_home(self):
        self.destroy()

    def refresh_complaints(self):
        self.selected_complaint_id = None
        for widget in self.info_frame.winfo_children():
            widget.destroy()
        self.change_status_menu.set("Pending")
        self.officer_menu.set("Select Officer")
        self.remarks_box.delete("1.0", "end")
        self.submitted_on_label.configure(text="—")
        self.last_updated_label.configure(text="—")
        self.updated_by_label.configure(text="—")
        self.assigned_officer_label.configure(text="—")
        self.load_complaints()

    def export_data(self):
        import csv
        from tkinter import filedialog, messagebox
        complaints = database.get_all_complaints()
        if not complaints:
            messagebox.showinfo("Export Data", "No complaints available to export.")
            return
        file_path = filedialog.asksaveasfilename(title="Save Complaint Data",defaultextension=".csv",filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        headers = ["Complaint ID","Student Name","Roll No","Department","Course","Category","Urgency","Subject","Description","Anonymous","Status","Assigned Officer","Admin Remarks","Submitted On","Last Updated","Updated By"]
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
        writer.writerow(headers)
        for complaint in complaints:
            writer.writerow(complaint)
        messagebox.showinfo("Export Successful","Complaint data has been exported successfully.")
        
    def load_complaints(self):
        complaints = database.get_all_complaints()

        for widget in self.complaint_scroll.winfo_children():
            widget.destroy()

        for complaint in complaints:
            self.create_complaint_card(complaint)

    def search_complaints(self):
        search_text = self.search_entry.get().lower().strip()
        complaints = database.get_all_complaints()
        filtered_complaints = []
        for complaint in complaints:
            complaint_id = str(complaint[0]).lower()
            complaint_id_with_prefix = "cms-" + str(complaint[0]).lower()
            student_name = str(complaint[1]).lower()
            subject = str(complaint[7]).lower()
            if (search_text in complaint_id or
                search_text in complaint_id_with_prefix or
                search_text in student_name or
                search_text in subject):
                filtered_complaints.append(complaint)
        for widget in self.complaint_scroll.winfo_children():
            widget.destroy()
        for complaint in filtered_complaints:
            self.create_complaint_card(complaint)

    def filter_complaints(self, selected_status):
        complaints = database.get_all_complaints()
        if selected_status == "All":
            filtered_complaints = complaints
        else:
            filtered_complaints = []
            for complaint in complaints:
                if complaint[10] == selected_status:
                    filtered_complaints.append(complaint)
        for widget in self.complaint_scroll.winfo_children():
            widget.destroy()
        for complaint in filtered_complaints:
            self.create_complaint_card(complaint)

    def filter_category(self, selected_category):
        complaints = database.get_all_complaints()
        if selected_category == "All":
            filtered_complaints = complaints
        else:
            filtered_complaints = []
            for complaint in complaints:
                if complaint[5] == selected_category:
                    filtered_complaints.append(complaint)
        for widget in self.complaint_scroll.winfo_children():
            widget.destroy()
        for complaint in filtered_complaints:
            self.create_complaint_card(complaint)

    def update_selected_status(self, selected_status):
        if self.selected_complaint_id is None:
            return
        database.update_complaint_status(self.selected_complaint_id,selected_status)
        self.load_complaints()
        complaints = database.get_all_complaints()
        for complaint in complaints:
            if complaint[0] == self.selected_complaint_id:
                self.show_complaint(complaint)
                break

    def update_assigned_officer(self, selected_officer):
        if self.selected_complaint_id is None:
            return
        database.update_assigned_officer(self.selected_complaint_id,selected_officer)
        self.assigned_officer_label.configure(text=selected_officer)

    def save_admin_actions(self):
        if self.selected_complaint_id is None:
            return
        status = self.change_status_menu.get()
        officer = self.officer_menu.get()
        remarks = self.remarks_box.get("1.0", "end-1c").strip()
        database.update_complaint_status(self.selected_complaint_id,status)
        database.update_assigned_officer(self.selected_complaint_id,officer)
        database.update_admin_remarks(self.selected_complaint_id,remarks)
        # Refresh the selected complaint
        complaints = database.get_all_complaints()
        for complaint in complaints:
            if complaint[0] == self.selected_complaint_id:
                self.show_complaint(complaint)
                break

    def update_admin_remarks(self):
        if self.selected_complaint_id is None:
            return
        remarks = self.remarks_box.get("1.0", "end-1c").strip()
        database.update_admin_remarks(self.selected_complaint_id,remarks)

    def create_complaint_card(self, complaint):
        complaint_id = complaint[0]
        student_name = complaint[1]
        roll_no = complaint[2]
        category = complaint[5]
        subject = complaint[7]
        status = complaint[10]
        card = ctk.CTkFrame(self.complaint_scroll,fg_color="white",corner_radius=10,border_width=1,border_color="#BFD8F5")
        card.pack(fill="x", padx=5, pady=5)
    # Left status line
        if status == "Pending":
            line_color = "#E53935"
        elif status == "In Progress":
            line_color = "#F59E0B"
        else:
            line_color = "#22A05A"
        left_line = ctk.CTkFrame(card,width=4,fg_color=line_color,corner_radius=4)
        left_line.pack(side="left", fill="y")
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(side="left",fill="both",expand=True,padx=12,pady=10)
    # Top row
        top_row = ctk.CTkFrame(content, fg_color="transparent")
        top_row.pack(fill="x")
        ctk.CTkLabel(top_row,text=f"CMS-{complaint_id}",font=("Arial", 14, "bold"),text_color="#123B72").pack(side="left")
        ctk.CTkLabel(top_row,text=f"📁 Category: {category}",font=("Arial", 12),text_color="#607080").pack(side="left", padx=25)
    # Status badge
        if status == "Pending":
            status_color = "#E53935"
            status_bg = "#FFE5E5"
        elif status == "In Progress":
            status_color = "#D97706"
            status_bg = "#FFF1D6"
        else:
            status_color = "#2E8B57"
            status_bg = "#E5F6EA"
        ctk.CTkLabel(top_row,text=f"● {status}",font=("Arial", 12, "bold"),text_color=status_color,fg_color=status_bg,corner_radius=15).pack(side="right", padx=5)
    # Subject
        ctk.CTkLabel(content,text=f"Subject:  {subject}",font=("Arial", 14, "bold"),text_color="#123B72").pack(anchor="w", pady=(8, 3))
    # Student
        ctk.CTkLabel(content,text=f"👤 Roll No: {roll_no}    |    Name: {student_name}",font=("Arial", 12),text_color="#607080").pack(anchor="w")
    # Arrow
        arrow = ctk.CTkLabel(card,text="›",font=("Arial", 28),text_color="#356A9A")
        arrow.pack(side="right", padx=12)

        def make_clickable(widget):
            widget.bind("<Button-1>",lambda event: self.show_complaint(complaint))
            for child in widget.winfo_children():
                make_clickable(child)
        make_clickable(card)
        
    def show_complaint(self, complaint=None):
        if complaint is None:
            return
    # Clear previous details
        for widget in self.info_frame.winfo_children():
            widget.destroy()
    # Get complaint data from database
        complaint_id = complaint[0]
        self.selected_complaint_id=complaint_id
        student_name = complaint[1]
        roll_no = complaint[2]
        department = complaint[3]
        course = complaint[4]
        category = complaint[5]
        urgency = complaint[6]
        subject = complaint[7]
        description = complaint[8]
        anonymous = complaint[9]
        status = complaint[10]
        assigned_officer = complaint[11]
        admin_remarks = complaint[12]
        submitted_on = complaint[13]
        last_updated = complaint[14]
        updated_by = complaint[15]
    # If complaint is anonymous
        if anonymous:
            student_name = "Anonymous"
            roll_no = "—"
    # Complaint ID
        ctk.CTkLabel(self.info_frame,text=f"Complaint ID :  CMS-{complaint_id}",font=("Arial", 13, "bold"),text_color="#123B72").pack(anchor="w", padx=15, pady=(12, 5))
    # Student Name
        ctk.CTkLabel(self.info_frame,text=f"Student Name :  {student_name}",font=("Arial", 13),text_color="#123B72").pack(anchor="w", padx=15, pady=5)
    # Roll Number
        ctk.CTkLabel(self.info_frame,text=f"Roll Number :  {roll_no}",font=("Arial", 13),text_color="#123B72").pack(anchor="w", padx=15, pady=5)
    # Department
        ctk.CTkLabel(self.info_frame,text=f"Department :  {department}",font=("Arial", 13),text_color="#123B72").pack(anchor="w", padx=15, pady=5)
    # Course
        ctk.CTkLabel(self.info_frame,text=f"Course :  {course}",font=("Arial", 13),text_color="#123B72").pack(anchor="w", padx=15, pady=5)
    # Category
        ctk.CTkLabel(self.info_frame,text=f"Category :  {category}",font=("Arial", 13),text_color="#123B72").pack(anchor="w", padx=15, pady=5)
    # Urgency
        ctk.CTkLabel(self.info_frame,text=f"Urgency :  {urgency}",font=("Arial", 13),text_color="#123B72").pack(anchor="w", padx=15, pady=5)
    # Subject
        ctk.CTkLabel(self.info_frame,text=f"Subject :  {subject}",font=("Arial", 13, "bold"),text_color="#123B72").pack(anchor="w", padx=15, pady=5)
    # Status
        ctk.CTkLabel(self.info_frame,text=f"Status :  {status}",font=("Arial", 13, "bold"),text_color="#123B72").pack(anchor="w", padx=15, pady=5)
    # Description heading
        ctk.CTkLabel(self.info_frame,text="Full Description",font=("Arial", 14, "bold"),text_color="#123B72").pack(anchor="w", padx=15, pady=(12, 5))
    # Description box
        self.description_box = ctk.CTkTextbox(self.info_frame,height=120,font=("Arial", 13),fg_color="white",border_width=1,border_color="#C7DCF2")
        self.description_box.pack(fill="x",padx=15,pady=(0, 15))
        self.description_box.insert("1.0",description if description else "No description provided.")
    # Make description read-only
        self.description_box.configure(state="disabled")
    # Set current status in Admin Actions
        self.change_status_menu.set(status)
        self.officer_menu.set(assigned_officer)
        self.assigned_officer_label.configure(text=assigned_officer)
        self.submitted_on_label.configure(text=submitted_on if submitted_on else "—")
        self.last_updated_label.configure(text=last_updated if last_updated else "—")
        self.updated_by_label.configure(text=updated_by if updated_by else "—")
        self.remarks_box.delete("1.0","end")
        self.remarks_box.insert("1.0",admin_remarks if admin_remarks else"")

