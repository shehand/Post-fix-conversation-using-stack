from Register import *
from postFix import *

begin = """

             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
             $$$$                                       $$$$
             $$$$             !!!WELCOME!!!             $$$$
             $$$$   Introducing PostFix Conversation    $$$$
             $$$$                                       $$$$
             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

             BASICS INTRO :

             LD means places the operand into the register
             ST means places the contents of the register into a variable
             AD means adds the contents of a variable to the register
             SB means subtracts the contents of a variable form the register
             ML means multiplies the contents of the register by the variable
             DV means divides the contents of the register by the variable

                    
"""
print(begin)
while True:
    p = postFix()
    p.process()

