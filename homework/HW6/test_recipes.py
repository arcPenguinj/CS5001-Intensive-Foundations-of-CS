from recipes import generate_valid_filename
from recipes import validate_user_input_menu
from recipes import val_userin_ingredient
from recipes import validate_user_input_time
from pytest import raises


def test_generate_valid_filename():
    with raises(ValueError):
        generate_valid_filename("   ")
    with raises(ValueError):
        generate_valid_filename(" 😂❤😍🤣")
    assert(generate_valid_filename("  a b") == 'a_b.txt')
    assert(generate_valid_filename(" A 😍") == 'a_.txt')
    assert(generate_valid_filename("  23 434") == '23_434.txt')
    assert(generate_valid_filename("A_B") == 'a_b.txt')
    assert(generate_valid_filename("A b") == 'a_b.txt')
    assert(generate_valid_filename(" A  ") == 'a.txt')


def test_validate_user_input_menu():
    with raises(ValueError):
        validate_user_input_menu("0")
    with raises(ValueError):
        validate_user_input_menu("5")
    with raises(ValueError):
        validate_user_input_menu("1.2")
    with raises(ValueError):
        validate_user_input_menu("two")
    assert(validate_user_input_menu("2") == 2)


def test_val_userin_ingredient():
    with raises(ValueError):
        val_userin_ingredient("")
    with raises(ValueError):
        val_userin_ingredient("    ")
    with raises(ValueError):
        val_userin_ingredient("  , ,  ")
    assert(val_userin_ingredient("  a , b ") == ["a", "b"])
    assert(val_userin_ingredient("  a ,") == ["a"])


def test_validate_user_input_time():
    with raises(ValueError):
        validate_user_input_time("-23")
    with raises(ValueError):
        validate_user_input_time("2.3")
    with raises(ValueError):
        validate_user_input_time("five")
    assert(validate_user_input_time("34") == 34)
    assert(validate_user_input_time("0") == 0)
