import pygame
import random

pygame.init()


WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SPEED = 5
BULLET_SPEED = 10
ENEMY_SPEED = 2
ENEMY_HORIZONTAL_SPEED = 3


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


ROBOT_IMG = pygame.image.load("robot.png")
BIRD_IMG = pygame.image.load("bird.png")
BULLET_IMG = pygame.Surface((5, 10))
BULLET_IMG.fill((255, 0, 0))  # Rosso

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ROBOT_IMG, (50, 50))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = BULLET_IMG
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(BIRD_IMG, (50, 50))
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), 0))
        self.direction = random.choice([-1, 1])

    def update(self):
        self.rect.y += ENEMY_SPEED
        self.rect.x += self.direction * ENEMY_HORIZONTAL_SPEED
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.direction *= -1
        if self.rect.top > HEIGHT:
            self.kill()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Robot vs Uccelli")
    clock = pygame.time.Clock()

    player = Player()
    player_group = pygame.sprite.GroupSingle(player)
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    bullets.add(bullet)

        player_group.update()
        bullets.update()
        enemies.update()

        if random.randint(1, 30) == 1:
            enemy = Enemy()
            enemies.add(enemy)

        for bullet in bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, enemies, True)
            if hit_enemies:
                bullet.kill()
                score += len(hit_enemies)

        screen.fill(BLACK)
        player_group.draw(screen)
        bullets.draw(screen)
        enemies.draw(screen)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Punteggio: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
