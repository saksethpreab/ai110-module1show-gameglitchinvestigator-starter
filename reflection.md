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

I used Claude Code inside VSCode

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One of the bug that Claude suggested a correct change was the range for the difficulty level. It raises the illogical aspect of the given range. I told it to expand the range of possible values for harder levels. It also suggested more attempts for harder levels. I thought that was a great idea so I also implemented that. I verified the result by doing manual testing of the game. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

When refactoring the logic in the update_score function, Claude suggested that | points = 100 - 10 * (attempt_number + 1) |. This lead to issue with score calculation. I later changed it to | points = 100 - 10 * (attempt_number - 1) | I verified correctness by manual testing and writting out my thoughts on a whiteboard. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I did extensive manual testing on the program. For example, with the the user's guess, I tested some common and rare wrong inputs I can think of, then adapt the code to prevent errors. I also asked Claude to write some tests for the program based on the behavior discussed.  

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.  

I tested negative numbers, floats, and letters. I learned that the program was not built for diverse inputs. So after encountering issues, I had to fix it manually and verify with Claude. Now, the program will only accept positive integers.

  
- Did AI help you design or understand any tests? How?

Absolutely. I used Claude to understand the program's general structure, and identify loopholes in the program. I review and improve on suggested possible actions. I also used it to write tests for app.py  

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

Initially, the change of the secret number depended on whether the current attempt is an even or odd number. On submission where the attempt was updated to an even number, the secret was converted from an integer to a string. Thus, when we run the check_guess function, a TypeError occurs and a string comparison is made. Since string comparisons can be inaccurate, for example when '2' is compared with '20', our program was faulty. In addition, our 'go higher' or 'go lower' logic was switched up too.  

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

A rerun is when the program restarts everything from scratch. The only thing that it 'remembers' are all the variables that are stored in the previous 'state'

- What change did you make that finally gave the game a stable secret number?

I dissociate the secret number's dependency on attempts and I fixed the logic error in check_guess. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  Looking through the code by myself first is a good thing. Then using AI to ask question about the code or give general gist of how everything works together. Claude and I verify each other's solutions, and I think I'll carry that into future projects too.

- What is one thing you would do differently next time you work with AI on a coding task?

  Take more time reviewing the generated code and asking questions about it.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  I think it's really smart at detecting problems, but sometimes it can fail basic logic. I have to be specific. 
