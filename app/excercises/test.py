import numpy as np
import matplotlib.pyplot as plt
import pybullet as p

# Parámetros del sistema de frenos
masa_vehiculo = 1000  # kg
velocidad_inicial = 20  # m/s
coef_friccion = 0.3  # coeficiente de fricción
radio_disco = 0.3  # m
fuerza_frenado = 5000  # N

# Configuración de PyBullet
physicsClient = p.connect(p.DIRECT)  # conexión sin GUI
p.setGravity(0, 0, -9.81)  # gravedad
planeId = p.loadURDF("plane.urdf")
carId = p.loadURDF("racecar/racecar.urdf")

# Simulación del frenado
tiempo = []
velocidad = []
posicion = []
t = 0
dt = 0.01  # intervalo de tiempo
v = velocidad_inicial
x = 0

while v > 0:
    aceleracion = -(fuerza_frenado / masa_vehiculo)
    v += aceleracion * dt
    x += v * dt
    t += dt
    tiempo.append(t)
    velocidad.append(v)
    posicion.append(x)

# Desconectar PyBullet
p.disconnect()

# Visualización de resultados
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(tiempo, velocidad)
plt.title('Simulación de Frenado')
plt.ylabel('Velocidad (m/s)')

plt.subplot(2, 1, 2)
plt.plot(tiempo, posicion)
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')

plt.show()
