from playingcard import PlayingCard


def test_set_name():
    no_name = PlayingCard(2, "Diamonds")
    assert(no_name.name is None)
    named = PlayingCard(1, "Diamonds")
    assert(named.name == "Ace")


def test_str():
    no_name = PlayingCard(2, "Diamonds")
    assert(str(no_name) == "2 of Diamonds")
    named = PlayingCard(1, "Diamonds")
    assert(str(named) == "Ace of Diamonds")


def test_eq():
    no_name = PlayingCard(2, "Diamonds")
    named = PlayingCard(1, "Diamonds")
    assert(no_name != named)
    assert(no_name == PlayingCard(2, "Diamonds"))
    assert(named != "Ace of Diamonds")
