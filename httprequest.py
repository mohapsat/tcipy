# request.py
import requests
import json


def get_uuid(url):
    """
    Returns UUID4.
    :param url: http://httpbin.org/uuid
    :return: json
    """
    response = requests.get(url)
    return response

def get_header(url):
    """
    Returns header dict.
    :param url: http://httpbin.org/headers
    :return: json
    """
    header = requests.get(url)
    return header.text
