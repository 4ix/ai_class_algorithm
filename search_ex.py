# %%
array = [ ['어린왕자', '쌩떽쥐베리'],['이방인', '까뮈'],['부활', '톨스토이'],['신곡', '단테'],['돈키호테', '세브반테스'],['동물농장', '조지오웰'],['데미안','헤르만헤세'],['파우스트', '괴테'],['대지', '펄벅'] ]
# 1. 작가명 색인표 생성 -> 작가명, 책이름, 인덱스
# 2. 작가명 정렬(bubble_sort)
# 3. 작가명 검색(이진 검색)

index = []

for i in range(len(array)):
    index.append([array[i][1], array[i][0], i]) # 1. 작가명 기준 인덱스 생성

print('1. 작가명 인덱스 생성 -> ', index)
print()

def bubble_sort(array):
    n = len(array)
    cnt = 0
    for end in range(n-1, 0, -1): # 사이클 돌리는 영역 (반복 횟수)
        sw = False
        for cur in range(0, end): # 0 부터 end 까지
            cnt+= 1
            if array[cur] > array[cur+1]: # 2. 작가명 기준 오름차순 정렬
                array[cur], array[cur+1] = array[cur+1], array[cur]
                sw = True
        if not sw:
            break
    return array, cnt

array, cnt = bubble_sort(index)
print('2. 작가명 오름차순 정렬 -> ', array)
print()

# bianry serach
def binarySearch(array, data):
    global cnt, f_name, f_title, f_index
    start = 0
    end = len(array)-1
    while start <= end:
        cnt += 1
        mid = (start+end)//2 # 중앙위치
        if data == array[mid][0]:
            f_name = array[mid][0]
            f_title = array[mid][1]
            f_index = array[mid][2]
            return mid
        elif data > array[mid][0]:
            start = mid + 1
        else:
            end = mid -1
    return -1

# print(array[0][0]) #작가명
# print(array[0][1]) #책이름
# print(array[0][2]) #인덱스

while True:
    data = input('찾을 작가명 입력 >')
    if data == 'q':
        break

    result = binarySearch(array, data)
    if result == -1:
        print('자료 없음')
    else:
        print(f'{f_name}의 {f_title}는 {f_index} 에 있습니다.')
    print('##', cnt, '회 검색함')
    break



