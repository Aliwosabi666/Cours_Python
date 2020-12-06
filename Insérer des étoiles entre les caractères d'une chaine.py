"""
     créer une fonction python nommée insertEtoile() qui place des étolies
     entre chaque caractéres d'une chaine founie en entrée. Exemple pour la
     chaine s = "python", InsertEtoie(s) donne p*t*h*o*n
     """
def insertEtoile(chaine):
    ch = ""
    for x in chaine:
        ch = ch + x + "*"
        n = len(ch)
    return ch[0:n-1]
print(insertEtoile("python"))
