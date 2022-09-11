###################################################################################################
#   Function     #   Description    #  Return Type   #   Return Value  #   Return Description     #
#----------------#------------------#----------------#-----------------#--------------------------#
#     check      #   Check syntax   #      bool      #      True       #   Syntax is correct      #
###################################################################################################

class Check:
    def check(line, correctSyntax):
        arguments = line.split(" ")
        baseARGS = correctSyntax.split(" ")
        
        if arguments[0] != baseARGS[0]:
            return False
        
        if len(arguments) == len(baseARGS):
            if arguments[0] == baseARGS[0]:
                args = arguments[1:]
                return True, args
                            
        elif arguments[-1] == baseARGS[0]:
            args = arguments[1:]
            return True, args
        
        elif len(arguments) < len(baseARGS):
            diff = len(baseARGS) - len(arguments)
            if diff >= True:
                if arguments[0] == baseARGS[0]:
                    args = arguments[1:]
                    return True, args
        return False

if __name__ == "__main__":
    correct = "exit -<> -<>" 
    print(Check.check("exat", correct))
    print(Check.check("exst -l", correct))
    print(Check.check("txit -m -k", correct))
    print(Check.check("exit -m -k -l", correct))
    print(Check.check("exat -m -k", correct))
    print(Check.check("exit -m -k", correct))
    print(Check.check("exit -m", correct))
    print(Check.check("exit", correct))