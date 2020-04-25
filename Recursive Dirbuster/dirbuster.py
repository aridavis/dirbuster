import requests
from itertools import combinations 

wordlist = [
    "berspasi juga", "kucing", "folder", "meong", "secret", "key  ", "miaw", "gadak ini", "aa", "ada spasinya"
]

extensions = ["py","jpg", "extensionIni", "txt"]

URL = "http://localhost:80/Dirbuster"

def brute_list(word):
    if requests.get(URL + word).status_code == 404:
        return
    print(word)
    for i in wordlist:
        brute_list(word + '/' + i)
        for j in extensions:
            brute_list(word + '/' + i + '.' + j)

if __name__ == "__main__":
    res = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(str(res.status_code) + "\n" + res.text)

    wordlist = map(lambda x: x.strip(), wordlist)
    wordlist = map(lambda x: x.replace(" ", "%20"), wordlist)
    wordlist = list(wordlist)

    brute_list('')
