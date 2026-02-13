from app import add, sub, multipuly, division
# def test_add():
#     result = add(2,3)
#     assert result == 6

# def test_sub():
#     result = sub(2,3)
#     assert result == -1

# def test_mul():
#     result = multipuly(2,3)
#     assert result == 6

# def test_dev():
#     result = division(10,5)
#     assert result == 2

def test_calc():
    assert add(1,2)==3
    assert sub(9,1)==8
    assert multipuly(3,4)==12

def test_calc_add():
    assert add(1,2)==3
    assert add(9,1)==10
    assert add(3,4)==7



