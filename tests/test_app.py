import ipaddress

import pytest

from app import app, get_ip_address


def test_ip_lookup_for_valid_domain():
    ip = get_ip_address("example.com")
    ipaddress.ip_address(ip)


def test_home_page_renders():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"URL IP Lookup" in response.data


def test_invalid_domain_raises_value_error():
    with pytest.raises(ValueError):
        get_ip_address("not-a-real-domain-12345.invalid")
