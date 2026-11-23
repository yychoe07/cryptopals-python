from utils import hex_to_bytes, bytes_to_b64

if __name__ == "__main__":
    sample = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(sample)
    print(bytes_to_b64(hex_to_bytes(sample)))