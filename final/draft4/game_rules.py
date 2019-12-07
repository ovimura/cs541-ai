
class Move:
    def __init__(self):
        self.x = -1
        self.y = -1

    def set(self, x, y):
        self.x = x
        self.y = y

    def isPass(self):
        return self.x == -1 and self.y == -1

    def convert_to_coord(self, m):
        if "pass" in m:
            self.x = -1
            self.y = -1
            return self
        if len(m) != 2:
            raise ("error: invalid move format")
        self.x = (ord(m[0])-97)
        self.y = int(m[1])-1
        return self

    def name(self):
        if self.x+1 == 1:
            return "a" + str(self.y + 1)
        elif self.x+1 == 2:
            return "b" + str(self.y + 1)
        elif self.x+1 == 3:
            return "c" + str(self.y + 1)
        elif self.x+1 == 4:
            return "d" + str(self.y + 1)
        elif self.x+1 == 5:
            return "e" + str(self.y + 1)
        elif self.x == -1 and self.y == -1:
            return "pass"
        else:
            raise ("error: invalid move format")


class Board:
    def __init__(self, b=None):
        self.GAME_OVER = 1
        self.CONTINUE = 0
        self.ILLEGAL_MOVE = -1
        self.PLAYER_WHITE = 1
        self.PLAYER_BLACK = 2
        self.OBSERVER = 3
        self.game_state = self.CONTINUE

        self.to_move = self.PLAYER_BLACK
        self.serial = 1

        # rules-specific game state
        self.previous_move = None
        self.square = [[0]*5 for x in range(5)]

        self.WHITE_CHECKER = self.PLAYER_WHITE
        self.BLACK_CHECKER = self.PLAYER_BLACK

        if b is not None:
            self.previous_move = b.previous_move
            for i in range(5):
                for j in range(5):
                    self.square[i][j] = b.square[i][j]

            self.to_move = b.to_move
            self.game_state = b.game_state
            self.serial = b.serial

    def print(self):
        print(self.serial)
        print(" ")
        if self.game_state == self.GAME_OVER:
            print("*")
        elif self.to_move == self.PLAYER_WHITE:
            print("w")
        else:
            print("b")
        print("\r\n")
        print("382\r\n")
        self.print_board()

    def print_board(self):
        for j in [4,3,2,1,0]:
            for i in [0,1,2,3,4]:
                if self.square[i][j] == 0:
                    print(".",end="")
                elif self.square[i][j] == self.BLACK_CHECKER:
                    print("b",end="")
                elif self.square[i][j] == self.WHITE_CHECKER:
                    print("w",end="")
                else:
                    print("?",end="")
            print()

    def opponent(self, player):
        if player == self.PLAYER_WHITE:
            return self.PLAYER_BLACK
        if player == self.PLAYER_BLACK:
            return self.PLAYER_WHITE
        print("internal error: bad player")
        raise


    # XXX see declaration of BLACK_CHECKER, WHITE_CHECKER
    def checker_of(self, player):
        return player

    def owner_of(self, checker):
        return checker


    def scratch_board(self):
        scratch = [[0]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                scratch[i][j] = False
        return scratch

    def flood(self, scratch, color, x, y):
        if (not (x >= 0 and x <= 4 and y >= 0 and y <= 4)):
            return
        if (scratch[x][y]):
            return
        if (self.square[x][y] != color):
            return
        scratch[x][y] = True
        self.flood(scratch, color, x - 1, y)
        self.flood(scratch, color, x + 1, y)
        self.flood(scratch, color, x, y - 1)
        self.flood(scratch, color, x, y + 1)
        return scratch

    def group_border(self, scratch, x, y):
        if scratch[x][y]:
            return False
        if x > 0 and scratch[x - 1][y]:
            return True
        if x < 4 and scratch[x + 1][y]:
            return True
        if y > 0 and scratch[x][y - 1]:
            return True
        if y < 4 and scratch[x][y + 1]:
            return True
        return False

    def liberties(self, x, y):
        scratch = self.scratch_board()
        self.flood(scratch, self.square[x][y], x, y)
        n = 0
        for i in range(5):
            for j in range(5):
                if self.square[i][j] == 0 and self.group_border(scratch, i, j):
                    n += 1
        return n


    def move_ok(self, m):
        if m.isPass():
            return True
        if self.square[m.x][m.y] != 0:
            return False
        self.square[m.x][m.y] = self.to_move
        n = self.liberties(m.x, m.y)
        self.square[m.x][m.y] = 0
        if n == 0:
            return False
        return True

    def genMoves(self):
        result = []
        m = None
        for i in range(5):
            for j in range(5):
                if self.square[i][j] == 0:
                    m = str(i)+str(j)
            if self.move_ok(m):
                result.append(m)
        return result

    def has_moves(self):
        ms = self.genMoves()
        return len(ms) > 0

    def capture(self, x, y):
        if self.liberties(x, y) > 0:
            return
        scratch = self.scratch_board()
        self.flood(scratch, self.square[x][y], x, y)
        for i in range(5):
            for j in range(5):
                if scratch[i][j]:
                    self.square[i][j] = self.to_move

    def do_captures(self,m):
        if (m.x > 0 and self.square[m.x - 1][m.y] == self.opponent(self.to_move)):
            self.capture(m.x - 1, m.y)
        if (m.x < 4 and self.square[m.x + 1][m.y] == self.opponent(self.to_move)):
            self.capture(m.x + 1, m.y)
        if (m.y > 0 and self.square[m.x][m.y - 1] == self.opponent(self.to_move)):
            self.capture(m.x, m.y - 1)
        if (m.y < 4 and self.square[m.x][m.y + 1] == self.opponent(self.to_move)):
            self.capture(m.x, m.y + 1)

    def makeMove(self,m):
        self.previous_move = m
        if (m.isPass()):
            return
        self.square[m.x][m.y] = self.to_move
        self.do_captures(m)

    def try_move(self, m):
        if (self.game_state != self.CONTINUE):
            return self.ILLEGAL_MOVE
        if m.isPass() and self.previous_move is not None and self.previous_move.isPass():
            self.game_state = self.GAME_OVER
            return self.GAME_OVER
        if (not self.move_ok(m)):
            return self.ILLEGAL_MOVE
        self.makeMove(m)
        self.to_move = self.opponent(self.to_move)
        if (self.to_move == self.PLAYER_BLACK):
            self.serial+=1
        return self.CONTINUE

    def referee(self):
        if self.game_state != self.GAME_OVER:
            raise ("internal error: referee unfinished game")
        nblack = 0
        nwhite = 0
        for i in range(5):
            for j in range(5):
                if(self.square[i][j] == self.BLACK_CHECKER):
                    nblack+=1
                    break
                if(self.square[i][j] == self.WHITE_CHECKER):
                    nwhite+=1
                    break
        if (nblack > nwhite):
            return self.PLAYER_BLACK
        if (nwhite > nblack):
            return self.PLAYER_WHITE
        return self.OBSERVER

# b = Board()
# scratch = [[0]*5 for _ in range(5)]
# print(scratch)
# b.flood(scratch=scratch, color=0,x=1,y=1)
# print(scratch)
