import click
import os

#import todotask.todotask


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




@click.command()
@click.argument('task')
# @click.option('--ls-list', '-lsl', is_flag=True, help='get list all todo lists')
@click.option('--ls-list', '-lsl', help='get list all todo lists')
def main(task, ls_list):
    """
        Tool CLI for manage with our tasks and checklists
    """
    if ls_list:
        all_tasks = getListLists(path_task)
        print("Найдены следующие списки: {}".format(all_tasks))
    else:
        print("Списков нет. Начните управлять своей жизнью.")