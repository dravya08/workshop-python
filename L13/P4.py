#wapp to update into student
import cx_Oracle
con = None
try:
	con = cx_Oracle.connect("system/abc123")
	print("connected")
	name = input("enter the name ")
	rno = int(input("input the rno "))
	
	cursor = con.cursor()
	sql = "update student set name= '%s' where rno = '%d'"
	args = (name, rno)
	cursor.execute(sql % args)
	con.commit()
	print(cursor.rowcount,'rows updated')
except cx_Oracle.DatabaseError as e:
	con.rollback()
	print("issue ", e)
finally:
	if con is not None:
		con.close()
		print("disconnected")