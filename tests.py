from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def file_tests():
    print("Test1:\n" + write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")+"\n")
    print("Test2:\n" + write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")+"\n")
    print("Errortest1:\n" + write_file("calculator", "/tmp/temp.txt", "this should not be allowed")+"\n")
file_tests()



""" older tests:
    print("Test1:\n" + get_file_content("calculator", "main.py")+"\n")
    print("Test2:\n" + get_file_content("calculator", "pkg/calculator.py")+"\n")
    print("Errortest1:\n" + get_file_content("calculator", "/bin/cat")+"\n")

    print("Test1:\n" + get_files_info("calculator", ".")+"\n")
    print("Test2:\n" + get_files_info("calculator", "pkg")+"\n")
    print("Errortest1:\n" + get_files_info("calculator", "/bin")+"\n")
    print("Errortest2:\n" + get_files_info("calculator", "../")+"\n")
"""



    


