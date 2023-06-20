
#python -m venv myenv
#myenv\Scripts\activate
#pip install requests
#pip install flask
#pip install flask-sqlalchemy
#API>pip freeze > requirements.txt
#https://api.stackexchange.com/docs/questions#order=desc&sort=activity&filter=default&site=stackoverflow&run=true

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Define your database model(s) here
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    drinks_data = [{'name': drink.name, 'description': drink.description} for drink in drinks]
    return jsonify({'drinks': drinks_data})

@app.route('/drinks/<int:drink_id>')
def get_drink(drink_id):
    drink = Drink.query.get(drink_id)
    if drink:
        drink_data = {'name': drink.name, 'description': drink.description}
        return jsonify(drink_data)
    else:
        return jsonify({'message': 'Drink not found'})
    
@app.route('/drinks', methods=['POST'])
def add_drink():
    drink_data = request.get_json()
    name = drink_data.get('name')
    description = drink_data.get('description')
    
    if not name or not description:
        return jsonify({'message': 'Invalid drink data'})
    
    existing_drink = Drink.query.filter_by(name=name).first()
    if existing_drink:
        return jsonify({'message': 'Drink already exists'})
    
    new_drink = Drink(name=name, description=description)
    db.session.add(new_drink)
    db.session.commit()
    
    return jsonify({'message': 'Drink added successfully'})

# http://127.0.0.1:5000/drinks
# {
#   "name": "New Drink",
#   "description": "New Drink Description"
# }
# body, raw, jsonify
# {
#     "message": "Drink added successfully"
# }

@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
def delete_drink(drink_id):
    drink = Drink.query.get(drink_id)
    if drink:
        db.session.delete(drink)
        db.session.commit()
        return jsonify({'message': 'Drink deleted successfully'})
    else:
        return jsonify({'message': 'Drink not found'})
    
    
@app.route('/drinks/<int:drink_id>', methods=['PUT'])
def update_drink(drink_id):
    drink = Drink.query.get(drink_id)
    if not drink:
        return jsonify({'message': 'Drink not found'}), 404

    drink_data = request.get_json()
    name = drink_data.get('name')
    description = drink_data.get('description')
    if not name or not description:
        return jsonify({'message': 'Invalid drink data'}), 400

    drink.name = name
    drink.description = description
    db.session.commit()

    return jsonify({'message': 'Drink updated successfully'})


if __name__ == '__main__':
    app.run(debug=True)
