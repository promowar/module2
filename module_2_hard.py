#я немного расширил пул чисел которые могут появится на первом столбе, через функцию


def secret(a):
    if a<= 2:
        print('Пароля для такого числа по сюжету не существует')
    password = []
    for i in range(a):
        if i <=0:
            continue
        for j in range(a):
            if j <= 0 or i == j or i > j:
                continue
            sum_ = i + j
            if sum_ > a:
                break
            if a % sum_ == 0:
                k = str(i)
                l = str(j)
                password.append(i)
                password.append(j)
    return print('Пароль для вашего числа: ', *password, sep='')


secret(3)
secret(4)
secret(5)
secret(6)
secret(7)
secret(8)
secret(9)
secret(10)
secret(11)
secret(12)
secret(13)
secret(14)
secret(15)
secret(16)
secret(17)
secret(18)
secret(19)
secret(20)
secret(21)
secret(34)
secret(39)
secret(70)



