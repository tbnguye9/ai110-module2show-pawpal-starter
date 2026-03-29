from dataclasses import dataclass, field
from typing import List

# Task class
@dataclass
class Task:
    title: str
    duration: int
    priority: str
    completed: bool = False

    def mark_complete(self):
        self.completed = True
        


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