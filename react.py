import pygame
import random
import time

pygame.init()


WIDTH, HEIGHT = 800, 600
OBJECT_SIZE = 50
OBJECT_COLOR = (0, 255, 0)  
BACKGROUND_COLOR = (255,255, 255)  
TEXT_COLOR = (0, 0, 0) 
TIME_LIMIT = 15


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("reaction time game")

def draw_objects(objects, score):
    screen.fill(BACKGROUND_COLOR)
    for obj in objects:
        pygame.draw.rect(screen, OBJECT_COLOR, obj)
    
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()

  
    objects = []
    score = 0
    game_start_time = time.time()
    game_end_time = game_start_time + TIME_LIMIT

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for obj in objects[:]:
                    if obj.collidepoint(mouse_x, mouse_y):
                        score += 1
                        objects.remove(obj)

      
        if random.random() < 0.05:
            new_object = pygame.Rect(random.randint(0, WIDTH - OBJECT_SIZE), random.randint(0, HEIGHT - OBJECT_SIZE), OBJECT_SIZE, OBJECT_SIZE)
            objects.append(new_object)

        
        current_time = time.time()
        if current_time > game_end_time:
            print(f"game over! your final score is: {score} and your average reaction time is- {(score/TIME_LIMIT)*1000} ms")
            running = False

        draw_objects(objects, score)

        clock.tick(30)  

    pygame.quit()

if __name__ == "__main__":
    main()
