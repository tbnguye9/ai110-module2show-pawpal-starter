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
AI was also helpful for creating test cases and improving code organization.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

I used AI to help design class structures, generate initial code, and debug issues.
AI was also helpful for creating test cases and improving code organization.

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
