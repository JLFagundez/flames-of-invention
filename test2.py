# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 22:37:29 2023

@author: jeanl
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configurações do espaço delimitado
xlim = (-10, 10)
ylim = (-10, 10)

# Classe para representar uma partícula
class Particle:
    def __init__(self):
        self.position = np.array([np.random.uniform(*xlim), np.random.uniform(*ylim)])
        self.velocity = np.random.uniform(-1, 1, size=2)

    def update(self):
        # Atualizar posição com base na velocidade
        self.position += self.velocity

        # Colisões elásticas com as paredes
        if self.position[0] <= xlim[0] or self.position[0] >= xlim[1]:
            self.velocity[0] *= -1
        if self.position[1] <= ylim[0] or self.position[1] >= ylim[1]:
            self.velocity[1] *= -1

# Criação de partículas
num_particles = 50
particles = [Particle() for _ in range(num_particles)]

# Configurações do gráfico
fig, ax = plt.subplots()
ax.set_xlim(xlim)
ax.set_ylim(ylim)
scat = ax.scatter([], [], s=50)

# Função de inicialização da animação
def init():
    scat.set_offsets([])
    return scat,

# Função para atualização do gráfico em cada frame da animação
def update(frame):
    for particle in particles:
        particle.update()

    # Atualizar posições das partículas
    positions = np.array([particle.position for particle in particles])
    scat.set_offsets(positions)
    return scat,

# Criação da animação
ani = FuncAnimation(fig, update, frames=100, interval=50, init_func=init, blit=True)

# Mostrar a animação
plt.show()
