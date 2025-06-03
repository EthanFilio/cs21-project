import sys
import os

# encodings for single-byte instructions
ENCODINGS = {
    "rot-r": 0b00000000,
    "rot-l": 0b00000001,
    "rot-rc": 0b00000010,
    "rot-lc": 0b00000011,
    "from-mba": 0b00000100,
    "to-mba": 0b00000101,
    "from-mdc": 0b00000110,
    "to-mdc": 0b00000111,
    "addc-mba": 0b00001000,
    "add-mba": 0b00001001,
    "subc-mba": 0b00001010,
    "sub-mba": 0b00001011,
    "inc*-mba": 0b00001100,
    "dec*-mba": 0b00001101,
    "inc*-mdc": 0b00001110,
    "dec*-mdc": 0b00001111,
        
}



if __name__ == '__main__':
    c_l_args = sys.argv
    if len(c_l_args) != 3:
        print(
            "Usage: python assembler.py <file.asm> <bin|hex>\n"
            "       or\n"
            "       python3 assembler.py <file.asm> <bin|hex>\n"
            "Arguments:\n"
            "  <file.asm>     Assembly source file written in Arch-242\n"
            "  <bin|hex>      Output format: 'bin' for binary, 'hex' for hexadecimal\n"
        )
        sys.exit(1)

    src_file = c_l_args[1]
    mode = c_l_args[2].lower()

    if mode not in ("bin", "hex"):
        print("Second argument must be \"bin\" or \"hex\".")
        sys.exit(1)
    
    if not os.path.exists(src_file):
        print(f"{src_file} not found.")
        sys.exit(1)
    with open(src_file) as sf:
        lines = sf.readlines()