# Planning, répartition et risques — Henry

## Planning de réalisation

| Période | Résultat attendu | Vérification |
|---|---|---|
| Fin semaine 1 | Dépôt GitHub, squelette Django, `/health/`, cas d'utilisation, MCD/MLD | Lancement local et revue croisée |
| Semaine 2 | Modèles, migrations, API catalogue/panier/commande/paiement, permissions, au moins 8 tests | Tests automatisés et démonstration Postman |
| Semaine 3 | Intégration Vue, parcours client multivendeur, tableaux vendeur/admin, documentation finale | Scénario complet sans accès direct à la base |

## Répartition opérationnelle

- Henry : dépôt, conventions Git, cas d'utilisation, MCD/MLD, choix PostgreSQL, suivi des risques.
- Yannick : étude comparative, diagramme de classes, design system.
- Yan : séquences de commande, maquette client, prototype interactif.
- Junior : documents partagés, séquence de paiement simulé, comptes rendus et checklists.
- Lindsay : états-transitions, maquette vendeur/admin, assemblage et cohérence du rapport.

La relecture suit l'ordre `Yannick > Yan > Junior > Lindsay > Henry` : chaque livrable est relu par les deux personnes suivantes dans cette chaîne avant fusion.

## Risques et réponses

| Risque | Impact | Réponse |
|---|---|---|
| Stock insuffisant ou double validation | Élevé | Transaction serveur, verrouillage de ligne, tests de concurrence et idempotence paiement |
| Permissions mal appliquées | Élevé | Vérification côté API, tests vendeur/client/admin et revue croisée |
| Secrets ou données réelles committés | Élevé | `.env.example`, `.gitignore`, données fictives, revue avant PR |
| Dépendances difficiles à installer | Moyen | Versions bornées, README reproductible, fallback SQLite pour le squelette |
| Retard d'intégration frontend/backend | Moyen | Contrat JSON documenté dès semaine 2 et branches courtes |
| Modèle incohérent entre diagrammes et code | Élevé | Une revue MCD/MLD avant migrations et mise à jour du rapport après chaque changement |

## Critères d'acceptation des livrables Henry

- Le dépôt se clone et démarre avec les commandes du README.
- `GET /health/` retourne HTTP 200 et un JSON avec `status: ok`.
- Le diagramme de cas d'utilisation couvre les quatre rôles du cahier des charges.
- Le MCD/MLD représente boutique, produit, panier, commande, lignes, paiement simulé et expédition.
- Le choix PostgreSQL explique les relations, transactions, contraintes et montants monétaires.
