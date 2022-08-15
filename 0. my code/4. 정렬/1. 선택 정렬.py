정렬이란: 
 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말한다. 
 일반적으로 문제상황에 따라서 적절한 정렬알고리즘이 공식처럼 사용된다. 

선택 정렬: 
 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복.
 선택정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야한다.
 구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산횟수는 다음과 같다. 
 N + (N-1) + (N-2) + ... +2
 이는 (N^2 + N - 2)/2로 표현 할 수 있는데 빅오 표기법에 따라서 O(N^2)라고 작성한다. 
 
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    # 가장 작은 원소의 인덱스
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)

스와프
# 0 인덱스와 1 인덱스의 원소 교체하기
array = [3, 5]
array[0], array[1] = array[1], array[0]

print(array)
