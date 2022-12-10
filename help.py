def remove_port(host_with_port):
    if host_with_port.count('.') == 3 and host_with_port.count(':') == 1:
        return host_with_port.split(':')[0]
    elif host_with_port.count(':') > 1:
        return host_with_port.rsplit(':', 1)[0]
    else:
        return host_with_port


def test_remove_port():
    # IPv6 test
    assert remove_port("2001:470:1:c84::11:4014") == "2001:470:1:c84::11"
    # IPv4 test
    assert remove_port("103.56.61.147:46614") == "103.56.61.147"


def is_connection_entry(text):
    if "New connection from" in text:
        return True
    return False


def test_is_connection_entry():
    assert is_connection_entry("1668755969: New connection from 2001:470:1:c84::11:4014 on port 1883.")
    assert not is_connection_entry("1668755969: New connectionfrom 2001:470:1:c84::11:4014 on port 1883.")
    assert is_connection_entry("1668743768: New connection from 103.56.61.147:46614 on port 1883.")


def get_client_ip(text):
    if is_connection_entry(text):
        parts = text.split(' ')
        if len(parts) > 5:
            return parts[4]


def test_get_client_ip():
    assert get_client_ip("1668755969: New connection from 2001:470:1:c84::11:4014 on port 1883.") == "2001:470:1:c84::11:4014"
    assert get_client_ip("1668743768: New connection from 103.56.61.147:46614 on port 1883.") == "103.56.61.147:46614"
