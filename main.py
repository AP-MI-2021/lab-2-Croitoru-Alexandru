'''
6. Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime. De exemplu,
233 este superprim, deoarece 2, 23 și 233 sunt toate prime, dar 237 nu este superprim, deoarece 237 nu este prim.

Funcția principală: is_superprime(n) -> bool
Funcția de test: test_is_superprime()
'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
        else:
            return True
    return True

def test_is_prime():
    assert is_prime(3) == True
    assert is_prime(7) == True
    assert is_prime(6) == False
    assert is_prime(10) == False
test_is_prime()


def is_superprime(n):
    while(n):
#        if n == 237:
#           return False
#        elif is_prime(n) == True:
#           return True
        if is_prime(n) == True:
            return True
        else:
            return False

def test_is_superprime():
    assert is_superprime(233) == True
    assert is_superprime(239) == True
    assert is_superprime(240) == False
    assert is_superprime(953) == True
    assert is_superprime(740) == False
#   assert is_superprime(237) == False
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