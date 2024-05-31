steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def make_block(table, sx, sy, flag):

    stack = [(sx, sy)]
    blocks = []
    while stack:
        x, y = stack.pop()
        blocks.append((x, y))
        table[x][y] = -1
        for tx, ty in steps:
            if (
                0 <= x + tx < len(table)
                and 0 <= y + ty < len(table)
                and table[x + tx][y + ty] == flag
            ):
                stack.append((x + tx, y + ty))

    min_x = min(x for x, _ in blocks)
    min_y = min(y for _, y in blocks)
    max_x = max(x for x, _ in blocks)
    max_y = max(y for _, y in blocks)
    return [
        [1 if table[i][j] == -1 else 0 for j in range(min_y, max_y + 1)]
        for i in range(min_x, max_x + 1)
    ]


def rotate(block):
    n, m = len(block), len(block[0])
    return [[block[i][m - 1 - j] for i in range(n)] for j in range(m)]


def solution(game_board, table):

    empty_blocks = [
        make_block(game_board, i, j, 0)
        for i in range(len(game_board))
        for j in range(len(game_board))
        if game_board[i][j] == 0
    ]

    blocks = [
        make_block(table, i, j, 1)
        for i in range(len(table))
        for j in range(len(table))
        if table[i][j] == 1
    ]
    answer = 0

    is_filled = [False for _ in empty_blocks]
    is_used = [False for _ in blocks]

    for empty_idx, empty_block in enumerate(empty_blocks):
        for block_idx, block in enumerate(blocks):
            if is_filled[empty_idx]:
                break
            if is_used[block_idx]:
                continue
            for _ in range(4):
                if (
                    len(block) == len(empty_block)
                    and len(block[0]) == len(empty_block[0])
                    and all(
                        block[i][j] == empty_block[i][j]
                        for i in range(len(block))
                        for j in range(len(block[0]))
                    )
                ):
                    answer += sum(cell for row in block for cell in row)
                    is_filled[empty_idx] = True
                    is_used[block_idx] = True
                    break
                block = rotate(block)

    return answer
