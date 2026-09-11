from pyswip import Prolog

prolog = Prolog()

prolog.consult("datos.pl")

resultados = list(prolog.query("abuelo(X, lucas)"))

for res in resultados:
    print(f"El abuelo es: {res['X']}")