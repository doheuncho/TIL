"""
수정을 통해 pypy는 통과를 시켰다. 사전식 우선 조건을 맞추기 위해 target_row와 target_col을 찾는 함수를 수정했고,
그에따라 possibilities의 원소를 set으로 할 이유가 사라져(오히려 손해다.) [list, int]식으로 수정했다.
중간 최단시간은 pypy기준 4500ms 정도였는데, 더 빠르게 만들기 위해 로직을 추가했더니 오히려 더 느려졌다.(그래도 로직은 더 깔끔해졌다.)
possibilities를 각 칸에 대하여 만들지않고 행, 렬, 3x3사각형에 대해 만들면 더 빨라질것도 같다.
근데 그러면 사람이 스도쿠를 푸는것을 따라한다는 처음 취지랑 맞지 않기도하고, 이미 이 문제에만 12시간 넘게 시간을 사용해서 이쯤하려한다.
인간이 스도쿠를 푸는 형태로 풀고 싶었는데 생각보다 인간은 비효율적이였다.(애초에 사전식으로 먼저오는 스도쿠를 푸는행위가 인간이 할짓이 아니다.)
"""
# 메모리 : 167020 KB
# 시간 : 6016 ms
# possibilities를 초기화하고 solve를 호출하는 함수.
def play_sudoku(board):
    # [[각 숫자가 각 인덱스에 들어갈 수 있는지 여부], 해당 자리에 넣을 수 있는 숫자 개수] 로 이루이진 9x9리스트 possibilities 생성
    possibilities = [[[[0, 1, 1, 1, 1, 1, 1, 1, 1, 1], 9] for _ in range(9)] for _ in range(9)]
    first_row = first_col = 0
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                possibilities[row][col] = None
    for row in range(8, -1, -1):
        for col in range(8, -1, -1):
            if board[row][col] != 0:
                change_possibilities(possibilities, board[row][col], row, col, False)
                first_row, first_col = row, col
    solve(possibilities, first_row, first_col, board)


# 스도쿠를 푸는 함수
def solve(possibilities, target_row, target_col, board):
    # 숫자를 채울칸을 찾음(우선순위: 들어갈 수 있는 숫자가 1개인 칸 -> 가장 앞에있는 칸)
    target_row, target_col = find_unique_possibilities(possibilities, target_row, target_col)
    # 스도쿠 판에 빈칸이 남아있지 않은 경우(완성을 한 경우)
    if target_row == -1:
        return True
    # 완성을 못했는데 남아있는 빈 칸에 넣을 수 있는 숫자가 없는 경우
    if possibilities[target_row][target_col][1] == 0:
        return False

    # 숫자를 넣기 위해 기존 possibilities[target_row][target_col]의 원소를 저장하고 그 위치의 값을 None으로 바꿔줌.
    possible_backup = possibilities[target_row][target_col]
    possibilities[target_row][target_col] = None

    for digit in range(1, 10):
        if possible_backup[0][digit] == 0:
            continue
        board[target_row][target_col] = digit
        points = change_possibilities(possibilities, digit, target_row, target_col, add=False)
        # 재귀호출을 통해 반복.
        if solve(possibilities, target_row, target_col, board):
            return True
        # 재귀를 탈출했다면(스도쿠 완성에 실패했다면) possibilities를 이전 단계로 복구함
        change_possibilities(possibilities, digit, target_row, target_col, points=points)

    # board와 possibilities를 이전상태로 되돌려준다.
    board[target_row][target_col] = 0
    possibilities[target_row][target_col] = possible_backup
    return False


# add가 True일 경우, points를 입력받아 points위치의 possibilities를 digit를 넣기 전으로 되돌려줌.
# add가 False일 경우, 주어진 row, col의 위치에 digit를 넣는 로직을 실행함.
def change_possibilities(possibilities, digit, row, col, add=True, points=None):
    removed_points = []

    # possibilities[r][c]의 위치에 change를 제거하거나(0) 추가하는(1) 작업을 실행. 만약 change를 제거했다면 제거한 위치를 removed_points에 저장해줌.
    def maybe_change(r, c, change):
        d = possibilities[r][c]
        if d is not None:
            if add:
                if d[0][change] == 0:
                    d[1] += 1
                d[0][change] = 1
            elif d[0][change] == 1:
                d[0][change] = 0
                d[1] -= 1
                removed_points.append((r, c))
    # 만약 되돌려주는 작업이라면 points의 인덱스를 따라 차례대로 롤백해줌.
    if add:
        for p in points:
            maybe_change(p[0], p[1], digit)
        return
    # 숫자를 넣는 작업이라면 digit를 (row, col)에 넣었을때 영향을 받는 possibilities 의 원소들을 변경함
    else:
        # 행&열
        for i in range(9):
            maybe_change(row, i, digit)
            maybe_change(i, col, digit)
        # 3x3 사각구역
        for i in range(3):
            for j in range(3):
                maybe_change(row // 3 * 3 + i, col // 3 * 3 + j, digit)

    return removed_points


# 넣을 수 있는 숫자가 1개인 칸의 좌표를 반환. 없다면 가장 앞에있는 좌표를 반환.
def find_unique_possibilities(possibilities, target_row, target_col):
    if possibilities[target_row][target_col] is not None:
        return target_row, target_col
    # 넣을 수 있는 숫자가 확정된 칸을 찾음
    for i in range(9):
        if possibilities[target_row][target_col] is not None and possibilities[target_row][i][1] == 1:
            return target_row, i
        if possibilities[target_row][target_col] is not None and possibilities[i][target_col][1] == 1:
            return i, target_col
    for i in range(3):
        for j in range(3):
            row, col = target_row // 3 * 3 + i, target_col // 3 * 3 + j
            if possibilities[target_row][target_col] is not None and possibilities[row][col][1] == 1:
                return row, col
    # 가장 앞에 있는 빈 칸을 찾음
    for row in range(9):
        for col in range(9):
            if possibilities[row][col] is not None:
                return row, col
    return -1, -1


sudoku_board = []

for _ in range(9):
    line = list(map(int, input()))
    sudoku_board.append(line)

play_sudoku(sudoku_board)

for line in sudoku_board:
    print("".join(map(str, line)))
