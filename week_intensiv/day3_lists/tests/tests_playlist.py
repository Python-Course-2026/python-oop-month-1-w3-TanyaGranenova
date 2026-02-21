import pytest
from  week_intensiv.day3_lists.tasks.playlist import Playlist

def test_playlist_duration():
    pl = Playlist()
    pl.tracks = [180, 220, 100] # секунды
    assert pl.get_duration() == 500, "Неверный подсчет общей длительности"

def test_playlist_empty():
    pl = Playlist()
    assert pl.get_duration() == 0, "Длительность пустого плейлиста должна быть 0"