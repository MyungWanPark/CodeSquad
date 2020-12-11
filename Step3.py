import copy

class Cube:

    # 3x3 큐브 값 입력받아 저장하기
    def __init__(self,total):

        self.total = total

        self.row1 = self.total[:3]
        self.row2 = self.total[3:6]
        self.row3 = self.total[6:9]

        self.col1 = [self.row1[0]] + [self.row2[0]] + [self.row3[0]]
        self.col2 = [self.row1[1]] + [self.row2[1]] + [self.row3[1]]
        self.col3 = [self.row1[2]] + [self.row2[2]] + [self.row3[2]]

        # 이러한 관계를 표현할 수 있어야 한다.
        """self.row1[0] = self.col1[0]
        self.row1[2] = self.col3[0]
        self.row3[0] = self.col1[2]
        self.row3[2] = self.col3[2]"""

    # 큐브 한쪽면 출력하기
    def Updating(*args):

        # command를 실행 후 각 면의 row와 col값이 바뀌었으니, rows와 cols를 업데이트 해줘야 이것을 이용한 출력이 제대로 된다.
        for i in args:
            i.rows = [i.row1, i.row2, i.row3]
            # print("rows = ", i.rows)
            i.cols = [i.col1, i.col2, i.col3]
            # print("i.col1 = ",i.col1)
            # print()

                i.col1[0] = i.row1[0]
                i.col1[1] = i.row2[0]
                i.col1[2] = i.row3[0]

                i.col2[0] = i.row1[1]
                i.col2[1] = i.row2[1]
                i.col2[2] = i.row3[1]

                i.col3[0] = i.row1[2]
                i.col3[1] = i.row2[2]
                i.col3[2] = i.row3[2]

            for j in range(3):
                i.col1[j] = i.row1[0]
                i.col2[j] = i.row2[1]
                i.col3[j] = i.row3[2]

    def print_one_side(self,Front,Right,Left,Up,Down,Back):

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
                self.Updating(Front,Right,Left,Up,Down,Back)
                self.print_one_side(Front,Right,Left,Up,Down,Back)
                print()

    def UpCW(self,Up,Front,Left,Right,Back):
        print("UpCW가 실행되었습니다.")
        # 윗면이 시계방향으로 바뀐다.
        Up.row1, Up.col3, Up.row3, Up.col1 = Up.col1, Up.row1, Up.col3, Up.row3
        self.Updating(Front, Right, Left, Up, Back)
        #옆면이 시계방향으로 바뀐다.
        Front.row1, Left.row1, Back.row1, Right.row1 = Right.row1, Front.row1, Left.row1, Back.row1
        # self.Updating(Front, Right, Left, Up, Back)

        print("Left.row1 = ",Left.row1)
        print("Left.col1 = ",Left.col1)
        print("Front.col1 = ", Front.col1)
    def UpCCW(self,Up,Front,Left,Right,Back):
        print("UpCCW가 실행되었습니다.")
        # 윗면이 반시계방향으로 바뀐다.
        Up.row1, Up.col3, Up.row3, Up.col1 = Up.col3, Up.row3, Up.col1, Up.row1

        # 옆면이 반시계방향으로 바뀐다.
        Front.row1, Left.row1, Back.row1, Right.row1 = Left.row1, Back.row1, Right.row1, Front.row1

    def UpCW2(self,Up,Front,Left,Right,Back):
        print("UpCW2가 실행되었습니다.")
        # 윗면이 바뀌는 경우
        Up.row1, Up.col3, Up.row3, Up.col1 = Up.row3, Up.col1, Up.row1, Up.col3

        # 옆면들이 바뀌는 경우
        Front.row1, Left.row1, Back.row1, Right.row1 = Back.row1, Right.row1, Front.row1, Left.row1

    def LeftCW(self,Up,Front,Left,Down,Back):
        # print("Left.row1 = ", Left.row1)
        print("Left.col1 = ", Left.col1)
        print("LeftCW 실행되었습니다.")
        # 왼쪽 면이 바뀌는 경우
        Left.row1, Left.col3, Left.row3, Left.col1 = Left.col1, Left.row1, Left.col3, Left.row3
        # print("Left.row1 = ", Left.row1)

        # 왼쪽면을 기준으로 옆면들이 바뀌는 경우
        Up.col1, Front.col1, Down.col1, Back.col1 = Back.col1, Up.col1, Front.col1, Down.col1
        # print("Up.col1 = ", Up.col1)

    def LeftCCW(self,Up,Front,Left,Down,Back):
        print("LeftCCW 실행되었습니다.")
        # 왼쪽 면이 바뀌는 경우
        Left.row1, Left.col3, Left.row3, Left.col1 = Left.col3, Left.row3, Left.col1, Left.row1

        # 왼쪽면을 기준으로 옆면들이 바뀌는 경우
        Up.col1, Front.col1, Down.col1, Back.col1 = Front.col1, Down.col1, Back.col1, Up.col1


    def LeftCW2(self,Up,Front,Left,Down,Back):
        print("LeftCW2 실행되었습니다.")
        # 왼쪽 면이 바뀌는 경우
        Left.row1, Left.col3, Left.row3, Left.col1 = Left.row3, Left.col1, Left.row1, Left.col3

        # 왼쪽면을 기준으로 옆면들이 바뀌는 경우
        Up.col1, Front.col1, Down.col1, Back.col1 = Down.col1, Back.col1, Up.col1, Front.col1

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

Main = Cube([9,9,9],[9,9,9],[9,9,9])
Main.start(Front,Right,Left,Up,Down,Back)
