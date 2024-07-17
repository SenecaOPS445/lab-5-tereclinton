#!/usr/bin/env python3
# Author ID: 119911220

import os

def read_file_string(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found!"

def read_file_list(file_name):
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return ["File not found!"]

def append_file_string(file_name, string_of_lines):
    with open(file_name, 'a') as file:
        file.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    with open(file_name, 'w') as file:
        for line in list_of_lines:
            file.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    with open(file_name_read, 'r') as file_read:
        lines = file_read.readlines()
    with open(file_name_write, 'w') as file_write:
        for index, line in enumerate(lines, 1):
            file_write.write(f"{index}:{line}")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    
    # Ensuring files are clear before writing to avoid confusion
    for file in [file1, file2, file3]:
        if os.path.exists(file):
            os.remove(file)
    
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print("Content of file1 after appending strings:")
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print("Content of file2 after writing list:")
    print(read_file_list(file2))

    copy_file_add_line_numbers(file2, file3)
    print("Content of file3 after copying with line numbers:")
    print(read_file_string(file3))
