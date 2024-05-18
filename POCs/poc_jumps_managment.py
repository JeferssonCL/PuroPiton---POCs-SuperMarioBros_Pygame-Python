import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("POC - Salto y Movimiento en Pygame")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Definir clase para el jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.vel_x = 0
        self.vel_y = 0
        self.jump_power = -15  # Ajustar la potencia del salto aquí
        self.on_ground = False

    def update(self):
        # Aplicar gravedad
        self.vel_y += 0.5
        self.rect.y += self.vel_y

        # Verificar colisión con el suelo
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
            self.on_ground = True
            self.vel_y = 0

        # Moverse horizontalmente
        self.rect.x += self.vel_x

    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

# Crear el jugador
player = Player()

# Grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.jump()
            elif event.key == pygame.K_LEFT:
                player.vel_x = -5
            elif event.key == pygame.K_RIGHT:
                player.vel_x = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.vel_x < 0:
                player.vel_x = 0
            elif event.key == pygame.K_RIGHT and player.vel_x > 0:
                player.vel_x = 0

    # Actualizar
    all_sprites.update()

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Dibujar los sprites
    all_sprites.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la velocidad de fotogramas
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()
