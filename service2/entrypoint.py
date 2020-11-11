import requests
import sys

SERVICE1_URL = "http://service1:8080"

message = sys.stdin.readline()
data = ["md5", message]

print(requests.post(SERVICE1_URL, data="\n".join(data)).content)