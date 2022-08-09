# Partidos Amistosos
import sqlite3
import random
conn = sqlite3.connect('futbol.db')
curs = conn.cursor()

Local = []
Visitante = []
Cont_Equipos = 0

# Eleccion de equipos
while Cont_Equipos < 2:
    print("¿Qué equipo juega hoy?")
    Rival = input()
    curs.execute('SELECT * FROM Equipo WHERE Nombre=?', [Rival])
    Cont_Equipos +=1
    if Cont_Equipos == 1:
        Local = curs.fetchone()
    else:
        Visitante = curs.fetchone()

print (Local)
print (Visitante)

# Comienza el partido
print ("Comienza el partido entre", Local[0], "y", Visitante[0])
Fuerza_local = random.randint(0, 6)
Fuerza_Visitante = random.randint(0, 6)

print ("El", Local[0], "ha conseguido", Fuerza_local, "Goles")
print ("El", Visitante[0], "ha conseguido", Fuerza_Visitante, "Goles")


Fuerza_local = Local[1] * Fuerza_local
Fuerza_Visitante = Visitante[1] * Fuerza_Visitante

# Resultado Final
if Fuerza_local > Fuerza_Visitante:
    print ("El equipo", Local[0], "ha ganado el partido")
elif Fuerza_local < Fuerza_Visitante:
   print ("El equipo", Visitante[0], "ha ganado el partido")
else:
    print ("Hemos tenido un empate")