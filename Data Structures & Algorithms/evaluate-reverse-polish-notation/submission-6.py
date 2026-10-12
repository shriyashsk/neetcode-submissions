class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i]=="+":
                a=stack.pop()
                b=stack.pop()
                summ=int(a)+int(b)
                stack.append(summ)
                

            elif tokens[i]=='-':
                a=stack.pop()
                b=stack.pop()

                stack.append(int(b)-int(a))
               
            elif tokens[i]=='*':
                a=stack.pop()
                b=stack.pop()
                stack.append(int(a) * int(b))
                
            elif tokens[i]=='/':
                a=stack.pop()
                b=stack.pop()

                stack.append(int(int(b)/int(a)))

            
            else:
                stack.append(tokens[i])

        return int(stack[0])

        