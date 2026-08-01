import encrypt_decrypt
import random_f

print()

print('One time pad encryption\n')

while True:
    command = input()

    print()

    if command[:3] == 'xor':
        try:
            args = command.split(' ')

            if len(args) != 4:
                raise SyntaxError('Console error: not enough arguments')
            
            args = args[1:]

            encrypt_decrypt.xor_file(args[0], args[1], args[2])

            print('Success!')

        except Exception as e:
            print(f'Python error: {e}')
    
    elif command[:3] == 'key':
        try:
            args = command.split(' ')

            if len(args) != 4:
                raise SyntaxError('Console error: not enough arguments')
            
            args = args[1:]

            bit_f = random_f.custom_rand

            if args[2] == 'python':
                bit_f = random_f.python_rand

            encrypt_decrypt.c_create_key_file(args[0], args[1], bit_f)

            print('Success!')

        except Exception as e:
            print(f'Python error: {e}')
    
    elif command == 'quit':
        break

    elif command == 'help':
        print('Command list:\n\nXor <file 1> with <file 2> and store as <file 3>: xor <file 1> <file2> <file3>\n\nCreate key for <file 1> as <file 2>, if <option> = "python", then use random python library PRNG, otherwise use my custom PRNG: key <file 1> <file 2> <option>\n\nQuit console: quit\n\nGet command list: help')

    # Add more commands

    else:
        print('Console error: invalid command')

    print()