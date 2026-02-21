import pytest
from  week_intensiv.day4_logic.tasks.event_planner import EventPlanner, Event


def test_event_date_filter():
    ep = EventPlanner()
    ep.add_event(Event("Python Conf", "2023-10-10", 100))
    ep.add_event(Event("Java Meetup", "2023-10-10", 50))
    ep.add_event(Event("AI Workshop", "2023-12-01", 30))

    events_10 = ep.get_events_on_date("2023-10-10")
    assert isinstance(events_10, list), "Метод должен возвращать список названий"
    assert len(events_10) == 2
    assert "Python Conf" in events_10
    assert "Java Meetup" in events_10


def test_total_participants():
    ep = EventPlanner()
    ep.add_event(Event("E1", "2023-01-01", 10))
    ep.add_event(Event("E2", "2023-01-02", 20))
    assert ep.get_total_participants() == 30


def test_planner_empty_date():
    ep = EventPlanner()
    assert ep.get_events_on_date("2023-01-01") == [], "На пустую дату должен возвращаться пустой список"