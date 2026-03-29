from pawpal_system import Task, Pet


def test_mark_complete():
    task = Task("Walk", 20, "high")
    task.mark_complete()
    assert task.completed == True


def test_add_task():
    pet = Pet("Dog", "dog")
    pet.add_task(Task("Feed", 10, "medium"))
    assert len(pet.tasks) == 1