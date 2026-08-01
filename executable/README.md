This is an educational implementation of a one-time pad (OTP). Encrypt data with this at your own risk.

The .exe file is a program that can produce a file that is the elementwise xor of two files of the same size. The program can also produce a pseudorandom key file that is the same size as a target file.

To start, place your unencrypted file or encrypted file and key file into this folder. This lets you enter file names into commands instead of entire file paths.

Next, run the "OTP encryption decryption.exe" file. Enter the command "help" to find information about commands that can be used.

To encrypt a file:

1) Ensure the unencrypted file is in this folder.

2) Create a key using the "key" command. <file 1> is the unencrypted file's name and <file 2> is the name that the generated key file will have.

3) Xor the unencrypted file with the key file using the "xor" command. <file 1> is the unencrypted file's name, <file 2> is the key file's name, and <file 3> is the name that the generated encrypted file will have.

To decrypt a file:

1) Ensure the encrypted file and the correct key file is in this folder.

2) Xor the encrypted file with the key file using the "xor" command. <file 1> is the encrypted file's name, <file 2> is the key file's name, and <file 3> is the name that the generated decrypted file will have.
