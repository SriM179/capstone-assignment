from grades import average

def test_letter_grade():
    assert letter_grade(95) == "A"
    assert letter_grade(72) == "C"