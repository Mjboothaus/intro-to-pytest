import os
import sys
import pytest

# fixtures/test_monkeypatch.py
def func():
    print("platform: " + sys.platform)
    print("PATH: " + os.environ.get("PATH", ""))

def test_one(monkeypatch):
    monkeypatch.setattr(sys, "platform", "MonkeyOS")
    monkeypatch.setenv("PATH", "/zoo")
    func()
    assert False

def test_two():
    func()
    assert False
