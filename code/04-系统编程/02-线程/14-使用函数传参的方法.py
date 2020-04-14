def process_student(name):
    std = Student(name)
    # std 是局部变量,但是每个函数都要用它,因此必须传递进去
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)