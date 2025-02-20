import base64
import zlib
import re

__author__ = "Who Knows"

class PhpObfuscationDecoder:
    def __init__(self, encoded_str):
        self.encoded_str = encoded_str
        self.decoded_result = None

    def decode(self):
        try:
            decoded = base64.b64decode(self.encoded_str) # Base64 decode
            decompressed = zlib.decompress(decoded, -15)  # -15 removes the header
            self.decoded_result = ''.join(chr(ord(c) - 1) for c in decompressed.decode(errors='ignore')) # Reverse character shift (-1 shift in ASCII)
            return self.decoded_result
        except Exception as e:
            return f"Decoding failed: {str(e)}"

    def save_output(self, filename):
        if self.decoded_result is None:
            raise ValueError("No decoded result found.")
        
        with open(filename, 'w') as file:
            file.write(self.decoded_result)

if __name__ == "__main__":
    php_file = input("Enter the PHP file Name : ")
    try:
        with open(php_file, 'r') as file:
            php_code = file.read()
        functions = re.findall(r"function\s+([a-zA-Z0-9_]+)\(.*?\)", php_code)
        print("Found functions:", functions)
        matches = re.findall(r"([a-zA-Z0-9_]+)\('([A-Za-z0-9+/=]+)'\)", php_code)
        
        if matches:
            for function_name, encoded_string in matches:
                print(f"Decoding from function: {function_name}")
                decoder = PhpObfuscationDecoder(encoded_string)
                decoded_result = decoder.decode() # Decode the string
                output_filename = "decoded_output.txt"
                decoder.save_output(output_filename)
                print(f"Decoded result saved to {output_filename}")
                break
        else:
            print("No encoded string found in the PHP file.")
    except FileNotFoundError:
        print("File not found. Please enter a valid PHP file path.")
