import pygame
import random
import time

pygame.init()


ppurple = (128, 0, 128)
Silver = (192, 192, 192)
yyelow = (231, 235, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BlUE = (0, 0, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255)


main_window = pygame.display.set_mode((500, 500))
main_window.fill(Silver)



class Area():
    def __init__(self, x, y, w, h, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

    def fill(self):
        pygame.draw.rect(main_window, self.color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(main_window, frame_color, self.rect, thickness)



Card1 = Area(100, 140, 60, 90, yyelow)
Card2 = Area(180, 140, 60, 90, yyelow)
Card3 = Area(260, 140, 60, 90, yyelow)
Card4 = Area(340, 140, 60, 90, yyelow)


class Label(Area):
    def set_text(self, text, size, color_text):
        self.image = pygame.font.Font(None, size).render(text, True, color_text)

    def draw(self, x=0, y=0):
        self.fill()
        main_window.blit(self.image, (self.rect.x + x, self.rect.y + y))


cards = []
x = 100
for i in range(4):
    label1 = Label(x, 140, 60, 90, yyelow)
    label1.set_text("Click", 35, (0, 0, 0))
    label1.outline(RED, 10)
    cards.append(label1)
    x += 80

wait = 0
p = 0
FPS = 20


point = Label(350, 20, 120, 35, Silver)
point.set_text('Рахунок: 0', 35, (0, 0, 0))

timer_label = Label(20, 20, 120, 35, Silver)
timer_label.set_text('Час: 10', 35, (0, 0, 0))
start_time = time.time()
total_time = 10


Game = True
while Game:
    elapsed_time = time.time() - start_time
    remaining_time = total_time - int(elapsed_time)
    if remaining_time < 0:
        remaining_time = 0
        Game = False
        if p > 3:
            game_done = Label(0, 0, 500, 500, DARK_BLUE)
            game_done.set_text('Win!!!!', 100, GREEN)
            game_done.draw(75, 200)
        else:
            game_over = Label(0, 0, 500, 500, DARK_BLUE)
            game_over.set_text('Game Over', 100, RED)
            game_over.draw(75, 200)
    timer_label.set_text(f'Час: {remaining_time}', 35, (0, 0, 0))

    point.draw()
    timer_label.draw()

    if wait == 0:
        wait = 15
        click = random.randint(0, 3)
        for j in range(4):
            cards[j].color = YELLOW
            if j == click:
                cards[j].draw(5, 25)
            else:
                cards[j].fill()
    else:
        wait -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                for j in range(4):
                    if cards[j].rect.collidepoint(x, y):
                        if j == click:
                            cards[j].color = GREEN
                            p += 1
                            point.set_text(f'Рахунок: {p}', 35, (0, 0, 0))
                        else:
                            cards[j].color = RED
                            p -= 1
                            point.set_text(f'Рахунок: {p}', 35, (0, 0, 0))
                        cards[j].fill()

    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(FPS)

pygame.quit()
