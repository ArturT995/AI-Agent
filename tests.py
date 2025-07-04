from functions.get_files_info import get_files_info

def file_tests():
    print("Test1:\n" + get_files_info("calculator", ".")+"\n")
    print("Test2:\n" + get_files_info("calculator", "pkg")+"\n")
    print("Errortest1:\n" + get_files_info("calculator", "/bin")+"\n")
    print("Errortest2:\n" + get_files_info("calculator", "../")+"\n")
file_tests()
    


