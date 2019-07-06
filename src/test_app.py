from app import get_greeting

def test_get_greeting():
    greeting = get_greeting('test_name')
    expected = 'Hello' + 'test_name' + ', Welcome to the Tour'
    assert greeting == expected

from app import day_break

def test_day_break():
    in_month = day_break(35)
    expected = False
    assert in_month == expected

def test_day_notbreak():
    in_month = day_break(30)
    expected = 30
    assert in_month == expected

from app import month_break

def test_month_break():
    in_year = month_break(13)
    expected = False
    assert in_year == expected

def test_month_notbreak():
    in_year = month_break(10)
    expected = 10
    assert in_year == expected