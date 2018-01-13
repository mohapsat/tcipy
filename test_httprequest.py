import httprequest
# import pytest


def test_get_statuscode():
    url = "http://httpbin.org/uuid"
    status_code = httprequest.get_statuscode(url)
    assert status_code == 200



