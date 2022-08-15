순차 탐색:
  리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
이진 탐색:
  정렬되어 있는 리스트에서 탐색범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
  이진탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다. 
  이진탐색의 시간복잡도는 단계마다 탐색범위를 2로 나누는 것과 동일하므로 연산횟수는 log2 N에 비례
  따라서 이진탐색은 탐색범위를 절반씩 줄이며, 시간 복잡도는 O(log N)을 보장
파라메트릭 서치(Parametric Search):
  최적화문제를 결정문제(예 혹은 아니오)로 바꾸어 해결하는 기법
  예시: 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
  일반적으로 코딩테스트에서 파라메트릭 서치 문제는 이진탐색을 이용하여 해결할 수 있다.  
  
1-1. 이진탐색-재귀함수 이용
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid # 찾은 경우 중간점 인덱스 반환
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1) # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    else:
        return binary_search(array, target, mid + 1, end) # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

1-2. 이진탐색-반복문 이용
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

2. 파이썬 이진탐색 라이브러리
bisect_left(a,x): 정렬된 순서를 유지하면서 배열a에 x를 삽입할 가장 왼쪽 인덱스를 반환
bisect_right(a,x): 정렬된 순서를 유지하면서 배열a에 x를 삽입할 가장 오른쪽 인덱스를 반환

2-1. 값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a,left_value)
  return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a,4,4)) #값이 4인 데이터 개수 출력
print(count_by_range(a,-1,3)) #[-1,3] 범위에 있는 데이터 개수 출력

3. 순차탐색
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환 (인덱스는 0부터 시작하므로 1 더하기)
    return -1 # 원소를 찾지 못한 경우 -1 반환

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")  
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
