from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Thuan")

pet1 = Pet("Milo", "Dog")
pet2 = Pet("Luna", "Cat")

task1 = Task("Feed Breakfast", 15, "high", datetime(2026, 3, 29, 8, 0), "daily")
task2 = Task("Walk Dog", 30, "medium", datetime(2026, 3, 29, 8, 0), "none")
task3 = Task("Vet Appointment", 60, "high", datetime(2026, 3, 29, 10, 0), "none")
task4 = Task("Give Medicine", 10, "medium", datetime(2026, 3, 30, 9, 0), "weekly")

pet1.add_task(task1)
pet1.add_task(task2)
pet2.add_task(task3)
pet2.add_task(task4)

owner.add_pet(pet1)
owner.add_pet(pet2)

scheduler = Scheduler()
all_tasks = scheduler.get_all_tasks(owner)

print("\n--- Sorted by Time ---")
for task in scheduler.sort_tasks_by_time(all_tasks):
    print(task)

print("\n--- Incomplete Tasks ---")
for task in scheduler.filter_tasks_by_status(all_tasks, False):
    print(task)

print("\n--- Tasks for Milo ---")
for task in scheduler.filter_tasks_by_pet(owner, "Milo"):
    print(task)

print("\n--- Complete Daily Task ---")
scheduler.complete_task(pet1, "Feed Breakfast")

for task in pet1.tasks:
    print(task)

print("\n--- Conflict Detection ---")
conflicts = scheduler.detect_conflicts(scheduler.get_all_tasks(owner))

if conflicts:
    for t1, t2 in conflicts:
        print(f"Conflict: '{t1.title}' and '{t2.title}' at {t1.due_time.strftime('%Y-%m-%d %H:%M')}")
else:
    print("No conflicts found.")