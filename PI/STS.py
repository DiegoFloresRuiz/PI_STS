from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='public', template_folder='templates')
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "STS"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('inicio1.html')

@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/tkd')
def tkd():
    return render_template('tkd.html')

@app.route('/nat')
def nat():
    return render_template('nat.html')

@app.route('/bl')
def bl():
    return render_template('bl.html')

@app.route('/fut')
def fut():
    return render_template('fut.html')

@app.route('/bol')
def bol():
    return render_template('bol.html')

@app.route('/box')
def box():
    return render_template('box.html')

@app.route('/don')
def don():
    return render_template('don.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        cursor.close()
        if user:
            session['user'] = user
            return redirect(url_for('inicio'))
        else:
            return render_template('login.html', error='Credenciales incorrectas. Inténtelo de nuevo.')
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)", (nombre, email, password))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('index'))
    return render_template('registro.html')

# Agrega más rutas y funciones según sea necesario

if __name__=='__main__':
    app.run(port= 9005, debug=True)


