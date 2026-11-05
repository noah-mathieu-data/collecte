def calculer_mediane(valeurs):
    valeurs = sorted(valeurs)
    n = len(valeurs)
    milieu = n // 2
    if n % 2 == 0:
        return (valeurs[milieu - 1] + valeurs[milieu]) / 2
    return valeurs[milieu]