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

### Installation de pytest

```bash
pip install pytest
```

### Exécution

```bash
python -m pytest tests/ -v
```

### Avec couverture de code (optionnel)

```bash
pip install pytest-cov
python -m pytest tests/ -v --cov=. --cov-report=term-missing
```

## Dépendances

- **pytest** - framework de tests
- **Flask** - nécessaire pour le client de test dans `test_app.py`
