import pygame


from compiled import SudokuGenerator

pygame.font.init()

width, height = 630, 630
win = pygame.display.set_mode((width, height))
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
fps = 90
font = pygame.font.Font('freesansbold.ttf', 32)
pygame.display.set_caption("Sudoku")


def draw(board):
    win.fill(white)
    pos = 0
    pygame.draw.line(win, black, [0, pos], [width, pos], 2)
    for i in range(1, 9):
        pos += width // 9
        thick = 2
        if i % 3 == 0:
            thick = 4
        pygame.draw.line(win, black, [0, pos], [width, pos], thick)
        pygame.draw.line(win, black, [pos, 0], [pos, height], thick)
    for i in range(9):
        for j in range(9):
            if board[i][j]:
                text = font.render(str(board[i][j]), 1, black)
                win.blit(text, (i * 70 + 26, j * 70 + 24))
    pygame.display.update()


def main(board):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board = obj.solved_board()
        draw(board)
    pygame.quit()


if __name__ == "__main__":
    obj = SudokuGenerator()
    obj.solve()
    grid = obj.obscure()
    main(grid)