import pygame
pygame.init()

WIDTH = 500
HEIGHT = 600
BLACK = 0,0,0
BLUE = 82, 153, 211
RED = 240, 58, 71

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("white")
pygame.display.set_caption("Matching Chess Pieces")
pygame.display.update()


bishop = pygame.image.load("./images/Chess_bdt60.png")
king = pygame.image.load("./images/Chess_kdt60.png")
knight = pygame.image.load("./images/Chess_ndt60.png")
pawn = pygame.image.load("./images/Chess_pdt60.png")
queen = pygame.image.load("./images/Chess_qdt60.png")
rook = pygame.image.load("./images/Chess_rdt60.png")

screen.blit(bishop, (50,30))
screen.blit(king, (50,130))
screen.blit(knight, (50,230))
screen.blit(pawn, (50,330))
screen.blit(queen, (50,430))
screen.blit(rook, (50,530))

font = pygame.font.SysFont("helvicta", 45)

text1 = font.render("Knight", False, BLACK)
text2 = font.render("Rook", False, BLACK)
text3 = font.render("Queen", True, BLACK)
text4 = font.render("Bishop", True, BLACK)
text5 = font.render("Pawn", False, BLACK)
text6 = font.render("King", False, BLACK)

screen.blit(text1, (250, 50))
screen.blit(text2, (250, 150))
screen.blit(text3, (250, 250))
screen.blit(text4, (250, 350))
screen.blit(text5, (250, 450))
screen.blit(text6, (250, 550))
pygame.display.update()

while 1:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, BLUE, (pos), 10, 0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, BLACK, (pos), (pos2), 2)
        pygame.draw.circle(screen, RED, (pos2), 10, 0)
        pygame.display.update()