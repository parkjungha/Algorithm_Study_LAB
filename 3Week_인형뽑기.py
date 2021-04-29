def solution(board, moves):
    answer = 0
    basket = []
    for m in moves:
        for i in range(len(board)):
            selected = board[i][m-1]
            if selected != 0:
                if basket and basket[-1] == selected:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(selected)
                board[i][m-1] = 0
                break
    return answer