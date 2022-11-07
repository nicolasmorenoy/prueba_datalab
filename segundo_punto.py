from flask import Flask, render_template

import sqlite3

app = Flask(__name__)
proyectos = []
usuarios = []



@app.route('/proyecto/<id_proyecto>', methods= ['GET'])
def proyecto(id_proyecto):
    database = sqlite3.connect("./sitio.db")
    cursor = database.cursor()
    cursor.execute("SELECT project_name FROM project WHERE id = ?", id_proyecto)
    project = cursor.fetchone()
    proyectos.append(project[0])
    print(proyectos)
    cursor.execute("SELECT user.id, user.username, user.password, user.profile_picture, user.user_full_name, role.id, role.name, role.description from user JOIN user_role_association_table ON user.id = user_role_association_table.user_id JOIN role ON user_role_association_table.role_id = role.id")
    query= cursor.fetchall()
    for i in query:
        usuarios.append(i)
    
    resultado_dict = {"proyectos": proyectos, "usuarios": usuarios}
    

    return render_template("proyecto.html",resultado_dict = resultado_dict)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

