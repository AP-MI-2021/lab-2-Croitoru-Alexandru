'''
5. Determină dacă un număr dat este palindrom.

Funcția principală: is_palindrome(n) -> bool
Funcția de test: test_is_palindrome()
'''
def is_palindrome(n):
    '''
    determina daca un numar este palindrom
    :param n: n este un numar intreg
    :return: returneaza True daca este palindrom si False daca nu este palindrom
    '''
    n = str(n)
    lungime = len(n) - 1
    i = 0
    k = 1
    while i < lungime:
        if n[i] != n[lungime]:
            k = 0
        i += 1
        lungime -= 1
    if k == 1:
        return True
    else:
        return False

def test_is_palindrome():
    assert is_palindrome(1331) == True
    assert is_palindrome(2662) == True
    assert is_palindrome(123454321) == True
    assert is_palindrome(5685) == False
test_is_palindrome()

'''
6. Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime. De exemplu,
233 este superprim, deoarece 2, 23 și 233 sunt toate prime, dar 237 nu este superprim, deoarece 237 nu este prim.

Funcția principală: is_superprime(n) -> bool
Funcția de test: test_is_superprime()
'''

def is_prime(n):
    '''
    is_prime determina daca un numar este prim sau nu
    :param n: este numar intreg
    :return: True daca este prim si False daca nu este prim
    '''
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(3) == True
    assert is_prime(7) == True
    assert is_prime(6) == False
    assert is_prime(10) == False
test_is_prime()


def is_superprime(n):
    '''
    determina daca un numar este superprim
    :param n: este numar intreg
    :return: True daca este superprim,Fals daca nu este superprim
    '''
    ok = 1
    while(n):
        if is_prime(n) is False:
            ok = 0
        n = n // 10
    if ok == 1:
        return True
    else:
        return False

        

def test_is_superprime():
    assert is_superprime(233) == True
    assert is_superprime(240) == False
    assert is_superprime(953) == False
    assert is_superprime(740) == False
    assert is_superprime(237) == False
test_is_superprime()
'''
7. Determină dacă un număr este antipalindrom: un număr este antipalindrom dacă oricare două cifre egal depărtate de extremități sunt diferite 
(excepție făcând cifra din mijloc dacă avem un număr impar de cifre). 
De exemplu: 2783 este antipalindrom, iar 2773 nu este.
Funcția principală: is_antipalindrome(n) -> bool
Funcția de test: test_is_antipalindrome()
'''

def is_antipalindrome(n):
    '''
    :param n: nr intreg
    :return: returneaza true daca este antipalindrom si false in caz contrar
    '''
    n = str(n)
    lungime = len(n) - 1
    i = 0
    k = 1
    while i < lungime :
        if n[i]==n[lungime]:
            k=0
        i+=1
        lungime-=1
    if k==0:
        return False
    else:
        return True


def test_is_antipalindrome():
    assert is_antipalindrome(2552) is False
    assert is_antipalindrome(2424) is True
    assert is_antipalindrome(2772) is False
test_is_antipalindrome()

option = '''
Daca doriti sa aflati daca un numar este antipalindrom scrie 1.
Daca doriti sa aflati daca un numar este superprim scrie 2.
Daca doriti sa opriti programul scrie 3.
'''

def main():
    while True:
        optiune = input(option)
        if optiune == '1':
            numar = int(input("Scrieti valoarea:"))
            if is_antipalindrome(numar):
                print("Este antipalindrom!")
            else:
                print("Nu este antipalindrom!")
        elif optiune == '2':
            numar = input("Scrieti numarul: ")
            if is_superprime(numar):
                print("Este numar superprim!")
            else:
                print("Nu este un numar superprim!")
        elif optiune == '3':
            print("programul s-a oprit!")
            break
        else:
            print("Nu exista comanda!")
if __name__ == main():
    main()
