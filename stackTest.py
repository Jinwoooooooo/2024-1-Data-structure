from stack import *

st = Stack()

# 괄호 매칭 점검 함수
# 반환값: 매칭에 문제가 없으면 True, 문제가 있으면 오류 메시지 출력하고 False 반환.
def checkParenthese(st):
    pass

# l[0] in "({["

checkParenthese("({(({[{{{[{()()}]}}}]}))})")

st.push(100)
st.showList()
st.push(200)
st.showList()
print("Stack Pop => {}".format(st.pop()))
st.showList()
print("Stack Peek => {}".format(st.peek()))
st.showList()