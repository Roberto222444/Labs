import pytest

from schedule import get_schedule

schedule = [
    {
        "day": "Monday",
        "subject": "Mathematics",
        "time": "09:00",
        "room": "101"
    },
    {
        "day": "Monday",
        "subject": "Programming",
        "time": "11:00",
        "room": "205"
    },
    {
        "day": "Tuesday",
        "subject": "English",
        "time": "10:00",
        "room": "303"
    }
]
def test_get_schedule_monday():
    result = get_schedule(schedule, "Monday")

    assert len(result) == 2
    
def test_get_schedule_empty_day():
    result = get_schedule(schedule, "Sunday")
    
    assert result == []
    
def test_get_schedule_tuesday():
    result = get_schedule(schedule, "Tuesday")
    assert len(result) == 1    

def test_get_schedule_case_insensitive():
    result = get_schedule(schedule, "MONDAY")

    assert len(result) == 2
    
def test_get_schedule_invalid_input():
    with pytest.raises(TypeError):
        get_schedule("not a list", "Monday")