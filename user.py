#!/usr/bin/env python
# coding: utf-8

# In[3]:


## 헤드 사용버전 ##


## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes():
    global head, tail, current, pre
    current = head                     
    if current == None:                 # 노드에 데이터가 하나도 없는 연결 리스트인 경우 반환
        return
    print(current.data, end=' ')        # 현재 노드 출력
    while current.link != None:         # 노드의 링크가 빌 때까지 출력
        current = current.link
        print(current.data, end=' ')
    print()

## 메뉴 표시 ##
def menu_print():
    pass

## 노드 삽입 ##
def add_node():
    global head, tail, current, pre
    while True:
        name = input("이름 >>> ")
        if name == '':
            printNodes()
            break
        e_mail = input("이메일 >>> ")
        node = Node()
        node.data = [name, e_mail]

        if not head: # 첫 노드 삽입
            head = node
            tail = node
            memory.append(node)
            printNodes()
        elif head.data[1] > e_mail:
            node.link = head
            head = node
            memory.append(node)
            printNodes()
        else:
            current = head
            while True:
                if current.link != None: # 중간 노드 삽입 
                    pre = current
                    current = current.link
                    if pre.data[1] < e_mail:
                        node.link = current
                        pre.link = node
                        memory.append(node)
                        printNodes()
                        break
                else:
                    current.link = node # 마지막 노드 삽입
                    tail = node
                    memory.append(node)
                    printNodes()
                    break
            
        
    
## 노드 삭제 ##
def del_node():
    pass


# In[4]:


## 전역 변수 선언 부분 ##
memory = []                             # 생성할 노드 저장할 메모리 준비
head, current, pre, tail = None, None, None, None   

add_node()

