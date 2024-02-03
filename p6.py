from tkinter import *
from sqlite3 import *
from tkinter.messagebox import *


root=Tk()
root.title("app by me")
root.geometry("800x600+200+100")
f=("Arial",30,"bold")
p=5


label=Label(root,text="success app",font=f)
label.pack(pady=p)

labname=Label(root,text="enter name",font=f)
entName= Entry(root,font=f)
labname.pack(pady=p)
entName.pack(pady=p)

labcollege=Label(root,text="enter college",font=f)
entCompany= Entry(root,font=f)
labcollege.pack(pady=p)
entCompany.pack(pady=p)

labelpkg=Label(root,text="enter pkg",font=f)
entPkg= Entry(root,font=f)
labelpkg.pack(pady=p)
entPkg.pack(pady=p)

def save():
	name = entName.get()
	company= entCompany.get()
	pkg=float(entPkg.get())
	con=None
	
	try:
		con=connect("tulsi.db")
		cursor=con.cursor()
		sql="insert into student values('%s','%s','%f')"
		cursor.execute(sql %(name,company,pkg))
		con.commit()
		showinfo("Done", "cograts")
		entName.delete(0,END)
		entCompany.delete(0,END)
		entPkg.delete(0,END)
		entName.focus()
		




	except Exception as e:
		msg="issue"+str(e)
		print("problem",msg)
	finally:
		if con is not None:
			con.close()

button = Button(root,text="Submit",font=f,command=save)
button.pack(pady=p)
root.mainloop()