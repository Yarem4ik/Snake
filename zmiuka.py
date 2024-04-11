import pygame
import random

pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Змійка")
green = (0, 255, 0)
red = (255, 0, 0)
font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

# основні параметри
cell_size = 20
snake_speed = 5
snake_length = 3
snake_body = []

for i in range(snake_length):
    snake_body.append(pygame.Rect((screen_width / 2) - (cell_size * i), screen_height / 2, cell_size, cell_size))
snake_direction = "right"
new_direction = "right"
apple_position = pygame.Rect(random.randint(0, screen_width - cell_size), random.randint(0, screen_height - cell_size), cell_size, cell_size)


while True:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "down":
                new_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                new_direction = "down"
            elif event.key == pygame.K_LEFT and snake_direction != "right":
                new_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                new_direction = "right"

    # новий напрямок руху
    snake_direction = new_direction
    # управління змійкою
    if snake_direction == "up":
        snake_body.insert(0, pygame.Rect(snake_body[0].left, snake_body[0].top - cell_size, cell_size, cell_size))
    elif snake_direction == "down":
        snake_body.insert(0, pygame.Rect(snake_body[0].left, snake_body[0].top + cell_size, cell_size, cell_size))
    elif snake_direction == "left":
        snake_body.insert(0, pygame.Rect(snake_body[0].left - cell_size, snake_body[0].top, cell_size, cell_size))
    elif snake_direction == "right":
        snake_body.insert(0, pygame.Rect(snake_body[0].left + cell_size, snake_body[0].top, cell_size, cell_size))

    # перевіряємо, чи з'їла змія яблуко
    if snake_body[0].colliderect(apple_position):
        apple_position = pygame.Rect(random.randint(0, screen_width - cell_size), random.randint(0, screen_height-cell_size), cell_size, cell_size)
        snake_length += 1

    if len(snake_body) > snake_length:
        snake_body.pop()

    # перевірка зіткнення зі стінами
    if snake_body[0].left < 0 or snake_body[0].right > screen_width or snake_body[0].top < 0 or snake_body[0].bottom > screen_height:
        score_text = font.render("LOZER", True, (255, 255, 255))
        screen.blit(score_text, (300, 300))
      

    # перевірка зіткнення із власним тілом
    for i in range(1, len(snake_body)):
        if snake_body[0].colliderect(snake_body[i]):

            score_text = font.render("LOZER", True, (255, 255, 255))
            screen.blit(score_text, (300, 300))
          

    screen.fill((0, 0, 0))
    # малюєм змійку
    for i in range(len(snake_body)):
        if i == 0:
            pygame.draw.circle(screen, green, snake_body[i].center, cell_size / 2)
        else:
            pygame.draw.circle(screen, green, snake_body[i].center, cell_size / 2)
            pygame.draw.circle(screen, (0, 200, 0), snake_body[i].center, cell_size / 4)

    # малюєм яблуко
    pygame.draw.circle(screen, red, apple_position.center, cell_size / 2)

    # виводими калькість яблук
    score_text = font.render(f"З'їдено яблук: {snake_length - 3}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    clock.tick(snake_speed)

pygame.quit()