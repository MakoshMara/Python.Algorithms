# https://drive.google.com/file/d/1ysGniNdHCNFrYEAhjEttCCmvFsv125mo/view?usp=sharing
def shetchik(n):
    ch = 0
    notch = 0
    while n > 0:
        if (n % 10) % 2 == 0:
            ch += 1
        else:
            notch += 1
        n = n // 10
    return f'Четных - {ch}, нечетных - {notch}'


print(shetchik(int(input("Введите натуральное число:"))))
