# CodeSquad

## step2
## 평면 큐브 구현하기

```python
import copy

class Cube:
    
    # 3x3 큐브 값 초기화하기
    def __init__(self):

        self.total = ['R','R','W','G','C','W','G','B','B']
        self.rows = []
        self.temp = []

    def make_rows(self):

        self.rows.clear()
        index = 0

        for i in range(3):
            self.rows.append(self.total[index:index+3])
            index += 3

    # 큐브 한쪽면 출력하기
    def print_one_side(self):

        self.make_rows()

        for i in range(3):
            for j in range(3):
                print(self.rows[i][j], end = " ")
            print()

    # 큐브게임 시작하기
    def start(self):

        self.print_one_side()
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
                # 함수 실행 전, 현재의 total을 temp로 복사한다.
                self.temp = copy.deepcopy(self.total)
                func()

                # 함수를 실행한 후 전체 출력
                self.print_one_side()
                print()

    def UpDirLeft(self):

        self.total[0],self.total[1],self.total[2] = self.temp[1],self.temp[2],self.temp[0]

    def UpDirRight(self):

        self.total[0], self.total[1], self.total[2] = self.temp[1], self.temp[2], self.temp[0]

    def RightDirUp(self):

        self.total[2], self.total[5], self.total[8] = self.temp[5], self.temp[8], self.temp[2]

    def RightDirDown(self):

        self.total[2], self.total[5], self.total[8] = self.temp[8], self.temp[2], self.temp[5]

    def LeftDirDown(self):

        self.total[0], self.total[3], self.total[6] = self.temp[6], self.temp[0], self.temp[3]

    def LeftDirUp(self):

        self.total[0], self.total[3], self.total[6] = self.temp[3], self.temp[6], self.temp[0]

    def BottomDirRight(self):

        self.total[6], self.total[7], self.total[8] = self.temp[8], self.temp[6], self.temp[7]

    def BottomDirLeft(self):

        self.total[6], self.total[7], self.total[8] = self.temp[7], self.temp[8], self.temp[6]

c1 = Cube()
c1.start()

```