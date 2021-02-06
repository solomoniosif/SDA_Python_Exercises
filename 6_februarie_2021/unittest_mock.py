from unittest.mock import patch

def cow():
    print('cow')
    return {'cow': 'moo'}

def dog():
    print('dog')
    return {'dog': 'bark'}

def animals():
    data = cow()
    data.update(dog())
    data['pig'] = 'oik'
    return data

def test_cow():
    assert cow() == {'cow': 'moo'}

def test_dog():
    assert dog() == {'dog': 'bark'}

# def test_animals():
#     assert animals() == {'dog': 'bark', 'cow': 'moo', 'pig': 'oik'}

@patch('__main__.dog')
@patch('__main__.cow')
def test_animals(patched_dog, patched_cow):
    patched_cow.return_value = {'c': 'm'}
    patched_dog.return_value = {'d': 'b'}
    data = animals()
    assert patched_dog.called is True
    assert patched_cow.called is True
    assert data == {'d': 'b', 'c': 'm', 'pig': 'oik'}

# test_cow()
# test_dog()
test_animals()
