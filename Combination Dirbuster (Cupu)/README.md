# Dirbuster

# PEMBERITAHUAN!!
Mohon untuk mengclone repository ini, dan host datanya di localhost sendiri. Jangan bruteforce folder github, kasihan.. Karena combinasi ini ada sampai 2304.

# Pendahuluan
Dirbuster adalah sebuah tool yang digunakan untuk melakukan [Directory Traversal Attack](https://owasp.org/www-community/attacks/Path_Traversal). Di mana tool ini akan membrute-force semua list kata yang ada dengan cara melakukan request ke setiap list kata.

# Library requests
Library ini dilakukan untuk melakukan HTTP Request terhadap suatu URL, cara menginstallnya adalah mengetikkan command di bawah ini di terminal/cmd
```
    pip install requests
```
di sini kita hanya akan menggunakan metode GET saja, untuk lebih detailnya. silahkan kunjungi [Python Requests Library](https://pypi.org/project/requests/)

## Cara menggunakan
```
    import requests
    ...
    res = requests.get(URL)

    print(res.status_code + " " + res.text)
```

## Response Code
Terdapat beberapa Response Code yang kita bisa pakai sebagai informasi apakah suatu URL itu valid atau tidak, dan lain sebagainya. Di sini kita gunakan **Response Code 200** untuk menandakan kalau URL itu tersedia. Untuk response code lain, silahkan kunjungi [Response Code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

# Library itertools
[Itertools](https://docs.python.org/3/library/itertools.html) adalah sebuah library yang menyediakan banyak sekali function yang bisa kita gunakan untuk melakukan iterasi yang sulit seperti permutasi dan kombinasi.
Di sini, kita akan membuat kombinasi dari setiap word list. Karena kita akan membruteforce directory sampai ke akar-akarnya dengan list kata yang ada. setelah kita menggunakan itertools, kita harus cast resultnya ke dalam sebuah list dahulu. Cara menggunakannya adalah
```
    from itertools import combinations
    ...
    
    print(list(combination), JUMLAH_N)
```

# Penjelasan singkat untuk dirbuster.py
Silahkan scroll ke atas untuk melihat semua directory yang tersedia. Sekarang, silahkan buka [dirbuster.py](https://raw.githubusercontent.com/aridavis/dirbuster/master/dirbuster.py).

**Requests** juga bisa kita gunakan untuk mengambil data API, silahkan lihat contoh di bawah.
```
    res = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print(str(res.status_code) + "\n" + res.text)
```

URL yang valid, tidak memiliki spasi. Seandainya directory kita memiliki spasi, maka kita harus merubah spasi tersebut menjadi '%20'
```
    wordlist = map(lambda x: x.strip(), wordlist)
    wordlist = map(lambda x: x.replace(" ", "%20"), wordlist)
    wordlist = list(wordlist)
```

Selanjutnya kita bruteforce, tapi kita cari dulu kombinasinya, kemudian kita append postfixnya. Dan jadilah sebuah URL. Kita validasikan jika Response Code nya adalah 200, maka kita outputkan URL tersebut
```
    for i in range(0, len(wordlist)):
        combination = list(combinations(wordlist,i+1))
        for j in range(0,len(combination)):
            postfix = ""
            for k in range(0, i+1):
                postfix = postfix + "/{}".format(combination[j][k])
            res = requests.get(URL + postfix)
            if(res.status_code == 200):
                print(URL + postfix)
```