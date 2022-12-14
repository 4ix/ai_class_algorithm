# %%
# stack size 입력 받음
# stack size 만큼 빈 리스트 생성
# 1. push() -> 스택에 넣을 자료 입력하는 함수 생성
# 2. pop() -> 스택에 가장 나중에 넣은 자료 꺼냄, 꺼낸 위치의 자료에는 None 입력
# 3. list() -> 스택 자료 출력
# 스택의 가장 마지막 위치는 top 으로 설정 -> 초기값은 top = -1

# %%
def menu_prt():
    print(' 1. 자료입력 -> ')
    print(' 2. 자료삭제 ')
    print(' 3. 전체 자료 조회  ')  
    print(' 4. 마지막 자료 조회  ')  
    print(' 9. 프로그램 종료 ')  
    print('==================================')    
    print('선택 > ',end='')
    menu = input()
    return menu

# %%
def creat_stack():
    global STACK, SIZE
    for _ in range(SIZE):
        STACK.append(None)

def stack_is_empty():
    if TOP == -1:
        return True
    else:
        return False

def stack_is_full():
    if TOP == len(STACK) - 1:
        return True
    else:
        return False


# %%
def push():
    global TOP
    if stack_is_full():
        print('스택에 넣을 위치 없음')
        return
    TOP += 1
    STACK[TOP] = input('자료 입력 > ')

def pop():
    global TOP    
    if stack_is_empty():
        print('스택에 자료 없음')
        return
        
    print("스택의 마지막 자료: ", STACK[TOP])
    data = STACK[TOP]
    STACK[TOP] = None
    TOP -= 1
    return data

def peek():
    if stack_is_empty():
        print('스택에 자료 없음')
        return None
    print(STACK[TOP])

def stack_list():
    if stack_is_empty():
        print('스택에 자료 없음')
        return

    for i in range(TOP+1):
        print(f'스택의 {i}의 값 -> {STACK[i]}')

# %%
TOP = -1
SIZE = int(input('스택 사이즈 입력 >'))
STACK = []
creat_stack()

while True:
    menu = menu_prt()
    if menu == '1':
        push()
    elif menu == '2':   
        pop()
    elif menu == '3':
        stack_list()
    elif menu == '4':
        peek()
    elif menu == '9':
        break

# %%
content = '''
진달래꽃
나 보기가 역겨워 
가실 때에는
말없이 고이 보내드리오리다.
'''


