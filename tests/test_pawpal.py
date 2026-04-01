from pawpal_system import Task, Pet, Owner, Scheduler

def test_task_completion():
    task = Task(name="Walk", duration=20, priority=3)
    task.mark_complete()
    assert task.completed == True

def test_task_addition():
    pet = Pet(name="Buddy", type="dog")
    task = Task(name="Feed", duration=10, priority=5)
    pet.add_task(task)
    assert len(pet.tasks) == 1