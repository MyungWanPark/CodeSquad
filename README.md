# CodeSquad

## step1 단어 밀어내기 구현하기

**동작 단계**
1. 단어, 숫자, 방향을 입력받는다. 
2. 방향의 대,소문자를 통일시킨다.
3. 숫자가 단어의 길이를 넘어가면 다시 반복되므로 숫자를 단어의 길이만큼 나눈 나머지를 숫자에 대입한다.
(양수, 음수 구분하여 적용하였다.)
4. 숫자가 음수일 경우 방향이 바뀐다.
5. left와 right만 있다는 가정하에 밀어내기를 구현한다.
6. 왼쪽 방향으로 밀어내는 경우,잘린 후부터 먼저 입력하고 뒤에 잘린 부분을 붙인다.
7. 오른쪽 방향으로 밀어내는 경우, 잘리는 만큼 먼저 입력하고 나머질 붙인다.

 
```python
# 단어, 숫자, 방향 입력받기
word,n,direct = input().split()
n = int(n)

# 방향 문자 통일
if direct == 'L' or direct == 'l':
    direct = 'left'
else:
    direct = 'right'

# n이 word길이를 넘어가면 순환되어서 같은 단어가 되므로 단어 길이로 나눈 나머지만 사용한다.
# n이 양수일때
if n > 0:
    n = n % len(word)
else:
    # n이 음수이면 먼저 양수로 바꿔주고, 순환되는 길이만큼 제외한 후, 다시 부호를 바꿔준다.
    n = (-1) * ((-1 * n) % len(word))

#n이 음수일때 방향이 바뀐다.
if n < 0:

    if direct == 'left':
        direct = 'right'
    else:
        direct = 'left'
    # n이 음수일때 방향을 바꿔줬으니 n을 양수로 바꿔준다.
    n = (-1) * n


# 왼쪽 방향으로 밀어내는 경우
if direct == 'left':
    for i in range(n, len(word)):
        print(word[i], end = '')

    for j in range(n):
        print(word[j], end = '')
# 오른쪽 방향으로 밀어내는 경우
else:
    for i in range(len(word)-n, len(word)):
        print(word[i], end = '')
    for j in range(len(word)-n):
        print(word[j], end = '')
```