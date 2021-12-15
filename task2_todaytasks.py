from datetime import date


def tasks_today(list_of_tasks):
    """
    list[list[str]] --> list[list[str]]
    Return tasks for today.
    """
    today = str(date.today().strftime('%d.%m.%Y'))
    # today = today.replace("/", ".")
    today_tasks = []
    for i in range(len(list_of_tasks)):
        if today in list_of_tasks[i]:
            today_tasks.append(list_of_tasks[i])
    return today_tasks
print(tasks_today([["Lab13","ЦШ","ніхто","20.12.2021","1"], ["Практична","Колегіум","моя група","15.12.2021","2"]]))