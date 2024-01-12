import main

def test_main():
    word = "nodigit"
    assert main.remove_digits(word) == "nodigit"