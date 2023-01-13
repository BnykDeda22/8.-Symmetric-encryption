from random import randint


def generate_key(length):
    return [randint(0, 26) for _ in range(length)]


def xor(char, key):
    return chr(ord(char) ^ key)


def encrypt_v(text):
    key = generate_key(len(text))
    return ''.join([xor(text[i], key[i]) for i in range(len(text))]), key


def decrypt_v(cryptedtext, key):
    return ''.join([xor(cryptedtext[i], key[i]) for i in range(len(cryptedtext))])


message = '''Текст (от лат. textus — ткань; сплетение, сочетание) — зафиксированная на каком-либо материальном 
носителе человеческая мысль; в общем плане связная и полная последовательность символов.'''
encrypt_v, key = encrypt_v(message)
print('Зашифрованный шифром Вернама текст: ', encrypt_v)
decrypt_v = decrypt_v(encrypt_v, key)
print('Расшифрованный текст: ', decrypt_v)
