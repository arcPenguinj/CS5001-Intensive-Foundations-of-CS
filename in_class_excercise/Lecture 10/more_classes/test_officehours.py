from officehours import OfficeHours


def test_is_happening_at():
    oh = OfficeHours(10, 12, "M", "Zoom", "Mr. T")
    assert(oh.is_happening_at(11, "M"))
    assert(oh.is_happening_at(11, "Tu") is False)
    assert(oh.is_happening_at(10, "M"))
    assert(oh.is_happening_at(12, "M"))
    assert(oh.is_happening_at(9, "M") is False)

