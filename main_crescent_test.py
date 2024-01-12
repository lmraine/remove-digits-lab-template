import main

def test_main():
    word = "1244Crescent"
    assert main.remove_digits(word) == "Crescent"