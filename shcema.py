import mysql.connector as c

def signin(user):
	con = c.connect(host = "localhost",user = "root",password = "honeychandu",database = 'python_db')
	cursor = con.cursor()
	cursor.execute(
		"""
	select password from signup where Fullname = '{name}' ORDER BY Fullname DESC;

			""".format(name = user)

			)
	data = cursor.fetchone()[0]
	con.commit()
	con.close()
	cursor.close()
	return data
def signup(user,passw):

	con = c.connect(host = "localhost",user = "root",password = "honeychandu",database = 'python_db',buffered = True)
	cursor = con.cursor()
	cursor.execute(
		"""
	select password from signup where Fullname = '{name}' ORDER BY Fullname DESC;

			""".format(name = user)

			)
	data = cursor.fetchone()
	
	if data is None :
		cursor.execute(
			"""
		insert into signup(Fullname,password)values('{n}','{p}');

				""".format(n = user,p=passw)

				)
		con.commit()
		con.close()
		cursor.close()
	else:
		message = 'Your Username Already Exist Please Login'
		return message
	message =  'Registered Successfully'
	return message
def change_pass(user,npass):
	con = c.connect(host = 'localhost',user = 'root',password = 'honeychandu',database = 'python_db')
	cursor = con.cursor()
	cursor.execute(
		'''
		select Fullname from signup where Fullname = '{user}' ORDER BY Fullname DESC;


		'''.format(user = user)
		)
	data = cursor.fetchone()
	if data is None:
		return 'Username is wrong!!!'
	else:	
		cursor.execute(
			'''
			update signup set password = '{npass}' where Fullname = '{user}';

			'''.format(npass = npass,user = user)
			)
		con.commit()
		con.close()
		cursor.close()	
		return 'Password updated Successfully'


def data2():
	con = c.connect(host = 'localhost',user = 'root',password = 'honeychandu',database = 'python_db')
	cursor = con.cursor()
	cursor.execute(
		'''
		select task from task ORDER BY s_no DESC;


		'''
		)
	a = []
	data2 = cursor.fetchall()
	for i in range(len(data2)):
		users = data2[i][0]
		a.append(users)


	con.commit()
	con.close()
	cursor.close()	
	return a
def data1():
	con = c.connect(host = 'localhost',user = 'root',password = 'honeychandu',database = 'python_db')
	cursor = con.cursor()
	cursor.execute(
		'''
		select s_no from task ORDER BY s_no DESC;


		'''
		)
	a = []
	data1 = cursor.fetchall()
	for i in range(len(data1)):
		users = data1[i][0]
		a.append(users)


	con.commit()
	con.close()
	cursor.close()	
	return a
def add_todo(no,task):
	con = c.connect(host = 'localhost',user = 'root',password = 'honeychandu',database = 'python_db')
	cursor = con.cursor()
	cursor.execute(
		'''
		insert into task(s_no,task)values('{no}','{task}');



		'''.format(no = no,task = task)
		)
	con.commit()
	con.close()
	cursor.close()
	return 'Successfully added a task'
def del_todo(task):
	con = c.connect(host = 'localhost',user = 'root',password = 'honeychandu',database = 'python_db')
	cursor = con.cursor()
	cursor.execute(
		'''
		delete from task where task = '{task}';



		'''.format(task = task)
		)
	con.commit()
	con.close()
	cursor.close()
	return 'Successfully deleted a task'
def del_list():
	con = c.connect(host = 'localhost',user = 'root',password = 'honeychandu',database = 'python_db')
	cursor = con.cursor()
	cursor.execute(
		'''
		drop table task;



		'''
		)
	con.commit()
	con.close()
	cursor.close()
	return 'Successfully deleted a list'
	
