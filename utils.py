#Reusuable cryptographic helpers for Cryptopals

#Mapping for base64 encoding
B64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
#convert hex to bytes
def hex_to_bytes(hex_str: str) -> bytes:
    '''
    array = []
    for i in range(0, len(hex_str), 2):
        val = int(hex_str[i: i+2], 16)
        array.append(val)
    return bytes(array)
    '''
    return bytes (int(hex_str[i : i+2], 16) for i in range(0, len(hex_str), 2))


#convert bytes to b64
def bytes_to_b64(bytes_data: bytes) -> str:
    out = []
    for i in range(0, len(bytes_data), 3):
        pad1 = False
        pad2 = False
        b0 = bytes_data[i]
        if (i + 1 >= len(bytes_data)):
            b1 = 0
            pad1 = True
        else:
            b1 = bytes_data[i+1]
        if (i+2 >= len(bytes_data)):
            b2 = 0
            pad2 = True
        else:
            b2 = bytes_data[i+2]
        x = (b0 << 16) | (b1 << 8) | b2  
        idx0 = (x >> 18) & 0x3F
        idx1 = (x >> 12) & 0x3F

        x2 = '='
        x3 = '='

        if not pad1:
            idx2 =(x >> 6) & 0x3F
            x2 = B64_ALPHABET[idx2]
        if not pad2:
            idx3 = x & 0x3F
            x3 = B64_ALPHABET[idx3]

        val = B64_ALPHABET[idx0] + B64_ALPHABET[idx1] + x2 + x3
        out.append(val)
    return "".join(out)
        