from flask import Flask,render_template,request,redirect,url_for
import shcema
data1 = shcema.data1()
data2 = shcema.data2()
app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def signin():
	if request.method == 'GET':
		message = ''
		return render_template('sigin.html',message=message )
	else:
		fullname = request.form['username']
		passw = request.form['pass']
		data = shcema.signin(fullname)
		if passw == data:
			message = 'signin successfull'
			return render_template('dashb.html',message = message,username = fullname,data1= data1,data2 = data2)

		else:
			message = 'Invalid password or username click sign up to register'
			return render_template('sigin.html',message=message)
@app.route('/signup',methods = ['GET','POST'])
def signup():
	if request.method == 'GET':
		message = 'signup'
		return render_template('signup.html',message=message )
	else:
		fullname = request.form['username']
		passw = request.form['pass']
		message = shcema.signup(fullname,passw)
		return render_template('sigin.html',message = message)
@app.route('/npass',methods = ['GET','POST'])
def npass():
	if request.method == 'GET':
		return render_template('npass.html')
	else:
		user = request.form['user']
		newp = request.form['newp']
		agian = request.form['agian']
		if newp == agian:
			if newp.istitle() and newp.isalnum():
				message = shcema.change_pass(user,newp)
				return render_template('sigin.html',message = message)
			else:
				message = 'The Password Should Contain Capital Letter At Begining and Atleast One Number !'
				return render_template('npass.html',message = message)
		else:
			message = "Password Miss Match"
			return render_template('npass.html',message = message)
@app.route('/dash',methods = ['GET' , 'POST'])
def data():
	if request.method == 'GET':
		
		return render_template('dashb.html',data1= data1,data2 = data2,message = 'Hello')
	return render_template('dashb.html',data1= data1,data2 = data2,message = 'Hello')
@app.route('/add_todo',methods = ['GET','POST'])
def add_todo():
	if request.method == 'GET':
		return render_template('add_task.html',data1= data1,data2 = data2)
	s_no = request.form['s_no']
	task = request.form['task']
	add = shcema.add_todo(s_no,task)
	return render_template('dashb.html',message = add,data1= data1,data2 = data2)

@app.route('/del_todo',methods = ['GET','POST'])
def del_todo():
	if request.method == 'GET':
		return render_template('del_task.html',data1= data1,data2 = data2)
	task = request.form['task']
	dele = shcema.del_todo(task)
	return render_template('dashb.html',message = dele,data1= data1,data2 = data2)

@app.route('/del_list',methods = ['GET','POST'])
def del_list():
	if request.method == 'GET':
		dele = shcema.del_list()
		return render_template('del_list.html',message = dele)
@app.route('/Terms',methods = ['GET'])
def terms():
	return render_template('terms.html')
@app.route('/About',methods = ['GET'])
def about():
	return render_template('aboutus.html')
@app.route('/Privacy',methods = ['GET'])
def privacy():
	return render_template('privacy.html')

if __name__ =='__main__':
	app.run(debug = True)