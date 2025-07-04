from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def file_tests():
    print("Test1:\n" + get_file_content("calculator", "main.py")+"\n")
    print("Test2:\n" + get_file_content("calculator", "pkg/calculator.py")+"\n")
    print("Errortest1:\n" + get_file_content("calculator", "/bin/cat")+"\n")
    #print("Errortest2:\n" + get_files_info("calculator", "../")+"\n")
file_tests()



""" older tests
    print("Test1:\n" + get_files_info("calculator", ".")+"\n")
    print("Test2:\n" + get_files_info("calculator", "pkg")+"\n")
    print("Errortest1:\n" + get_files_info("calculator", "/bin")+"\n")
    print("Errortest2:\n" + get_files_info("calculator", "../")+"\n")
"""



    


