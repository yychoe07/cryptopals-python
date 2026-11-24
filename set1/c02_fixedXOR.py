from utils import hex_to_bytes, fixed_xor

if __name__ == "__main__":
    str1 = "1c0111001f010100061a024b53535009181c"
    str2 = "686974207468652062756c6c277320657965"

    bytes1 = hex_to_bytes(str1)
    bytes2 = hex_to_bytes(str2)

    print(fixed_xor(bytes1, bytes2).hex())
