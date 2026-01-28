x = 1
def escopo():
    #global x
    x = 10
    print(x)
    def outra_funcao():
        #global x
        x = 11
        y = 2
        print(x, y)
    #return outra_funcao()
    outra_funcao()
    print(x)

#x = 1
print(x)
escopo()
print(x)