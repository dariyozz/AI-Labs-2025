def count_mines(field, row, col):
    n = len(field)
    mine_count = 0
    for i in range(max(0, row - 1), min(n, row + 2)):
        for j in range(max(0, col - 1), min(n, col + 2)):
            if field[i][j] == '#':
                mine_count += 1
    return mine_count

def minesweeper(field):
    return [
        [
            str(count_mines(field, i, j)) if cell == '-' else '#'
            for j, cell in enumerate(row)
        ]
        for i, row in enumerate(field)
    ]

def main():
    n = int(input().strip())
    field = [input().strip().split() for _ in range(n)]

    result = minesweeper(field)

    for row in result:
        print('   '.join(row))

if __name__ == "__main__":
    main()