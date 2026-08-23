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

Les fichiers `TestCases_GBank_V*.xlsx` couvrent 9 modules fonctionnels du SRS (Nouveau/Modifier/Supprimer client et compte, relevés, solde, tests d'intégration), avec une structure standard et une colonne dédiée au retesting V2.

> Conformément au SRS (section 1.2, tests d'automatisation hors périmètre), ces fichiers reflètent les tests **manuels**. L'automatisation présentée ici est une démarche personnelle complémentaire.

### Méthodologie de conception

Les cas de test sont construits directement à partir des exigences fonctionnelles et techniques du SRS, avec une structure et une nomenclature cohérentes sur l'ensemble du projet.

**Organisation par module** : chaque fonctionnalité du système (Nouveau client, Modifier client, Nouveau compte...) a son propre onglet, avec un identifiant unique construit sur le modèle `[Initiales du module][N°]` — par exemple `NC1` à `NC29` pour "Nouveau Client", `MC1` à `MC30` pour "Modifier Client".

**Structure de chaque cas de test** (8 colonnes) :

| Colonne | Rôle |
|---|---|
| Ref | Identifiant unique du cas |
| Test Scenario | Fonctionnalité/champ concerné |
| Test Case | Règle métier précise vérifiée |
| Test Steps | Étapes d'exécution |
| Test Data | Données d'entrée utilisées |
| Expected Result | Résultat attendu selon le SRS |
| Actual Result | Résultat observé à l'exécution |
| Pass/Fail | Statut |

**Exemple concret** (module Nouveau Client, validation du champ Nom) :

| Ref | Test Case | Test Data | Expected Result | Actual Result | Statut |
|---|---|---|---|---|---|
| NC1 | Le nom ne peut pas contenir de chiffres | `77Name66` | "Numbers are not allowed" | "Numbers are not allowed" | ✅ Pass |
| NC4 | Le nom ne peut pas commencer par un espace | `" name"` | "First character cannot be space" | "Numbers are not allowed" | ❌ Fail |

Le cas NC4 illustre une anomalie réelle détectée par cette méthode : le message affiché ne correspond pas au message attendu par le SRS pour cette règle précise.

Chaque champ de saisie est couvert par un jeu de cas systématique (vide, valeur invalide par type de caractère, position d'un espace) plutôt que testé de façon isolée ou aléatoire, afin de garantir une couverture homogène et reproductible sur l'ensemble des modules.

## Suivi des anomalies

Les fichiers `suivieBugs_V*_GBank.xlsx` centralisent les anomalies détectées (statut, priorité, sévérité, étapes de reproduction). Les défauts liés à une même cause racine sont consolidés plutôt que dupliqués.

## Automatisation (Playwright / pytest)

Le dossier `Automation/` applique une architecture **Page Object Model** : chaque page du site a sa propre classe (`Pages/`), isolant les locators et actions. Les tests eux-mêmes sont écrits avec **pytest**, organisés par module fonctionnel, et réutilisent une fixture de connexion partagée (`conftest.py`) pour éviter toute duplication.

Chaque module couvert suit la même approche :
- Un scénario positif (happy path), vérifiant qu'une action se déroule normalement
- Des cas négatifs, isolant chaque règle de validation testée (un test = une seule vérification)

Pour lancer l'ensemble des tests :
```
python -m pytest -s --headed
```
Pour lancer un seul fichier :
```
python -m pytest test_nom_du_fichier.py -s --headed
```

## Prérequis pour exécuter les tests

1. Va sur https://demo.guru99.com/V4/index.php et suis la procédure « Steps To Generate Access » pour obtenir un identifiant manager
2. Crée un fichier `.env` dans `Automation/` avec :
```
GURU99_USER=ton_identifiant
GURU99_PASSWORD=ton_mot_de_passe
```
3. Installe les dépendances :
```
pip install playwright pytest pytest-playwright python-dotenv
playwright install
```

## Compétences démontrées

Analyse de SRS, conception et exécution de cas de test manuels, gestion d'un bug tracker, tests de régression, automatisation avec Python/Playwright/pytest (Page Object Model, fixtures), gestion des secrets, versionning Git/GitHub.
