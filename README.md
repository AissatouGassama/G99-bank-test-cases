# Cas de test — Guru99 Bank (module Client & Compte)

Suite de cas de test manuels, écrite à l'entraînement à partir de la **Spécification des
Exigences Logicielles (SRS)** du site de démo public [Guru99 Bank](https://demo.guru99.com) —
une application volontairement mise à disposition par Guru99 pour s'entraîner aux tests
fonctionnels et à l'automatisation.

## Objectif

M'entraîner à transformer un document d'exigences (SRS) en cas de test structurés et
exploitables, en couvrant :
- la **validation de champs** (obligatoire, format, longueur, caractères interdits) ;
- les **règles métier** au-delà du simple champ (ex. : un e-mail déjà utilisé, un dépôt
  initial minimum, l'autorisation d'un gestionnaire sur un client/compte) ;
- des **scénarios d'intégration de bout en bout** (créer → modifier → supprimer), pas
  seulement des vérifications isolées.

## Contenu

| Fichier | Description |
|---|---|
| `TestCases_GBank.xlsx` | ~90 cas de test répartis sur 9 feuilles (Nouveau Client, Modification Client, Suppression Client, Nouveau/Modifier/Supprimer Compte, Mini Relevé, Relevé Personnalisé, Tests d'intégration) |

## Méthode

Chaque feuille suit la même structure :

| Réf | Scénario de test | Cas de test | Étapes | Données de test | Résultat attendu | Résultat obtenu | Réussi/Échoué |
|---|---|---|---|---|---|---|---|

Les colonnes *Résultat obtenu* et *Réussi/Échoué* sont volontairement laissées vides : ces
cas sont des cas de test **définis** à partir de la spécification, pas encore tous exécutés
contre le site réel.

### Exemple (feuille `NouvauClient`)

| Réf | Cas de test | Données de test | Résultat attendu |
|---|---|---|---|
| NC1 | Le nom de client ne peut pas contenir de chiffres | `77Name66` | Un message d'erreur *"Les chiffres ne sont pas autorisés"* doit s'afficher |
| NC19 | Le code postal ne peut pas contenir moins de 6 chiffres | `69003` | *"Le code postal doit comporter 6 chiffres"* |

### Exemple (feuille `Test Integration`)

| Réf | Cas de test | Résultat attendu |
|---|---|---|
| TI2 | Vérifier qu'un client ne peut être ajouté deux fois | *"L'adresse e-mail existe déjà dans le système"* |
| TI13 | Vérifier que le dépôt initial ne peut être inférieur à 500 | *"Le dépôt initial ne doit pas être inférieur à 500"* |

## Automatisation

Une partie de ces cas (champ Nom, `NouvauClient`) a été automatisée avec **Python +
Playwright**, en s'exécutant directement contre le site réel `demo.guru99.com`. Voir le
dossier [`automation/`](./automation) .

Prérequis pour exécuter les scripts d'automatisation

Les scripts du dossier `Automation/` nécessitent des identifiants manager valides pour se connecter à Guru99 Bank.

1. Va sur https://demo.guru99.com/V4/index.php
2. Suis la procédure "Steps To Generate Access" indiquée sur la page pour obtenir un identifiant et un mot de passe
3. Dans les scripts, remplace `METS_TON_IDENTIFIANT_ICI` et `METS_TON_MOT_DE_PASSE_ICI` par tes propres identifiants

## Contexte

Ce dépôt fait partie de ma reconversion vers le métier de testeuse QA / automatisation.
Guru99 Bank est un site de démo public conçu pour ce type d'entraînement — aucune donnée
réelle n'y est utilisée.


