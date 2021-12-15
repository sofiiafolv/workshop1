def delete_notion(filepath,object):
    """Accepts a file a delete a done task, which the user enters"""
    with open(filepath,mode='r',encoding='utf-8') as file:
        data=file.readlines()
    for i in range(len(data)):
        data[i]=data[i].strip("\n")
        data[i]=data[i].split(',')
    for i in data:
        if object in i:
            data.pop(data.index(i))
    with open(filepath,mode='w',encoding='utf-8') as file:
        for item in data:
            file.write(",".join(item))
            file.write('\n')

def add_tasks():
    """Asks information about task and returns it in csv format"""
    task=input('Write a task: ')
    location=input('Write a location: ')
    collaborators=input('Write your coworkers: ')
    date=input('Write the date by which the task must be completed in format dd.mm.yyyy: ')
    priority=input('Write a priority from 1 to the number of the last task: ')
    lst=[task,location,collaborators,date,priority]
    return ','.join(lst)


