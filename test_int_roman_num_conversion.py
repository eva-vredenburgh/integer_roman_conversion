#unit test coverage

from integer_roman_conversion import conversion_function

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