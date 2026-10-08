import customtkinter as ctK
from tkinter import messagebox
from tkinter import filedialog
import database
add_complaint_window=None
def open_add_complaint(parent,student_name_value, roll_no_value, department_value, course_value):
    global add_complaint_window
    app=ctK.CTkToplevel(parent)
    add_complaint_window=app
    app.title("Add Complaint")
    app.geometry("1100x800")
    app.resizable(True,True)
    app.state("zoomed")
    app.transient(parent)
    app.lift()
    app.focus_force()

    def attach_file():
        file_path = filedialog.askopenfilename(title="Select File",filetypes=[("All Files", "*.*"),("Images", "*.jpg *.jpeg *.png"),("PDF Files", "*.pdf"),("Word Documents", "*.doc *.docx")])
        if file_path:
            file_name = file_path.split("/")[-1]
            upload_text.configure(text=file_name)

    #HEADER/TITLE/SUBTITLE

    header = ctK.CTkFrame(app,fg_color="#1F4E79",corner_radius=0,height=140)
    header.pack(fill="x")
    header.pack_propagate(False)
    icon_label = ctK.CTkLabel(header,text="📄",font=("Arial", 48),text_color="white")
    icon_label.pack(side="left", padx=(40,15))
    header_text = ctK.CTkFrame(header, fg_color="transparent")
    header_text.pack(side="left")
    title_label = ctK.CTkLabel(header_text,text="Add Complaint",font=("Arial", 32, "bold"),text_color="white")
    title_label.pack(anchor="w")
    subtitle_label = ctK.CTkLabel(header_text,text="Your voice matters. Help us improve.",font=("Arial", 17),text_color="white")
    subtitle_label.pack(anchor="w",pady=(2,0))
    scroll_frame = ctK.CTkScrollableFrame(app,fg_color="transparent")
    scroll_frame.pack(fill="both", expand=True)

    #STUDENT INFORMATION

    student_frame = ctK.CTkFrame(scroll_frame,fg_color="#F4F8FC",corner_radius=12,border_width=1,border_color="#D6E4F0")
    student_frame.pack(fill="x", padx=30, pady=(25, 12))

    # Student information heading

    student_heading = ctK.CTkFrame(student_frame,fg_color="#EAF3FC",corner_radius=0)
    student_heading.pack(fill="x")
    student_icon = ctK.CTkLabel(student_heading,text="👤",font=("Arial", 22))
    student_icon.pack(side="left", padx=(20, 8), pady=10)
    student_title = ctK.CTkLabel(student_heading,text="Student Information",font=("Arial", 20, "bold"),text_color="#1F4E79")
    student_title.pack(side="left", pady=10)

    # Four columns
    fields_frame = ctK.CTkFrame(student_frame,fg_color="transparent")
    fields_frame.pack(fill="x", padx=20, pady=(18, 22))

    # Student Name
    name_frame = ctK.CTkFrame(fields_frame, fg_color="transparent")
    name_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))
    name_label = ctK.CTkLabel(name_frame,text="Student Name",font=("Arial", 15, "bold"),text_color="#1F3555")
    name_label.pack(anchor="w", pady=(0, 8))
    student_name = ctK.CTkEntry(name_frame,height=42,placeholder_text="Enter Student Name")
    student_name.pack(fill="x")
    student_name.insert(0,student_name_value)

    # Roll No
    roll_frame = ctK.CTkFrame(fields_frame, fg_color="transparent")
    roll_frame.pack(side="left", fill="x", expand=True, padx=10)
    roll_label = ctK.CTkLabel(roll_frame,text="Roll No.",font=("Arial", 15, "bold"),text_color="#1F3555")
    roll_label.pack(anchor="w", pady=(0, 8))
    roll_no = ctK.CTkEntry(roll_frame,height=42,placeholder_text="Enter Roll No.")
    roll_no.pack(fill="x")
    roll_no.insert(0,roll_no_value)

    # Department
    department_frame = ctK.CTkFrame(fields_frame, fg_color="transparent")
    department_frame.pack(side="left", fill="x", expand=True, padx=10)
    department_label = ctK.CTkLabel(department_frame,text="Department",font=("Arial", 15, "bold"),text_color="#1F3555")
    department_label.pack(anchor="w", pady=(0, 8))
    department = ctK.CTkComboBox(department_frame,height=42,values=["Computer Science", "Physics", "Mathematics"])
    department.pack(fill="x")
    department.set(department_value)

    # Course
    course_frame = ctK.CTkFrame(fields_frame, fg_color="transparent")
    course_frame.pack(side="left", fill="x", expand=True, padx=(10, 0))
    course_label = ctK.CTkLabel(course_frame,text="Courses",font=("Arial", 15, "bold"),text_color="#1F3555")
    course_label.pack(anchor="w", pady=(0, 8))
    course = ctK.CTkComboBox(course_frame,height=42,values=["B.Sc. (Non-Medical)", "B.Sc. Computer Science", "B.Sc. Mathematics"])
    course.pack(fill="x")
    course.set(course_value)

    #COMPLAINT CATEGORY AND Urgeny BUTTON

    # CATEGORY + URGENCY ROW
    category_urgency_frame = ctK.CTkFrame(scroll_frame,fg_color="transparent")
    category_urgency_frame.pack(fill="x", padx=30, pady=10)

    # COMPLAINT CATEGORY
    category_frame = ctK.CTkFrame(category_urgency_frame,fg_color="#F4F8FC",corner_radius=12,border_width=1,border_color="#D6E4F0")
    category_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
    category_heading = ctK.CTkLabel(category_frame,text="📋  Complaint Category",font=("Arial", 18, "bold"),text_color="#1F4E79")
    category_heading.pack(anchor="w", padx=20, pady=(15, 10))
    complaint_category = ctK.CTkComboBox(category_frame,height=42,values=["Academic Related","Infrastructure","Faculty / Staff","Examination","Fees / Finance","Other"])
    complaint_category.pack(fill="x", padx=20, pady=(0, 18))
    complaint_category.set("Select Complaint Category")

    # URGENCY LEVEL

    urgency_frame = ctK.CTkFrame(category_urgency_frame,fg_color="#F4F8FC",corner_radius=12,border_width=1,border_color="#D6E4F0")
    urgency_frame.pack(side="left", fill="both", expand=True, padx=(10, 0))
    urgency_heading = ctK.CTkLabel(urgency_frame,text="⚠️  Urgency Level",font=("Arial", 18, "bold"),text_color="#1F4E79")
    urgency_heading.pack(anchor="w", padx=20, pady=(15, 10))
    urgency_level = ctK.CTkSegmentedButton(urgency_frame,values=["Low", "Medium", "High"])
    urgency_level.pack(fill="x", padx=20, pady=(5, 18))
    urgency_level.set("Medium")

    #COMPLAINT SECTION

    # COMPLAINT SUBSTANCE
    content_row = ctK.CTkFrame(scroll_frame,fg_color="transparent")
    content_row.pack(fill="x", padx=30, pady=10)
    substance_frame = ctK.CTkFrame(content_row,fg_color="#F4F8FC",corner_radius=12,border_width=1,border_color="#D6E4F0")
    substance_frame.pack(side="left",fill="both",expand=True,padx=(0, 10))
    right_frame = ctK.CTkFrame(content_row,fg_color="transparent")
    right_frame.pack(side="left",fill="both",expand=True,padx=(10, 0))

    # Heading
    substance_heading = ctK.CTkLabel(substance_frame,text="📄  Complaint Substance",font=("Arial", 18, "bold"),text_color="#1F4E79")
    substance_heading.pack(anchor="w", padx=20, pady=(15, 12))

    # Subject
    subject_label = ctK.CTkLabel(substance_frame,text="Subject",font=("Arial", 15, "bold"),text_color="#1F3555")
    subject_label.pack(anchor="w", padx=20, pady=(0, 7))
    subject_entry = ctK.CTkEntry(substance_frame,height=42,placeholder_text="Enter a short subject for your complaint...")
    subject_entry.pack(fill="x", padx=20, pady=(0, 15))

    # Detailed Description
    description_label = ctK.CTkLabel(substance_frame,text="Detailed Description",font=("Arial", 15, "bold"),text_color="#1F3555")
    description_label.pack(anchor="w", padx=20, pady=(0, 7))
    description_box = ctK.CTkTextbox(substance_frame,height=120,corner_radius=8)
    description_box.pack(fill="x", padx=20, pady=(0, 5))

    # Character counter
    character_count = ctK.CTkLabel(substance_frame,text="0/1000",font=("Arial", 12),text_color="#6B7C93")
    character_count.pack(anchor="e", padx=20, pady=(0, 15)) 
    def update_character_count(event=None):
        text=description_box.get("1.0","end-1c")
        count=len(text)
        character_count.configure(text=f"{count}/1000")
    description_box.bind("<KeyRelease>",update_character_count)

    #FILE ATTACHMENT

    attachment_frame = ctK.CTkFrame(right_frame,fg_color="#F4F8FC",corner_radius=12,border_width=1,border_color="#D6E4F0")
    attachment_frame.pack(fill="x", pady=(0, 10))
    attachment_heading = ctK.CTkLabel(attachment_frame,text="📎  File Attachment (Optional)",font=("Arial", 18, "bold"),text_color="#1F4E79")
    attachment_heading.pack(anchor="w", padx=20, pady=(15, 12))
    upload_area = ctK.CTkFrame(attachment_frame,fg_color="transparent",border_width=2,border_color="#B8C9DC",corner_radius=8,height=180)
    upload_area.pack(fill="x", padx=20, pady=(0, 20))
    upload_area.pack_propagate(False)
    upload_icon = ctK.CTkLabel(upload_area,text="☁️",font=("Arial", 35))
    upload_icon.pack(pady=(15, 3))
    upload_text = ctK.CTkLabel(upload_area,text="Click to upload or drag and drop",font=("Arial", 14),text_color="#1F3555")
    upload_text.pack()
    file_types = ctK.CTkLabel(upload_area,text="(JPG, PNG, PDF, DOC, etc.)",font=("Arial", 12),text_color="#6B7C93")
    file_types.pack(pady=(2, 0))
    attach_button = ctK.CTkButton(upload_area,text="Choose File",command=attach_file,width=120,height=35)
    attach_button.pack(pady=(8, 10))

    #ANONYMOUS MODE

    anonymous_frame = ctK.CTkFrame(right_frame,fg_color="#F4F8FC",corner_radius=12,border_width=1,border_color="#D6E4F0")
    anonymous_frame.pack(fill="x", pady=(10, 0))
    anonymous_heading = ctK.CTkLabel(anonymous_frame,text="🔒  Anonymous Mode",font=("Arial", 18, "bold"),text_color="#1F4E79")
    anonymous_heading.pack(anchor="w", padx=20, pady=(15, 5))
    anonymous_switch = ctK.CTkSwitch(anonymous_frame,text="Submit complaint anonymously",font=("Arial", 14),text_color="#1F3555")
    anonymous_switch.pack(anchor="w", padx=20, pady=(5, 15))

    #SUBMIT AND CLEAR/RESET BUTTON
    button_frame = ctK.CTkFrame(scroll_frame,fg_color="transparent")
    button_frame.pack(fill="x", padx=0, pady=(10, 10))
    def submit_complaint():
        subject = subject_entry.get().strip()
        description = description_box.get("1.0", "end-1c").strip()
        is_anonymous=anonymous_switch.get()
        if is_anonymous:
            saved_name = ""
            saved_roll_no = ""
            saved_department = ""
            saved_course = ""
        else:
            saved_name = student_name.get()
            saved_roll_no = roll_no.get()
            saved_department = department.get()
            saved_course = course.get()

        if complaint_category.get() == "Select Complaint Category":
            status_bar.configure(text="❌  Please select a complaint category.",text_color="#B42318",fg_color="#FDECEC")
            return
        if subject == "":
            status_bar.configure(text="❌  Please enter a subject.",text_color="#B42318",fg_color="#FDECEC")
            return

        if description == "":
            status_bar.configure(text="❌  Please enter a detailed description.",text_color="#B42318",fg_color="#FDECEC")
            return
        database.create_complaint(saved_name,saved_roll_no,saved_department,saved_course,complaint_category.get(),urgency_level.get(),subject,description,is_anonymous) 
        status_bar.configure(text="✅  Complaint submitted successfully.",text_color="#247A4D",fg_color="#E8F7EF")
    submit_button = ctK.CTkButton(button_frame,text="➤  Submit Complaint",font=("Arial", 16, "bold"),height=55,fg_color="#1976D2",hover_color="#1565C0",command=submit_complaint)
    submit_button.pack(side="left",fill="x",expand=True,padx=(0, 10))
    def clear_form():
        subject_entry.delete(0, "end")
        description_box.delete("1.0", "end")
        complaint_category.set("Select Complaint Category")
        urgency_level.set("Medium")
        character_count.configure(text="0 / 1000")
    clear_button = ctK.CTkButton(button_frame,text="↻  Clear / Reset",font=("Arial", 16, "bold"),height=55,fg_color="#EAF1F8",hover_color="#DCE7F2",text_color="#1F4E79",command=clear_form)
    clear_button.pack(side="left",fill="x",expand=True,padx=(10, 0))
    status_bar = ctK.CTkLabel(scroll_frame,text="🟢  Ready to submit. Please fill in all required fields.",font=("Arial", 14),text_color="#247A4D",fg_color="#E8F7EF",corner_radius=10,height=50,anchor="w")
    status_bar.pack(fill="x", padx=0, pady=(0, 15))
    bottom_space=ctK.CTkFrame(scroll_frame,height=40,fg_color="transparent")
    bottom_space.pack(fill="x")
    scroll_frame.update_idletasks()



















