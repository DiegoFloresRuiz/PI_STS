from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import os

app = Flask(__name__, static_folder='public', template_folder='templates')

# Configuración de la base de datos
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "STS"
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

# Directorio para guardar imágenes subidas
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Rutas básicas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inicio')
def inicio():
    return render_template('index.html')

@app.route('/tkd')
def tkd():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tkd")
    data = cursor.fetchall()
    cursor.close()
    return render_template('tkd.html', items=data)

@app.route('/nat')
def nat():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM natacion")
    data = cursor.fetchall()
    cursor.close()
    return render_template('nat.html', items=data)

@app.route('/bl')
def bl():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM baloncesto")
    data = cursor.fetchall()
    cursor.close()
    return render_template('bl.html', items=data)

@app.route('/fut')
def fut():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM futbol")
    data = cursor.fetchall()
    cursor.close()
    return render_template('fut.html', items=data)

@app.route('/bol')
def bol():
    return render_template('bol.html')

@app.route('/don')
def don():
    return render_template('don.html')

# Donar Taekwondo
@app.route('/donar_tkd', methods=['POST'])
def donar_tkd():
    article_name = request.form['articleName']
    size = request.form['size']
    color = request.form['color']
    team_name = request.form.get('teamName', '')

    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO tkd (Nombre, Talla, Color, NombreEquipo) VALUES (%s, %s, %s, %s)",
        (article_name, size, color, team_name)
    )
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('tkd'))

# Donar Natación
@app.route('/donar_nat', methods=['POST'])
def donar_nat():
    article_name = request.form['articleName']
    size = request.form['size']
    color = request.form['color']
    team_name = request.form.get('teamName', '')

    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO natacion (Nombre, Talla, Color, NombreEquipo) VALUES (%s, %s, %s, %s)",
        (article_name, size, color, team_name)
    )
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('nat'))

# Donar Baloncesto
@app.route('/donar_bl', methods=['POST'])
def donar_bl():
    article_name = request.form['articleName']
    size = request.form['size']
    color = request.form['color']
    team_name = request.form.get('teamName', '')

    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO baloncesto (Nombre, Talla, Color, NombreEquipo) VALUES (%s, %s, %s, %s)",
        (article_name, size, color, team_name)
    )
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('bl'))

# Donar Fútbol
@app.route('/donar_fut', methods=['POST'])
def donar_fut():
    article_name = request.form['articleName']
    size = request.form['size']
    color = request.form['color']
    team_name = request.form.get('teamName', '')

    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO futbol (nombre_articulo, talla, color, nombre_equipo) VALUES (%s, %s, %s, %s)",
        (article_name, size, color, team_name)
    )
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('fut'))

# Voleibol
@app.route('/voleibol')
def voleibol():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM voleibol')
    items = cursor.fetchall()
    cursor.close()
    items = [{'nombre_articulo': item[1], 'talla': item[2], 'color': item[3], 'nombre_equipo': item[4]} for item in items]
    return render_template('bol.html', items=items)

@app.route('/donar_vo', methods=['POST'])
def donar_vo():
    article_name = request.form['articleName']
    size = request.form['size']
    color = request.form['color']
    team_name = request.form.get('teamName')

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO voleibol (nombre_articulo, talla, color, nombre_equipo) VALUES (%s, %s, %s, %s)',
                   (article_name, size, color, team_name))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('voleibol'))

# Box
@app.route('/box_items')
def box_items():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM box')
    items = cursor.fetchall()
    cursor.close()
    items = [{'nombre_articulo': item[1], 'talla': item[2], 'color': item[3], 'nombre_equipo': item[4]} for item in items]
    return render_template('box.html', items=items)

@app.route('/donar_box', methods=['POST'])
def donar_box():
    article_name = request.form['articleName']
    size = request.form['size']
    color = request.form['color']
    team_name = request.form.get('teamName')

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO box (nombre_articulo, talla, color, nombre_equipo) VALUES (%s, %s, %s, %s)',
                   (article_name, size, color, team_name))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('box_items'))

if __name__ == '__main__':
    app.run(port=9005, debug=True)









