
from sqlite3 import *
con=None


try:
	con=connect("kit.db");
	cursor=con.cursor();
	sql="delete from emp where id ='%d'"
	id = int(input("enter the id "))
	cursor.execute(sql %(id))
	if cursor.rowcount == 1:
		con.commit()
		print("record deleted")
	else:
		print("record does not exist")
except Exception as e:
	print("isseu",e)
finally:
	if con is not None:
		con.close()