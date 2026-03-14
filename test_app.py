from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score


# ---------------------------------------------------------------------------
# get_range_for_difficulty
# ---------------------------------------------------------------------------

def test_easy_range():
    """Easy difficulty should return a range of 1 to 20."""
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    """Normal difficulty should return a range of 1 to 100."""
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_hard_range():
    """Hard difficulty should return a range of 1 to 200."""
    assert get_range_for_difficulty("Hard") == (1, 200)

def test_hard_range_larger_than_normal():
    """Hard difficulty should have a wider range than Normal, making it harder to guess."""
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_normal_range_larger_than_easy():
    """Normal difficulty should have a wider range than Easy, making it harder to guess."""
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert normal_high > easy_high


# ---------------------------------------------------------------------------
# parse_guess
# ---------------------------------------------------------------------------

def test_parse_empty_string():
    """An empty string should fail validation and prompt the user to enter a guess."""
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_none():
    """A None input (no text entered) should fail validation and prompt the user to enter a guess."""
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_decimal():
    """A decimal number should fail validation since only integers are accepted."""
    ok, value, err = parse_guess("3.5")
    assert ok is False
    assert value is None
    assert err == "No decimals allowed. Enter an integer."

def test_parse_letters():
    """A purely alphabetic input should fail validation and ask the user to enter a number."""
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "No letters allowed. Please enter a number."

def test_parse_negative():
    """A negative number should fail validation since all difficulty ranges start at 1."""
    ok, value, err = parse_guess("-5")
    assert ok is False
    assert value is None
    assert err == "Negative numbers are not allowed. Please enter a positive number."

def test_parse_mixed_invalid():
    """A mix of digits and letters should fail as an unrecognised input."""
    ok, value, err = parse_guess("12abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."

def test_parse_valid_integer():
    """A valid integer string should parse successfully and return the integer value."""
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_valid_single_digit():
    """A single-digit integer string should parse successfully and return the integer value."""
    ok, value, err = parse_guess("7")
    assert ok is True
    assert value == 7
    assert err is None

def test_parse_valid_large_number():
    """A large integer string (within Hard range) should parse successfully."""
    ok, value, err = parse_guess("199")
    assert ok is True
    assert value == 199
    assert err is None


# ---------------------------------------------------------------------------
# check_guess
# ---------------------------------------------------------------------------

def test_check_correct_guess():
    """Guessing the exact secret number should return a Win outcome with a congratulations message."""
    outcome, message = check_guess(42, 42, 1, 100)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_check_too_high():
    """A guess above the secret should return Too High and tell the player to go lower."""
    outcome, message = check_guess(80, 42, 1, 100)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_check_too_low():
    """A guess below the secret should return Too Low and tell the player to go higher."""
    outcome, message = check_guess(10, 42, 1, 100)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_check_boundary_one_below():
    """A guess exactly one below the secret should still be Too Low, not a win."""
    outcome, _ = check_guess(41, 42, 1, 100)
    assert outcome == "Too Low"

def test_check_boundary_one_above():
    """A guess exactly one above the secret should still be Too High, not a win."""
    outcome, _ = check_guess(43, 42, 1, 100)
    assert outcome == "Too High"

def test_check_type_error_returns_invalid():
    """If the secret is a non-integer type, a TypeError should be caught and return Invalid.
    This guards against the bug where the secret was cast to a string on even attempts."""
    outcome, message = check_guess(5, "not_a_number", 1, 100)
    assert outcome == "Invalid"
    assert "1" in message and "100" in message

def test_check_invalid_message_contains_range():
    """The Invalid error message should include the valid range boundaries so the player knows what to enter."""
    _, message = check_guess(5, "bad", 1, 200)
    assert "1" in message
    assert "200" in message


# ---------------------------------------------------------------------------
# update_score
# ---------------------------------------------------------------------------

def test_win_on_first_attempt():
    """Winning on the first attempt should award the maximum 100 points."""
    # Formula: 100 - 10*(1-1) = 100
    new_score = update_score(0, "Win", 1)
    assert new_score == 100

def test_win_on_fifth_attempt():
    """Winning on the fifth attempt should award 60 points (penalty for extra guesses)."""
    # Formula: 100 - 10*(5-1) = 60
    new_score = update_score(0, "Win", 5)
    assert new_score == 60

def test_win_on_tenth_attempt():
    """Winning on the tenth attempt should award exactly the minimum 10 points."""
    # Formula: 100 - 10*(10-1) = 10
    new_score = update_score(0, "Win", 10)
    assert new_score == 10

def test_win_score_minimum_cap():
    """Win points should never drop below 10, even at very high attempt numbers."""
    # Without cap: 100 - 10*(15-1) = -40; cap enforces minimum of 10
    new_score = update_score(0, "Win", 15)
    assert new_score == 10

def test_win_adds_to_existing_score():
    """Win points should be added on top of an existing score, not replace it."""
    new_score = update_score(50, "Win", 1)
    assert new_score == 150

def test_too_high_deducts_five():
    """A Too High guess should subtract 5 from the current score as a penalty."""
    new_score = update_score(100, "Too High", 3)
    assert new_score == 95

def test_too_low_deducts_five():
    """A Too Low guess should subtract 5 from the current score as a penalty."""
    new_score = update_score(100, "Too Low", 3)
    assert new_score == 95

def test_score_can_go_negative():
    """Score should be allowed to go negative if the player accrues enough penalties."""
    new_score = update_score(3, "Too Low", 1)
    assert new_score == -2

def test_unknown_outcome_leaves_score_unchanged():
    """An unrecognised outcome (e.g. Invalid) should leave the score untouched."""
    new_score = update_score(50, "Invalid", 1)
    assert new_score == 50
