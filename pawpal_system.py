from asyncio import tasks
from dataclasses import dataclass, field
from typing import List
from datetime import datetime, timedelta

# Task class
@dataclass
class Task:
    title: str
    duration: int
    priority: str
    due_time: datetime
    recurrence: str = "none"
    completed: bool = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        return (
            f"{self.title} ({self.duration} mins, {self.priority}, "
            f"due: {self.due_time.strftime('%Y-%m-%d %H:%M')}, "
            f"recurrence: {self.recurrence}, completed: {self.completed})"
        ) 


# Pet class
@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)


# Owner class
@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        self.pets.append(pet)


# Scheduler class
class Scheduler:
    def get_all_tasks(self, owner: Owner):
        tasks = []
        for pet in owner.pets:
            tasks.extend(pet.tasks)
        return tasks

    def sort_tasks(self, tasks):
        priority_order = {"high": 1, "medium": 2, "low": 3}
        return sorted(tasks, key=lambda t: priority_order[t.priority])

    def sort_tasks_by_time(self, tasks):
        return sorted(tasks, key=lambda t: t.due_time)

    def filter_tasks_by_status(self, tasks, completed: bool):
        return [task for task in tasks if task.completed == completed]

    def filter_tasks_by_pet(self, owner: Owner, pet_name: str):
        for pet in owner.pets:
            if pet.name.lower() == pet_name.lower():
                return pet.tasks
        return []

    def complete_task(self, pet: Pet, task_title: str):
        for task in pet.tasks:
            if task.title == task_title and not task.completed:
                task.mark_complete()

                if task.recurrence == "daily":
                    new_task = Task(
                        title=task.title,
                        duration=task.duration,
                        priority=task.priority,
                        due_time=task.due_time + timedelta(days=1),
                        recurrence="daily"
                    )
                    pet.add_task(new_task)

                elif task.recurrence == "weekly":
                    new_task = Task(
                        title=task.title,
                        duration=task.duration,
                        priority=task.priority,
                        due_time=task.due_time + timedelta(weeks=1),
                        recurrence="weekly"
                    )
                    pet.add_task(new_task)

                return True
        return False

    def detect_conflicts(self, tasks):
        conflicts = []
        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                if tasks[i].due_time == tasks[j].due_time:
                    conflicts.append((tasks[i], tasks[j]))
        return conflicts


    