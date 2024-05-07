import pytest
import os

from z2 import merge_and_write


def test_merge_and_write():
    assert merge_and_write("text1.txt", "text2.txt", "text3.txt") == "some text"

def test_merge_and_write_no_one_file():
    assert merge_and_write("text1.txt", "text2.txt", "text4.txt") == "some text"


def test_merge_and_write_no_any_file():
    assert merge_and_write("text5.txt", "text6.txt", "text7.txt") == "Один из файлов не найден"


def test_merge_and_write_two_file():
    assert merge_and_write("text1.txt", "text1.txt", "text3.txt") == "some some"


def test_merge_and_write_no():
    assert merge_and_write("text1.txt", "text2.txt", "text3.txt") != "Один из файлов не найден"
