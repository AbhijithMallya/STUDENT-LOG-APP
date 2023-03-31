from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
 
mysql = MySQL(app)
 
@app.route('/')
@app.route('/form')
def form():
    return render_template('form.html')
 

@app.route('/view',  methods = ['POST', 'GET'] )
def view_page():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student")
    data = cur.fetchall()
    return render_template('view.html', data=data)



@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO student VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
        return form()


if __name__ =='__main__':
    app.debug=True
    app.run()