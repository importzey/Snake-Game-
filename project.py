import pygame
import sys
import random 

speed = 13
snake_position=[100, 50]
snake_body=[[100, 50], [90, 50], [80, 50]]
running = True
direction='RIGHT'
new_direction=direction
def main():
    global running
    global snake_position
    global snake_body
    global speed
    global direction
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.SCALED | pygame.RESIZABLE)
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()


    food_position=[random.randrange(1, 80)*10, random.randrange(1, 60)*10]
    food_spawn=True 
    score = 0
  



    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        
        score_font = pygame.font.SysFont("Arial", 24)
        score_surface = score_font.render(f'Score: {score}', True, "white")
        score_rect = score_surface.get_rect()
        screen.blit(score_surface, score_rect)

        pygame.draw.rect(screen, "red", (*food_position, 10, 10))
        pygame.draw.rect(screen, "green", (*snake_position, 10, 10))
        keys = pygame.key.get_pressed()
        new_direction = keydirection(keys)

        # stop snake to go opposite direction
        if new_direction == 'UP' and direction != 'DOWN':
            direction = new_direction
        if new_direction == 'DOWN' and direction != 'UP':
            direction = new_direction
        if new_direction == 'LEFT' and direction != 'RIGHT':
            direction = new_direction   
        if new_direction == 'RIGHT' and direction != 'LEFT':
            direction = new_direction
        # moving
        if direction == 'UP':
            snake_position[1] -= 10     
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # eating food
        if snake_position == food_position:
            food_spawn = False  
            score +=10
            speed = speed_update(score)
        else:
            snake_body.pop()
        snake_body.insert(0,list(snake_position))

        if not food_spawn:
            food_position = [random.randrange(1, 80)*10, random.randrange(1, 60)*10]
            food_spawn = True
        
        for pos in snake_body:
            pygame.draw.rect(screen, "green", pygame.Rect(*pos, 10, 10))
        

        running = is_game_running(running)
        pygame.display.flip()
        clock.tick(speed) 

    pygame.quit()
    sys.exit()


def keydirection(keys):
    global direction
    if keys[pygame.K_w]:
        return 'UP'
    if keys[pygame.K_s]:
        return 'DOWN'
    if keys[pygame.K_a]:
        return 'LEFT'
    if keys[pygame.K_d]:
        return 'RIGHT'
    return direction


def speed_update(score):
        global speed
        if score == 80:
            return speed + 2
        elif score == 150:
            return speed + 4
        elif score == 200:
            return speed + 6
        elif score == 250:
            return speed + 8
        return speed


def is_game_running(running):
    global snake_position
    global snake_body
    if snake_position[0] < 0 or snake_position[0] > 790 or snake_position[1] < 0 or snake_position[1] > 590:
        return False 
    
    for block in snake_body[1:]:
        if snake_position == block:
            return False
    return True


if __name__ == "__main__":
    main()
