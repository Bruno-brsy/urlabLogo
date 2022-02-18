# urlab logo with turtle

#  _    _      _           _     
# | |  | |    | |         | |    
# | |  | |_ __| |     __ _| |__  
# | |  | | '__| |    / _` | '_ \ 
# | |__| | |  | |___| (_| | |_) |
#  \____/|_|  |______\__,_|_.__/ 

import turtle as t

def square(size, X, Y, skipNbrSquareInX=0, skipNbrSquareInY=0):
    X += skipNbrSquareInX * size
    Y += skipNbrSquareInY * size
    t.goto(X - 0.5 * size, Y + 0.5 * size)
    t.down()
    t.begin_fill()
    t.goto(X + 0.5 * size, Y + 0.5 * size)
    t.goto(X + 0.5 * size, Y - 0.5 * size)
    t.goto(X - 0.5 * size, Y - 0.5 * size)
    t.goto(X - 0.5 * size, Y + 0.5 * size)
    t.end_fill()
    t.up()
    return X, Y


def spaceInvender(sizeSquare, centerX, centerY):
    # virtually goto the top left of the space invader
    X = centerX - 5.5 * sizeSquare
    Y = centerY + 4 * sizeSquare
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=2)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=6)
    
    # second row
    X = centerX - 5.5 * sizeSquare
    Y -= 1 * sizeSquare
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=3)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=4)

    # third row
    X = centerX - 5.5 * sizeSquare
    Y -= 1 * sizeSquare
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=2)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)

    # fourth row
    X = centerX - 5.5 * sizeSquare
    Y -= 1 * sizeSquare
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=2)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=2)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)

    # fifth row
    X = centerX - 5.5 * sizeSquare
    Y -= 1 * sizeSquare
    X, Y = square(sizeSquare, X, Y)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)

    # sixth row
    X = centerX - 5.5 * sizeSquare
    Y -= 1 * sizeSquare
    X, Y = square(sizeSquare, X, Y)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=2)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=2)

    # seventh row
    X = centerX - 5.5 * sizeSquare
    Y -= 1 * sizeSquare
    X, Y = square(sizeSquare, X, Y)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=2)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=6)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=2)

    # eighth row
    X = centerX - 5.5 * sizeSquare
    Y -= 1 * sizeSquare
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=3)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=2)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)


def UrLabText(sizeSquare, centerX, centerY):
    # virtually goto the top left of the text UrLab
    X = centerX - 14 * sizeSquare
    Y = centerY + 3.5 * sizeSquare

    # U
    X, Y = square(sizeSquare, X, Y)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y,skipNbrSquareInX=1, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y,skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y,skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y,skipNbrSquareInX=1, skipNbrSquareInY=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=1)

    # r
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=2, skipNbrSquareInY=-2)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1, skipNbrSquareInY=3)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1, skipNbrSquareInY=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)

    # L
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=2, skipNbrSquareInY=2)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)

    # a
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=3, skipNbrSquareInY=4)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=-1, skipNbrSquareInY=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1, skipNbrSquareInY=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)

    # b
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=3, skipNbrSquareInY=4)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=-1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInX=1, skipNbrSquareInY=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=1)
    X, Y = square(sizeSquare, X, Y, skipNbrSquareInY=1)
    X, Y = square(sizeSquare, X, Y,skipNbrSquareInX=-1, skipNbrSquareInY=1)
    X, Y = square(sizeSquare, X, Y,skipNbrSquareInX=-1)
    X, Y = square(sizeSquare, X, Y,skipNbrSquareInX=-1)






def main():
    t.up()
    t.speed(0)
    spaceInvender(20, 0, 0)

    UrLabText(15, 0, -170)




if __name__ == '__main__':
    # input()
    main()
    input()