"""
리트코드에도 스도쿠 풀이 문제가 있길래 37.Sudoku Solver 를 먼저 풀고,
이때 사용했던 코드에 INPUT/OUTPUT 부분을 추가하여 제출하였는데 오답판정을 받았다.
확인해보니 단일해가 보장된 리트코드의 문제와 달리, 백준의 문제는 복수해 중 사전식으로 앞서는 것을 출력해야하는데
이를 고려하지 않았기 떄문인 것으로 보인다. 맘같아선 기존 코드의 알고리즘으로 풀고 싶은데 아직은 방법을 모르곘다.
시간이 늦어서 며칠 더 고민해 보고 그래도 해결이 안되면 처음부터 새로 풀어보려고 한다.
"""


# 각 빈칸에 들어갈 수 있는 숫자를 리스트 안에 set 형태로 저장하고 solve()를 호출하는 함수.
def play_sudoku(board):
    # {1, 2, 3, 4, 5, 6, 7, 8, 9}로 이루이진 9x9리스트 possibilities 생성
    possibilities = [[{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            # 만약 빈칸이 아니라면 비워줌.
            if board[row][col] != 0:
                possibilities[row][col] = None
    for row in range(9):
        for col in range(9):
            # 이미 채워져 있는 칸을 통해 possibilities의 원소들 수정
            if board[row][col] != 0:
                change_possibilities(possibilities, board[row][col], row, col, False)
    solve(possibilities, board)


# 스도쿠를 푸는 함수
def solve(possibilities, board):
    # 가장 채우기 쉬운 칸(가능한 숫자가 적은 칸)을 먼저 찾음
    target_row, target_col = find_minimum_possibilities(possibilities)
    # 빈칸이 없다면 True 반환
    if target_row == -1:
        return True
    # 빈칸에 들어갈 수 있는 숫자가 없다면(불가능한 스도쿠라면) False 반환
    if len(possibilities[target_row][target_col]) == 0:
        return False

    possible_nums = possibilities[target_row][target_col]
    possibilities[target_row][target_col] = None

    # 목표칸에 들어갈 수 있는 숫자를 차례대로 넣어봄
    for digit in possible_nums:
        board[target_row][target_col] = digit
        # board[target_row][target_col]에 digit 를 넣었을때 영향을 받는 possibilities의 원소의 인덱스 저장.
        points = change_possibilities(possibilities, digit, target_row, target_col, add=False)
        # 재귀호출. 무사히 재귀를 마쳤다면 True 반환.
        if solve(possibilities, board):
            return True
        # 만약 재귀 과정 도중 불가능한 스도쿠를 만들었다면 digit를 넣었던 작업을 취소함
        change_possibilities(possibilities, digit, target_row, target_col, points=points)
    # 모든 숫자에 대해 재귀를 마치지 못했다면 이 칸은 채울 수 없다
    board[target_row][target_col] = 0
    # possibilities를 원래대로 되돌림
    possibilities[target_row][target_col] = possible_nums
    return False


# 지정한 위치([r][c])에 특정 숫자(digit)가 들어 갈 때의 작업을 하는 함수.
# add : m의 원소에 digit 를 다시 넣는 작업을 할지의 여부 작업을 해 줄 위치를 지정한 points 를 같이 입력
# removed_points : 목표로 한 [r][c]에 digit 가 들어갔을 때, 영향을 받는 칸들을 저장.
def change_possibilities(possibilities, digit, row, col, add=True, points=None):
    removed_points = []

    # add 의 값에 따라 m의 원소에 change 를 추가/제거 해줌
    def maybe_change(r, c, change):
        d = possibilities[r][c]
        if d is not None:
            # [r][c]에 넣을 수 있는 숫자 집합에 change 를 추가
            if add:
                d.add(change)
            # [r][c]에 넣을 수 있는 숫자 집합에서 change 를 제거
            elif change in d:
                d.remove(change)
                removed_points.append((r, c))

    if points is not None:
        for p in points:
            maybe_change(p[0], p[1], digit)
        return

    # 각 열과 행에 대해 작업 반복
    for i in range(9):
        maybe_change(row, i, digit)
        maybe_change(i, col, digit)

    # 각 3x3 행렬에 대해 작업 반복
    for i in range(3):
        for j in range(3):
            maybe_change(row // 3 * 3 + i, col // 3 * 3 + j, digit)

    return removed_points


# 빈 칸에 넣을 수 있는 숫자가 가장 적은 곳의 좌표를 반환하는 함수
def find_minimum_possibilities(possibilities):
    minimum = 10
    min_row = min_col = -1
    for row in range(9):
        for col in range(9):
            if possibilities[row][col] is not None and len(possibilities[row][col]) < minimum:
                minimum = len(possibilities[row][col])
                min_row, min_col = row, col
    return min_row, min_col


sudoku_board = []

for _ in range(9):
    line = list(map(int, input().split()))
    sudoku_board.append(line)

play_sudoku(sudoku_board)

for line in sudoku_board:
    print(" ".join(map(str, line)))
