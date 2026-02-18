from planet import *
import pytest
    
def test_planet_moons():
    for key, val in planetDict.items():
        if key == "Venus":
            assert(val.moon_list == [])
        elif key == "Uranus":
            for i in range(len(val.moon_list)):
                if val.moon_list[i].name == "Sycorax":
                    assert(val.moon_list[i].name == "Sycorax")
        elif key == "Earth":
            assert(val.moon_list[0].name == "Moon")
            
def test_planet_moon_amount():
    for key, val in planetDict.items():
        if key == "Mars":
            assert(len(val.moon_list) == 2)
        elif key == "Jupiter":
            assert(len(val.moon_list) == 79)
        elif key == "Neptune":
            assert(len(val.moon_list) == 14)