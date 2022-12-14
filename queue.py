# %%
# queue size 입력 받음
# queue size 만큼 빈 리스트 생성
# 1. enQueue() -> 큐에 넣을 자료 입력하는 함수 생성
# 2. deQueue() -> 큐에 가장 처음에 넣은 자료 꺼냄, 꺼낸 위치의 자료에는 None 입력
# 3. peekQueue() -> 큐에서 빼낼 자료 확인
# 큐의 가장 처음 위치는 front, 마지막 위치는 rear으로 설정 -> top=rear=-1

# %%
def menu_prt():
    print(' 1. 데이터 삽입 ')
    print(' 2. 데이터 추출 ')
    print(' 3. 처음 데이터 조회  ')  
    print(' 4. 큐 데이터 조회  ')  
    print(' 9. 프로그램 종료 ')  
    print('==================================')    
    print('선택 > ',end='')
    menu = input()
    return menu

# %%
def creat_que():
    global QUEUE, SIZE, FRONT, REAR
    for _ in range(SIZE):
        QUEUE.append(None)

def queue_is_empty():
    global QUEUE, SIZE, FRONT, REAR
    if FRONT == REAR:
        return True
    else:
        return False

def queue_is_full():
    global QUEUE, SIZE, FRONT, REAR
    if (REAR == SIZE - 1):
        return True
    else:
        return False

# %%
def enQueue():
    global SIZE, QUEUE, FRONT, REAR
    if queue_is_full():
        print('큐가 꽉 참')
        return
    REAR += 1
    QUEUE[REAR] = input('자료 입력 > ')

def deQueue():
    global SIZE, QUEUE, FRONT, REAR
    if queue_is_empty():
        print('큐가 비어 있음')
        return None
    FRONT += 1
    data = QUEUE[FRONT]
    print("큐의 처음 자료: ", QUEUE[FRONT])
    QUEUE[FRONT] = None

    # 빈 배열의 자리로 뒤에 있는 데이터 이동
    for i in range(FRONT + 1, SIZE):
        QUEUE[i-1] = QUEUE[i]
        QUEUE[i] = None
    FRONT -= 1
    REAR -= 1
    return data

def peekQueue():
    global SIZE, QUEUE, FRONT, REAR
    if queue_is_empty():
        print('큐에 자료 없음')
        return None
    print(QUEUE[FRONT+1])

def printInfo():
    global SIZE, QUEUE, FRONT, REAR
    print(f'큐 사이즈:{SIZE}, 현재 큐 정보:{QUEUE}, FRONT:{FRONT}, REAR:{REAR}')

# %%
FRONT = REAR = -1
SIZE = int(input('큐 사이즈 입력 >'))
QUEUE = []
creat_que()

while True:
    menu = menu_prt()
    if menu == '1':
        enQueue()
    elif menu == '2':   
        deQueue()
    elif menu == '3':
        peekQueue()
    elif menu == '4':
        printInfo()
    elif menu == '9':
        break


