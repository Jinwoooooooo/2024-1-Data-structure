from stack import *

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
teststr = "(<>{[{]})"
print(checkParenthese(teststr))

print(toTokens("323   *(4+5)-6/2"))

# l[0] in "({["

# st.push(100)
# st.showList()
# st.push(200)
# st.showList()
# print("Stack Pop => {}".format(st.pop()))
# st.showList()
# print("Stack Peek => {}".format(st.peek()))
# st.showList()