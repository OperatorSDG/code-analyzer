import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from analyzer import analyze_code

def test_analyze_code():
    assert analyze_code() == "Code analysis not implemented yet!"