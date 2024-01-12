import main

def test_main():
    word = "12 * 12 = 144"
    assert main.remove_digits(word) == " *  = "