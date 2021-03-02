from reverse_alphabet import traspose

def test_traspose():
    assert traspose('abcdefghijklmnopqrstuvwxyz') == 'zyxwvutsrqponmlkjihgfedcba'
    assert traspose('alpha') == 'zoksz'
