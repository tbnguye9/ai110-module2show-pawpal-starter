# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The system is designed using four main classes:

- Owner: manages pets
- Pet: stores tasks for each pet
- Task: represents a care activity (walk, feed, etc.)
- Scheduler: generates and organizes tasks into a schedule

The Owner contains multiple Pets, and each Pet contains multiple Tasks.
The Scheduler collects all tasks and determines their execution order.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

During implementation, I added a priority-based sorting mechanism in the Scheduler class.
This change ensures that more important tasks are completed first, improving usability.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers task priority (high, medium, low) as the main constraint.
Higher priority tasks are scheduled first.

I chose priority as the main factor because it directly impacts the importance of tasks.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The system prioritizes task importance over time optimization.

This tradeoff is reasonable because completing important tasks is more critical than optimizing schedule efficiency.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI to help design class structures, generate initial code, and debug issues.

One AI suggestion I modified was how to retrieve tasks. Initially, AI suggested adding a method inside the Pet class, but I decided to use a separate Scheduler class instead. This keeps responsibilities separated and improves system design.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

I did not accept one AI suggestion about placing task retrieval logic inside the Pet class. Instead, I moved that logic to a separate Scheduler class to maintain clear separation of responsibilities.

I verified this decision by testing the system and ensuring that tasks were correctly collected and sorted through the Scheduler. This approach made the code more modular and easier to maintain.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task completion and task addition.

These tests ensure that core functionalities of the system work correctly.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am confident that the scheduler works correctly for basic cases.

If I had more time, I would test edge cases such as empty task lists and tasks with equal priority.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The system design and implementation went smoothly.
The use of classes helped organize the code clearly.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would improve the scheduling algorithm to consider time constraints and optimize task order further.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

I learned how to design a system using object-oriented principles and how to collaborate effectively with AI tools.
Additionally, in Phase 3, I successfully connected the Streamlit UI to the backend logic using session_state. This allowed tasks and pets to persist across interactions and enabled real-time schedule generation.

## Phase 4 – Algorithmic Layer

In Phase 4, I enhanced PawPal+ by adding core algorithmic features including sorting, filtering, recurring task handling, and conflict detection.

### Features Implemented

- Sorting tasks by due time using Python’s built-in `sorted()` function
- Filtering tasks by completion status and by pet
- Automatically generating recurring tasks (daily and weekly) when a task is marked complete
- Detecting scheduling conflicts when two tasks share the same due time

### Design Choices

- I used Python’s `datetime` and `timedelta` to handle time calculations for recurring tasks.
- I used list comprehensions for filtering because they are concise and readable.
- I implemented conflict detection using a simple pairwise comparison approach.

### Tradeoffs

- Conflict detection only checks for exact matching times and does not handle overlapping durations.
- Recurring tasks are only generated when the original task is completed, not automatically over time.
- The current implementation prioritizes readability over performance.

### Reflection

I focused on keeping the logic simple and easy to understand while still meeting all functional requirements. This approach makes the system easier to maintain and extend in future phases.

## Phase 5 Reflection

In this phase, I implemented automated tests to verify the core functionality of the PawPal system. The tests cover task completion, scheduling, sorting by time, conflict detection, and recurring tasks.

Using pytest helped ensure that the system behaves correctly under both normal and edge-case scenarios. It also improved confidence in the reliability and correctness of the scheduling logic.

Overall, this phase demonstrated the importance of automated testing in validating software behavior and preventing future bugs.

## Phase 6 Reflection

In this final phase, I polished the Streamlit user interface and connected it to the backend scheduling logic.

The UI allows the user to:

- create an owner and pet
- add tasks with title, duration, priority, and due time
- generate a schedule sorted by due time
- detect conflicts when multiple tasks have the same due time

I used AI tools such as ChatGPT and Copilot to help with debugging, testing, and improving the UI integration. AI was especially helpful when generating pytest test cases, identifying missing parameters like `due_time`, and resolving Streamlit issues such as duplicate widget IDs.

One important lesson I learned is that AI suggestions must always be reviewed and adapted to match the actual implementation. Some suggested method names did not exist in my code, so I had to compare the recommendations with my real classes and functions before applying them.

Using separate chat sessions for different phases helped me stay organized and focus on one goal at a time. Overall, this project helped me better understand scheduling logic, automated testing, UI integration, and how to work effectively with AI as the human lead architect.

I revisited my initial UML diagram in Phase 6 and updated it to match the final implementation.
