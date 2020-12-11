import copy


class Cube:

    # 3x3 큐브 값 입력받아 저장하기
    def __init__(self,row1,row2,row3):

        self.row1 = row1
        self.row2 = row2
        self.row3 = row3

        self.rows = [self.row1, self.row2, self.row3]

        self.col1 = []
        self.col2 = []
        self.col3 = []

        # 큐브를 돌릴때 임시로 값을 넣어놓기 위한 리스트
        self.temp = []

        for i in range(3):
            self.col1 += [self.rows[i][0]]
            self.col2 += [self.rows[i][1]]
            self.col3 += [self.rows[i][2]]

        self.cols = [self.col1, self.col2, self.col3]
    # 큐브 한쪽면 출력하기
    def print_one_side(*args):

        # command를 실행 후 각 면의 row와 col값이 바뀌었으니, rows와 cols를 업데이트 해줘야 이것을 이용한 출력이 제대로 된다.
        for i in args:
            i.rows = [i.row1, i.row2, i.row3]
            i.cols = [i.col1, i.col2, i.col3]

        # 큐브 Up 출력
        for i in range(3):
            print("              ", end = " ")
            for j in range(3):
                print(Up.rows[i][j], end = " ")
            print()

        # 큐브에서 윗면과 아랫면 제외한 후 출력
        for i in range(3):

            # 큐브 Left 출력
            for j in range(3):
                print(Left.rows[i][j], end=' ')
            print("   ",end = " ")

            # 큐브 Front 출력
            for j in range(3):
                print(Front.rows[i][j], end=' ')
            print("   ", end=" ")

            # 큐브 Right 출력
            for j in range(3):
                print(Right.rows[i][j], end=' ')
            print("   ", end=" ")

            # 큐브 Back 출력
            for j in range(3):
                print(Back.rows[i][j], end=' ')
            print("   ", end=" ")
            print()

        # 큐브 Down 출력
        for i in range(3):
            print("              ", end = " ")
            for j in range(3):
                print(Down.rows[i][j], end=' ')
            print()

    # 큐브게임 시작하기
    def start(self,Front,Right,Left,Up,Down,Back):

        self.print_one_side(Front,Right,Left,Up,Down,Back)
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

            # '2' 을 처리하기 위해 '2'이 발견되면 전의 알파벳에 합친다.
            i = 0
            while True:

                if i == len(command):
                    break

                if command[i] == "2":
                    command[i - 1] = command[i - 1] + "2"
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
                    'U': self.UpCW,
                    'U\'': self.UpCCW,
                    'U2': self.UpCW2,

                    'L': self.LeftCW,
                    'L\'': self.LeftCCW,
                    'L2': self.LeftCW2,

                    'F': self.FrontCW,
                    'F\'': self.FrontCCW,
                    'F2': self.FrontCW2,

                    'R': self.RightCW,
                    'R\'': self.RightCCW,
                    'R2': self.RightCW2,

                    'B': self.BackCW,
                    'B\'': self.BackCCW,
                    'B2': self.BackCW2,

                    'D': self.DownCW,
                    'D\'': self.DownCCW,
                    'D2': self.DownCW2

                }

                func = functions[i]
                print(i)

                # command가 Up과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
                if 'U' in i:
                    func(Up,Front,Left,Right,Back)

                # command가 Left과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
                if 'L' in i:
                    func(Up,Front,Left,Down,Back)

                # command가 Front과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
                if 'F' in i:
                    func(Up,Front,Left,Right,Down)

                # command가 Right과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
                if 'R' in i:
                    func(Up,Front,Down,Right,Back)

                # command가 Back과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
                if 'B' in i:
                    func(Up,Down,Left,Right,Back)

                # command가 Down과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
                if 'D' in i:
                    func(Down,Front,Left,Right,Back)

                # 함수를 실행한 후 전체 출력
                self.print_one_side(Front,Right,Left,Up,Down,Back)
                print()

    def UpCW(self,Up,Front,Left,Right,Back):
        print("UpCW가 실행되었습니다.")
        # 윗면이 시계방향으로 바뀐다.
        Up.temp = Up.col3
        Up.col3 = Up.row1
        Up.row1 = Up.col1
        Up.col1 = Up.row3
        Up.row3 = Up.temp

        #아랫면 빼고 row1이 시계방향으로 바뀐다.
        Front.temp = Front.row1
        Front.row1 = Right.row1
        Right.row1 = Back.row1
        Back.row1 = Left.row1
        Left.row1 = Front.temp
        print("Front.row1 = ",Front.row1)

    def UpCCW(self,Up,Front,Left,Right,Back):
        print("UpCCW가 실행되었습니다.")

    def UpCW2(self,Up,Front,Left,Right,Back):
        print("UpCW2가 실행되었습니다.")

    def LeftCW(self,Up,Front,Left,Down,Back):
        print("LeftCW 실행되었습니다.")

    def LeftCCW(self,Up,Front,Left,Down,Back):
        print("LeftCCW 실행되었습니다.")

    def LeftCW2(self,Up,Front,Left,Down,Back):
        print("LeftCW2 실행되었습니다.")

    def FrontCW(self,Up,Front,Left,Right,Down):
        print("FrontCW 실행되었습니다.")

    def FrontCCW(self,Up,Front,Left,Right,Down):
        print("FrontCCW 실행되었습니다.")

    def FrontCW2(self,Up,Front,Left,Right,Down):
        print("FrontCW2 실행되었습니다.")

    def RightCW(self,Up,Front,Down,Right,Back):
        print("RightCW 실행되었습니다.")

    def RightCCW(self,Up,Front,Down,Right,Back):
        print("RightCCW 실행되었습니다.")

    def RightCW2(self,Up,Front,Down,Right,Back):
        print("RightCW2 실행되었습니다.")

    def BackCW(self,Up,Down,Left,Right,Back):
        print("BackCW 실행되었습니다.")

    def BackCCW(self,Up,Down,Left,Right,Back):
        print("BackCCW 실행되었습니다.")

    def BackCW2(self,Up,Down,Left,Right,Back):
        print("BackCW2 실행되었습니다.")

    def DownCW(self,Down,Front,Left,Right,Back):
        print("DownCW 실행되었습니다.")

    def DownCCW(self,Down,Front,Left,Right,Back):
        print("DownCCW 실행되었습니다.")

    def DownCW2(self,Down,Front,Left,Right,Back):
        print("DownCW2 실행되었습니다.")

Front = Cube(['O','O','O'],['O','O','O'],['O','O','O'])
Right = Cube(['G','G','G'],['G','G','G'],['G','G','G'])
Left = Cube(['W','W','W'],['W','W','W'],['W','W','W'])
Up = Cube(['B','B','B'],['B','B','B'],['B','B','B'])
Down = Cube(['R','R','R'],['R','R','R'],['R','R','R'])
Back = Cube(['Y','Y','Y'],['Y','Y','Y'],['Y','Y','Y'])

Main = Cube([9,9,9],[9,9,9],[9,9,9])
Main.start(Front,Right,Left,Up,Down,Back)
