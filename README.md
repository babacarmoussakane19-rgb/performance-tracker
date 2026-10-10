##Application de suivi d'habitudes et d'analyse de progression personnelle.

Personal Performance Tracker est un projet de développement visant à concevoir une application permettant de suivre ses habitudes quotidiennes, de mesurer ses performances et d'analyser leur évolution dans le temps.

L'objectif est de dépasser la simple checklist en transformant les activités quotidiennes en données exploitables grâce à des statistiques, des visualisations et des rapports périodiques.


 Objectifs du projet

Suivre ses habitudes et objectifs personnels au quotidien.

Maintenir des séries de jours consécutifs de réussite (streaks).

Mesurer sa régularité et ses performances.

Visualiser sa progression grâce à des graphiques.

Générer des rapports hebdomadaires et mensuels.

Exploiter les données collectées pour identifier des tendances et améliorer ses habitudes.

Explorer, à terme, des fonctionnalités d'analyse avancée et d'intelligence artificielle.

 Fonctionnalités prévues

1. Gestion des habitudes

Créer, modifier et supprimer des habitudes.

Définir une fréquence et un objectif.

Choisir une unité de mesure : minutes, heures, pages, répétitions, séances, etc.

Organiser les habitudes par catégories.

Consulter l'historique de chaque habitude.

2. Suivi quotidien

Enregistrer les réalisations de chaque journée.

Suivre des objectifs binaires (réalisé / non réalisé).

Enregistrer des valeurs quantitatives : durée, nombre de répétitions, pages lues, etc.

Ajouter des notes pour contextualiser les performances.

3. Streaks et régularité

Calculer le streak actuel.

Identifier le meilleur streak atteint.

Mesurer le taux de réalisation des objectifs.

Visualiser les jours réussis et les jours manqués.

4. Tableau de bord et visualisation

Consulter un résumé des performances quotidiennes.

Visualiser l'évolution des habitudes.

Comparer les résultats sur différentes périodes.

Afficher des indicateurs de régularité et de progression.

5. Rapports périodiques

Générer des bilans hebdomadaires et mensuels.

Comparer les performances avec les périodes précédentes.

Identifier les habitudes les plus régulières.

Repérer les objectifs nécessitant davantage d'attention.

6. Analyse avancée — évolutions futures

Étudier les tendances de progression.

Analyser les relations entre différentes habitudes.

Détecter les baisses de régularité.

Explorer des recommandations personnalisées à partir des données collectées.

Technologie

Langage principal du backend    Python

Développement de l'API REST     FastAPI

Stockage relationnel des données PostgreSQL

SQLAlchemy  Interaction avec la base de données

Validation et structuration des données    Pydantic

Tests automatisés            Pytest

Interface utilisateur prévue   React

Analyse des données    Pandas / NumPy

Visualisation des performances prévue   Plotly


Les technologies seront intégrées progressivement au fil du développement.

 Architecture envisagée

```text
personal-performance-tracker/
│
├── backend/
│   ├── app/
│   │   ├── api/          # Endpoints de l'API
│   │   ├── models/       # Modèles de données
│   │   ├── schemas/      # Validation des données
│   │   ├── services/     # Logique métier
│   │   ├── database.py   # Configuration de la base
│   │   └── main.py       # Point d'entrée FastAPI
│   │
│   ├── tests/            # Tests automatisés
│   └── requirements.txt
│
├── frontend/             # Interface React (à développer)
│
├── .gitignore
└── README.md



Cette architecture pourra évoluer selon les besoins du projet.

