
from sqlite3 import *
con=None


try:
	con=connect("kit.db");
	cursor=con.cursor();
	sql="insert into emp values('%d','%s','%f')"
	id = int(input("enter the id "))
	name =input("enter the name ")
	salary =float(input("enter the salary"))
	cursor.execute(sql %(id, name ,salary))
	con.commit()
	print("record created")
except Exception as e:
	print("isseu",e)
finally:
	if con is not None:
		con.close()