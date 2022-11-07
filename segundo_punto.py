from flask import Flask, jsonify

import sqlite3, json

app = Flask(__name__)


@app.route('/proyecto/<id_proyecto>', methods= ['GET'])
def proyecto(id_proyecto):
    database = sqlite3.connect("./sitio.db")
    cursor = database.cursor()
    #cursor.execute("SELECT project_name FROM project WHERE id LIKE ?", (f"%{id_proyecto}%",))
    cursor.execute("SELECT * FROM project WHERE project_name LIKE ?", (f"%{id_proyecto}%",))

    projects = cursor.fetchall()
    proyectos = [i for i in projects]
    proyectos = json.dump(proyectos)
    print(proyectos)
    cursor.execute("SELECT user.id, user.username, user.password, user.profile_picture, user.user_full_name, role.id, role.name, role.description from user JOIN user_role_association_table ON user.id = user_role_association_table.user_id JOIN role ON user_role_association_table.role_id = role.id")
    #cursor.execute("SELECT * from user JOIN user_role_association_table ON user.id = user_role_association_table.user_id JOIN role ON user_role_association_table.role_id = role.id")
    query= cursor.fetchall()
    usuarios = [i for i in query]
    usuarios = json.dump(usuarios)
    
    resultado_dict = {"proyectos": proyectos, "usuarios": usuarios,}
    
    return jsonify(resultado_dict)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

