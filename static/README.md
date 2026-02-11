# static/

## Raison d'être

Ce répertoire contient les **fichiers statiques** servis directement par Flask au navigateur. Par convention, Flask sert automatiquement tout fichier placé dans le dossier `static/` via la route `/static/<filename>`.

## Fichiers

| Fichier     | Rôle                                                                                                                                                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `style.css` | Feuille de styles principale de la calculatrice. Définit la mise en page (centrage flexbox), l'apparence du conteneur sombre, la zone d'affichage, la grille de boutons en 4 colonnes et les états interactifs (hover, active). |

## Hypothèses

- Les fichiers statiques sont référencés dans les templates via `url_for('static', filename='...')` afin de garantir la portabilité des chemins.
- En production, un serveur web (Nginx, Apache) servirait typiquement ces fichiers directement, mais en développement Flask les sert lui-même.
- Tout nouveau fichier statique (images, JavaScript supplémentaire, polices) doit être placé dans ce répertoire pour être accessible via la route `/static/`.
