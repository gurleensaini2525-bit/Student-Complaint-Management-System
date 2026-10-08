import sqlite3
from datetime import datetime
DATABASE_NAME="complaint_management.db"
def get_connection():
    return sqlite3.connect(DATABASE_NAME)

def create_tables():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,username TEXT,password TEXT,user_type TEXT)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS complaints (id INTEGER PRIMARY KEY AUTOINCREMENT,student_name TEXT,roll_no TEXT,department TEXT,course TEXT,category TEXT,urgency TEXT,subject TEXT,description TEXT,anonymous INTEGER DEFAULT 0,status TEXT DEFAULT 'Pending')""")
    try:
        cursor.execute("ALTER TABLE complaints ADD COLUMN assigned_officer TEXT DEFAULT 'Select Officer' ")
    except sqlite3.OperationalError:
        pass
    try:
        cursor.execute("ALTER TABLE complaints ADD COLUMN admin_remarks TEXT DEFAULT '' ")
    except sqlite3.OperationalError:
            pass
    try:
        cursor.execute("ALTER TABLE complaints ADD COLUMN submitted_on TEXT")
    except sqlite3.OperationalError:
        pass

    try:
        cursor.execute("ALTER TABLE complaints ADD COLUMN last_updated TEXT")
    except sqlite3.OperationalError:
        pass

    try:
        cursor.execute("ALTER TABLE complaints ADD COLUMN updated_by TEXT")
    except sqlite3.OperationalError:
        pass
    conn.commit()
    conn.close()

def create_user(name,username,password,user_type):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO users(name,username,password,user_type)VALUES(?,?,?,?)",(name,username,password,user_type))
    conn.commit()
    conn.close()

def login_user(username,password,user_type):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT*FROM users WHERE username=? AND password=? AND user_type=?",(username,password,user_type))
    account=cursor.fetchone()
    conn.close()
    return account
create_tables()

def create_complaint(student_name,roll_no,department,course,category,urgency,subject,description,anonymous):
    conn = get_connection()
    cursor = conn.cursor()
    submitted_on = datetime.now().strftime("%d-%b-%Y %I:%M %p")
    cursor.execute("""INSERT INTO complaints(student_name,roll_no,department,course,category,urgency,subject,description,anonymous,submitted_on,last_updated,updated_by)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?)""", (student_name,roll_no,department,course,category,urgency,subject,description,anonymous,submitted_on,submitted_on,"Student"))
    conn.commit()
    conn.close()

def get_all_complaints():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT id, student_name, roll_no, department, course,category, urgency, subject, description, anonymous, status, assigned_officer, admin_remarks, submitted_on, last_updated, updated_by FROM complaints ORDER BY id DESC""")
    complaints = cursor.fetchall()
    conn.close()
    return complaints

def update_complaint_status(complaint_id, status):
    conn = get_connection()
    cursor = conn.cursor()
    last_updated = datetime.now().strftime("%d-%b-%Y %I:%M %p")
    cursor.execute("UPDATE complaints SET status=?, last_updated=?, updated_by=? WHERE id=?",(status, last_updated, "Admin", complaint_id))
    conn.commit()
    conn.close()

def update_assigned_officer(complaint_id, officer):
    conn = get_connection()
    cursor = conn.cursor()
    last_updated = datetime.now().strftime("%d-%b-%Y %I:%M %p")
    cursor.execute("UPDATE complaints SET assigned_officer=?, last_updated=?, updated_by=? WHERE id=?",(officer, last_updated, "Admin", complaint_id))
    conn.commit()
    conn.close()

def update_admin_remarks(complaint_id, remarks):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE complaints SET admin_remarks=? WHERE id=?",(remarks, complaint_id))
    conn.commit()
    conn.close()

def get_complaint_by_id(complaint_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT id, student_name, roll_no, department, course,category, urgency, subject, description,anonymous, status FROM complaints WHERE id=?""", (complaint_id,))
    complaint = cursor.fetchone()
    conn.close()
    return complaint

def update_student_complaint(complaint_id,category,urgency,subject,description):
    conn = get_connection()
    cursor = conn.cursor()
    last_updated = datetime.now().strftime("%d-%b-%Y %I:%M %p")
    cursor.execute("""UPDATE complaints SET category=?,urgency=?,subject=?,description=?,last_updated=?,updated_by=? WHERE id=?""", (category,urgency,subject,description,last_updated,"Student",complaint_id))
    conn.commit()
    conn.close()

def get_student_complaints(student_name, roll_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT id, student_name, roll_no, department, course,category, urgency, subject, description, anonymous,status, assigned_officer, admin_remarks,submitted_on, last_updated, updated_by FROM complaints WHERE student_name=? AND roll_no=? ORDER BY id DESC""", (student_name, roll_no))
    complaints = cursor.fetchall()
    conn.close()
    return complaints

def delete_complaint(complaint_id, student_name, roll_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(""" DELETE FROM complaints WHERE id=? AND student_name=? AND roll_no=? """,(complaint_id, student_name, roll_no))
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted > 0