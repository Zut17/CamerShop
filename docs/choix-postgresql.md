# Choix de PostgreSQL

PostgreSQL est retenu pour CamerShop car le domaine est fortement relationnel : un client possède un panier, une commande contient plusieurs lignes, chaque ligne référence un produit et une boutique, puis une commande peut être associée à un paiement simulé et à une expédition.

Le passage de panier à commande et la décrémentation du stock doivent être traités dans une transaction. PostgreSQL fournit les transactions, les contraintes `CHECK`, les contraintes d'unicité et les verrous nécessaires pour empêcher un stock négatif ou une double confirmation concurrente. Ces garanties sont plus adaptées que de simples validations dans l'interface Vue.

Les montants sont stockés en `NUMERIC(12,2)` plutôt qu'en flottants afin d'éviter les erreurs d'arrondi. Les références, les slugs et la référence de paiement sont indexés ou uniques pour accélérer les recherches et éviter les doublons.

MongoDB resterait possible pour un catalogue très variable, mais il obligerait à gérer plus explicitement les cohérences entre commande, stock, paiement et boutique. CamerShop privilégie ici l'intégrité transactionnelle et la lisibilité du modèle. Les données de démonstration restent fictives et aucun paiement réel n'est exécuté.
