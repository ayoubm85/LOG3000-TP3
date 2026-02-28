# LOG3000-TP3 - Calculatrice Web

**Équipe : 27**

## Description

Ce projet est une **calculatrice web** développée avec le micro-framework **Flask** (Python). L'application permet d'effectuer des opérations arithmétiques simples (addition, soustraction, multiplication, division) via une interface graphique intuitive rendue dans le navigateur.

### Portée du projet

- Évaluation d'expressions arithmétiques à **un seul opérateur** (ex. `12+7`, `3.5/2`).
- Interface de type calculatrice avec grille de boutons (chiffres 0-9 et opérateurs `+`, `-`, `*`, `/`).
- Construction de l'expression **côté client** (JavaScript), évaluation **côté serveur** (Python/Flask).
- Résultat affiché dans le champ d'affichage après soumission du formulaire.

## Structure du projet

```
LOG3000-TP3/
├── README.md              # Documentation principale (ce fichier)
├── app.py                 # Point d'entrée Flask : routes, parsing et évaluation
├── operators.py           # Fonctions arithmétiques (add, subtract, multiply, divide)
├── templates/             # Templates HTML Jinja2
│   ├── README.md          # Documentation du module templates
│   └── index.html         # Interface de la calculatrice
├── static/                # Fichiers statiques (CSS)
│   ├── README.md          # Documentation du module static
│   └── style.css          # Styles visuels de la calculatrice
└── tests/                 # Tests unitaires pytest
    ├── README.md          # Documentation du module tests
    ├── __init__.py        # Initialisation du package
    ├── test_operators.py  # Tests des fonctions arithmétiques
    └── test_app.py        # Tests de la route Flask et de calculate()
```

| Fichier                | Responsabilité                                                                                                   |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `app.py`               | Définit la route `/`, parse l'expression soumise par l'utilisateur et retourne le résultat via le template HTML. |
| `operators.py`         | Contient les quatre fonctions arithmétiques (`add`, `subtract`, `multiply`, `divide`) appelées par `app.py`.     |
| `templates/index.html` | Page HTML avec le formulaire, la grille de boutons et le JS client pour construire l'expression.                 |
| `static/style.css`     | Mise en page et styles visuels de la calculatrice (grille, couleurs, états interactifs).                         |
| `tests/`               | Suite de tests unitaires pytest couvrant `operators.py` et `app.py` (34 tests, couverture 99 %).                 |

## Prérequis

- **Python 3.x** ([télécharger](https://www.python.org/downloads/))
- **pip** (inclus avec Python 3.4+)
- **Git** ([télécharger](https://git-scm.com/downloads))

## Guide d'installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ayoubm85/LOG3000-TP3.git
cd LOG3000-TP3
```

### 2. Créer un environnement virtuel (recommandé)

```bash
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows
```

### 3. Installer les dépendances

```bash
pip install flask pytest pytest-cov
```

## Instructions d'utilisation

### Lancer l'application

```bash
python app.py
```

Le serveur de développement Flask démarre sur `http://127.0.0.1:5000`.

### Utiliser la calculatrice

1. Ouvrir un navigateur et accéder à `http://127.0.0.1:5000`.
2. Cliquer sur les **boutons chiffres** (0-9) pour composer le premier opérande.
3. Cliquer sur un **bouton opérateur** (`+`, `-`, `*`, `/`) pour sélectionner l'opération.
4. Cliquer sur les **boutons chiffres** pour composer le second opérande.
5. Cliquer sur **`=`** pour soumettre l'expression et afficher le résultat.
6. Cliquer sur **`C`** pour effacer l'affichage et recommencer.

### Exemple

Pour calculer `17 + 9` :

- Cliquer sur `1`, `7`, `+`, `9`, puis `=`.
- Le résultat `26.0` s'affiche dans le champ.

## Tests

Les tests unitaires sont situés dans le répertoire `tests/` et couvrent les fonctions arithmétiques de `operators.py` ainsi que la route Flask dans `app.py`.

### Exécuter les tests

```bash
python -m pytest tests/ -v
```

### Avec couverture de code

```bash
python -m pytest tests/ -v --cov=. --cov-report=term-missing
```

Résultat attendu : **34 tests passés, couverture à 99 %**.

## Contribution

### Flux de travail Git

1. **Créer une branche** à partir de `main` pour chaque fonctionnalité ou correctif :

   ```bash
   git checkout -b feature/nom-de-la-feature
   ```

2. **Développer** la fonctionnalité en effectuant des commits clairs et atomiques :

   ```bash
   git add .
   git commit -m "Ajouter la fonctionnalité X"
   ```

3. **Pousser** la branche vers le dépôt distant :

   ```bash
   git push origin feature/nom-de-la-feature
   ```

4. **Ouvrir une Pull Request (PR)** sur GitHub vers la branche `main`.

5. **Revue de code** : un autre membre de l'équipe doit approuver la PR avant la fusion.

6. **Fusionner** la PR une fois approuvée.

### Conventions

- **Branches** : utiliser le préfixe `feature/`, `fix/` ou `docs/` selon le type de modification.
- **Commits** : messages en français, concis et au présent (ex. _« Ajouter la validation des entrées »_).
- **Issues** : ouvrir une issue GitHub pour signaler un bug ou proposer une amélioration avant de commencer le travail.
- **Documentation** : toute nouvelle fonction ou classe doit inclure un docstring décrivant son rôle, ses entrées et ses sorties.
