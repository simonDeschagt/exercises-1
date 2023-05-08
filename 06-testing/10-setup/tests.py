from datetime import date
from tasks import Task, TaskList
from calendars import CalenderStub
import pytest



def setup_function():
    global today
    global tomorrow
    global future
    global past
    global cs
    global tasklist
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    future = date(2000, 5, 5)
    past = date(1999, 1, 1)
    cs  = CalenderStub(today)
    tasklist = TaskList(cs)



def test_task_becomes_overdue():
    #arrange
    task = Task('some description', tomorrow)
    tasklist.add_task(task)

    #act
    cs.today = future

    #assert
    assert [task] == tasklist.overdue_tasks


def test_creation():
    #arrange


    #assert
    assert len(tasklist) == 0
    assert [] == tasklist.due_tasks
    assert [] == tasklist.finished_tasks
    assert [] == tasklist.overdue_tasks

def test_adding_task_with_due_day_in_future():
    #arrange
    task = Task("de beste beschrijving ooit", future)

    #act
    tasklist.add_task(task)


    #assert
    assert [task] == tasklist.due_tasks

def test_adding_task_with_due_day_in_past():
    #arrange
    task = Task("adfaservsd", past)
    

    #act
    with pytest.raises(RuntimeError):
        tasklist.add_task(task)
    assert 0 == len(tasklist)

def test_task_becomes_finished():
    #arrange
    task = Task("asdfasdf", tomorrow)
    

    #act
    tasklist.add_task(task)
    task.finished = True

    #assert
    assert [task] == tasklist.finished_tasks
    assert [] == tasklist.due_tasks
     