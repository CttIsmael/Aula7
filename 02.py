def posso_pagar(pc):
    pp = 10000
    t = 0
    
    while pp<=pc:
        pp *=1.007
        pc *=1.004
        t +=1
        if pp >= pc:
            return t
            break

def main():
    pc = float(input())
    qnd = posso_pagar(pc)
    print(f'{qnd}')


if __name__=='__main__':
    main()
