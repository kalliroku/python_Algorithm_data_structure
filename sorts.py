# 병합 정렬 - 잘게 쪼개서 다시 합치면서 정렬 진행

def merge_sort(arr):
    if len(arr) < 2:
        return arr

# 가운대를 기준으로 잘게 쪼개기
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
# 쪼갠 조각 정렬하면서 합치기
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
# 정렬된 조각들이 9, 10 line으로 return
# ----------------------------------------------------------------------

# quick_sort
def quick_sort(arr):
# 2. 1짜리 리스트를 건드리지 않고 그대로 리턴(종료)<-틀렸어.
    def sort(low, high):
        if high <= low:
            return
# 3. 1차 분할 정렬
        mid = partition(low, high)
# 5. 1차 mid(1차의 pivot의 인덱스) 중심으로 둘로 나눠서 sort함수 재귀
        sort(low, mid - 1)
        sort(mid, high)
# 4. 임의의 pivot을 중심으로 0~피봇까지, high-> 피봇까지 탐색하다가
# pivot 값보다 크거나 작은 값을 만나면 두 값을 스왑
# low 와 high 인덱스가 만날 때 까지 진행
    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)
# 1. 리스트의 길이를 갖고 리턴


# counting sort 구현(메모리를 적게 먹을까?)
def counting_sort(array, max):
    # counting array 생성
    counting_array = [0] * (max + 1)

    # counting array에 input array내 원소의 빈도수 담기
    for i in array:
        counting_array[i] += 1

    # counting array 업데이트.
    for i in range(max):
        counting_array[i + 1] += counting_array[i]

    # output array 생성
    output_array = [-1] * len(array)

    # output array에 정렬하기(counting array를 참조)
    for i in array:
        output_array[counting_array[i] - 1] = i
        counting_array[i] -= 1
    return output_array
