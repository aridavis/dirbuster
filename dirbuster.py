import requests
from itertools import combinations 

wordlist = [
    "berspasi juga", "aa.txt"
]
URL = "https://github.com/aridavis/dirbuster/tree/master"

if __name__ == "__main__":

    wordlist = map(lambda x: x.strip(), wordlist)
    wordlist = map(lambda x: x.replace(" ", "%20"), wordlist)
    wordlist = list(wordlist)

    x = 0
    for i in range(0, len(wordlist)):
        combination = list(combinations(wordlist,i+1))
        for j in range(0,len(combination)):
            postfix = ""
            for k in range(0, i+1):
                postfix = postfix + "/{}".format(combination[j][k])
            res = requests.get(URL + postfix)
            if(res.status_code == 200):
                print(URL + postfix)
