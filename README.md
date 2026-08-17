# Guru99 Bank — Test Cases, Bug Tracking & Automation

Projet personnel de test QA (manuel + automatisé) sur **Guru99 Bank**, le site bancaire de démonstration public (`demo.guru99.com`), dans le cadre d'une reconversion vers le métier de QA/Testeur Automaticien.

Le dépôt couvre le cycle de test complet : analyse des exigences, conception de cas de test, exécution manuelle, suivi des anomalies, retesting après évolution du système, et automatisation avec Python, Playwright et pytest.

## Contexte du projet

Guru99 Bank propose des versions successives de son cahier des charges (SRS v1 puis v2, v3 et v4), avec une évolution du site entre les versions. Ce dépôt suit ce cycle de bout en bout :

1. Analyse du SRS v1 et rédaction de ~90 cas de test (9 modules)
2. Exécution manuelle sur la V1, documentation des anomalies
3. Retesting complet en V2 : vérification des correctifs, détection de régressions
4. Automatisation progressive des scénarios avec Python, Playwright et pytest

## Structure du dépôt
├── TestCases_GBank_V1.xlsx # Cas de test manuels, V1
├── suivieBugs_V1_GBank.xlsx # Suivi des anomalies V1
├── TestCases_GBank_V2.xlsx # Cas de test manuels, retesting V2
├── suivieBugs_V2_GBank.xlsx # Suivi des anomalies V2
├── Automation/
│ ├── Pages/ # Page Object Model : un fichier par page du site
│ ├── conftest.py # Fixtures pytest partagées (connexion, etc.)
│ ├── .env # Identifiants (non versionné, voir Prérequis)
│ └── test_*.py # Un fichier de test par module fonctionnel
└── README.md


## Cas de test manuels

Les fichiers `TestCases_GBank_V*.xlsx` couvrent 9 modules fonctionnels du SRS (Nouveau/Modifier/Supprimer client et compte, relevés, solde, tests d'intégration), avec une structure standard (référence, étapes, résultat attendu/obtenu, statut) et une colonne dédiée au retesting V2.

> Conformément au SRS (section 1.2, tests d'automatisation hors périmètre), ces fichiers reflètent les tests **manuels**. L'automatisation présentée ici est une démarche personnelle complémentaire.

## Suivi des anomalies

Les fichiers `suivieBugs_V*_GBank.xlsx` centralisent les anomalies détectées (statut, priorité, sévérité, étapes de reproduction). Les défauts liés à une même cause racine sont consolidés plutôt que dupliqués.

## Automatisation (Playwright / pytest)

Le dossier `Automation/` applique une architecture **Page Object Model** : chaque page du site a sa propre classe (`Pages/`), isolant les locators et actions. Les tests eux-mêmes sont écrits avec **pytest**, organisés par module fonctionnel, et réutilisent une fixture de connexion partagée (`conftest.py`) pour éviter toute duplication.

Chaque module couvert suit la même approche :
- Un scénario positif (happy path), vérifiant qu'une action se déroule normalement
- Des cas négatifs, isolant chaque règle de validation testée (un test = une seule vérification)

Pour lancer l'ensemble des tests :

python -m pytest -s --headed

Pour lancer un seul fichier :

python -m pytest test_nom_du_fichier.py -s --headed


## Prérequis pour exécuter les tests

1. Va sur https://demo.guru99.com/V4/index.php et suis la procédure « Steps To Generate Access » pour obtenir un identifiant manager
2. Crée un fichier `.env` dans `Automation/` avec :

GURU99_USER=ton_identifiant
GURU99_PASSWORD=ton_mot_de_passe

3. Installe les dépendances :

pip install playwright pytest pytest-playwright python-dotenv
playwright install


## Compétences démontrées

Analyse de SRS, conception et exécution de cas de test manuels, gestion d'un bug tracker, tests de régression, automatisation avec Python/Playwright/pytest (Page Object Model, fixtures), gestion des secrets, versionning Git/GitHub.

