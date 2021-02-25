from compression import compress_str

def test_compression():
    test_str = compress_str('aaaabbcccccdddea')
    assert test_str == '4a2b5c3d1e1a'
    assert compress_str('abcdefg') == '1a1b1c1d1e1f1g'
    assert compress_str('g') == '1g'
    assert compress_str('abbbbbc') == '1a5b1c'
