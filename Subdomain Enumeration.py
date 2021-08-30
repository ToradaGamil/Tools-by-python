import sys
import requests
sub_list = open("wordlist2.txt").read()
subdoms = sub_list.splitlines()
for sub in subdoms :
    sub_test = f"http://{sub}.{sys.argv[1]}"
    try:
        requests.get(sub_test)

    except requests.ConnectionError:
        pass

    else:
        print("Valid domain: ", sub_test)
