#!/usr/bin/python3
"""
Test EnvironmentSensor DHT22

Run with pytest
"""
from context import EnvironmentSensor

sensor = None

def test_init():
    global sensor
    sensor = EnvironmentSensor.DHT22(EnvironmentSensor.PIN13)
    assert sensor != None

def test_temperature():
    global sensor
    temp = sensor.temperature
    assert temp != None

def test_humidity():
    global sensor
    hum = sensor.humidity
    assert hum != None

def test_pressure():
    global sensor
    pres = sensor.pressure
    assert pres == None

def test_altitude():
    global sensor
    alt = sensor.altitude
    assert alt == None

def test_del():
    global sensor
    del sensor
    try:
        assert sensor == None
    except NameError:
        assert True
