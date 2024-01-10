from flask import Flask, request, jsonify
app = Flask(__name__)

users_list = [
    {
        "id": 0,
        "name": "Is-haaq Omar",
        "age": "23",
        "DOB": "10 aprill 2000",
    },
]

@app.route("/")
def index():
    return "Hi!"

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        if len(users_list) > 0:
            return jsonify(users_list)
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        new_name = request.form['name']
        new_age = request.form['age']
        new_DOB = request.form['DOB']
        iD = users_list[-1]['id']+1

        new_obj = {
            'id' : iD,
            'name' : new_name,
            'age' : new_age,
            'DOB' : new_DOB,
        }
        users_list.append(new_obj)
        return jsonify(users_list), 201
    
@app.route('/user/<int:id>', methods= ['GET', 'PUT', 'DELETE'])
def single_user(id):
    if request.method == 'GET':
        for user in users_list:
            if user['id'] == id:
                return jsonify(user)
            pass
    if request.method == 'PUT':
        for user in users_list:
            if user['id'] == id:
                user['name'] = request.form['name']
                user['age'] = request.form['age']
                user['DOB'] = request.form['DOB']
                updated_user = {
                    'id': id,
                    'name': user['name'],
                    'age': user['age'], 
                    'DOB': user['DOB']
                }
                return jsonify(updated_user)
    if request.method == 'DELETE':
        for index, user in enumerate(users_list):
            if user['id'] == id:
                users_list.pop(index)
                return jsonify(users_list)     

if __name__ == '__main__':
    app.run()
