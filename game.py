import pygame
from snake import Snake 

pygame.init()

#Create a screen 
width = 800
height = 600


# Create A Snake 
length = 10
color = (255,255,255)
snake =Snake(length, color)
snake_speed = snake.get_snake_speed()        
x_speed = snake_speed
y_speed = 0


screen =pygame.display.set_mode([width,height])
clock = pygame.time.Clock()

#done 
done = False

while not done:
    #events : tracks keyboard ,and mouse clicks 
    
    for event in pygame.event.get():
        #keys events
        if  event.type == pygame.QUIT:
            done = True

    #snake : up,down,left,right

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("LEFT")
                x_speed = snake_speed *-1
                y_speed = 0
            
            if event.key == pygame.K_RIGHT:
                print("RIGHT")
                x_speed = snake_speed
                y_speed = 0 

            if event.key == pygame.K_UP:
                print("UP")
                x_speed = 0
                y_speed = snake_speed *-1

            if event.key == pygame.K_DOWN:
                print("DOWN")
                x_speed =0
                y_speed= snake_speed

        snake.change_direction(x_speed, y_speed)

        #Draw 
        screen.fill((0,0,0)) 
        snake.get_snake().draw(screen)
        pygame.display.flip()


        clock.tick(15)   
