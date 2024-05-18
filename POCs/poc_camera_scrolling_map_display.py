import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar pantalla
viewport_width = 800
viewport_height = 240
screen = pygame.display.set_mode((viewport_width, viewport_height))
pygame.display.set_caption("POC - Camera scrolling (simulation) and map display ")

# Cargar la imagen del mapa
map_image = pygame.image.load('Assets/Map1.png')

# Obtener el tamaño de la imagen del mapa
map_width, map_height = map_image.get_size()

# Variables para controlar el desplazamiento
x_offset = 0
y_offset = 0

# Velocidad de desplazamiento
scroll_speed = 5

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener el estado de las teclas
    keys = pygame.key.get_pressed()

    # Desplazamiento
    if keys[pygame.K_LEFT]:
        x_offset += scroll_speed
    if keys[pygame.K_RIGHT]:
        x_offset -= scroll_speed
    if keys[pygame.K_UP]:
        y_offset += scroll_speed
    if keys[pygame.K_DOWN]:
        y_offset -= scroll_speed

    # Limitar el desplazamiento para no salir del mapa
    x_offset = max(min(x_offset, 0), viewport_width - map_width)
    y_offset = max(min(y_offset, 0), viewport_height - map_height)

    # Dibujar la parte visible del mapa
    screen.fill((0, 0, 0))  # Llenar el fondo de negro para evitar arrastre de imágenes anteriores
    screen.blit(map_image, (x_offset, y_offset))

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la velocidad de fotogramas
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()
