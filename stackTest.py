from stack import *
from queue2 import *

# 괄호 매칭 점검 함수
# 반환값: 매칭에 문제가 없으면 True, 문제가 있으면 오류 메시지 출력하고 False 반환.

pleft = "(<{["
pright = "]>})"
pairs = "()[]<>{}"

def checkParenthese(st):
    #괄호 매칭에 활용할 스택을 하나 생성한다.
    stack = Stack()

    #입력 문자열(st)에서 글자 하나씩 차례대로 가져와서 처리한다.
    for item in st:
        if item in pleft:           # 현재 글자가 왼쪽 괄호 문자이면
            stack.push(item)            # 스택에 저장한다.
        elif item in pright:        # 현재 글자가 오른쪽 괄호 문자이면
            top = stack.pop()           # 스택의 값(왼쪽 괄호)을 하나 꺼낸다.
            if (top + item) in pairs:   # 현재 문자와 스택의 값이 서로 매칭이 되면
                continue                   # 입력 문자열의 다음 글자 확인하러 이동.
            else:                       # 현재 문자와 서로 매칭이 되지 않았으면
                print("매칭 오류 발생: ({}, {})".format(top, item))
                return False
        else:                       # 괄호 문자가 아니면
            continue                    # 다음 입력문자 처리하러 이동
    
    # for 문이 완료되면 입력 문자 처리가 모두 끝났다는 말이 되므로
    # 스택을 체크한다. 
    if stack.isEmpty(): # 스택이 비었으면 괄호 매칭이 완료되었다는 뜻.
        return True
    else:
        print("매칭되지 않은 왼쪽 괄호가 남았음!!!")
        return False
#============================================================
# 수식 문자열(괄호 포함)을 입력받아 연산자(+,-,*,/), 괄호("()"), 피연산자 등으로
#   구분하여 토큰 리스트로 만들어 반환한다.
def toTokens(strInput):
    chList = list(strInput) # 문자열을 문자 단위로 모두 잘라서 리스트로 만든다.
    tokenList = []      # 분해된 토큰들을 모아서 반환할 리스트, 초기값은 빈 리스트
    numToken = ""          # 2이상의 문자열로 된 수를 모으기 위한 변수
    ops = "+-*/()"

    # 문자열에서 한 문자씩 가져와서 차례대로 처리한다.
    while chList:   # chList에 처리할 항목이 남아 있으면
        ch = chList.pop(0)          # chList의 맨 앞에 있는 글자를 가져온다.
        if ch in ops:               # 한 문자로 된 토큰(연산자, 괄호)이면 
            tokenList.append(ch)    #   반환할 변수 tokenList에 저장한다.
        elif ch.isdigit() or ch == ".":          # 현재 문자가 숫자이면
            numToken += ch          #   numToken 변수에 누적 시작
            while chList:           # chList에서 digit가 아닌 문자를 만날때까지 반복한다.
                if chList[0].isdigit() or chList[0] == ".": # chList의 첫 문자가 digit이면
                    numToken += chList.pop(0)   # 꺼내서 numToken에 누적시킨다.
                else:
                    break           # 숫자 누적처리를 중단하고 다음으로 넘어간다.
            tokenList.append(float(numToken))  # 그동안 누적시킨 number 문자열을 토큰으로 저장한다.
            numToken = ""           # 다음 수를 수집하기 위해 numToken 값은 빈 문자열로 초기화 한다.
        else:
            continue
    #최종 결과물 (tokenList)을 반환한다.
    return tokenList
#============================================================
# 중위표기법으로 된 수식 문자열을 입력받고
#   후위표기법으로 변환된 Queue를 반환한다.
def infix2Postfix(strInput):
    ops = "+-*/"    # 연산자 모음 문자열
    priority = {"*":3, "/":3, "+":2, "-":2, "(":1, ")":1}

    #중위표기법 문자열을 토큰 단위로 구분한다.
    tokenList = toTokens(strInput)

    #변환에 사용할 스택과 큐(출력용)를 생성한다.
    stack = Stack()
    queue = Queue()

    #tokenList에서 하나씩 차례대로 가져와서 처리한다.
    while tokenList:    # tokenList에 항목이 남아 있으면 반복한다.
        token = tokenList.pop(0)    # 맨 앞의 항목을 하나 가져온다.
        if type(token) == type(1.1):         # token이 피연산자(수)이면
            queue.add(token)     #   queue에 출력한다.
        elif token == "(":          # token이 왼쪽 괄호이면
            stack.push(token)       #   stack에 저장
        elif token == ")":          # token이 오른쪽 괄호이면
            while stack.peek() != "(":  # stack에서 왼쪽 괄호를 만날때까지
                queue.add(stack.pop())  #  pop하여 바로 출력(queue에)
            stack.pop()             # 스택의 맨 위에 있는 왼쪽 괄호는 버린다.
        else:                       # 연산자의 경우만 처리한다.
            if stack.isEmpty():     # 만일, 스택이 비어있는 경우
                stack.push(token)   #   스택에 현재 연산자(token)를 저장한다.
            else:
                while not stack.isEmpty():
                    if priority[stack.peek()] >= priority[token]:   # 스택에서 현재 연산자의 우선순위보다 낮은 연산자를 만날 때까지
                        queue.add(stack.pop())                      # 스택에서 꺼내 출력한다.
                    else:
                        break
                stack.push(token)   #현재 연산자는 스택에 저장한다.

    # 입력 토큰들을 모두 처리한 후에 스택에 남아 있는 것들을 모두 출력한다.
    while not stack.isEmpty():
        queue.add(stack.pop())

    # 최종 결과물(후위 표기법 순서로 저장된 queue)을 반환한다.
    return queue
#==============================================================================
# 스택 계산기 (stack calculator)
# 입력: 후위 표기법으로 정리된(토큰들로 구성된) queue
# 출력: 계산결과값(number)
#==============================================================================
def stackCalc(q):
    stack = Stack() # 계산용 스택 생성

    while not q.isEmpty():
        token = q.remove()
        
        if type(token) == type(" "):
            b = stack.pop()
            a = stack.pop() 
            if token == "+":
                stack.push(a+b)
            elif token == "-":
                stack.push(a-b)
            elif token == "*":
                stack.push(a*b)
            else: 
                stack.push(a/b)
        else:
            stack.push(token)

    # 스택에 남아 있는 최종 연산 결과를 반환한다.
    return stack.pop()
        




#teststr = "232 * (  43+ 456 / 345 )"
teststr = "100 / 20.123"
qPost = infix2Postfix(teststr)
print(stackCalc(qPost))

#print(toTokens(teststr))




