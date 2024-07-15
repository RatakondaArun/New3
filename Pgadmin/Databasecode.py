from flask import Flask,redirect,url_for,render_template,jsonify,request
import psycopg2
from psycopg2 import Error,extras
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def con():
    connection=None
    try:
        connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="admin",
    dbname="postgres",
    port=5432
  
        )
    except Error as e:
        print(f"the error is '{e}")
    return connection
@app.route('/')
def fetch():
    return 'helloworld'
@app.route('/item/<int:id>',methods=["GET"])
def fun(id):
    connection= con()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('select * from surya1 where id = %s',(id,))
    items = cursor.fetchone()
    cursor.close()
    connection.close()
    if items:
        return jsonify(dict(items))
    else:
        return jsonify({"error":"item not found"})
    
@app.route('/postitem',methods=["POST"])
def createitem():
    data = request.get_json()
    name=data.get('name')
    email=data.get('email')
    connection=con()
    cursor= connection.cursor()
    cursor.execute("insert into surya1 (name,email) values(%s,%s)",(name,email))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message":"item inserted to the database"})


if __name__ == "__main__":
    app.run(debug=True)