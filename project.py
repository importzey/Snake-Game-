import pygame
import sys
import random 

speed = 13

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.SCALED | pygame.RESIZABLE)
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    running = True
    snake_position=[100, 50]
    snake_body=[[100, 50], [90, 50], [80, 50]]
    food_position=[random.randrange(1, 80)*10, random.randrange(1, 60)*10]
    food_spawn=True 
    score = 0
  
    direction='RIGHT'
    new_direction=direction


    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        pygame.draw.rect(screen, "red", (*food_position, 10, 10))
        pygame.draw.rect(screen, "green", (*snake_position, 10, 10))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            new_direction = 'UP'
        if keys[pygame.K_s]:
            new_direction = 'DOWN'
        if keys[pygame.K_a]:
            new_direction = 'LEFT'
        if keys[pygame.K_d]:
            new_direction = 'RIGHT'
        
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
            level(score)
        else:
            snake_body.pop()
        snake_body.insert(0, list(snake_position))

        if not food_spawn:
            food_position = [random.randrange(1, 80)*10, random.randrange(1, 60)*10]
            food_spawn = True
        
        for pos in snake_body:
            pygame.draw.rect(screen, "green", pygame.Rect(*pos, 10, 10))
        
        if snake_position[0] < 0 or snake_position[0] > 790 or snake_position[1] < 0 or snake_position[1] > 590:
            running = False 
        
        for block in snake_body[1:]:
            if snake_position == block:
                running = False
 
        
        pygame.display.flip()
        clock.tick(speed) 

    pygame.quit()
    sys.exit()


def new_collision():
    ...


def level(score):
        global speed
        if score == 100:
            speed += 2
        elif score == 150:
            speed += 3
        elif score == 200:
            speed += 6


def function_n():
    ...


if __name__ == "__main__":
    main()
