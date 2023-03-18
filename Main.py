import pygame
import QuickModifyVariables
import Map
import Sprite
import AI


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((QuickModifyVariables.screenSizeX,
                                      QuickModifyVariables.screenSizeY))
    
    map = Map.Map(xSizeInPixels=QuickModifyVariables.screenSizeX,
                  ySizeInPixels=QuickModifyVariables.screenSizeY)
    
    Character = Sprite.Sprite(xStartInPixels=QuickModifyVariables.playerSpawnX,
                              yStartInPixels=QuickModifyVariables.playerSpawnY,
                              shape=QuickModifyVariables.playerShape,
                              width=QuickModifyVariables.playerWidth,
                              height=QuickModifyVariables.playerHeight,
                              latchMove=QuickModifyVariables.playerLatchMove,
                              availableDirections=QuickModifyVariables.playerAvailableDirections,
                              speed=QuickModifyVariables.playerSpeed,
                              lives=QuickModifyVariables.playerStartingLives,
                              primaryColor=QuickModifyVariables.playerPrimaryColor,
                              secondaryColor=QuickModifyVariables.playerSecondaryColor)
    
    AI1 = AI.AI(xStartInPixels=0,
                yStartInPixels=0,
                shape='r',
                width=15,
                height=5,
                radius=0,
                availableDirections=4,
                latchMove=False,
                speed=2,
                lives=1,
                primaryColor=(255,255,255,0),
                secondaryColor=(255,255,255,0))


    
    '''
    Compatible with Sprite class
       Direction options:
           'right', 'right-up', 'right-down', 'left', 'left-up', 'left-down', 'up', 'down'
       lives options:
           'L0' - do nothing
           'L+1' - add life
           'L-1' - remove life
    '''
    characterUpdateOptions = {
        'direction':'n',
        'lives':'L0'
    }



    #Bool initialization
    if True:
        run = True
        left = False
        right = False
        up = False
        down = False
        reset = False
    
    #Main game loop
    while run:
        #Refresh rate:
        clock.tick(60)

        '''
        Draw map and characters
        '''
        #Refresh screen to black
        pygame.draw.rect(screen,(0,0,0,0),(0,0,QuickModifyVariables.screenSizeX,QuickModifyVariables.screenSizeY))
        #Draw map
        for i in range(len(map.map)):
            for j in range(len(map.map[0])):
                if map.map[i][j] != (0,0,0,0):
                    screen.set_at((j,i),map.map[i][j])
        #Draw character based on character's orientation
        if Character.orientation == 'u' or Character.orientation == 'd':
            pygame.draw.rect(screen, Character.primaryColor,(int(Character.x-(Character.width/2)),int(Character.y-(Character.height/2)),Character.width,Character.height))
        elif Character.orientation == 'r' or Character.orientation == 'l':
            pygame.draw.rect(screen, Character.primaryColor,(int(Character.x-(Character.height/2)),int(Character.y-(Character.width/2)),Character.height,Character.width))
        
        screen.set_at((AI1.x,AI1.y),AI1.primaryColor)
        '''
        End draw map and characters
        '''





        #Event management (pygame key functions)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_LEFT:
                    left = True
                    if Character.availableDirections == 4:
                        right = False
                        up = False
                        down = False
                if event.key == pygame.K_RIGHT:
                    right = True
                    if Character.availableDirections == 4:
                        left = False
                        up = False
                        down = False
                if event.key == pygame.K_UP:
                    up = True
                    if Character.availableDirections == 4:
                        left = False
                        right = False
                        down = False
                if event.key == pygame.K_DOWN:
                    down = True
                    if Character.availableDirections == 4:
                        up = False
                        right = False
                        left = False
                if event.key == pygame.K_RETURN:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_DOWN:
                    down = False

            if event.type == pygame.QUIT:
                run = False





        '''
        Player-controller character functions
        '''
        #Forces continual input for characters with non-latching input
        if not Character.latchMove:
            characterUpdateOptions['direction'] = 'n'
        #Update character direction
        if True:
            if right and up:
                characterUpdateOptions['direction'] = 'right-up'
            elif right and down:
                characterUpdateOptions['direction'] = 'right-down'
            elif left and up:
                characterUpdateOptions['direction'] = 'left-up'
            elif left and down:
                characterUpdateOptions['direction'] = 'left-down'
            elif right and Character.currentDirection != 'left':
                characterUpdateOptions['direction'] = 'right'
            elif left and Character.currentDirection != 'right':
                characterUpdateOptions['direction'] = 'left'
            elif up and Character.currentDirection != 'down':
                characterUpdateOptions['direction'] = 'up'
            elif down and Character.currentDirection != 'up':
                characterUpdateOptions['direction'] = 'down'
        #Movement and collision detection
        for i in range(Character.speed):
            Character.update(characterUpdateOptions)
            characterUpdateOptions['lives'] = 'L0'
            
            #Collision Detection - 
            #   First conditional checks if map object contains other data at character's current position
            #   Second conditional checks if character is currently moving (to prevent character from "colliding" with itself)
            if map.get_pixel_value(int(Character.y),int(Character.x)) != (0,0,0,0) and Character.currentDirection != 'n':
                reset = True
                characterUpdateOptions['direction'] = 'n'
                
            #Make trail behind character
            else:
                map.set_pixel_value(int(Character.y), int(Character.x), Character.secondaryColor)
        '''
        End player-controller character functions
        '''


        '''
        AI functions
        '''
        for i in range(AI1.speed):
            AI1updateOptions = {
                'direction':'n'
            }
            AI1updateOptions['direction'] = AI1.determine_direction(map.map,Character.x,Character.y)
            AI1.update(AI1updateOptions)



        '''
        End AI functions
        '''



        #Reset after death etc.
        if reset:
            Character.reset()
            map.reset()
            reset = False
            characterUpdateOptions['lives'] = 'L-1'
            left = False
            right = False
            up = False
            down = False   
            if Character.lives <= 0:
                run = False     







        pygame.display.update()


    pygame.display.quit()






if __name__ == "__main__":
    main()