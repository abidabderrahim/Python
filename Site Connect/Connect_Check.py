"""
tool with Python for check if website connect or not .
"""

import urllib.request as urllib

def main(url):
    print("Checking Connectivity ...")
    response = urllib.urlopen(url)
    print(f"Connect to {url} Succesfuly")
    print(f"Code Response is {response.getcode()} Ok")

print("# checking Connectivity of Your WebSite #")
url_check = str(input("Enter Your URL : "))
main(url_check)
