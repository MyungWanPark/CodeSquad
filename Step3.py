import copy


class Cube:

    # 3x3 큐브 값 입력받아 저장하기
    def __init__(self,row1,row2,row3):

        #self.one_side = [['R', 'R', 'W'], ['G', 'C', 'W'], ['G', 'B', 'B']]
        self.one_side = [row1, row2, row3]

        self.row1 = row1
        self.row2 = row2
        self.row3 = row3

        self.col1 = []
        self.col2 = []
        self.col3 = []

        # 큐브를 돌릴때 임시로 값을 넣어놓기 위한 리스트
        self.temp = []

        for i in range(3):
            self.col1 += [self.one_side[i][0]]
            self.col2 += [self.one_side[i][1]]
            self.col3 += [self.one_side[i][2]]

    # 큐브 한쪽면 출력하기
    def print_one_side(self,Front,Right,Left,Up,Down,Back):

        # 큐브 Up 출력
        for i in range(3):
            print("              ", end = " ")
            for j in range(3):
                print(Up.one_side[i][j], end=' ')
            print()

        for i in range(3):

            # 큐브 왼쪽부터 출력
            for j in range(3):
                print(Left.one_side[i][j], end=' ')
            print("   ",end = " ")

            # 큐브 Front 출력
            for j in range(3):
                print(Front.one_side[i][j], end=' ')
            print("   ", end=" ")

            # 큐브 Right 출력
            for j in range(3):
                print(Right.one_side[i][j], end=' ')
            print("   ", end=" ")

            # 큐브 Back 출력
            for j in range(3):
                print(Back.one_side[i][j], end=' ')
            print("   ", end=" ")
            print()

        # 큐브 Down 출력
        for i in range(3):
            print("              ", end = " ")
            for j in range(3):
                print(Down.one_side[i][j], end=' ')
            print()

    # 큐브게임 시작하기
    def start(self,front,Right,Left,Up,Down,Back):

        self.print_one_side(front,Right,Left,Up,Down,Back)
        print()

        while True:

            command = list(input("CUBE> "))

            # '\'' 을 처리하기 위해 '\''이 발견되면 전의 알파벳에 합친다.
            i = 0
            while True:

                if i == len(command):
                    break

                if command[i] == "'":
                    command[i - 1] = command[i - 1] + "'"
                    del command[i]
                    continue

                i += 1

            # command 명령에 있는 각각의 명령 하나씩 실행하기
            for i in command:

                if i == 'Q':
                    print("Bye~")
                    return

                # switch-case 문 대신에 활용
                functions = {
                    'U': self.UpDirLeft,
                    'U\'': self.UpDirRight,
                    'R': self.RightDirUp,
                    'R\'': self.RightDirDown,
                    'L': self.LeftDirDown,
                    'L\'': self.LeftDirUp,
                    'B': self.BottomDirRight,
                    'B\'': self.BottomDirLeft
                }

                func = functions[i]
                print(i)
                func()

                # 함수를 실행한 후 전체 출력
                self.print_one_side()
                print()

    def UpDirLeft(self):

        self.temp = copy.deepcopy(self.row1)

        # self.row1[0] = self.temp[1]
        # self.row1[1] = self.temp[2]
        # self.row1[2] = self.temp[0]

        # row1은 3개로 이루어져 있어서 반복을 3번 함
        for i in range(3):
            # 움직인 후 마지막 값은 기존의 첫번째 값이 와야한다.
            if i == 2:
                self.row1[i] = self.temp[0]
                break
            # 한칸씩 옆으로 움직인 값을 넣어준다.
            self.row1[i] = self.temp[i + 1]

    def UpDirRight(self):

        self.temp = copy.deepcopy(self.row1)

        # row1은 3개로 이루어져 있어서 반복을 3번 함
        for i in range(3):
            # 움직인 후 첫번째 값은 기존의 마지막 값이 와야한다.
            if i == 0:
                self.row1[i] = self.temp[2]
                continue
            # 한칸씩 옆으로 움직인 값을 넣어준다.
            self.row1[i] = self.temp[i - 1]

    def RightDirUp(self):

        self.temp = copy.deepcopy(self.col3)

        # col3은 3개로 이루어져 있어서 반복을 3번 함
        for i in range(3):
            # 움직인 후 마지막 값은 기존의 첫번째 값이 와야한다.
            if i == 2:
                self.col3[i] = self.temp[0]
                break
            # 한칸씩 위로 움직인 값을 넣어준다.
            self.col3[i] = self.temp[i + 1]

    def RightDirDown(self):

        self.temp = copy.deepcopy(self.col3)

        # col3은 3개로 이루어져 있어서 반복을 3번 함
        for i in range(3):
            # 움직인 후 첫번째 값은 기존의 마지막 값이 와야한다.
            if i == 0:
                self.col3[i] = self.temp[2]
                continue
            # 한칸씩 아래로 움직인 값을 넣어준다.
            self.col3[i] = self.temp[i - 1]

    def LeftDirDown(self):

        self.temp = copy.deepcopy(self.col1)

        # col1은 3개로 이루어져 있어서 반복을 3번 함
        for i in range(3):
            # 움직인 후 첫번째 값은 기존의 마지막 값이 와야한다.
            if i == 0:
                self.col1[i] = self.temp[2]
                continue
            # 한칸씩 아래로 움직인 값을 넣어준다.
            self.col1[i] = self.temp[i - 1]

    def LeftDirUp(self):

        self.temp = copy.deepcopy(self.col1)

        # col1은 3개로 이루어져 있어서 반복을 3번 함
        for i in range(3):
            # 움직인 후 마지막 값은 기존의 첫번째 값이 와야한다.
            if i == 2:
                self.col1[i] = self.temp[0]
                break
            # 한칸씩 위로 움직인 값을 넣어준다.
            self.col1[i] = self.temp[i + 1]

    def BottomDirRight(self):

        self.temp = copy.deepcopy(self.row3)

        # row3은 3개로 이루어져 있어서 반복을 3번 함
        for i in range(3):
            # 움직인 후 첫번째 값은 기존의 마지막 값이 와야한다.
            if i == 0:
                self.row3[i] = self.temp[2]
                continue
            # 한칸씩 옆으로 움직인 값을 넣어준다.
            self.row3[i] = self.temp[i - 1]

    def BottomDirLeft(self):

        self.temp = copy.deepcopy(self.row3)

        # row3은 3개로 이루어져 있어서 반복을 3번 함
        for i in range(3):
            # 움직인 후 마지막 값은 기존의 첫번째 값이 와야한다.
            if i == 2:
                self.row3[i] = self.temp[0]
                break
            # 한칸씩 옆으로 움직인 값을 넣어준다.
            self.row3[i] = self.temp[i + 1]


Front = Cube(['O','O','O'],['O','O','O'],['O','O','O'])
Right = Cube(['G','G','G'],['G','G','G'],['G','G','G'])
Left = Cube(['W','W','W'],['W','W','W'],['W','W','W'])
Up = Cube(['B','B','B'],['B','B','B'],['B','B','B'])
Down = Cube(['R','R','R'],['R','R','R'],['R','R','R'])
Back = Cube(['Y','Y','Y'],['Y','Y','Y'],['Y','Y','Y'])

Main = Cube([9,9,9],[9,9,9],[9,9,9])
Main.start(Front,Right,Left,Up,Down,Back)
