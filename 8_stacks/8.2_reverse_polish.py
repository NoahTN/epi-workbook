# https://leetcode.com/problems/evaluate-reverse-polish-notation
# O(n), O(1)

def evalRPN(self, tokens: List[str]) -> int:
      stack = []
      operators = {
         '+': lambda x, y: x + y,
         '-': lambda y, x: x - y,
         '*': lambda x, y: x * y,
         '/': lambda y, x: int(operator.truediv(x, y))
      }
      for t in tokens:
         if t in operators:
               stack.append(operators[t](stack.pop(), stack.pop()))
         else:
               stack.append(int(t))
               
      return stack[0]