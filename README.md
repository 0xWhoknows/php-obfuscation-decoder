# PHP Obfuscation Decoder

## Overview

This Python script decodes obfuscated PHP code that has been encoded using Base64, compressed with zlib, and had a character shift applied. It extracts and deciphers such encoded strings found within a given PHP file.

## Features

- Detects obfuscated PHP code containing Base64 encoded, zlib compressed, and character-shifted strings.
- Decodes and decompresses the extracted strings.
- Identifies PHP function names present in the file.
- Saves the decoded output to a text file.

## Requirements

- Python 3.x

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/0xWhoknows/php-obfuscation-decoder.git
cd php-obfuscation-decoder
```

## Usage

Run the script and provide the path to the PHP file when prompted:

```bash
python main.py
```

### Example

```
Enter the PHP file path: obfuscated.php
Found functions: ['decode_function']
Potential encoded strings found: [('decode_function', 'eJzT0yMAAGTvBe8=')]
Decoding from function: decode_function
Decoded Result:
<?php echo "Hello, World!"; ?>
Decoded result saved to decoded_output.txt
```

## Output

The decoded result will be saved in a file named `decoded_output.txt`.

## License

This project is open-source and available under the MIT License.

## Contributions

Feel free to submit pull requests or report issues.

## Disclaimer

Use this tool responsibly. It is intended for ethical and educational purposes only.

