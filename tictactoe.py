import pygame
import sys

pygame.init()

display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Lets play Tic Tac Toe!")

gridCol = (0, 0, 0)

display.fill((255, 255, 255))

# Draw vertical lines
for i in range(1, 3):
    pygame.draw.line(display, gridCol, (0,i*500/3), (500,i*500/3), 16)

for i in range(1, 3):
    pygame.draw.line(display, gridCol, (i*500/3,500), (i*500/3,0), 16)

pygame.display.update()


def getQuad(x,y):
    if(x <= 160):
        if(y<=160):
            return[1,1]
        if(y>170 and y<330):
            return[2,1]
        if(y>340 and y<=500):
            return[3,1]
    if(x>170 and x<330):
        if(y<=160):
            return[1,2]
        if(y>170 and y<330):
            return[2,2]
        if(y>340 and y<=500):
            return[3,2]
    if(x>=340):
        if(y<=160):
            return[1,3]
        if(y>170 and y<330):
            return[2,3]
        if(y>340 and y<=500):
            return[3,3]
        
def addXO(quad, board, turn):
    row = quad[0]-1
    col = quad[1]-1
    if(board[row][col] == ""):
        board[row][col] = turn

def isWinner(board, turn):
    for i in range(3):
        if(board[i][0]== turn and board[i][1]== turn and board[i][2]== turn):
            return True
        if(board[0][i]== turn and board[1][i]== turn and board[2][i]== turn):
            return True
        if(board[0][0]== turn and board[1][1]== turn and board[2][2]== turn):
            return True
        if(board[0][2]== turn and board[1][1]== turn and board[2][0]== turn):
            return True
        
def isTie(board):
    for row in board:
        if "" in row:
            return False
    return True
        
# Main game loop
board = [["" for _ in range(3)] for _ in range(3)]
curTurn = "X"

game_over = False
while not game_over:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_over = True
        elif (event.type == pygame.MOUSEBUTTONDOWN):
             # Get the mouse click position
            mouseX, mouseY = pygame.mouse.get_pos()
            addXO(getQuad(mouseX,mouseY),board, curTurn)
            
            row = (getQuad(mouseX,mouseY)[0]-1)
            col = (getQuad(mouseX,mouseY)[1]-1)
            
            if(board[row][col] == "X"):
                pygame.draw.line(display, (0, 0, 255),[(col * 500/3)+20, ((row+1) * 500/3)-20],[((col+1) * (500 / 3)-20), row * 500/3+20],10)
                pygame.draw.line(display, (0, 0, 255),[(col * 500/3)+20, (row * 500/3)+20],[((col+1) * (500 / 3))-20, (row+1) * 500/3-20],10)
            elif(board[row][col] == "O"):
                pygame.draw.circle(display, (255, 0, 0), (col * (500 / 3) + 250 // 3, row * (500 / 3) + 250 // 3),80, 10)
            pygame.display.update()
            if(isWinner(board,curTurn)):
                print("\nCongratulations on your win!")
                game_over = True

            elif(isTie(board)):
                print("\nYou tied!")
                game_over = True

            else:
                if(curTurn == "X"):
                    curTurn = "O"
                else:
                    curTurn = "X"
