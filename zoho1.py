def printPattern(string1):
    m = len(string1)//2
    n= len(string1)

    newStr = string1[m:] + string1[:m]

    for i in range(0,n):
        k=n-1-i
        while(k):
            print(' ',end='')
            k-=1
        j=0
        while(j<i+1):
            print(newStr[j],end='')
            j+=1
        print('')

if __name__ == "__main__":
    str1 = input(str('Enter string: '))
    printPattern(str1)
    