
import sqlite3 as db
 
def conexion():
    conn = db.connect("BD/asistencia_db.db")
    return conn

def verifica_usuario(usuario, password):
    try:
        conn = conexion()
        cursor = conn.cursor()
        cursor.execute(f"""SELECT u.nom_usuario, u.email, u.contraseña, r.descripcion
                        from Usuario as u INNER JOIN Rol as r ON u.id_rol = r.id_rol
                        where (u.nom_usuario = '{usuario}' or u.email = '{usuario}') 
                       and u.contraseña = '{password}';""")
        filas = cursor.fetchall()
    except Exception as e:
        print("ERROR:", e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        if len(filas) > 1:
            return False, True
        elif len(filas)==0:
            return False, False
        else:
            return True, filas[0][3]
        
    