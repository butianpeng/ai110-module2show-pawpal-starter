from dataclasses import dataclass, field
from typing import List
from datetime import date, timedelta

@dataclass
class Task:
    name: str
    duration: int
    priority: int
    frequency: str = "daily"
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def next_occurrence(self):
        """Return the next due date based on frequency."""
        today = date.today()
        if self.frequency == "daily":
            return today + timedelta(days=1)
        elif self.frequency == "weekly":
            return today + timedelta(weeks=1)
        else:
            return None
        
    def __str__(self):
        """Return a readable string for this task."""
        return f"{self.name} ({self.duration} mins, priority {self.priority})"

@dataclass
class Pet:
    name: str
    type: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def get_all_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks

@dataclass
class Owner:
    name: str
    time_available: int
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's pet list."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_all_tasks())
        return all_tasks

class Scheduler:
    def __init__(self, owner: Owner):
        """Initialize scheduler with an owner and their tasks."""
        self.owner = owner
        self.tasks = owner.get_all_tasks()
        self.constraints = {"time_available": owner.time_available}

    def sort_by_priority(self):
        """Sort tasks from highest to lowest priority."""
        return sorted(self.tasks, key=lambda t: t.priority, reverse=True)

    def generate_plan(self):
        """Generate a daily plan within the owner's available time."""
        sorted_tasks = self.sort_by_priority()
        plan = []
        time_left = self.constraints.get("time_available", 60)
        for task in sorted_tasks:
            if task.duration <= time_left:
                plan.append(task)
                time_left -= task.duration
        return plan

    def sort_by_time(self):
        """Sort tasks by duration, shortest first."""
        return sorted(self.tasks, key=lambda t: t.duration)

    def filter_by_pet(self, pet_name: str):
        """Filter tasks belonging to a specific pet."""
        for pet in self.owner.pets:
            if pet.name == pet_name:
                return pet.get_all_tasks()
        return []

    def filter_incomplete(self):
        """Return only tasks that are not yet completed."""
        return [t for t in self.tasks if not t.completed]
    
    def detect_conflicts(self):
        """Warn if two tasks have the same name scheduled together."""
        seen = []
        conflicts = []
        for task in self.tasks:
            if task.name in seen:
                conflicts.append(f"Conflict: '{task.name}' appears more than once!")
            else:
                seen.append(task.name)
        return conflicts