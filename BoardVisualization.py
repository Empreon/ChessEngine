import pygame as pg
import chess

from AlgorithmSetup import moveSelect

pg.init()

screen = pg.display.set_mode((1024, 640))
pg.display.set_caption('Python Chess Bot')
clock = pg.time.Clock()
########################################################################################################################

def arrangeBoard(image_dir):
    if image_dir[-1] != '/':
        image_dir += '/'
    d = {'p': image_dir + 'BlackPawn.png',
         'r': image_dir + 'BlackRook.png',
         'n': image_dir + 'BlackKnight.png',
         'b': image_dir + 'BlackBishop.png',
         'q': image_dir + 'BlackQueen.png',
         'k': image_dir + 'BlackKing.png',
         'P': image_dir + 'WhitePawn.png',
         'R': image_dir + 'WhiteRook.png',
         'N': image_dir + 'WhiteKnight.png',
         'B': image_dir + 'WhiteBishop.png',
         'Q': image_dir + 'WhiteQueen.png',
         'K': image_dir + 'WhiteKing.png',
         }
    return d

def reDesignBoard(board):
    b = str(board.fen).split()[4].replace('/', '')[7:]

    for num in range(1, 10):
        b = b.replace(str(num), '.' * num)

    image_dir = "../chess-pieces/"
    image_dict = arrangeBoard(image_dir)

    d = []
    for x in zip(range(64), list(b)):
        if x[1] != '.':
            image = image_dict[x[1]]
            d.append(image)
        else:
            image = "../chess-pieces/" + 'transparency.png'
            d.append(image)
    return d

def showBoard(board):
    boardlist = reDesignBoard(board)
    bg = pg.image.load("../chess-pieces/chessBoard.png")
    screen.blit(bg, (50, 50))
    for i in range(64):
        if i <= 7:
            image = pg.image.load(boardlist[7 - i])
            screen.blit(image, (43 + 70*i, 533))
        if 7 < i <= 15:
            image = pg.image.load(boardlist[23 - i])
            screen.blit(image, (43 + 70*(i - 8), 463))
        if 15 < i <= 23:
            image = pg.image.load(boardlist[39 - i])
            screen.blit(image, (43 + 70*(i - 16), 393))
        if 23 < i <= 31:
            image = pg.image.load(boardlist[55 - i])
            screen.blit(image, (43 + 70*(i - 24), 323))
        if 31 < i <= 39:
            image = pg.image.load(boardlist[71 - i])
            screen.blit(image, (43 + 70*(i - 32), 253))
        if 39 < i <= 47:
            image = pg.image.load(boardlist[87 - i])
            screen.blit(image, (43 + 70*(i - 40), 183))
        if 47 < i <= 55:
            image = pg.image.load(boardlist[103 - i])
            screen.blit(image, (43 + 70*(i - 48), 113))
        if 55 < i <= 63:
            image = pg.image.load(boardlist[119 - i])
            screen.blit(image, (43 + 70*(i - 56), 43))
                
########################################################################################################################
# https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
COLOR_INACTIVE = pg.Color('navy')
COLOR_ACTIVE = pg.Color('firebrick1')
FONT = pg.font.Font(None, 32)

class InputBox:

    def __init__(self, x, y, w, h, data, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

        self.history = []
        self.data = data
        self.data = []

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.data.append(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def data_read(self):
        if len(self.data) == 1:
            self.history.append(self.data[0])
            return self.data
        if len(self.data) >= 1:
            self.data.remove(self.data[0])
            return

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

########################################################################################################################
chessboard = chess.Board()
font = pg.font.Font(None, 32)
inputdata = []
moveBox = InputBox(710, 310, 140, 36, inputdata)

def main():
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            moveBox.handle_event(event)

        moveBox.update()
        screen.fill((240, 248, 255))

        moveBox.draw(screen)
        data = moveBox.data_read()
        if chessboard.turn:
            if data is not None:
                chessboard.push_san(data[0])
                data.clear()
                showBoard(chessboard)
            else:
                showBoard(chessboard)
        else:
            move = moveSelect(chessboard, 7)
            chessboard.push(move)
            showBoard(chessboard)

        pg.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
    pg.quit()
