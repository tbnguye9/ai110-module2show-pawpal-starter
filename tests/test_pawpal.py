from datetime import datetime, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


def test_mark_complete():
    task = Task("Walk", 20, "high", datetime(2026, 3, 29, 8, 0))
    task.mark_complete()
    assert task.completed is True


def test_add_task():
    pet = Pet("Dog", "dog")
    task = Task("Feed", 10, "medium", datetime(2026, 3, 29, 9, 0))
    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].title == "Feed"
    assert pet.tasks[0].duration == 10
    assert pet.tasks[0].priority == "medium"


def test_get_all_tasks():
    owner = Owner("Thuan")
    pet1 = Pet("Milo", "dog")
    pet2 = Pet("Luna", "cat")

    task1 = Task("Feed Breakfast", 15, "medium", datetime(2026, 3, 29, 8, 0))
    task2 = Task("Vet Appointment", 30, "high", datetime(2026, 3, 29, 10, 0))

    pet1.add_task(task1)
    pet2.add_task(task2)

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    scheduler = Scheduler()
    all_tasks = scheduler.get_all_tasks(owner)

    assert len(all_tasks) == 2
    assert task1 in all_tasks
    assert task2 in all_tasks


def test_tasks_are_sorted_by_time():
    scheduler = Scheduler()

    task1 = Task("Vet Appointment", 30, "high", datetime(2026, 3, 29, 10, 0))
    task2 = Task("Give Medicine", 10, "medium", datetime(2026, 3, 29, 9, 0))
    task3 = Task("Feed Breakfast", 15, "low", datetime(2026, 3, 29, 8, 0))

    tasks = [task1, task2, task3]
    sorted_tasks = scheduler.sort_tasks_by_time(tasks)

    assert sorted_tasks[0].title == "Feed Breakfast"
    assert sorted_tasks[1].title == "Give Medicine"
    assert sorted_tasks[2].title == "Vet Appointment"


def test_conflict_detection():
    scheduler = Scheduler()

    same_time = datetime(2026, 3, 29, 8, 0)
    task1 = Task("Walk Dog", 20, "high", same_time)
    task2 = Task("Feed Breakfast", 10, "medium", same_time)

    conflicts = scheduler.detect_conflicts([task1, task2])

    assert len(conflicts) == 1
    assert (task1, task2) in conflicts or (task2, task1) in conflicts


def test_daily_recurring_task():
    scheduler = Scheduler()
    pet = Pet("Milo", "dog")

    original_time = datetime(2026, 3, 29, 8, 0)
    task = Task("Feed", 10, "medium", original_time, recurrence="daily")
    pet.add_task(task)

    result = scheduler.complete_task(pet, "Feed")

    assert result is True
    assert task.completed is True
    assert len(pet.tasks) == 2
    assert pet.tasks[1].title == "Feed"
    assert pet.tasks[1].due_time == original_time + timedelta(days=1)
    assert pet.tasks[1].recurrence == "daily"
    assert pet.tasks[1].completed is False