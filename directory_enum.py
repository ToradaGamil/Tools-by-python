import requests
import sys
sub_list = open("wordlist2.txt").read()
directories = sub_list.splitlines()
if len(sys.argv) < 2 :
    print("for help use -h")
if sys.argv[1] == "-h":
    print("usage : \n directory_enum ip/ ext "
    + "\n directory_enum ip dir"
         )
elif sys.argv[2] == "dir":
    for dir in directories:
        dir_enum = f"http://{sys.argv[1]}/{dir}"
        r = requests.get(dir_enum)
        if r.status_code==404:
            pass
        else:
            print("Valid directory:" ,dir_enum)
elif sys.argv[2] == 'html':
    for dir in directories:
        dir_enum = f"http://{sys.argv[1]}/{dir}.{sys.argv[2]}"
        r = requests.get(dir_enum)
        if r.status_code==404:
            pass
        else:
            print("Valid directory:" ,dir_enum)