from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Thuan")

pet = Pet("Mochi", "dog")
owner.add_pet(pet)

pet.add_task(Task("Walk", 20, "high"))
pet.add_task(Task("Feed", 10, "medium"))
pet.add_task(Task("Play", 15, "low"))

scheduler = Scheduler()

tasks = scheduler.get_all_tasks(owner)
tasks = scheduler.sort_tasks(tasks)

print("Today's Schedule:")
for t in tasks:
    print(f"{t.title} - {t.priority}")