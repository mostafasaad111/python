# قائمة لتخزين المهام
todo_list = []


def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added")


def view_tasks():
    if not todo_list:
        print("No tasks to display")
    else:
        print("Tasks:")
        for task in todo_list:
            print(task)


def remove_task():
    if not todo_list:
        print("No tasks to remove")
    else:
        task_to_remove = input("Enter a task to remove: ")
        if task_to_remove in todo_list:
            todo_list.remove(task_to_remove)
            print("Task removed")
        else:
            print("Task not found")


# الحلقة الرئيسية لتكرار البرنامج حتى يتم اختيار الخروج
while True:
    # استخدام مدخل المستخدم لاختيار الأمر
    user_action = input("Enter a command (add, view, remove, exit): ")

    # إضافة مهمة إلى القائمة
    if user_action == "add":
        add_task()

    # عرض المهام الموجودة في القائمة
    elif user_action == "view":
        view_tasks()

    # حذف مهمة من القائمة
    elif user_action == "remove":
        remove_task()

    # الخروج من البرنامج
    elif user_action == "exit":
        break

    # في حالة إدخال أمر غير صالح
    else:
        print("Invalid command")
