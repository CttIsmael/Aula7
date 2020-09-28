def sua_sorte(num):
    n_sorte =0

    while num > 0:
        n_sorte +=(num%10)
        num = num//10
    
    return n_sorte

def main():
    num = int(input())

    s =sua_sorte(num)
    print(f'{s}')

if __name__=='__main__':
    main()
