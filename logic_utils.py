def get_range_for_difficulty(difficulty: str):
    """
    Return the numeric range for a given difficulty level.

    Input: difficulty (str) — one of "Easy", "Normal", or "Hard".
    Returns: a tuple (low, high) representing the inclusive guessing range.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 200


def parse_guess(raw: str):
    """
    Validate and parse a raw text input into an integer guess.

    Input: raw (str) — the raw string entered by the user in the text box.
    Returns: a tuple (ok, value, error_message) where ok is a bool indicating
             success, value is the parsed int (or None on failure), and
             error_message is a string describing the problem (or None on success).
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    elif "." in raw:
        return False, None, "No decimals allowed. Enter an integer."

    if raw.isdigit():
        value = int(raw)
    elif raw.isalpha():
        return False, None, "No letters allowed. Please enter a number."
    elif '-' in raw:
        return False, None, "Negative numbers are not allowed. Please enter a positive number."
    else:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret, low: int, high: int):
    """
    Compare the player's guess against the secret number and return a result.

    Input: guess (int) — the player's parsed integer guess.
           secret (int) — the secret number to guess.
           low (int) — the lower bound of the valid range (used in error messages).
           high (int) — the upper bound of the valid range (used in error messages).
    Returns: a tuple (outcome, message) where outcome is one of "Win", "Too High",
             "Too Low", or "Invalid", and message is a user-facing feedback string.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"

    except TypeError:
        return "Invalid", f"Please enter a number between {low} and {high}."


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Calculate the updated score based on the outcome of a guess.

    Input: current_score (int) — the player's score before this guess.
           outcome (str) — the result of the guess: "Win", "Too High", or "Too Low".
           attempt_number (int) — the 1-based count of guesses made so far.
    Returns: the new score (int) after applying points for the given outcome.
             Win awards 100 - 10*(attempt_number-1) points, minimum 10.
             Too High or Too Low deducts 5 points.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High" or outcome == "Too Low":
        return current_score - 5

    return current_score
