# Finding FILES
"""
Goal: To find all paths of files which has ".c" in their name
Using import os and recursion, I have tried to traverse in file system and get file with name for suffix
1. Solution is independent of depth of sub directories
2. Solution can work for any suffix

Idea for recursion is
In end> Either file will finish in a directory or we will get file which has our suffix
For loop> takes us through all files in any directory
and If loop when suffix is there in file we just add that path which we are rotating in our main function

Time complexity:
If there are n files in main directory and each directory has m files then it si O(n * m) complexity
"""

import os


def find_files(suffix, path, all_paths=[]):
    # all_paths = list()
    if suffix is None or suffix == '':
        return -1

    for dir_in in os.listdir(path):
        sub_path = path + '/' + dir_in

        if os.path.isfile(sub_path):
            if suffix in dir_in:
                all_paths.append(sub_path)

        if os.path.isdir(sub_path):
            find_files(suffix, sub_path, all_paths)

    return all_paths


if __name__ == '__main__':
    # Testing Code
    print(find_files('.c', './testdir', all_paths=[]))

    # Testing code 1 - Changing Suffix
    print(find_files('.h', './testdir', all_paths=[]))

    # Testing code 2 - None/ "" Suffix values, returns -1
    print(find_files('', './testdir', all_paths=[]))

    # Test 3, Suffix large all most like full name
    print(find_files('.gitkeep', './testdir', all_paths=[]))
