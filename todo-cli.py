import click
import os

from todotask.todotask import ToDoTask, ToDoList


# https://pythlife.blogspot.ru/2016/03/init-py-file-packages.html


"""
    TODO:
    * вывод название всех списков 
    * вывод дел в конктретном списке
    * создание списка дел в текущем списке дел
    * указать текущий список дел   
    * указать признак выполнения задачи 
    * указать признак выполнения всего списка задач
"""

path_task = "data/mytasks/"  #  путь в котором хранятся списки задач

def getListLists(path):
    """
        получение всех списков TODO папке path
    """
    result = []
    filenames = os.listdir(path)
    if filenames == []:
        return result
    for el in filenames:
        result.append(ToDoList(namefile=el).getInfoList())
    return result


@click.command()
#@click.argument('task')
@click.option('--ls-list', '-lsl', is_flag=True, help='get list all todo lists')
#@click.option('--ls-list', '-lsl', help='get list all todo lists')
def main(ls_list):
    """
        Tool CLI for manage with our tasks and checklists
    """
    if ls_list:
        all_tasks = getListLists(path_task)
        if all_tasks == []:
            print("Списков нет. Возьмите под контроль свою жизнь.")
        else:
            print("Найдены следующие списки: {}".format(all_tasks))


if __name__ == "__main__":
    main()