import sqlite3


#----------las funciones extras de modificacion de datos mas abajo del codigo
#conecta a la base datos
#conn = sqlite3.connect('escuela2.db')

#crea cursor
#c = conn.cursor()

#--------------crea tabla
# c.execute("""CREATE TABLE escuela2 (
# 	fist_name text,
# 	last_name text,
# 	email text
# )""")


#--------------inserta datos en las tablas de la base de datos escuela2
# many_escuela2 = [
# ('andres', 'gutierrez', 'garlot7@gmail.com'),
# ('jose', 'perez', 'jose@gmail.com'),
# ('josefina', 'ramirez', 'fina@gmail.com'),

# ]

# c.executemany("INSERT INTO escuela2 VALUES (?,?,?)", many_escuela2)


#--------------asigna clave primaria a los datos de la tabla
# c.execute("SELECT rowid, * FROM escuela2")

# items = c.fetchall()

# for item in items:
# 	print(item)


#--------------editar tablas en este caso se edita el nombre josefina con el id de 3 
#--------------por el nombre de maria
# c.execute("""UPDATE escuela2 SET fist_name = 'maria'
#               WHERE rowid = 3
#               """)

# conn.commit()

# c.execute("SELECT rowid, * FROM escuela2")

# items = c.fetchall()

# for item in items:
# 	print(item)


#--------------eliminar datos en este caso se elimina el dato con el id 3que en este caso es maria

# c.execute("DELETE from escuela2 WHERE rowid = 3")

# #commit nuestro comando
# conn.commit()

# c.execute("SELECT rowid, * FROM escuela2")

# items = c.fetchall()
# for item in items:
# 	print(item)


#cierra conexion
#conn.close()

#---------muestra los datos

def mostrar():
	conn = sqlite3.connect('escuela2.db')

	c = conn.cursor()

	c.execute("SELECT rowid, * FROM escuela2")

	items = c.fetchall()

	for item in items:
		print(item)

	conn.commit()

	conn.close()

#---------agrega nuevos datos a la tabla

def agregar(fist_name,last_name,email):
	conn = sqlite3.connect('escuela2.db')

	c = conn.cursor()

	c.execute("INSERT INTO escuela2 VALUES (?,?,?)", (fist_name,last_name,email))

	conn.commit()



# 	conn.close()

def eliminar(id):
	conn = sqlite3.connect('escuela2.db')
	c = conn.cursor()
	c.execute("DELETE from escuela2 WHERE rowid = (?)", id)

	#commit de nuestro comando
	conn.commit()
	conn.close()
