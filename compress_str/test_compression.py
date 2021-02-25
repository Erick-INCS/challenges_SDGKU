from compression import compress_str

def test_compression():
    test_str = compress_str('aaaabbcccccdddea')
    assert test_str == '5a2b5c3d1e'