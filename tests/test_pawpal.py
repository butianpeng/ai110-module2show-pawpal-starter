from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date, timedelta

def test_task_completion():
    task = Task(name="Walk", duration=20, priority=3)
    task.mark_complete()
    assert task.completed == True

def test_task_addition():
    pet = Pet(name="Buddy", type="dog")
    task = Task(name="Feed", duration=10, priority=5)
    pet.add_task(task)
    assert len(pet.tasks) == 1

def test_sorting_correctness():
    owner = Owner(name="James", time_available=60)
    pet = Pet(name="Buddy", type="dog")
    pet.add_task(Task(name="Walk", duration=20, priority=1))
    pet.add_task(Task(name="Feed", duration=10, priority=5))
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()
    assert sorted_tasks[0].duration <= sorted_tasks[1].duration

def test_recurrence_logic():
    task = Task(name="Walk", duration=20, priority=3, frequency="daily")
    next_date = task.next_occurrence()
    assert next_date == date.today() + timedelta(days=1)

def test_conflict_detection():
    owner = Owner(name="James", time_available=60)
    pet = Pet(name="Buddy", type="dog")
    pet.add_task(Task(name="Walk", duration=20, priority=3))
    pet.add_task(Task(name="Walk", duration=20, priority=3))
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) > 0