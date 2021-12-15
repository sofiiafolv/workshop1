from idlelib.multicall import r


def read_csv(path):
    """
    :param path: path to csv file
    :return: list of lists, consists of 5 elements:
    0 - name of task
    1 - plasce
    2 - teammates
    3 - deadline
    4 - priority
    """
    all_list = []
    with open(path, 'r', encoding='utf-8') as csv_file:
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


def delete_notion(filepath, object):
    """Accepts a file a delete a done task, which the user enters"""
    with open(filepath, mode='r', encoding='utf-8') as file:
        data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip("\n")
        data[i] = data[i].split(',')
    for i in data:
        if object in i:
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


def write_csv(path, new_task):
    """
    :param new_task: what to write in csv file
    :param path: path to csv file
    :return: nothing
     writes a new line (task) to csv file
    """
    with open(path, 'a', encoding='utf-8') as csv_file:
        csv_file.write("\n")
        csv_file.write(new_task)
