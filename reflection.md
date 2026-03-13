# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

It was roughly playble. I understood the concept pretty quickly. Some button works but the logic of the game were primarily faulty. I've observed the bugs and list them down below. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1. The current app struggles with creating a new game. When the user completes their first round of the game and go on to make a new game, the app will reset the attempts back to 8, but will not register new guesses into the system. What I mean is, when the user submit their new guess using the "Submit Guess" button, the attempt remain the same(8) instead of going down. The expected behvaior is that when the new game is created, the user should be able to enter in new guesses and interact with the game without any influence from previous games. Essentially, the game begins at a new 'state'.  

2. The lower/higher logic checking must be incorrect. There is one time when the secret number is 26, but the program told the user to go LOWER when they entered 12. There is a clear logic error here. 

3. When the user still have 1 attempt left, the program said they ran out of attempts. This is a logic error. The "Out of attempt" message should only come up AFTER the user use up their last guess. 

4. When you press the new game button, the Game Over message doesn't go away. There was no proper status update of the new game. The expected behavior is when you press the button, it should display a blue message that says "New Game Created!" and update the right number to a different number. The previous dictionary that stores our previous guesses needs to be deleted while a new, clean dictionary is created to keep track of the new guesses. 

5. The Show Hint button doesn't seem to connect to anything. It should have displayed a message saying "the number is around x" under the guess box. 

6. The range for 'Harder' level is actually smaller -- which translates to an easier game. It should have been a larger range such as 1 - 200



---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
