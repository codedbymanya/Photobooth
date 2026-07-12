COUNTDOWN_STEPS = [
    (1, "3"),
    (2, "2"),
    (3, "1"),
    (4, "Smile"),
]   #Tuples
 
def get_countdown_text(elapsed):
    """
    Return the text to display for the given elapsed seconds since the
    countdown started, or None once the countdown is finished (i.e. the
    photo should be captured now).
    """
    for threshold, text in COUNTDOWN_STEPS:
        if elapsed < threshold:
            return text
    return None