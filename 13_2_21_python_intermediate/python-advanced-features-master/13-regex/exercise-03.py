"""
Write a pattern matching the following e-mails. Test it.
    bjandourek0@stanford.edu
    mtimothy1@deviantart.com
    mdodding2@de-decms.com
    kwessing3@linkedin.com
    cstallion4@printfriendly.com
"""
import re

pattern = re.compile("^[a-z0-9]+@[a-z0-9-]+\.[a-z]{2,10}")
emails = [
    "bjandourek0@stanford.edu",
    "mtimothy1@deviantart.com",
    "mdodding2@de-decms.com",
    "kwessing3@linkedin.com",
    "cstallion4@printfriendly.com",
]
for email in emails:
    match = pattern.search(email)
    if match:
        print(match.group())
