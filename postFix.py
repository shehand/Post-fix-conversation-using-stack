from Register import *

class postFix:
    def __init__(self):
        self.operator_list = ['+','-','*','/']
        self.operand_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.sequence = input("Enter the Sequance : ")
        self.r = Register()
        

    def process(self):
        n = 1
        for i in self.sequence:
            if i  in self.operand_list:
                self.r.push(i)
            elif i in self.operator_list:
                operand_one = self.r.pop()
                operand_two = self.r.pop()
                print('LD ',operand_two)

                if(i == '+'):
                    print('AD ',operand_one)
                    self.r.push('TEMP'+str(n))
                    n = n + 1
                    print('ST  '+self.r.peek())
                elif(i == '-'):
                    print('SB ',operand_one)
                    self.r.push('TEMP'+str(n))
                    n = n + 1
                    print('ST  '+self.r.peek())
                elif(i == '*'):
                    print('ML ',operand_one)
                    self.r.push('TEMP'+str(n))
                    n = n + 1
                    print('ST  '+self.r.peek())
                elif(i == '/'):
                    print('DV ',operand_one)
                    self.r.push('TEMP'+str(n))
                    n = n + 1
                    print('ST  '+self.r.peek())
            else:
                print('Please enter valid operands')
                break

        

