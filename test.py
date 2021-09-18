
from nextday import next_day

def test_next_day():
    assert next_day(2021, 2, 4) == '2021-2-5'
    assert next_day(2021, 8, 24) == '2021-8-25'
    assert next_day(2021, 11, 30) == '2021-12-1'
    assert next_day(2021, 2, 25) == '2021-2-26'
    assert next_day(2021, 2, 28) == '2021-3-1'
    assert next_day(2021, 6, 30) == '2021-7-1'
    assert next_day(2021, 8, 31) == '2021-9-1'
    assert next_day(2021, 12, 31) == '2022-1-1'
    assert next_day(2020, 2, 29) == '2020-3-1'
    assert next_day(2020, 2, 28) == '2020-2-29'

def test_next_day_invalid():
    assert next_day(2021, 14, 30) == None
    assert next_day(2021, 1, 33) == None
    assert next_day(2021, 2, 29) == None
    assert next_day(2021, 6, 31) == None
    assert next_day(2020, 0, 28) == None
    assert next_day(2020, 2, 0) == None
    assert next_day(2020, -2, 0) == None
    assert next_day(2020, 0, -12) == None
    assert next_day(2020, 3, -12) == None
    assert next_day(1499, 5, 12) == None