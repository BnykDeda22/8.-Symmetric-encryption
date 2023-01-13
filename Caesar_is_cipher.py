import numpy as np


def encrypt(m, k=1):
    symbols = list(map(lambda y: chr(y % 65536), np.array(list(map(lambda x: ord(x), list(m)))) + k))
    return ''.join(symbols)


def decrypt(c, k):
    symbols = list(map(lambda y: chr(y % 65536), np.array(list(map(lambda x: ord(x), list(c)))) - k))
    return ''.join(symbols)


message = '''Текст (от лат. textus — ткань; сплетение, сочетание) — зафиксированная на каком-либо материальном 
носителе человеческая мысль; в общем плане связная и полная последовательность символов. '''

cod_message = encrypt(message, 4)
print(f'Закодированное сообщение: {cod_message}')

dec_message = decrypt(cod_message, 4)
print(f'Раскодированное сообщение: {dec_message}')


def hack_cipher(message):
    symbols = list(map(lambda x: ord(x), list(message)))
    res = max(sorted(symbols, reverse=True), key=lambda x: symbols.count(x))
    key = res - ord(' ')
    return ''.join(list(map(lambda y: chr(y % 65536), np.array(symbols) - key)))


print(f"Закодированное сообщение: {cod_message}")
print("Раскодированное сообщение: ")
print(hack_cipher(cod_message))
