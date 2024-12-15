import pygame
import sys
import random

# Pygame başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Renkler
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)

# FPS ayarı
clock = pygame.time.Clock()
FPS = 60

# Kuş özellikleri
bird_x, bird_y = 100, 300
bird_width, bird_height = 30, 30
bird_velocity = 0
gravity = 0.5
flap_strength = -10

# Boru özellikleri
pipe_width = 50
pipe_gap = 150
pipe_velocity = 4
pipe_timer = 0
pipes = []

# Puan
score = 0
font = pygame.font.Font(None, 50)

# Oyun durumu
game_active = True


# Kuşu çizen fonksiyon
def draw_bird(x, y):
    pygame.draw.rect(screen, (255, 255, 0), (x, y, bird_width, bird_height))


# Boruları çizen fonksiyon
def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)


# Ana oyun döngüsü
while True:
    screen.fill(BLUE)  # Arka plan rengi

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird_velocity = flap_strength  # Kuş zıplar
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Restart
                bird_x, bird_y = 100, 300
                bird_velocity = 0
                pipes = []
                score = 0
                game_active = True

    if game_active:
        # Kuş hareketi
        bird_velocity += gravity
        bird_y += bird_velocity

        # Yeni boru oluşturma
        pipe_timer += 1
        if pipe_timer >= 90:
            pipe_timer = 0
            pipe_height = random.randint(100, HEIGHT - pipe_gap - 100)
            pipes.append(pygame.Rect(WIDTH, 0, pipe_width, pipe_height))  # Üst boru
            pipes.append(pygame.Rect(WIDTH, pipe_height + pipe_gap, pipe_width, HEIGHT))  # Alt boru

        # Boru hareketi
        for pipe in pipes:
            pipe.x -= pipe_velocity

        # Boruları temizleme
        pipes = [pipe for pipe in pipes if pipe.x + pipe_width > 0]

        # Çarpışma kontrolü
        for pipe in pipes:
            if pygame.Rect(bird_x, bird_y, bird_width, bird_height).colliderect(pipe):
                game_active = False

        # Yere veya tavana çarpma kontrolü
        if bird_y < 0 or bird_y + bird_height > HEIGHT:
            game_active = False

        # Puan artırma
        for pipe in pipes:
            if pipe.x + pipe_width == bird_x:
                score += 0.5  # Her boru çifti için 1 puan

        # Kuşu ve boruları çiz
        draw_bird(bird_x, bird_y)
        draw_pipes(pipes)

        # Skoru ekrana yazdır
        score_text = font.render(str(int(score)), True, WHITE)
        screen.blit(score_text, (WIDTH // 2, 20))

    else:
        game_over_text = font.render("GAME OVER", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
        restart_text = font.render("Press SPACE", True, WHITE)
        screen.blit(restart_text, (WIDTH // 2 - 150, HEIGHT // 2 + 50))

    pygame.display.flip()
    clock.tick(FPS)