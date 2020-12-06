"""

    Ecrire un programme en python qui permet de transformer une adresse
    url saisie au clavier en un lien

    """
url = input("Saisir une adresse url :")
text_lien = input("Saisir le texte du lien")

lien = "<a href=" + url + ">" + text_lien + "</a>"
htmlFile = open("C:/Users/Ali_s/AppData/Local/Programs/Python/Python38/Ex/test.html","w")
htmlFile.write(lien)
htmlFile.close()
print(lien)
