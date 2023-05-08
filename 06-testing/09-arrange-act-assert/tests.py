from datetime import date
from tasks import Task, TaskList
from calendars import CalenderStub
import pytest


def test_task_becomes_overdue():
    #arrange
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    test_date = date(2000, 5, 5)
    calender = CalenderStub(today)
    task = Task('some description', tomorrow)
    tasks = TaskList(calender)
    tasks.add_task(task)

    #act
    calender.today = test_date

    #assert
    assert [task] == tasks.overdue_tasks


def test_creation():
    #arrange
    today = date(2000, 1, 1)
    calender = CalenderStub(today)
    tasklist = TaskList(calender)

    #assert
    assert len(tasklist) == 0
    assert [] == tasklist.due_tasks
    assert [] == tasklist.finished_tasks
    assert [] == tasklist.overdue_tasks

def test_adding_task_with_due_day_in_future():
    #arrange
    today = date(2000, 1, 1)
    future = date(2000, 2, 4)
    calender = CalenderStub(today)
    task = Task("de beste beschrijving ooit", future)
    tasklist = TaskList(calender)

    #act
    tasklist.add_task(task)


    #assert
    assert [task] == tasklist.due_tasks

def test_adding_task_with_due_day_in_past():
    #arrange
    today = date(2000, 1, 1)
    past = date(1999, 1, 1)
    cs = CalenderStub(today)
    task = Task("adfaservsd", past)
    tasklist = TaskList(cs)

    #act
    with pytest.raises(RuntimeError):
        tasklist.add_task(task)
    assert 0 == len(tasklist)

def test_task_becomes_finished():
    #arrange
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    future = date(2001, 1, 1)
    cs = CalenderStub(today)
    task = Task("asdfasdf", tomorrow)
    tasklist = TaskList(cs)

    #act
    tasklist.add_task(task)
    task.finished = True

    #assert
    assert [task] == tasklist.finished_tasks
    assert [] == tasklist.due_tasks
     