from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk   #pip install pillow
import mysql.connector 
from tkinter import messagebox 

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        
        
        
        
        #veriables for entry fill and save 
        
        
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
     

        # 1st image
        img = Image.open(r"college_images/7th.jpg")
        img = img.resize((510, 160), Image.LANCZOS)

        self.photoimg = ImageTk.PhotoImage(img)

        self.btn_1 = Button(self.root, image=self.photoimg, cursor="hand2")
        self.btn_1.place(x=0, y=0, width=510, height=160)

        # 2nd image
        img_2 = Image.open(r"college_images/6th.jpg")
        img_2 = img_2.resize((510, 160), Image.LANCZOS)

        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        self.btn_2 = Button(self.root, image=self.photoimg_2, cursor="hand2")
        self.btn_2.place(x=510, y=0, width=510, height=160)

        # 3rd image
        img_3 = Image.open(r"college_images/5th.jpg")
        img_3 = img_3.resize((510, 160), Image.LANCZOS)

        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        self.btn_3 = Button(self.root, image=self.photoimg_3, cursor="hand2")
        self.btn_3.place(x=1020, y=0, width=510, height=160)
        
        
        # bg image
        
        img_4 = Image.open(r"college_images/university.jpg")
        img_4 = img_4.resize((1530,710), Image.LANCZOS)

        self.photoimg_4 = ImageTk.PhotoImage(img_4)
        
        bg_lbl=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1530,height=710)
         
         # CREATE A TITLE WITH THE HELP OF LABEL
         
        lbl_title =Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",37,"bold"),fg="blue",bg="white")
        lbl_title.place(x=0,y=0,width=1530,height=50)
        
        # creat a frame, frame work as a container
        
        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_frame.place(x=15,y=55,width=1500,height=560)
    
        
        #left Frame 
        DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        DataLeftFrame.place(x=10,y=10,width=660,height=537)
        
        #img left frame 
        
        img_5 = Image.open(r"college_images/3rd.jpg")
        img_5 = img_5.resize((650,120), Image.LANCZOS)

        self.photoimg_5 = ImageTk.PhotoImage(img_5)
        
        my_lbl=Label(DataLeftFrame,image=self.photoimg_5,bd=2,relief=RIDGE)
        my_lbl.place(x=0,y=0,width=650,height=120)
        
        
       # Current course LabelFrame Information
       
        std_lbl_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current course Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_frame.place(x=0,y=120,width=650,height=115)
        
        # Label and combobox
        
        # department
        lbl_dep=Label(std_lbl_frame,text="Department",font=("arial",12,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        
        combo_dep=ttk.Combobox(std_lbl_frame,textvariable=self.var_dep,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","Computer","IT","Civil")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        
        
        # Course
        course_std = Label(std_lbl_frame, text="Courses:", font=("arial", 12, "bold"), bg="white")
        course_std.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        com_txtcourse_std = ttk.Combobox(std_lbl_frame,textvariable=self.var_course,font=("arial", 12, "bold"), width=17, state="readonly")
        com_txtcourse_std["value"] = ("Select Course", "AI", "ML", "Data Learning")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        
        
        #YEAR
        
        current_year=Label(std_lbl_frame,text="Year :", font=("arial", 12, "bold"), bg="white")
        current_year.grid(row=1,column=0,sticky=W,padx=2,pady=10)
        
        com_txt_current_year=ttk.Combobox(std_lbl_frame,textvariable=self.var_year, font=("arial", 12, "bold"), width=17, state="readonly")
        
        com_txt_current_year['value']=("Select Year","2022-23","2023-24","2024-25","2025-2026")
        com_txt_current_year.current(0)
        com_txt_current_year.grid(row=1,column=1,sticky=W,padx=2)
        
        
        #Semester
        
        label_student=Label(std_lbl_frame,text="Semester :", font=("arial", 12, "bold"), bg="white")
        label_student.grid(row=1,column=2,sticky=W,padx=2,pady=10)
        comsemester=ttk.Combobox(std_lbl_frame,textvariable=self.var_semester, font=("arial", 12, "bold"), width=17, state="readonly")
        
        comsemester['value']=("Select Semester","1","2","3","4","5","6")
        comsemester.current(0)
        comsemester.grid(row=1,column=3,sticky=W,padx=2,pady=10)  
        
        
        # Student Class LabelFrame Information
        std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Class course Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_class_frame.place(x=0,y=235,width=650,height=250)
       
       # Label entry
       
       #Id
       
        lbl_id=Label(std_lbl_class_frame,text="Student Id:", font=("arial", 12, "bold"), bg="white")
        lbl_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)
        
        
        id_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_id,font=("arial", 11, "bold"),width=22)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)
        
        #Name
        
        lbl_id=Label(std_lbl_class_frame,text="Student Name:", font=("arial", 11, "bold"), bg="white")
        lbl_id.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        
        
        name_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_name,font=("arial", 11, "bold"),width=22)
        name_entry.grid(row=0,column=3,sticky=W,padx=2,pady=7)
        
        #Division
        
        lbl_id=Label(std_lbl_class_frame,text="Student Division:", font=("arial", 11, "bold"), bg="white")
        lbl_id.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        
        com_txt_div=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_div, font=("arial", 12, "bold"), width=18, state="readonly")
        com_txt_div['value']=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,sticky=W,padx=7)
        
        #Roll no.
        
        lbl_roll=Label(std_lbl_class_frame,text=" Roll No.:", font=("arial", 11, "bold"), bg="white")
        lbl_roll.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        
        
        roll_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_roll,font=("arial", 11, "bold"),width=22)
        roll_entry.grid(row=1,column=3,sticky=W,padx=2,pady=7)
        
        #gender
        
        lbl_gender=Label(std_lbl_class_frame,text="Student Gender", font=("arial", 11, "bold"), bg="white")
        lbl_gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        
        com_txt_gender=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender, font=("arial", 12, "bold"), width=18, state="readonly")
        com_txt_gender['value']=("Select Gender","M","F")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,sticky=W,padx=7)
        
        
        #DOB
        
        lbl_dob=Label(std_lbl_class_frame,text=" DOB :", font=("arial", 11, "bold"), bg="white")
        lbl_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)
        
        
        roll_entry=ttk.Entry(std_lbl_class_frame,textvariable= self.var_dob,font=("arial", 11, "bold"),width=22)
        roll_entry.grid(row=2,column=3,sticky=W,padx=2,pady=7)
        
        #Email
        
        lbl_email=Label(std_lbl_class_frame,text=" Email :", font=("arial", 11, "bold"), bg="white")
        lbl_email.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        
        
        email_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_email,font=("arial", 11, "bold"),width=22)
        email_entry.grid(row=3,column=1,sticky=W,padx=2,pady=7)
        
        #phone no.
        
        lbl_phone=Label(std_lbl_class_frame,text="phone No:", font=("arial", 11, "bold"), bg="white")
        lbl_phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        
        
        phone_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_phone,font=("arial", 11, "bold"),width=22)
        phone_entry.grid(row=3,column=3,sticky=W,padx=2,pady=7)
        
        #address
        
        lbl_address=Label(std_lbl_class_frame,text="Address:", font=("arial", 11, "bold"), bg="white")
        lbl_address.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        
        
        address_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_address,font=("arial", 11, "bold"),width=22)
        address_entry.grid(row=4,column=1,sticky=W,padx=2,pady=7)
        
        #teacher
        
        lbl_teacher=Label(std_lbl_class_frame,text="Teacher Name:", font=("arial", 11, "bold"), bg="white")
        lbl_teacher.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        
        
        teacher_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_teacher,font=("arial", 11, "bold"),width=22)
        teacher_entry.grid(row=4,column=3,sticky=W,padx=2,pady=7)
        
        
       #left side button frame
       
        btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=470,width=650,height=38)
        
        #save button
        
        btn_Add=Button(btn_frame,text="Save", command=self.add_data,font=("arial", 11, "bold"),width=17 ,bg="blue",fg="white")
        btn_Add.grid(row=0,column=0,sticky=W,padx=1)
        
        # update
        
        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial", 11, "bold"),width=17 ,bg="blue",fg="white")
        btn_update.grid(row=0,column=1,sticky=W,padx=1)
        
        #delete
        
        btn_delete=Button(btn_frame,text="Delete",font=("arial", 11, "bold"),width=17 ,bg="blue",fg="white")
        btn_delete.grid(row=0,column=2,sticky=W,padx=1)
        
        
        #reset
        
        btn_reset=Button(btn_frame,text="Reset",font=("arial", 11, "bold"),width=17 ,bg="blue",fg="white")
        btn_reset.grid(row=0,column=4,sticky=W,padx=1)
        
        #************************************************************************************************************
        #right label frame start
        
        
    
        
        #right Frame 
        DatarightFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        DatarightFrame.place(x=680,y=10,width=800,height=540)
        
        
        #img1
        
        img_6 = Image.open(r"college_images\6th.jpg")
        img_6 = img_6.resize((790,200), Image.LANCZOS)

        self.photoimg_6 = ImageTk.PhotoImage(img_6)
        
        my_img=Label(DatarightFrame,image=self.photoimg_6,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=790,height=200)
        
        #right hand search frame
        
        Search_Frame=LabelFrame(DatarightFrame,bd=4,relief=RIDGE,padx=2,text=" Search Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        Search_Frame.place(x=0,y=200,width=790,height=60)
        
        #search option btn
        
        search_by=Label(Search_Frame,text="Search By:", font=("arial", 11, "bold"), bg="black",fg="red")
        search_by.grid(row=0,column=0,sticky=W,padx=2,pady=7)
        
         #combo box creat
        com_txt_search=ttk.Combobox(Search_Frame, font=("arial", 12, "bold"), width=18, state="readonly")
        com_txt_search['value']=("Select Option","Rollno","phoneno","Student_id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)
        
        #entry fill
        
        search_entry=ttk.Entry(Search_Frame,font=("arial", 11, "bold"),width=22)
        search_entry.grid(row=0,column=2,sticky=W,padx=5,)
        
        # right side button for rest
        
        btn_search=Button(Search_Frame,text="Reset",font=("arial", 11, "bold"),width=14,bg="blue",fg="white")
        btn_search.grid(row=0,column=3,sticky=W,padx=5)
        
        #show all btn
        
        btn_showAll=Button(Search_Frame,text="Show All",font=("arial", 11, "bold"),width=14 ,bg="blue",fg="white")
        btn_showAll.grid(row=0,column=4,sticky=W,padx=5)
        
        
        
        
        #*****************STUDENT TABLE AND SCROLL BAR  *****************************************
        
        
        
      # use place for outside of frame
      
      #use grid for put somne thing inside the frame
      
        table_frame=Frame(DatarightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=260,width=790,height=250)
        
        #scrol bar
        
        
        # Scrollbars
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
    
    columns=("dep", "course","year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher"),
    xscrollcommand=scroll_x.set,
    yscrollcommand=scroll_y.set
)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        # Define headings
        self.student_table.heading("course", text="Course")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Class Division")
        self.student_table.heading("roll", text="Roll Number")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone Number")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("year", text="Year")
        
        
        self.student_table["show"]= "headings"
        
      #  Set column widths (optional)
        for col in self.student_table["columns"]:
         self.student_table.column(col, width=100)
         
    
        self.student_table.pack(fill=BOTH, expand=1)
        
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        #create a function  and with the help of this function enetr the data in database

    def add_data(self):
      if(self.var_dep.get()==""or self.var_email.get()==""or self.var_id.get()==""):
        messagebox.showerror("Error","All fields Are Required")
      else:
          try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Sumit@0000",database="project_student")
            my_cursur=conn.cursor() 
            my_cursur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
              
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(), 
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_id.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        
                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Seccess","Student has been added!",parent=self.root)
            
          except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)                   
        
        # fetch function
        
        
    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="Sumit@0000",database="project_student")
      my_cursur=conn.cursor()
      my_cursur.execute("select * from student")
      data=my_cursur.fetchall()
      if len(data)!=0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
          self.student_table.insert("",END,values=i)
        conn.commit()
      conn.close()
        
          # GET CURSOR
    def get_cursor(self,event=""):
      cursor_row=self.student_table.focus()
      content=self.student_table.item(cursor_row)
      data=content["values"]
      
      self.var_dep.set(data[0])
      self.var_course.set(data[1])
      self.var_year.set(data[2])
      self.var_semester.set(data[3])
      self.var_id.set(data[4])
      self.var_name.set(data[5])
      self.var_div.set(data[6])
      self.var_roll.set(data[7])
      self.var_gender.set(data[8])
      self.var_dob.set(data[9])
      self.var_email.set(data[10])
      self.var_phone.set(data[11])
      self.var_address.set(data[12])
      self.var_teacher.set(data[13])       
        
      #update data 
      # update student set dep=%s,course=%s,year=%s,sem=%s, name=%s, div=%s, roll=%s,gender=%s,dob=%s, email=%s, phone=%s, address=%s, teacher=%s     ehere id=%s"
    def update_data(self):
      if(self.var_dep.get()==""or self.var_email.get()==""or self.var_id.get()==""):
        messagebox.showerror("Error","All fields Are Required")
      else:
        try:
          update=messagebox.askyesno("update","Are you sure update this student data",parent=self.root)
          if update>0:  
            conn=mysql.connector.connect(host="localhost",username="root",password="Sumit@0000",database="project_student")
            my_cursur=conn.cursor()
            my_cursur.execute("update student set dep=%s,course=%s,year=%s,sem=%s, name=%s, div=%s, roll=%s,gender=%s,dob=%s, email=%s, phone=%s, address=%s, teacher=%s    where id=%s",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(), 
                                                                                                        self.var_semester.get(),
                                                                                                        # self.var_id.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_id.get()
                                                                                                        
                                                                                                         ))
        
        
          else:
            if not update:
              return
          conn.commit()
          self.fetch_data()
          conn.close() 
          
          messagebox.showinfo("Seccess","Student Successfully update",parent=self.root) 
              
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)   
        
        
      # delete
      
   

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
