# Guru99 Bank — Test Cases, Bug Tracking & Automation

Projet personnel de test QA (manuel + automatisé) réalisé sur **Guru99 Bank**, le site bancaire de démonstration public (`demo.guru99.com`), dans le cadre d'une reconversion vers le métier de QA/Testeur Automaticien.

Ce dépôt couvre l'ensemble du cycle de test : analyse des exigences, conception de cas de test, exécution manuelle, suivi des anomalies, tests de régression suite à une évolution du système, et automatisation avec Python/Playwright.

## Sommaire

- [Contexte du projet](#contexte-du-projet)
- [Structure du dépôt](#structure-du-dépôt)
- [Cas de test](#cas-de-test)
- [Suivi des anomalies (Bug Tracker)](#suivi-des-anomalies-bug-tracker)
- [Tests de régression (V1 → V2)](#tests-de-régression-v1--v2)
- [Automatisation (Playwright / Python)](#automatisation-playwright--python)
- [Prérequis pour exécuter les scripts](#prérequis-pour-exécuter-les-scripts)
- [Compétences démontrées](#compétences-démontrées)

## Contexte du projet

Guru99 Bank propose deux versions successives de son cahier des charges (SRS v1 puis v2), avec une évolution du site entre les deux versions. Ce dépôt suit cette évolution du début à la fin :

1. Analyse du **SRS v1** (traduit en français) et rédaction de ~90 cas de test
2. Exécution manuelle des tests sur la V1 du site
3. Documentation des anomalies rencontrées
4. Réception du **SRS v2** et d'une nouvelle version du site
5. **Retesting** complet en V2 pour vérifier les correctifs et détecter d'éventuelles régressions
6. Automatisation d'un scénario complet (création client → création compte) avec Python et Playwright

## Structure du dépôt

```
├── TestCases_GBank_V1.xlsx     # Cas de test (manuel), 9 modules, test v1
├── suivieBugs_V1_GBank.xlsx     # Suivi des anomalies V1(bug tracker)
├── TestCases_GBank_V2.xlsx      # Cas de test (manuel), 9 modules, retesting V1/V2
   suivieBugs_V2_GBank           # Suivi des anomalies V2 (bug tracker)
├── Automation/                    # Scripts Python + Playwright
│   └── scenario_new_customer.py   # Scénario complet : connexion → client → compte
├──
└── README.md
```

## Cas de test

Le fichier `TestCases_GBank_V1.xlsx` couvre 9 modules fonctionnels du SRS :

| Module | Cas de test |
| --- | --- |
| Nouveau client | NC1–NC29 |
| Modifier client | MC1–MC30 |
| Supprimer client | SC1–SC4 |
| Nouveau compte | NCO1–NCO8 |
| Modifier compte | MCO1–MCO5 |
| Supprimer compte | SCO1–SC04 |
| Mini relevé | MR1–MR4 |
| Relevé personnalisé | RP1–RP9 |
| Consultation solde | CS1–CS3 |
| Tests d'intégration (bout en bout) | TI1–TI24 |

Chaque cas de test suit une structure standard : référence, scénario, cas de test, étapes, données de test, résultat attendu, résultat obtenu, statut Pass/Fail — avec une colonne dédiée au **retesting en V2**.

> **Note sur le périmètre :** conformément à la section 1.2 du SRS (« les tests d'automatisation sont hors périmètre »), les résultats de ce fichier reflètent les **tests manuels**. L'automatisation présentée dans ce dépôt est une démarche personnelle complémentaire, réalisée à des fins d'apprentissage et de démonstration de compétences.

## Suivi des anomalies (Bug Tracker)

Le fichier `suivieBugs_V1_GBank.xlsx` centralise les anomalies détectées, avec statut, priorité, sévérité et étapes de reproduction.

Points clés de la démarche :
- Les défauts causés par une même cause racine (instabilité du serveur de démo, ~51 cas impactés en V1) sont **consolidés en une seule entrée** plutôt que dupliqués, pour garder le tracker lisible et actionnable.
- Chaque défaut a été **retesté en V2** pour vérifier sa résolution.
- Un défaut fonctionnel réel a été identifié lors du retesting : la contrainte d'unicité de l'email (exigence F34 du SRS) n'est pas appliquée lors de la **modification** d'un client, permettant d'enregistrer un email déjà utilisé par un autre client sans message d'erreur.

## Tests de régression (V1 → V2)

Entre la V1 et la V2 du système, plusieurs changements ont été introduits (voir historique de révision du SRS v2) :

- Renommage de champ : « Limite inférieure de montant » → « Valeur minimale de transaction »
- Les champs Identifiant client et Solde sont désactivés dans le formulaire « Modifier compte »
- Les champs Nom, Sexe et Date de naissance sont désactivés dans le formulaire « Modifier client »

Le retesting complet a permis de confirmer :
- La résolution de l'instabilité serveur observée en V1 (la grande majorité des cas passent désormais de Fail à Pass)
- La persistance de 3 anomalies réelles indépendantes du serveur (validation manquante sur le dépôt initial et le formulaire de relevé personnalisé)
- Une régression sur un cas (email avec espace lors de la modification d'un client)
- Un nouveau défaut fonctionnel non détecté en V1 (unicité de l'email non vérifiée à la modification)

Cette démarche complète — cas de test, exécution, documentation, puis retesting suite à évolution — reproduit un vrai cycle de test de régression tel qu'on le rencontre en entreprise.

## Automatisation (Playwright / Python)

Le dossier [`automation/`](https://github.com/AissatouGassama/G99-bank-test-cases/tree/master/Automation) . contient un scénario positif complet, écrit en Python avec Playwright :

**Scénario couvert :** connexion manager → création d'un nouveau client → création d'un compte associé, avec vérification à chaque étape.

Pratiques appliquées :
- Attentes explicites (`expect(...).to_be_visible()`) plutôt que des pauses fixes (`wait_for_timeout`)
- Gestion de tous les types de champs du formulaire (texte, date, radio, liste déroulante)

## Prérequis pour exécuter les scripts

Les scripts du dossier `Automation/` nécessitent des identifiants manager valides pour se connecter à Guru99 Bank :

1. Va sur https://demo.guru99.com/V4/index.php
2. Suis la procédure « Steps To Generate Access » indiquée sur la page pour obtenir un identifiant et un mot de passe
3. Dans les scripts, remplace `METS_TON_IDENTIFIANT_ICI` et `METS_TON_MOT_DE_PASSE_ICI` par tes propres identifiants

Dépendances Python :
```
pip install playwright pytest
playwright install
```

## Compétences démontrées

- Analyse d'un cahier des charges (SRS) et identification d'incohérences dans la documentation
- Conception de cas de test structurés à partir d'exigences fonctionnelles et techniques
- Exécution de tests manuels et documentation rigoureuse des résultats
- Gestion d'un bug tracker professionnel (consolidation, priorisation, suivi de statut)
- Tests de régression suite à une évolution de version
- Automatisation de tests avec Python et Playwright
- Versionning avec Git/GitHub
