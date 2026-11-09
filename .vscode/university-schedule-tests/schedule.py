def get_schedule(schedule, day):
    if not isinstance(schedule, list):
        raise TypeError("Schedule must be a list")

    if not isinstance(day, str):
        raise TypeError("Day must be a string")

    result = []

    for lesson in schedule:
        if lesson["day"].lower() == day.lower():
            result.append(lesson)

    return result

def test_get_schedule_monday():
    result = get_schedule(schedule, "Monday")

    assert len(result) == 2