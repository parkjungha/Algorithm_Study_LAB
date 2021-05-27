import heapq
def solution(operations):
    minheap = [] # 최소힙을 위한 리스트 만들기
    for o in operations:
        op,num = o.split()
        
        if op == 'I': # 삽입
            heapq.heappush(minheap,int(num))
            
        elif minheap and op == 'D': # 삭제
            
            if num == '1': # 최댓값 
                minheap.remove(max(minheap))
                
            elif num == '-1': # 최소값
                heapq.heappop(minheap)
                
    if not minheap: # 비어있으면
        return [0,0]
    
    else: # 아니면
        return [max(minheap),heapq.heappop(minheap)]
