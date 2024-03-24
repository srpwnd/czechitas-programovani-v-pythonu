def orameckuj(slovo, znak="*"):
    stred = f"{znak}  {slovo} {znak}"
    ram = znak * len(stred)
    print(ram)
    print(stred)
    print(ram)

orameckuj("ahoj", "#")