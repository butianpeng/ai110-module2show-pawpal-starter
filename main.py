from pawpal_system import Task, Pet, Owner, Scheduler

# Create owner
owner = Owner(name="James", time_available=60)

# Create two pets
dog = Pet(name="Buddy", type="dog")
cat = Pet(name="Luna", type="cat")

# Add tasks to dog
dog.add_task(Task(name="Morning walk", duration=20, priority=3))
dog.add_task(Task(name="Feeding", duration=10, priority=5))

# Add tasks to cat
cat.add_task(Task(name="Grooming", duration=15, priority=2))
cat.add_task(Task(name="Meds", duration=5, priority=4))
cat.add_task(Task(name="Playtime", duration=20, priority=1))

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Generate plan
scheduler = Scheduler(owner)
plan = scheduler.generate_plan()

print("=== Today's Schedule ===")
for task in plan:
    print(f"- {task}")