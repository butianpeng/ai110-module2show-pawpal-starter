from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    name: str
    duration: int
    priority: int
    completed: bool = False

    def mark_complete(self):
        self.completed = True

@dataclass
class Pet:
    name: str
    type: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

@dataclass
class Owner:
    name: str
    time_available: int
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

class Scheduler:
    def __init__(self, tasks: List[Task], constraints: dict):
        self.tasks = tasks
        self.constraints = constraints

    def sort_by_priority(self):
        return sorted(self.tasks, key=lambda t: t.priority, reverse=True)

    def generate_plan(self):
        return self.sort_by_priority()