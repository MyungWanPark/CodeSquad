import copy

class Cube:

    # 3x3 큐브 값 입력받아 저장하기
    def __init__(self,total):

        self.total = total
        self.temp = copy.deepcopy(total)

        self.index = 0
        self.rows = []
        # print("total = ",self.total)

        # 이러한 관계를 표현할 수 있어야 한다.
        """self.row1[0] = self.col1[0]
        self.row1[2] = self.col3[0]
        self.row3[0] = self.col1[2]
        self.row3[2] = self.col3[2]"""

    def update_temp(*args):

        for i in args:
            i.temp = copy.deepcopy(i.total)

    def make_rows(self):

        self.rows.clear()
        self.index = 0

        for i in range(3):
            self.rows.append(self.total[self.index:self.index+3])
            self.index += 3

    def print_all_side(*args):

        # 출력 간편하게 하기 위해 행 만들기
        for i in args:
            i.make_rows()

        # 윗면 출력하기
        for i in range(3):
            print("                ",end = "")
            for j in range(3):
                print(Up.rows[i][j], end = " ")
            print()

        for i in range(3):
            # Left, Front, Right, Back 순으로 출력하기
            for j in range(3):
                print(Left.rows[i][j], end = " ")
            print("    ",end = '')

            for j in range(3):
                print(Front.rows[i][j], end = " ")
            print("     ",end = '')

            for j in range(3):
                print(Right.rows[i][j], end = " ")
            print("     ",end = '')

            for j in range(3):
                print(Back.rows[i][j], end = " ")
            print("     ",end = '')
            print()

        # 밑면 출력하기
        for i in range(3):
            print("                ", end="")
            for j in range(3):
                print(Down.rows[i][j], end = " ")
            print()
    # 큐브게임 시작하기
    def start(self,Up,Left,Front,Right,Back,Down):

        self.print_all_side(Up,Left,Front,Right,Back,Down)
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
                    func(Up,Left,Front,Right,Back)

                # command가 Left과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
                if 'L' in i:
                    func(Up,Left,Front,Back,Down)

                # command가 Front과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
                if 'F' in i:
                    func(Up,Left,Front,Right,Down)

                # command가 Right과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
                if 'R' in i:
                    func(Up,Front,Right,Back,Down)

                # command가 Back과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
                if 'B' in i:
                    func(Up,Left,Right,Back,Down)

                # command가 Down과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
                if 'D' in i:
                    func(Left,Front,Right,Back,Down)

                # 함수를 실행한 후 전체 출력
                self.print_all_side(Up,Left,Front,Right,Back,Down)
                # 현재 값으로 temp를 update 하기
                self.update_temp(Up,Left,Front,Right,Back,Down)


    def UpCW(self,Up,Left,Front,Right,Back):
        print("UpCW가 실행되었습니다.")
        # Up면의 시계방향 변경
        Up.total[2], Up.total[5], Up.total[8] = Up.temp[0], Up.temp[1], Up.temp[2]
        Up.total[6], Up.total[7], Up.total[8] = Up.temp[8], Up.temp[5], Up.temp[2]
        Up.total[0], Up.total[3], Up.total[6] = Up.temp[6], Up.temp[7], Up.temp[8]
        Up.total[0], Up.total[1], Up.total[2] = Up.temp[6], Up.temp[3], Up.temp[0]

        Left.total[0],Left.total[1],Left.total[2] = Front.temp[0],Front.temp[1],Front.temp[2]
        Front.total[0], Front.total[1], Front.total[2] = Right.temp[0],Right.temp[1],Right.temp[2]
        Right.total[0], Right.total[1], Right.total[2] = Back.temp[0],Back.temp[1],Back.temp[2]
        Back.total[0], Back.total[1], Back.total[2] = Left.temp[0],Left.temp[1],Left.temp[2]

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

Front = Cube(['O','O','O','O','O','O','O','O','O'])
Right = Cube(['G','G','G','G','G','G','G','G','G'])
Left = Cube(['W','W','W','W','W','W','W','W','W'])
Up = Cube(['B','B','B','B','B','B','B','B','B'])
Down = Cube(['R','R','R','R','R','R','R','R','R'])
Back = Cube(['Y','Y','Y','Y','Y','Y','Y','Y','Y'])

Main = Cube([9,9,9,9,9,9,9,9,9])
Main.start(Up,Left,Front,Right,Back,Down)
