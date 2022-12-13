# %%
# 단순 링크드 리스트
# 학생들의 이름과 성적을 입력 받아 성적순으로 클래스의 data에 딕셔너리로 저장
class Student:
    def __init__(self) -> None:
        self.data = {}
        self.link = None

# 성적순으로 링크드 리스트 작성
# insert_node() 수정
# 1. 학생 정보 입력
# 2. 학생 정보 삭제(이름 입력)
# 3. 학생 정보 검색(이름 입력)
# 4. 전체 학생의 정보 출력(등수도 출력)
# 5. 프로그램 종료

# %%
def menu():
    print()
    print()
    print('%17s'% ('학생 관리 프로그램'))
    print('='*30)
    print('1. 학생 정보 입력')
    print('2. 학생 정보 삭제')
    print('3. 학생 정보 검색')
    print('4. 전체 학생 정보 출력')
    print('5. 프로그램 종료')
    print('='*30)
    
    menu_btn = int(input('선택> '))
    return menu_btn

# %%
def insert_student():
    global head
    name = input('이름 입력> ')
    score = int(input('점수 입력> '))
    node = Student()
    node.data[name] = score

    # 비어있을 때 가장 앞에 넣음
    if not head:
        head = node
        return

    temp = head
    # 비어있지 않을때
    while True:
        # 마자막 노드 뒤에 삽입할 때
        if not temp.link:
            if node.data[name] < temp.data[list(temp.data.keys())[0]]:
                head = node
                node.link = temp
            else:
                temp.link = node
            return

        # 중간에 삽입할 때
        # 새로 추가할 학생의 성적이 기존의 학생 성적보다 크다면(다음 비교)
        if node.data[name] > temp.data[list(temp.data.keys())[0]]:
            prev = temp
            temp = temp.link
        # 성적이 같다면(뒤에 삽입)
        elif node.data[name] == temp.data[list(temp.data.keys())[0]]:
            node.link = temp.link
            temp.link = node
            return
        # 기존 학생의 성적이 더 크다(앞에 삽입)
        else:
            prev.link = node
            node.link = temp
    print(f'{name} 추가 완료')

# %%
def delete_student():
    global head
    name = input('삭제할 학생 이름을 입력하세요> ')

    temp = head
    
    while True:
        # 검색한 이름을 찾으면
        if name == list(temp.data.keys())[0]:
            # 가장 앞에 있을 경우
            if head == temp:
                head = temp.link
                del(temp)
                return
            # 마지막에 있을 경우
            elif not temp.link:
                prev.link = None
                del(temp)
                return
            # 중간에 있을 경우
            else:
                prev.link = temp.link
                del(temp)
                return
            
        prev = temp
        temp = temp.link
    print(f'{name} 삭제 완료')

# %%
def find_student():
    global head
    name = input('검색할 학생의 이름을 입력하세요> ')

    temp = head
    
    while head:
        # 학생 찾음
        if name == list(head.data.keys())[0]:
            # 학생 출력
            print(head.data)
        head = head.link
    head = temp

# %%
def print_student():
    global head
    temp = head
    while head:
        print(head.data)
        head = head.link
    head = temp

# %%
head = None
while True:
    btn = menu()
    if btn == 1:
        insert_student()
    elif btn == 2:
        delete_student()
    elif btn == 3:
        find_student()
    elif btn == 4:
        print_student()
    else:
        print('프로그램 종료')
        break


