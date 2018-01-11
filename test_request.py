import httprequest
import json


def test_get_uuid():
    url = "http://httpbin.org/uuid"
    status = httprequest.get_uuid(url).status_code
    assert status == 200


def test_get_header():
    url = "http://httpbin.org/headers"
    response = httprequest.get_header(url)
    json_resp = json.loads(response)
    assert json_resp["headers"]["Host"] == "httpbin.org"


