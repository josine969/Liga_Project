# Importo el modulo SQLITE. Abro la conexion con la BBDD
import sqlite3
conn = sqlite3.connect('futbol.db')
curs = conn.cursor()
# Creo Tabla
#curs.execute('create table Liga_Verano (Nombre, Puntos, Media)')
# Añado un valor
#curs.execute("insert into Equipo values ('Oviedo', 60)")
# Añado muchos valores
values = [('Compostela', 0, 50), ('Valencia', 0, 65), ('Oviedo', 0, 70), ('Deportivo', 0, 80)]
curs.executemany('insert into Liga_Verano values(?,?,?)', values)
# Hago Commit y cierro conexion
conn.commit()
conn.close()