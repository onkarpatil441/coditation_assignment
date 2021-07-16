from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request

car = Flask(__name__)

car.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/category'
 
db= SQLAlchemy(car)



class carcompany(db.Model):
   no = db.Column(db.Integer, primary_key = True)
   companyname = db.Column(db.String(500))

   def __init__(self,no,companyname):
	   self.no = no
	   self.companyname = companyname




@car.route("/carcompany", methods=["GET"])
def get_carcompanys():
	result = db.engine.execute("select * from carcompany")
	response = []
	for row in result:
		response.append({
			"No": row["no"],
			"Companyname": row["companyname"]
			})
	response = {"carcompany": response}
	return response





@car.route("/carcompany", methods=["POST"])
def create_carcompany():
	print(request.json)
	carcompany = Carcompany(request.json["no"], request.json["companyname"])
	db.session.add(carcompany)
	db.session.commit()
	





if __name__ == "__main__":
	car.run(host="localhost", port="100")