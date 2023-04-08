import os
import random
import subprocess

fc = 0

def main(file_name, inputt, pik):
    input_string = '{} {}\n{}\n'.format(len(inputt), pik, ' '.join(map(str, inputt)))
    process = subprocess.Popen(file_name, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, _ = process.communicate(input=input_string.encode())
    return(stdout.decode())

def rand(file1, file2):
    global fc
    lenn = random.randint(1, 10)
    pik = random.randint(1, 10)
    inputt = [random.randint(1, 10) for _ in range(lenn)]

    file1op = main(file1, inputt, pik)
    file2op = main(file2, inputt, pik)

    if file1op == file2op:
        result = "pass"
    else:
        result = "fail"
        fc += 1
    return (lenn, pik, inputt, file1op, file2op, result)

with open("tc.csv", "a") as opfile:
    for i in range(100): # write 10 test cases
        result = rand("./workin.out", "./notworkin.out")
        opfile.write("{},{},{},{},{},{}\n".format(result[0], result[1], result[5], result[3], result[4], result[2]))

print("Number of failed test cases:", fc)

