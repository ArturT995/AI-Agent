from functions.run_python_file import run_python_file

def file_tests():
    print("Test1:\n" + run_python_file("calculator", "main.py")+"\n")
    print("Test2:\n" + run_python_file("calculator", "tests.py")+"\n")
    print("Errortest1:\n" + run_python_file("calculator", "../main.py")+"\n")
    print("Errortest1:\n" + run_python_file("calculator", "nonexistent.py")+"\n")
file_tests()



    


