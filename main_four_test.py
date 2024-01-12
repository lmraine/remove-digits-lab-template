import main

def test_main():
    word = "123four56"
    assert main.remove_digits(word) == "four"