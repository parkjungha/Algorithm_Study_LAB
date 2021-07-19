def check(answer):
    for x,y,what in answer:

        if what == 0: # 기둥
            # 1 바닥 위에 있거나 2 보의 한쪽 끝 부분 위에 있거나 3 다른 기둥 위에 있어야 함
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            else:
                return False
        
        elif what == 1: # 보
            # 1 한쪽 끝 부분이 기둥 위에 있거나 2 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for f in build_frame:
        x, y, what, how = f    

        if how == 1: # 설치
            answer.append([x,y,what])
            if check(answer) == False: # 만약 작업을 수행한 결과가 조건을 만족하지 않는다면 해당 작업은 무시
                answer.remove([x,y,what])
        
        else: # 삭제
            answer.remove([x,y,what])
            if check(answer) == False:
                answer.append([x,y,what])

    answer.sort()
    return answer

# 답지 안보고 생각해내기엔 어려웠는데 막상 풀이를 찾아보고 이해하고 나니까 쉬웠던 문제..... 