from flask import Flask 
#from sqlalchemy import create_engine
#from json import dumps
from flask import jsonify
from flask import request


#sqleng = create_engine('sqlite:///employee.db')
app = Flask(__name__)

employeeDB=[
 {
 'name':'john',
 'email_id':'john@gmail.com',
 'manager_email_id':'johnsmanager@gmail.com'
 },
 {
 'name':'snow',
 'email_id':'snow@gmail.com',
 'manager_email_id':'john@gmail.com'
 },
 {
 'name':'rick',
 'email_id':'rick@gmail.com',
 'manager_email_id':'snow@gmail.com'
 }
 ]

@app.route('/')
def index():
	return "Hello Fyle!"

@app.route('/addEmployee', methods=['POST'])
def createEmployee():
	name = str(input("Enter the name: "))
	email_id = str(input("Enter the employee emailID: "))
	manager_email_id = str(input("Enter the employee manager emailID: "))
	data = {
	'name' : name,
	'email_id' : email_id,
	'manager_email_id' : manager_email_id
	}

	employeeDB.append(data)
	return jsonify(data)


@app.route('/orgTree/<empId>', methods=['GET'])
def getOrgTree(empId):
	relationList = []
	relationList.append(empId)
	for i in range(len(employeeDB)):
		if employeeDB[i]['manager_email_id']==empId:
			relationList.append(employeeDB[i]['email_id'])
		if empId==employeeDB[i]['email_id']:
			relationList.insert(0,employeeDB[i]['manager_email_id'])
	
	return relationList



@app.route('/emp/<empId>', methods=['GET'])
def getEmployee(empId):
	usr = [emp for emp in employeeDB if (emp['email_id'] == empId)] 
	return jsonify({'emp':usr})



if __name__ == '__main__':
	app.run(debug=True)