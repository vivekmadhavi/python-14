
#wapp to insert data into student table

from sqlite3 import *

con = None

try:
	con = connect("kc.db")
	cursor = con.cursor()
	sql = "insert into student values('%d','%s')"
	rno = int(input("enter the roll no"))
	name = input("enter the name ")
	cursor.execute(sql % (rno,name))
	con.commit()
	print("record created")

except Exception as e:
	con.rollback()
	print("issue",e)


finally:
	if con is not None:
		con.close()