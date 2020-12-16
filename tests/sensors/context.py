#!/usr/bin/python3
"""Context for testing sensors"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# pylint: disable=import-error
from snraspi.sensors import EnvironmentSensor