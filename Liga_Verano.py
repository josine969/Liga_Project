import sqlite3
import random
conn = sqlite3.connect('futbol.db')
curs = conn.cursor()

Temporal = []
Local = ["Test"]
Visitante = []
Cont_Equipos = 0

# Eleccion de equipos
while Cont_Equipos < 2:
    Rival = 0
    Rival = random.randint(1, 4)
    print(Rival)
    curs.execute('SELECT * FROM Liga_Verano WHERE rowid=?', [Rival])
    Temporal = curs.fetchone()
    print(Temporal[0])
    print(Local[0])
    if Temporal[0] == Local[0]:
        print("Repeditos")
    else:
        Cont_Equipos +=1
        if Cont_Equipos == 1:
            Local = Temporal
        else:
            Visitante = Temporal

print (Local)
print (Visitante)

# Partido
print ("Comienza el partido entre", Local[0], "y", Visitante[0])
Fuerza_local = random.randint(0, 6)
Fuerza_Visitante = random.randint(0, 6)
# Test para Git

print ("El", Local[0], "ha conseguido", Fuerza_local, "Goles")
print ("El", Visitante[0], "ha conseguido", Fuerza_Visitante, "Goles")


Fuerza_local = Local[2] * Fuerza_local
Fuerza_Visitante = Visitante[2] * Fuerza_Visitante

# Resultado Final
if Fuerza_local > Fuerza_Visitante:
    print ("El equipo", Local[0], "ha ganado el partido")
    curs.execute('Update Liga_Verano set Puntos = Puntos + 3 Where Nombre=?', [Local[0]])
elif Fuerza_local < Fuerza_Visitante:
   print ("El equipo", Visitante[0], "ha ganado el partido")
   curs.execute('Update Liga_Verano set Puntos = Puntos + 3 Where Nombre=?', [Visitante[0]])
else:
    print ("Hemos tenido un empate")
    curs.execute('Update Liga_Verano set Puntos = Puntos + 1 Where Nombre=?', [Local[0]])
    curs.execute('Update Liga_Verano set Puntos = Puntos + 1 Where Nombre=?', [Visitante[0]])

conn.commit()
conn.close()
