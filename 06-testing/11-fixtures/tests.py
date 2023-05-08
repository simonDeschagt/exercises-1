from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalenderStub
import pytest


@pytest.fixture
def today():
    return date(2000, 1, 1)

@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)

@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)

@pytest.fixture
def cs(today):
    return CalenderStub(today)

@pytest.fixture
def tasklist(cs):
    return TaskList(cs)

def test_task_becomes_overdue(tomorrow, cs, tasklist):
    #arrange
    task = Task('some description', tomorrow)
    tasklist.add_task(task)

    #act
    cs.today = date(2000, 2, 2)

    #assert
    assert [task] == tasklist.overdue_tasks


def test_creation(tasklist):
    #arrange


    #assert
    assert len(tasklist) == 0
    assert [] == tasklist.due_tasks
    assert [] == tasklist.finished_tasks
    assert [] == tasklist.overdue_tasks

def test_adding_task_with_due_day_in_future(tomorrow, tasklist):
    #arrange
    task = Task("de beste beschrijving ooit", tomorrow)

    #act
    tasklist.add_task(task)


    #assert
    assert [task] == tasklist.due_tasks

def test_adding_task_with_due_day_in_past(yesterday, tasklist):
    #arrange
    task = Task("adfaservsd", yesterday)
    

    #act
    with pytest.raises(RuntimeError):
        tasklist.add_task(task)
    assert 0 == len(tasklist)

def test_task_becomes_finished(tomorrow, tasklist):
    #arrange
    task = Task("asdfasdf", tomorrow)
    

    #act
    tasklist.add_task(task)
    task.finished = True

    #assert
    assert [task] == tasklist.finished_tasks
    assert [] == tasklist.due_tasks
     