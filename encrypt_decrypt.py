from typing import Callable
import os

def bool_list_to_byte(l: list[bool]) -> bytes:
    return bytes([int(''.join('1' if b else '0' for b in l), 2)])

def create_key_file(file_name: str, n: int, bit_f: Callable[[int], bool]) -> None:
    with open(file_name, 'wb') as file:
        for i in range(n):
            buffer = []

            for j in range(8):
                k = 8 * i + j

                buffer.append(bit_f(k))
            
            file.write(bool_list_to_byte(buffer))

def c_create_key_file(message_file: str, key_file: str, bit_f: Callable[[int], bool]) -> None:
    n = os.path.getsize(message_file)

    create_key_file(key_file, n, bit_f)

def xor_file(file_name_1: str, key_file: str, file_name_2: str) -> str:
    with open(file_name_1, 'rb') as file_1, open(key_file, 'rb') as key, open(file_name_2, 'wb') as file_2:
        for b1, b2 in zip(file_1.read(), key.read()):
            file_2.write(bytes([b1 ^ b2]))