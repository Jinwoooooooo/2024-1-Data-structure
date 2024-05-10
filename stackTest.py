from stack import *
from queue2 import *

st = Stack()

# 괄호 매칭 점검 함수
# 반환값: 매칭에 문제가 없으면 True, 문제가 있으면 오류 메시지 출력하고 False 반환.
pleft = "(<{["
pright = ")>}]"
pairs = "(){}[]<>"

def checkParenthese(st):
    #괄호 매칭에 활용할 스택을 하나 생성한다.
    stack = Stack()

    #입력 문자열 st에서 글자 하나씩 차례대로 가져와서 처리한다.
    for item in st:
        if item in pleft:       #현재 글자가 왼쪽 괄호 문자이면
            stack.push(item)        #스택에 저장한다.
        elif item in pright:    #현재 글자가 오른쪽 괄호 문자이면
            top = stack.pop()       #스택의 값을 하나 꺼낸다.
            if (top + item) in pairs: #현재 문자와 스택의 값이 서로 매칭이 되면
                continue            #입력 문자열의 다음 글자 확인하러 이동
            else:               #현재 문자와 서로 매칭이 되지 않았으면
                print("매칭 오류 발생: ({}, {})".format(top, item))
                return False
        else:                   #괄호 문자가 아니면
            continue                #다음 입력문자 처리하러 이동


    #for 문이 완료되면 입력 문자 처리가 모두 끝났다는 말이 되므로
    #스택을 체크한다.
    if stack.isEmpty(): #스택이 비었으면 괄호 매칭이 완료되었다는 뜻.
        return True
    else:
        print("매칭 되지 않은 왼쪽 괄호가 남음.")
        return False

#=========================================================
#수식 문자열(괄호 포함)을 입력받아 연산자(+, -, *, /), 괄호("()"), 피연산자 등으로
#구분하여 토근 리스트로 만들어 반환한다.
def toTokens(strInput):
    tokens = []
    current_token = ''

    for char in strInput:
        if char in ['+', '-', '*', '/']:
            # 연산자일 경우 현재 토큰을 추가하고 연산자도 추가.
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)
        elif char in ['(', ')']:
            # 괄호일 경우 현재 토큰을 추가하고 괄호도 추가.
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)
        else:
            # 피연산자일 경우 현재 토큰에 추가.
            current_token += char
    
    # 마지막으로 현재 토큰을 추가.
    if current_token:
        tokens.append(current_token)
    
    return tokens

#=========================================================
#중위표기법으로 된 수식 문자열을 입력받고
#   후위표기법으로 변환된 Queue를 반환한다.
def infix2Postfix(strInput):
    ops = "+-*/"
    priority = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1, ")": 1}
    
    #중위표기법 문자열을 토근 단위로 구분한다.
    tokenList = toTokens(strInput)
    #변환에 사용할 스택과 큐(출력용)를 생성한다.
    stack = Stack()
    queue = Queue()
    
    #tokenList에서 하나씩 차례대로 가져와서 처리한다.
    while tokenList:    #tokenList에 항목이 남이 있으면 반복한다.
        token = tokenList.pop(0)    #맨 앞의 항목을 하나 가져온다.
        if token.isdigit():         #token이 피연산자이면
            queue.add(token)         #Queue에 출력한다.
        elif token == "(":          #token이 왼쪽 괄호이면
            stack.push(token)           #stack에 저장
        elif token == ")":          #token이 오른쪽 괄호이면
            while stack.peek() != "(":  #stack에서 왼쪽 괄호를 만날 떄까지
                queue.add(stack.pop())  #pop하여 바로 출력(queue에)
            stack.pop()             #스택의 맨 위에 있는 왼쪽 괄호는 버린다.
        else:                       #연산자의 경우
            if stack.isEmpty():     #만일, 스택이 비어있는 경우
                stack.push(token)       #스택에 현재 연산자(token)를 저장한다.
            else:
                while not stack.isEmpty():
                    if priority[stack.peek()] >= priority[token]:   #스택에서 현재 연산자의 우선순위보다 낮은 연산자를 만날 때까지
                        queue.add(stack.pop())                          #스택에서 꺼내어 출력한다.
                    else:
                        break
                stack.push(token)   #현재 연산자는 스택에 저장한다.
    #입력 토근들을 모두 처리한 후에 스택에 남아 있는 것들을 모두 출력한다.
    while not stack.isEmpty:    #스택이 비어있지 않으면 
        queue.add(stack.pop())

    #최종 결과물(후위 표기법 순서로 저장된 Queue)을 반환한다.
    return queue
#=========================================================
#스택 계산기 (stack calculator)
#입력: 후위 표기법으로 정리된(토큰들로 구성된) queue
#출력: 계산결과값(number)
#=========================================================
def stackCalc(q):
    stack = Stack() #계산용 스택 생성

    ops = "+-*/"
    
    while not q.isEmpty():
        q.remove()
        if token.isdigit():
            q.pop()
            q.pop()
        
        
#=========================================================

print(infix2Postfix("23 + 34 * 123"))
# teststr = "(<>{[{]})"
# print(checkParenthese(teststr))

# print(toTokens("323*(4+5)-6/2"))

# l[0] in "({["

# st.push(100)
# st.showList()
# st.push(200)
# st.showList()
# print("Stack Pop => {}".format(st.pop()))
# st.showList()
# print("Stack Peek => {}".format(st.peek()))
# st.showList()