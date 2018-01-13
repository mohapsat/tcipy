# request.py
import requests
import json

# def get_uuid(url):
#     """
#     Returns UUID4.
#     :param url: http://httpbin.org/uuid
#     :return: json
#     """
#     response = requests.get(url)
#     return response
#
# def get_header(url):
#     """
#     Returns header dict.
#     :param url: http://httpbin.org/headers
#     :return: json
#     """
#     header = requests.get(url)
#     return header.text

# url= "http://httpbin.org/uuid"
# response = requests.get(url)
# status_code = response.status_code
# print(status_code)

def get_statuscode(url):
    response = requests.get(url)
    status_code = response.status_code
    # return status_code
    print(status_code)
    return status_code
# url= "http://httpbin.org/uuid"
# get_statuscode(url)