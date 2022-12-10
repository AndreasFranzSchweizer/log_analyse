def is_connection_entry(text):
    if "New connection from" in text:
        return True
    return False


def test_is_connection_entry():
    assert is_connection_entry("1668755969: New connection from 2001:470:1:c84::11:4014 on port 1883.")
    assert not is_connection_entry("1668755969: New connectionfrom 2001:470:1:c84::11:4014 on port 1883.")
    assert is_connection_entry("1668743768: New connection from 103.56.61.147:46614 on port 1883.")
