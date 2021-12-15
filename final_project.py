from idlelib.multicall import r


def read_csv(path_file):
    """
    :param path_file: path to csv file
    :return: list of lists, consists of 5 elements:
    0 - name of task
    1 - plasce
    2 - teammates
    3 - deadline
    4 - priority
    """
    all_list = []
    with open(path_file, 'r', encoding='utf-8') as csv_file:
        for line in csv_file:
            line = line.strip()
            line = line.split(',')
            all_list.append(line)
    return all_list


def print_csv(all_list):
    """
    :param all_list: list of all tasks
    :return: nothing
    prints all tasks
    """
    all_list = sorted(all_list, key=lambda x: x[4])
    for i in range(len(all_list)):
        print(all_list[i])
    print()


def delete_notion(filepath, name_task):
    """
    Delete task from csv file
    :param filepath:
    :param name_task:
    :return:
    """
    with open(filepath, mode='r', encoding='utf-8') as file:
        data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip("\n")
        data[i] = data[i].split(',')
    for i in data:
        if name_task in i:
            data.pop(data.index(i))
    with open(filepath, mode='w', encoding='utf-8') as file:
        for item in data:
            file.write(",".join(item))
            file.write('\n')


def tasks_today(list_of_tasks):
    """
    list[list[str]] --> list[list[str]]
    Return tasks for today.
    """
    from datetime import date

    today = str(date.today().strftime('%d.%m.%Y'))
    # today = today.replace("/", ".")
    today_tasks = []
    for i in range(len(list_of_tasks)):
        if today in list_of_tasks[i]:
            today_tasks.append(list_of_tasks[i])
    if len(today_tasks) == 0:
        print('No task for today, Relax :)')
    else:
        print(today_tasks)
    print()


def write_csv(path_file, new_task):
    """
    :param new_task: what to write in csv file
    :param path_file: path to csv file
    :return: nothing
     writes a new line (task) to csv file
    """
    with open(path_file, 'a', encoding='utf-8') as csv_file:
        csv_file.write('\n' + new_task)


def add_tasks():
    """Asks information about task and returns it in csv format"""
    task = input('Write a task: ')
    location = input('Write a location: ')
    collaborators = input('Write your coworkers: ')
    date = input('Write the date by which the task must be completed in format dd.mm.yyyy: ')
    priority = input('Write a priority from 1 to the number of the last task: ')
    lst = [task,location,collaborators,date,priority]
    return ','.join(lst)

if __name__ == '__main__':
    print('enter your path to csv file with tasks')
    path = input()
    while True:
        print('Enter 1 if you want to add task')
        print('Enter 2 if you want to delete task')
        print('Enter 3 if you want to see today task')
        print('Enter 4 to see all task, sorted by priority')
        print('Enter exit if you want to exit')
        action = input()
        if action == '1':
            print("What task do you want to add ?")
            task = add_tasks()
            write_csv(path, task)
        elif action == '2':
            print("What task do you want to delete ?")
            task = input()
            delete_notion(path, task)
        elif action == '3':
            print("Do you want to see today tasks ?")
            tasks_today(read_csv(path))
        elif action == '4':
            print_csv(read_csv(path))
        elif action == "exit":
            print('thanks for using, bye')
            break
        else:
            print('wrong input, repeat one more time')
