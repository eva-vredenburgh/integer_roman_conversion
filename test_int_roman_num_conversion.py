#unit test coverage

from integer_roman_conversion import conversion_function
import pytest

#small numbers
def test_small_num_1():
    result = conversion_function(1)
    assert result == "I"

def test_small_num_2():
    result = conversion_function(2)
    assert result == "II"

def test_small_num_3():
    result = conversion_function(8)
    assert result == "VIII"

#big numbers
def test_big_num_1():
    result = conversion_function(1000)
    assert result == "M"

def test_big_num_2():
    result = conversion_function(1512)
    assert result == "MDXII"

def test_big_num_3():
    result = conversion_function(3999)
    assert result == "MMMCMXCIX"

#Edge cases
def test_edge_1():
    result = conversion_function(4)
    assert result == "IV"

def test_edge_2():
    result = conversion_function(9)
    assert result == "IX"

def test_edge_3():
    result = conversion_function(400)
    assert result == "CD"

#repeating numerals
def test_repeat_1():
    result = conversion_function(3)
    assert result == "III"

def test_repeat_2():
    result = conversion_function(30)
    assert result == "XXX"

def test_repeat_3():
    result = conversion_function(300)
    assert result == "CCC"

#special cases
def test_zero():
    with pytest.raises(ValueError):
        conversion_function(0)

def test_missing():
    with pytest.raises(TypeError):
        conversion_function()

def test_string():
    with pytest.raises(TypeError):
        conversion_function("abc")

def test_neg1():
    with pytest.raises(ValueError):
        conversion_function(-5)

def test_neg2():
    with pytest.raises(ValueError):
        conversion_function(-250)