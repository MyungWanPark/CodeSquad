# CodeSquad

## step3: 루빅스 큐브 구현하기
## 동작 단계
1. 큐브 6면 각각의 객체를 생성한다.
2. 생성된 객체에 각각의 컬러를 초기화 한다.
3. 시작을 위한 main 객체를 만든다.
4. 시작 함수를 실행한다.
5. 큐브의 모든 면을 출력한다.
6. 명령어를 입력받는다.
7. 명령어 중에 따옴표나 2를 구분해준다.
8. 명령어 기반으로 큐브를 움직여 준다. 
9. 이때 큐브의 움직임 함수는 윗면, 옆의 4면이 움직이는 패턴이 똑같은 것을 적용한다. 
10. 즉, 윗면이 시계방향으로 움직일때와 옆면이 시계방향으로 움직일때를 비교해보면,    옆면을 윗면으로 간주하고 움직일때와 같은 패턴을 보인다. 
11. 모든 면이 다 맞거나, 명령어 Q를 입력하면 종료된다.
12. 이때 명령어 조작 갯수와 총 실행시간을 출력한다. 

```python
import copy,time,sys

class Cube:

    # 3x3 큐브 값 입력받아 초기화하기
    def __init__(self,total):

        self.total = total
        self.temp = copy.deepcopy(total)
        self.rows = []

    # temp 갱신하기
    def update_temp(*args):

        for i in args:
            i.temp = copy.deepcopy(i.total)

    # print all side를 위한 임시로 rows 만들기
    def make_rows(self):

        self.rows.clear()
        index = 0

        for i in range(3):
            self.rows.append(self.total[index:index+3])
            index += 3

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

        # 시작 시점 시간 취득
        t1 = time.time()
        command_count = 0

        self.print_all_side(Up,Left,Front,Right,Back,Down)
        print()

        while True:

            # self.execute_command(t1, command_count)

            command = list(input("CUBE> "))

            # '\'' 을 처리하기 위해 '\''이 발견되면 전의 알파벳에 합친다.
            command = self.HandleQuotes(command)

            # '2' 을 처리하기 위해 '2'이 발견되면 전의 알파벳에 합친다.
            command = self.HandleCharTwo(command)

            # command 명령에 있는 각각의 명령 하나씩 실행하기
            for i in command:

                # command 실행, 조작 횟수 1 증가
                command_count += 1

                # 명령 실행
                self.execute_command(i, t1, command_count,Up,Left,Front,Right,Back,Down)

                # 현재 값으로 temp를 update 하기
                self.update_temp(Up,Left,Front,Right,Back,Down)

    def execute_command(self,i, t1,command_count,Up,Left,Front,Right,Back,Down):

        isQcounted = False
        if i == 'Q':

            isQcounted = True

            self.Quit(t1,command_count,isQcounted)

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
            func(Up, Left, Front, Right, Back)

        # command가 Left과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
        elif 'L' in i:
            func(Up, Left, Front, Back, Down)

        # command가 Front과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
        elif 'F' in i:
            func(Up, Left, Front, Right, Down)

        # command가 Right과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
        elif 'R' in i:
            func(Up, Front, Right, Back, Down)

        # command가 Back과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
        elif 'B' in i:
            func(Up, Left, Right, Back, Down)

        # command가 Down과 관련있는 경우, 아래와 같은 파라미터를 넘겨준다.
        elif 'D' in i:
            func(Left, Front, Right, Back, Down)

        # 모든 면 출력하기
        self.print_all_side(Up,Left,Front,Right,Back,Down)

        # 모든 면이 다 맞았는지 확인하기
        if self.all_match(Up, Left, Front, Right, Back, Down):
            print("축하합니다. 모든 면을 맞추셨습니다!!")
            self.Quit(t1,command_count,isQcounted)

    def Quit(self,t1,command_count,isQcounted):

        # 종류 시점 시간 취득
        t2 = time.time()

        # 동작 시간 계산
        elapsed_time = t2 - t1

        # 경과 시간 출력
        print("경과시간: ", elapsed_time)

        if isQcounted:
            # 조작횟수 Q 포함하여 1 증가시킴
            command_count += 1

        print("조작갯수: ", command_count)
        print("이용해주셔서 감사합니다. 뚜뚜뚜.")

        sys.exit()

    def HandleQuotes(self,command):

        i = 0

        while True:

            if i == len(command):
                return command

            if command[i] == "'":
                command[i - 1] = command[i - 1] + "'"
                del command[i]
                continue

            i += 1

    def HandleCharTwo(self,command):

        i = 0
        while True:

            if i == len(command):
                return command

            if command[i] == "2":
                command[i - 1] = command[i - 1] + "2"
                del command[i]
                continue

            i += 1

    def all_match(*args):

        count = 0
        is_all_match = False

        for i in args:
            if i.total[0] == i.total[1] == i.total[2] == i.total[3] == i.total[4] == i.total[5] == i.total[6] == i.total[7] == i.total[8] :
                count += 1

        if count == 6:
            is_all_match = True
        else:
            is_all_match = False

        return is_all_match

    # 기준면을 윗면으로 둔다.+ 시계방향
    def UPPER_CW(self,UPPER):

        UPPER.total[2], UPPER.total[5], UPPER.total[8] = UPPER.temp[0], UPPER.temp[1], UPPER.temp[2]
        UPPER.total[6], UPPER.total[7], UPPER.total[8] = UPPER.temp[8], UPPER.temp[5], UPPER.temp[2]
        UPPER.total[0], UPPER.total[3], UPPER.total[6] = UPPER.temp[6], UPPER.temp[7], UPPER.temp[8]
        UPPER.total[0], UPPER.total[1], UPPER.total[2] = UPPER.temp[6], UPPER.temp[3], UPPER.temp[0]

    # 기준면을 윗면으로 둔다.+ 반시계방향
    def UPPER_CCW(self, UPPER):

        UPPER.total[2], UPPER.total[5], UPPER.total[8] = UPPER.temp[8], UPPER.temp[7], UPPER.temp[6]
        UPPER.total[6], UPPER.total[7], UPPER.total[8] = UPPER.temp[0], UPPER.temp[3], UPPER.temp[6]
        UPPER.total[0], UPPER.total[3], UPPER.total[6] = UPPER.temp[2], UPPER.temp[1], UPPER.temp[0]
        UPPER.total[0], UPPER.total[1], UPPER.total[2] = UPPER.temp[2], UPPER.temp[5], UPPER.temp[8]

    # 기준면을 윗면으로 둔다.+ 시계방향
    def UPPER_CW2(self,UPPER):

        UPPER.total[0], UPPER.total[1], UPPER.total[2] = UPPER.temp[8], UPPER.temp[7], UPPER.temp[6]
        UPPER.total[2], UPPER.total[5], UPPER.total[8] = UPPER.temp[6], UPPER.temp[3], UPPER.temp[0]
        UPPER.total[8], UPPER.total[7], UPPER.total[6] = UPPER.temp[0], UPPER.temp[1], UPPER.temp[2]
        UPPER.total[6], UPPER.total[3], UPPER.total[0] = UPPER.temp[2], UPPER.temp[5], UPPER.temp[8]

    # 기준면이 윗면일때 나머지 옆면들 + 시계방향
    def SIDES_CW(self,Left_,Front_,Right_,Back_,Left_arr,Front_arr,Right_arr,Back_arr):

        Left_.total[Left_arr[0]], Left_.total[Left_arr[1]], Left_.total[Left_arr[2]] = Front_.temp[Front_arr[0]], Front_.temp[Front_arr[1]], Front_.temp[Front_arr[2]]
        Front_.total[Front_arr[0]], Front_.total[Front_arr[1]], Front_.total[Front_arr[2]] = Right_.temp[Right_arr[0]], Right_.temp[Right_arr[1]], Right_.temp[Right_arr[2]]
        Right_.total[Right_arr[0]], Right_.total[Right_arr[1]], Right_.total[Right_arr[2]] = Back_.temp[Back_arr[0]], Back_.temp[Back_arr[1]], Back_.temp[Back_arr[2]]
        Back_.total[Back_arr[0]], Back_.total[Back_arr[1]], Back_.total[Back_arr[2]] = Left_.temp[Left_arr[0]], Left_.temp[Left_arr[1]], Left_.temp[Left_arr[2]]

    # 기준면이 윗면일때 나머지 옆면들 + 반시계방향
    def SIDES_CCW(self, Left_, Front_, Right_, Back_,Left_arr,Front_arr,Right_arr,Back_arr):

        Left_.total[Left_arr[0]], Left_.total[Left_arr[1]], Left_.total[Left_arr[2]] = Back_.temp[Back_arr[0]], Back_.temp[Back_arr[1]], Back_.temp[Back_arr[2]]
        Front_.total[Front_arr[0]], Front_.total[Front_arr[1]], Front_.total[Front_arr[2]] = Left_.temp[Left_arr[0]], Left_.temp[Left_arr[1]], Left_.temp[Left_arr[2]]
        Right_.total[Right_arr[0]], Right_.total[Right_arr[1]], Right_.total[Right_arr[2]] = Front_.temp[Front_arr[0]], Front_.temp[Front_arr[1]], Front_.temp[Front_arr[2]]
        Back_.total[Back_arr[0]], Back_.total[Back_arr[1]], Back_.total[Back_arr[2]] = Right_.temp[Right_arr[0]], Right_.temp[Right_arr[1]], Right_.temp[Right_arr[2]]

    # 기준면이 윗면일때 나머지 옆면들 + 시계방향 180도 회전
    def SIDES_CW2(self, Left_, Front_, Right_, Back_, Left_arr, Front_arr, Right_arr, Back_arr):

        Left_.total[Left_arr[0]], Left_.total[Left_arr[1]], Left_.total[Left_arr[2]] = Right_.temp[Right_arr[0]], Right_.temp[Right_arr[1]], Right_.temp[Right_arr[2]]
        Front_.total[Front_arr[0]], Front_.total[Front_arr[1]], Front_.total[Front_arr[2]] = Back_.temp[Back_arr[0]], Back_.temp[Back_arr[1]], Back_.temp[Back_arr[2]]
        Right_.total[Right_arr[0]], Right_.total[Right_arr[1]], Right_.total[Right_arr[2]] = Left_.temp[Left_arr[0]], Left_.temp[Left_arr[1]], Left_.temp[Left_arr[2]]
        Back_.total[Back_arr[0]], Back_.total[Back_arr[1]], Back_.total[Back_arr[2]] = Front_.temp[Front_arr[0]], Front_.temp[Front_arr[1]], Front_.temp[Front_arr[2]]

    def UpCW(self,Up,Left,Front,Right,Back):

        self.UPPER_CW(Up)
        self.SIDES_CW(Left,Front,Right,Back,[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8])

    def UpCCW(self,Up,Left,Front,Right,Back):

        self.UPPER_CCW(Up)
        self.SIDES_CCW(Left, Front, Right, Back,[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8])

    def UpCW2(self,Up,Left,Front,Right,Back):

        self.UPPER_CW2(Up)
        self.SIDES_CW2(Left,Front,Right,Back,[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8],[0,1,2,3,4,5,6,7,8])

    def LeftCW(self,Up,Left,Front,Back,Down):

        self.UPPER_CW(Left)
        self.SIDES_CW(Back,Down,Front,Up,[2,5,8,1,4,7,0,3,6],[6,3,0,7,4,1,8,5,2],[6,3,0,7,4,1,8,5,2],[6,3,0,7,4,1,8,5,2])

    def LeftCCW(self,Up,Left,Front,Back,Down):

        self.UPPER_CCW(Left)
        self.SIDES_CCW(Back,Down,Front,Up,[2,5,8,1,4,7,0,3,6],[6,3,0,7,4,1,8,5,2],[6,3,0,7,4,1,8,5,2],[6,3,0,7,4,1,8,5,2])

    def LeftCW2(self,Up,Left,Front,Back,Down):

        self.UPPER_CW2(Left)
        self.SIDES_CW2(Back,Down,Front,Up,[2,5,8,1,4,7,0,3,6],[6,3,0,7,4,1,8,5,2],[6,3,0,7,4,1,8,5,2],[6,3,0,7,4,1,8,5,2])

    def FrontCW(self,Up,Left,Front,Right,Down):

        self.UPPER_CW(Front)
        self.SIDES_CW(Left,Down,Right,Up,[2,5,8,1,4,7,0,3,6],[0,1,2,3,4,5,6,7,8],[6,3,0,7,4,1,8,5,2],[8,7,6,5,4,3,2,1,0])

    def FrontCCW(self,Up,Left,Front,Right,Down):

        self.UPPER_CCW(Front)
        self.SIDES_CCW(Left,Down,Right,Up,[2,5,8,1,4,7,0,3,6],[0,1,2,3,4,5,6,7,8],[6,3,0,7,4,1,8,5,2],[8,7,6,5,4,3,2,1,0])

    def FrontCW2(self,Up,Left,Front,Right,Down):

        self.UPPER_CW2(Front)
        self.SIDES_CW2(Left,Down,Right,Up,[2,5,8,1,4,7,0,3,6],[0,1,2,3,4,5,6,7,8],[6,3,0,7,4,1,8,5,2],[8,7,6,5,4,3,2,1,0])

    def RightCW(self,Up,Front,Right,Back,Down):

        self.UPPER_CW(Right)
        self.SIDES_CW(Front,Down,Back,Up,[2,5,8,1,4,7,0,3,6],[2,5,8,1,4,7,0,3,6],[6,3,0,7,4,1,8,5,2],[2,5,8,1,4,7,0,3,6])

    def RightCCW(self,Up,Front,Right,Back,Down):

        self.UPPER_CCW(Right)
        self.SIDES_CCW(Front,Down,Back,Up,[2,5,8,1,4,7,0,3,6],[2,5,8,1,4,7,0,3,6],[6,3,0,7,4,1,8,5,2],[2,5,8,1,4,7,0,3,6])

    def RightCW2(self,Up,Front,Right,Back,Down):

        self.UPPER_CW2(Right)
        self.SIDES_CW2(Front,Down,Back,Up,[2,5,8,1,4,7,0,3,6],[2,5,8,1,4,7,0,3,6],[6,3,0,7,4,1,8,5,2],[2,5,8,1,4,7,0,3,6])

    def BackCW(self,Up,Left,Right,Back,Down):

        self.UPPER_CW(Back)
        self.SIDES_CW(Right,Down,Left,Up,[2,5,8,1,4,7,0,3,6],[8,7,6,5,4,3,2,1,0],[6,3,0,7,4,1,8,5,2],[0,1,2,3,4,5,6,7,8])

    def BackCCW(self,Up,Left,Right,Back,Down):

        self.UPPER_CCW(Back)
        self.SIDES_CCW(Right,Down,Left,Up,[2,5,8,1,4,7,0,3,6],[8,7,6,5,4,3,2,1,0],[6,3,0,7,4,1,8,5,2],[0,1,2,3,4,5,6,7,8])

    def BackCW2(self,Up,Left,Right,Back,Down):

        self.UPPER_CW2(Back)
        self.SIDES_CW2(Right,Down,Left,Up,[2,5,8,1,4,7,0,3,6],[8,7,6,5,4,3,2,1,0],[6,3,0,7,4,1,8,5,2],[0,1,2,3,4,5,6,7,8])

    def DownCW(self,Left,Front,Right,Back,Down):

        self.UPPER_CW(Down)
        self.SIDES_CW(Left,Back,Right,Front,[8,7,6,5,4,3,2,1,0],[8,7,6,5,4,3,2,1,0],[8,7,6,5,4,3,2,1,0],[8,7,6,5,4,3,2,1,0])

    def DownCCW(self,Left,Front,Right,Back,Down):

        self.UPPER_CCW(Down)
        self.SIDES_CCW(Left,Back,Right,Front,[8,7,6,5,4,3,2,1,0],[8,7,6,5,4,3,2,1,0],[8,7,6,5,4,3,2,1,0],[8,7,6,5,4,3,2,1,0])

    def DownCW2(self,Left,Front,Right,Back,Down):

        self.UPPER_CW2(Down)
        self.SIDES_CW2(Left,Back,Right,Front,[8,7,6,5,4,3,2,1,0],[8,7,6,5,4,3,2,1,0],[8,7,6,5,4,3,2,1,0],[8,7,6,5,4,3,2,1,0])

Front = Cube(['O','O','O','O','O','O','O','O','O'])
Right = Cube(['G','G','G','G','G','G','G','G','G'])
Left = Cube(['W','W','W','W','W','W','W','W','W'])
Up = Cube(['B','B','B','B','B','B','B','B','B'])
Down = Cube(['R','R','R','R','R','R','R','R','R'])
Back = Cube(['Y','Y','Y','Y','Y','Y','Y','Y','Y'])

Main = Cube([1,2,3,4,5,6,7,8,9])
Main.start(Up,Left,Front,Right,Back,Down)

```