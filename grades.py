def average(scores):
    return sum(scores) / len(scores)
def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    return "F"