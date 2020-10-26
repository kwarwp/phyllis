# phyllis.roxanne.main.py
from _spy.vitollino.main  import Cena, Elemento, Texto

MAR = "https://i.imgur.com/fk9FgaR.jpg"
MORANGO = " https://i.imgur.com/TYqfeqN.png"
CAMPO = " https://i.imgur.com/JD7nQxw.jpg"
ABELHA = "https://i.imgur.com/koKQC7y.png"


mar=Cena(img= MAR)
morango = Elemento( img= MORANGO)
morango.entra(mar)
campo =Cena(img=CAMPO)
mar.direita=campo
campo.esquerda=mar
abelha = Elemento(img= ABELHA)
abelha.entra(campo)




mar.vai ()