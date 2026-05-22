import pygame
import sys
import random 
import cowsay

direction="RIGHT"
new_direction=direction

def main():
    global direction
    
    snake_head_pos=[100, 50]
    snake_body=[[100, 50], [90, 50], [80, 50]]
    speed=12

    #creating screen 
    pygame.init()
    screen = pygame.display.set_mode((700, 500), pygame.SCALED | pygame.RESIZABLE)
    pygame.display.set_caption("Snake Game")
    clock= pygame.time.Clock()

    food_position=[random.randrange(1, 70)*10, random.randrange(1, 50)*10] 
    food_spawn=True  # for checking if there is already food or not
    score_list=[]
    score=0
  

    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        screen.fill("black")
        #showing score on screen
        score_font = pygame.font.SysFont("Arial", 25)
        score_surface = score_font.render(f"Score: {score}", True, "white")
        score_rect = score_surface.get_rect()
        screen.blit(score_surface, score_rect)

        # draw food and snake
        pygame.draw.rect(screen,"red", (*food_position, 10, 10))
        pygame.draw.rect(screen,"green", (*snake_head_pos, 10, 10))

        # get key direction
        keys = pygame.key.get_pressed()
        new_direction = keydirection(keys)

        # stop snake to go opposite direction
        if new_direction=="UP" and direction!="DOWN":
            direction=new_direction
        if new_direction=="DOWN" and direction!="UP":
            direction=new_direction
        if new_direction=="LEFT" and direction!="RIGHT":
            direction=new_direction   
        if new_direction=="RIGHT" and direction!="LEFT":
            direction=new_direction

        # moving
        if direction=="UP":
            snake_head_pos[1]-=10     
        if direction=="DOWN":
            snake_head_pos[1]+=10
        if direction=="LEFT":
            snake_head_pos[0]-=10
        if direction=="RIGHT":
            snake_head_pos[0]+=10

        # eating food
        if snake_head_pos== food_position:
            food_spawn= False  
            score +=10
            speed=speed_update(score,speed)
        else:
            snake_body.pop()   # if food is eaten no need to remove tail which simulate snake moving
        snake_body.insert(0,list(snake_head_pos))   # adding new head to first index of body

        #spawn food
        if not food_spawn:
            food_position=[random.randrange(1, 70)*10, random.randrange(1, 50)*10]
            food_spawn=True

        # draw snake
        for block in snake_body:
            pygame.draw.rect(screen, "green", pygame.Rect(*block, 10, 10))
        
        #is game over or not 
        running = is_game_running(snake_head_pos, snake_body)
        
        pygame.display.flip()
        clock.tick(speed) 
    #writing all scores in txt file and printing the max
    with open("scores.txt", "a") as file:
        file.write(f"{score}\n")
    with open("scores.txt", "r") as file:
        lines= file.readlines()
        for score in lines:
            print(score_list.append(score))
    print(cowsay.char_names)
    cowsay.cow(f"Your maximum score is: {max(score_list)}")

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


def speed_update(score,speed):
        
        if score==50:
            return speed+2
        elif score==100:
            return speed+4
        elif score==170:
            return speed+4
        elif score==230:
            return speed+2
        return speed

def is_game_running(snake_head_pos, snake_body):

    #if collide with screen's border
    if snake_head_pos[0]<10 or snake_head_pos[0]>690 or snake_head_pos[1]<10 or snake_head_pos[1]>490:
        return False 
    
    # if head touch body
    for block in snake_body[1:]:
        if snake_head_pos==block:
            return False
    return True


if __name__ == "__main__":
    main()
