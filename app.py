import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# Step 1: Owner setup
st.subheader("Owner Info")
owner_name = st.text_input("Your name", value="James")
time_available = st.number_input("Time available today (minutes)", min_value=10, max_value=300, value=60)

# Step 2: Keep owner in memory
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name=owner_name, time_available=time_available)

# Step 3: Add a pet
st.subheader("Add a Pet")
pet_name = st.text_input("Pet name", value="Buddy")
pet_type = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add pet"):
    new_pet = Pet(name=pet_name, type=pet_type)
    st.session_state.owner.add_pet(new_pet)
    st.success(f"Added {pet_name}!")

# Step 4: Add a task
st.subheader("Add a Task")
task_name = st.text_input("Task name", value="Morning walk")
duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
priority = st.slider("Priority (1-5)", min_value=1, max_value=5, value=3)

if st.button("Add task"):
    if st.session_state.owner.pets:
        task = Task(name=task_name, duration=duration, priority=priority)
        st.session_state.owner.pets[-1].add_task(task)
        st.success(f"Added task: {task_name}")
    else:
        st.warning("Add a pet first!")

st.divider()

# Step 5: Generate schedule
st.subheader("Generate Today's Schedule")
if st.button("Generate schedule"):
    owner = st.session_state.owner
    if owner.get_all_tasks():
        scheduler = Scheduler(owner)
        plan = scheduler.generate_plan()
        st.success("Here's your plan:")
        for task in plan:
            st.markdown(f"- **{task.name}** — {task.duration} mins, priority {task.priority}")
    else:
        st.warning("Add some tasks first!")