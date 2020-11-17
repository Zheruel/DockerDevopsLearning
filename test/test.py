import requests
import sys

SERVICE2_URL = "http://service2:8080"

message = "test"

r = requests.post(SERVICE2_URL, data=message)


if r.text.strip() == "098f6bcd4621d373cade4e832627b4f6":
    print("Test passed")
    exit(0)
    
else:
    print("Test failed")
    exit(1)