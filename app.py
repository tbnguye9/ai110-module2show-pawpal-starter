import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime


if "owner" not in st.session_state:
    st.session_state.owner = None

if "pet" not in st.session_state:
    st.session_state.pet = None

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Create Owner and Pet"):
    st.session_state.owner = Owner(owner_name)
    st.session_state.pet = Pet(pet_name, species)
    st.session_state.owner.add_pet(st.session_state.pet)
    st.success(f"Created owner {owner_name} and pet {pet_name}")

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3, col4 = st.columns(4)

with col1:
    task_title = st.text_input("Task title", value="Morning walk")

with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)

with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

with col4:
    due_time = st.time_input("Due time")

if st.button("Add task"):
    if st.session_state.pet is None:
        st.warning("Please create the owner and pet first.")
    else:
        now = datetime.now()
        due_datetime = datetime.combine(now.date(), due_time)

        new_task = Task(task_title, int(duration), priority, due_datetime)
        st.session_state.pet.add_task(new_task)

        st.session_state.tasks.append(
            {"title": task_title, "duration_minutes": int(duration), "priority": priority}
        )

        st.success(f"Added task: {task_title}")

if st.session_state.tasks:
    st.write("Current tasks:")

    st.table([
        {
            "Title": t.title,
            "Time": t.due_time.strftime("%H:%M"),
            "Duration": t.duration,
            "Priority": t.priority,
            "Completed": t.completed
        }
        for t in st.session_state.pet.tasks
    ])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    if st.session_state.owner is None:
        st.warning("Please create the owner and pet first.")
    else:
        scheduler = Scheduler()

        all_tasks = scheduler.get_all_tasks(st.session_state.owner)
        sorted_tasks = scheduler.sort_tasks_by_time(all_tasks)

        if sorted_tasks:
            st.success("Schedule generated successfully!")
            st.table([
                {
                    "Title": t.title,
                    "Time": t.due_time.strftime("%H:%M"),
                    "Duration": t.duration,
                    "Priority": t.priority,
                    "Completed": "✅" if t.completed else "❌"
                }
                for t in sorted_tasks
            ])

            conflicts = scheduler.detect_conflicts(sorted_tasks)

            if conflicts:
                st.warning("⚠️ Conflict detected! Some tasks have the same time.")
            else:
                st.success("✅ No conflicts detected.")
        else:
            st.info("No tasks available.")
