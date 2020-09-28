def maior_populacao():
    t = 0
    pop_A = float(input())
    pop_B = float(input())

    maior = pop_A
    menor = pop_B

    if pop_B > maior:
        maior = pop_B
    if pop_A<menor:
        menor = pop_A

    while maior>menor:
        t +=1
        maior *=1.02
        menor *=1.03
        
        if menor > maior:
            return t
            break
        
def main():
    ano =maior_populacao()
    print(f'{ano}')
    

if __name__=='__main__':
    main()
