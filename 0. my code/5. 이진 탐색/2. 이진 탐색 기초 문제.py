문제1: 떡볶이 떡 만들기 
    동빈이는 여행가신 부모님을 대신해서 떡집 일을 하기로 했다. 오늘은 떡볶이 떡을 만드는 날이다.
    동빈이네 떡볶이 떡은 길이가 일정하지 않다. 대신에 한봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다. 
    절단기에 높이(H)를 지정하면 줄지어진 떡을 한번에 절단한다. 
    높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고 낮은 떡은 잘리지 않는다.
    예를 들어 높이가 19,14,10,17CM인 떡이 나란히 있고 절단기 높이를 15CM로 지정하면 자른 뒤 떡의 높이는 15,14,10,15CM가 될 것이다. 
    잘린 떡의 길이는 차례대로 4,0,0,2CM이다. 손님은 6CM만큼의 길이를 가져간다. 
    손님이 왔을 때 요청한 총 길이가 M일때, 적어도 M 만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하라.
 
N,M = map(int, input().split())
array = list(map(int, input().split()))

start = 0 # 시작점
end= max(array) # 끝점 
result = 0 # 높이

# 이진탐색-반복
while (start < = end):
  total = 0 
  mid = (start+end)//2
  for x in array:
    if x > mid:
      total += x-mid # 잘린 떡의 길이
  if total < M:
    end = mid-1
  else:
    result = mid # 손님이 원하는 것만큼 떡이 잘렸으니까 최대한 덜 잘랐을때가 정답이므로, 여기에서 result기록
    start = mid+1

print(result)
     
문제2: 정렬된 배열에서 특정 수의 개수 구하기
    N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어있다.
    이때 이 수열에서 x가 등장하는 횟수를 계산하라. 
    예를 들어 수열{1,1,2,2,2,2,3}이 있을 때 x=2라면, 현재 수열에서 값이 2인 원소가 4개 이므로 4를 출력한다. 
    단, 이문제는 시간복잡도O(logN)으로 알고리즘을 설계하지 않으면 시간초과 판정을 받는다. 

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a,left_value)
  return right_index - left_index

N, X = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x,x) # [x,x]범위안에 있는 데이터의 개수 계산
if count == 0 :
  print(-1)
else: 
  print(count)
