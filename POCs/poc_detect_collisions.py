import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("POC - Colisiones en Pygame")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Definir rectángulos (jugador y obstáculo)
player_rect = pygame.Rect(50, 50, 50, 50)  # (x, y, width, height)
obstacle_rect = pygame.Rect(200, 200, 100, 100)  # (x, y, width, height)

# Velocidad de movimiento del jugador
player_speed = 5

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener el estado de las teclas
    keys = pygame.key.get_pressed()

    # Actualizar la posición del jugador
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Verificar si hay colisión entre el jugador y el obstáculo
    collision = player_rect.colliderect(obstacle_rect)

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Dibujar el jugador y el obstáculo
    pygame.draw.rect(screen, RED, player_rect)
    pygame.draw.rect(screen, RED, obstacle_rect)

    # Si hay colisión, dibujar un mensaje
    if collision:
        font = pygame.font.Font(None, 36)
        text = font.render("¡Colisión!", True, (255, 0, 0))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la velocidad de fotogramas
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()
