import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("POC - Lanzamiento de Proyectiles en Pygame")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Definir clase para el jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (100, screen_height // 2)
        self.vel_y = 0
        self.jump_power = -12
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

    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Definir clase para los proyectiles
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))  # Cambiar dimensiones para proyectiles verticales
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -10  # Cambiar la velocidad hacia arriba

    def update(self):
        self.rect.y += self.speed  # Mover el proyectil hacia arriba
        if self.rect.bottom <= 0:
            self.kill()  # Eliminar proyectil cuando sale de la pantalla

# Definir clase para el enemigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (700, screen_height // 2)
        self.vel_x = -3

    def update(self):
        self.rect.x += self.vel_x
        if self.rect.right <= 0:
            self.rect.left = screen_width

# Grupo de sprites
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Crear el jugador
player = Player()
all_sprites.add(player)

# Crear el enemigo
enemy = Enemy()
all_sprites.add(enemy)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.jump()
            elif event.key == pygame.K_a:
                player.shoot()

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
