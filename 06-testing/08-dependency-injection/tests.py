from datetime import date
from tasks import Task, TaskList
from calendars import CalenderStub


def test_task_becomes_overdue():
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    test_date = date(2000, 5, 5)
    calender = CalenderStub(today)
    task = Task('some description', tomorrow)
    tasks = TaskList(calender)

    tasks.add_task(task)
    calender.today = test_date

    assert [task] == tasks.overdue_tasks