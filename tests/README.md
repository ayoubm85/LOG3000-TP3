# tests/

## Raison d'être

Ce répertoire contient les **tests unitaires** du projet, écrits avec le framework **pytest**. Les tests vérifient le bon fonctionnement des opérations arithmétiques (`operators.py`) et de la logique applicative (`app.py`).

## Fichiers

| Fichier             | Rôle                                                           |
| ------------------- | -------------------------------------------------------------- |
| `__init__.py`       | Fichier d'initialisation du package (vide).                    |
| `test_operators.py` | Tests des fonctions `add`, `subtract`, `multiply` et `divide`. |
| `test_app.py`       | Tests de la fonction `calculate()` et de la route Flask `/`.   |

## Couverture des tests

### `test_operators.py`

- **Addition** : entiers positifs, zéro, négatifs, flottants
- **Soustraction** : résultat positif, négatif, zéro, soustraction de zéro
- **Multiplication** : entiers, par zéro, par un, négatifs, flottants
- **Division** : résultat flottant, résultat entier, par un, flottants

### `test_app.py`

- **calculate()** : addition, soustraction, multiplication, division, espaces, flottants, expression vide/None, opérateurs multiples, opérateur en début/fin, opérandes non numériques, sans opérateur
- **Route Flask `/`** : GET (page d'accueil), POST valide, POST invalide, champ vide

## Comment exécuter les tests

### Installation des dépendances

```bash
pip install pytest pytest-cov
```

### Exécution

```bash
python -m pytest tests/ -v
```

### Avec couverture de code (optionnel)

```bash
python -m pytest tests/ -v --cov=. --cov-report=term-missing
```

Résultat attendu : **34 tests passés, couverture à 99 %**.

## Bugs identifiés et corrigés

Les tests ont été rédigés pour détecter les bugs suivants, qui ont depuis été corrigés :

| Issue | Fichier        | Bug initial               | Correction apportée |
| ----- | -------------- | ------------------------- | ------------------- |
| #1    | `operators.py` | `subtract` faisait `b-a`  | Remplacé par `a-b`  |
| #2    | `operators.py` | `multiply` faisait `a**b` | Remplacé par `a*b`  |
| #3    | `operators.py` | `divide` faisait `a//b`   | Remplacé par `a/b`  |

## Dépendances

- **pytest** – framework de tests
- **pytest-cov** – mesure de couverture de code
- **Flask** – nécessaire pour le client de test dans `test_app.py`
