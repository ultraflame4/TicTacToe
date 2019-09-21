import pygame
from gameEngine import colors
class hud:
    def __init__(self):
        self.screen = pygame.display.set_mode((700, 700))
        self.MenuRECT = pygame.rect.Rect(600, 0, 100, 700)

    def update(self):
        self.draw()

    def draw(self):
        self.main()
        pygame.display.update()
        pass

    def main(self):
        self.screen.fill(colors.grey)
        self.menu()
        self.ticTacToeLines()

    def ticTacToeLines(self):
        #1st Vertical Line
        pygame.draw.line(self.screen, colors.black, (175, 50), (175, 600), 5)
        #2nd verticle Line
        pygame.draw.line(self.screen, colors.black, (375, 50), (375, 600), 5)
        #1st Horizontal Line
        pygame.draw.line(self.screen, colors.black, (25, 200), (525, 200), 5)
        #2nd Horizontal Line
        pygame.draw.line(self.screen, colors.black, (25, 400), (525, 400), 5)
        pass

    def menu(self):
        pygame.draw.rect(self.screen, colors.azure4, self.MenuRECT)
