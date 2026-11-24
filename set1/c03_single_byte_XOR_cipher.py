from utils import single_char_decrypt

if __name__ == "__main__":
    c = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    #chose 58 since 37 xor 6f = 58. chose 'o' -> 6f since 37 appeared twice in succesion and 'oo' words are common
    k0 = "58"
    '''
    ka = []
    for i in range(0, len(c), 2):
        ka.append(k0)
    k = "".join(ka)
    print(k)

    cb = hex_to_bytes(c)
    kb = hex_to_bytes(k)

    m = fixed_xor(cb, kb)

    print(m)
    print("\n")

    for i in range(0, len(c), 2):
        c0 = c[i : i+2]
        c0b = hex_to_bytes(c0)
        b0 = b'\x58'
        print(c0 + " " + fixed_xor(c0b, b0).hex())
    '''

    print(single_char_decrypt(c, k0))


