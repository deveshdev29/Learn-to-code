from calculator import addition



def test_positive():
    assert addition(2,2) == 4
    assert addition(3,2) == 5

def test_negative():
    assert addition(-3,2) == -1
    assert addition(-2,-2) == -4

def test_zero():
    assert addition(0,0) == 0

    
if __name__ == "__main__":
    main()