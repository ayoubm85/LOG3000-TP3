# templates/

## Raison d'être

Ce répertoire contient les **templates HTML Jinja2** utilisés par Flask pour générer les pages web de l'application. Flask s'attend par convention à trouver les templates dans un dossier nommé `templates/` à la racine du projet.

## Fichiers

| Fichier      | Rôle                                                                                                                                                                                            |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `index.html` | Page principale de la calculatrice. Contient le formulaire de saisie, la grille de boutons (chiffres et opérateurs) et le JavaScript côté client pour construire l'expression avant soumission. |

## Fonctionnement

- Le template est rendu par la fonction `index()` dans `app.py` via `render_template('index.html', result=result)`.
- La variable Jinja2 `{{ result }}` est injectée dans le champ d'affichage pour montrer le résultat de l'évaluation.
- Les boutons utilisent du JavaScript (`appendToDisplay`, `clearDisplay`) pour manipuler le champ de saisie côté client. Le calcul lui-même est effectué côté serveur après soumission du formulaire en POST.

## Dépendances

- **Flask / Jinja2** - moteur de rendu des templates.
- **`static/style.css`** - feuille de styles référencée via `url_for('static', filename='style.css')`.
