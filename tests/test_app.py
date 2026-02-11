"""Tests unitaires pour le module app.

Ce fichier vérifie le comportement de la fonction calculate() ainsi
que la route Flask '/'. Les tests utilisent le client de test Flask
pour simuler des requêtes HTTP sans lancer le serveur.
"""

import sys
import os

# Ajouter le répertoire racine du projet au path pour permettre l'import de app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from app import app, calculate


# =====================================================================
# Tests de la fonction calculate
# =====================================================================

class TestCalculate:
    """Tests pour la fonction de parsing et d'évaluation d'expressions."""

    def test_addition_simple(self):
        """Vérifie l'évaluation d'une addition simple.

        Entrée : "2+3"
        Sortie attendue : 5.0
        """
        assert calculate("2+3") == 5.0

    def test_soustraction_simple(self):
        """Vérifie l'évaluation d'une soustraction simple.

        Entrée : "10-3"
        Sortie attendue : 7.0
        Bug potentiel : retourne -7.0 si subtract fait b - a
        """
        assert calculate("10-3") == 7.0

    def test_multiplication_simple(self):
        """Vérifie l'évaluation d'une multiplication simple.

        Entrée : "3*4"
        Sortie attendue : 12.0
        Bug potentiel : retourne 81.0 si multiply fait a ** b
        """
        assert calculate("3*4") == 12.0

    def test_division_simple(self):
        """Vérifie l'évaluation d'une division simple.

        Entrée : "7/2"
        Sortie attendue : 3.5
        Bug potentiel : retourne 3.0 si divide fait a // b
        """
        assert calculate("7/2") == 3.5

    def test_expression_avec_espaces(self):
        """Vérifie que les espaces sont correctement ignorés.

        Entrée : " 2 + 3 "
        Sortie attendue : 5.0
        """
        assert calculate(" 2 + 3 ") == 5.0

    def test_expression_avec_flottants(self):
        """Vérifie l'évaluation avec des nombres décimaux.

        Entrée : "1.5+2.5"
        Sortie attendue : 4.0
        """
        assert calculate("1.5+2.5") == 4.0

    def test_expression_vide(self):
        """Vérifie qu'une expression vide déclenche une ValueError.

        Entrée : ""
        Sortie attendue : ValueError
        """
        with pytest.raises(ValueError):
            calculate("")

    def test_expression_none(self):
        """Vérifie qu'une valeur None déclenche une ValueError.

        Entrée : None
        Sortie attendue : ValueError
        """
        with pytest.raises(ValueError):
            calculate(None)

    def test_operateurs_multiples(self):
        """Vérifie qu'une expression avec plusieurs opérateurs est rejetée.

        Entrée : "1+2+3"
        Sortie attendue : ValueError (un seul opérateur autorisé)
        """
        with pytest.raises(ValueError):
            calculate("1+2+3")

    def test_operateur_en_debut(self):
        """Vérifie qu'un opérateur en début d'expression est rejeté.

        Entrée : "+5"
        Sortie attendue : ValueError
        """
        with pytest.raises(ValueError):
            calculate("+5")

    def test_operateur_en_fin(self):
        """Vérifie qu'un opérateur en fin d'expression est rejeté.

        Entrée : "5+"
        Sortie attendue : ValueError
        """
        with pytest.raises(ValueError):
            calculate("5+")

    def test_operandes_non_numeriques(self):
        """Vérifie que des opérandes non numériques déclenchent une ValueError.

        Entrée : "abc+def"
        Sortie attendue : ValueError
        """
        with pytest.raises(ValueError):
            calculate("abc+def")

    def test_sans_operateur(self):
        """Vérifie qu'une expression sans opérateur est rejetée.

        Entrée : "123"
        Sortie attendue : ValueError
        """
        with pytest.raises(ValueError):
            calculate("123")


# =====================================================================
# Tests de la route Flask
# =====================================================================

class TestFlaskRoute:
    """Tests de la route '/' via le client de test Flask."""

    @pytest.fixture
    def client(self):
        """Crée un client de test Flask pour simuler des requêtes HTTP.

        Returns:
            FlaskClient: Client de test configuré en mode test.
        """
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client

    def test_get_page_accueil(self, client):
        """Vérifie que la page d'accueil se charge correctement en GET.

        Sortie attendue : code HTTP 200 et présence du titre dans le HTML.
        """
        response = client.get('/')
        assert response.status_code == 200
        assert b'Flask Calculator' in response.data

    def test_post_addition(self, client):
        """Vérifie qu'une addition soumise en POST retourne le bon résultat.

        Entrée : display="2+3"
        Sortie attendue : "5.0" présent dans la réponse HTML.
        """
        response = client.post('/', data={'display': '2+3'})
        assert response.status_code == 200
        assert b'5.0' in response.data

    def test_post_expression_invalide(self, client):
        """Vérifie qu'une expression invalide retourne un message d'erreur.

        Entrée : display="abc"
        Sortie attendue : "Error" présent dans la réponse HTML.
        """
        response = client.post('/', data={'display': 'abc'})
        assert response.status_code == 200
        assert b'Error' in response.data

    def test_post_champ_vide(self, client):
        """Vérifie qu'un champ vide retourne un message d'erreur.

        Entrée : display=""
        Sortie attendue : "Error" présent dans la réponse HTML.
        """
        response = client.post('/', data={'display': ''})
        assert response.status_code == 200
        assert b'Error' in response.data
