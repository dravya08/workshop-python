#wapp to delete into student
import cx_Oracle
con = None
try:
	con = cx_Oracle.connect("system/abc123")
	print("connected")
	rno = int(input("enter the rno to delete "))
	
	cursor = con.cursor()
	sql = "delete from student where rno ='%d'"
	args = (rno)
	cursor.execute(sql % args)
	con.commit()
	print(cursor.rowcount,'rows deleted')
except cx_Oracle.DatabaseError as e:
	con.rollback()
	print("issue ", e)
finally:
	if con is not None:
		con.close()
		print("disconnected")