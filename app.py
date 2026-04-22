from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def conectar():
    return sqlite3.connect('citas.db')

# 🔸 Mostrar citas
@app.route('/')
def index():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes")
    citas = cursor.fetchall()
    conn.close()
    return render_template('index.html', citas=citas)

# 🔸 Agregar cita
@app.route('/agregar', methods=['GET','POST'])
def agregar():
    if request.method == 'POST':
        mascota = request.form['mascota']
        propietario = request.form['propietario']
        especie = request.form['especie']
        fecha = request.form['fecha']

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pacientes (mascota, propietario, especie, fecha) VALUES (?,?,?,?)",
                       (mascota, propietario, especie, fecha))
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('agregar.html')

# 🔸 Editar cita
@app.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    conn = conectar()
    cursor = conn.cursor()

    if request.method == 'POST':
        mascota = request.form['mascota']
        propietario = request.form['propietario']
        especie = request.form['especie']
        fecha = request.form['fecha']

        cursor.execute("""
        UPDATE pacientes 
        SET mascota=?, propietario=?, especie=?, fecha=? 
        WHERE id=?
        """, (mascota, propietario, especie, fecha, id))

        conn.commit()
        conn.close()
        return redirect('/')

    cursor.execute("SELECT * FROM pacientes WHERE id=?", (id,))
    cita = cursor.fetchone()
    conn.close()

    return render_template('editar.html', cita=cita)

# 🔸 Eliminar cita
@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pacientes WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)