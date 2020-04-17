import requests

# Sample URLS
urls = [ "http://api.open-notify.org/iss-now.json",
         "https://example.com",
         "https://python.org/"         
       ]

# Get responses form the sample sites
responses = []
for url in urls:
    responses.append(requests.get(url))


# Print the response parts out for comparison
print(f"APPARENT_ENCODING ")
for resp in responses:
    print(f"{resp.apparent_encoding}\n")

print(f"\n\nCLOSE")
for resp in responses:
    print(f"{resp.close()}\n") 

print(f"\n\nCONNECTION")
for resp in responses:
    print(f"{resp.connection}\n") 

print(f"\n\nCONTENT")
for resp in responses:
    #print(f"{resp.content}\n") 
    pass

print(f"\n\nCOOKIES")
for resp in responses:
    print(f"{resp.cookies}\n") 

print(f"\n\nELAPSED")
for resp in responses:
    print(f"{resp.elapsed}\n") 

print(f"\n\nENCODING")
for resp in responses:
    print(f"{resp.encoding}\n") 

print(f"\n\nHEADERS")
for resp in responses:
    print(f"{resp.headers}\n") 

print(f"\n\nHISTORY")
for resp in responses:
    print(f"{resp.history}\n") 

print(f"\n\nIS_PERMANENT_REDIRECT")
for resp in responses:
    print(f"{resp.is_permanent_redirect}\n") 

print(f"\n\nIS_REDIRECT")
for resp in responses:
    print(f"{resp.is_redirect}\n") 

print(f"\n\nITER_CONTENT")
for resp in responses:
    print(f"{resp.iter_content()}\n") 

print(f"\n\nITER_LINES")
for resp in responses:
    print(f"{resp.iter_lines()}\n") 

print(f"\n\nJSON")
for resp in responses:
    # No json on example.com, causes error with json()
    #print(f"{resp.json()}\n") 
    print(f"{resp.json}\n") 

print(f"\n\nLINKS")
for resp in responses:
    print(f"{resp.links}\n") 

print(f"\n\nNEXT")
for resp in responses:
    print(f"{resp.next}\n") 

print(f"\n\nOK")
for resp in responses:
    print(f"{resp.ok}\n") 

print(f"\n\nRAISE_FOR_STATUS")
for resp in responses:
    print(f"{resp.raise_for_status}\n") 

print(f"\n\nRAW")
for resp in responses:
    print(f"{resp.raw}\n") 

print(f"\n\nREASON")
for resp in responses:
    print(f"{resp.reason}\n") 

print(f"\n\nREQUEST")
for resp in responses:
    print(f"{resp.request}\n") 

print(f"\n\nSTATUS_CODE")
for resp in responses:
    print(f"{resp.status_code}\n") 

print(f"\n\nTEXT")
for resp in responses:
    # python.org has an encoding error converting to ascii output
    #print(f"{resp.text}\n") 
    pass

print(f"\n\nURL")
for resp in responses:
    print(f"{resp.url}\n")
