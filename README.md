# CamerShop

CamerShop est une marketplace e-commerce multivendeur pour le contexte camerounais. Le backend est construit avec Django + Django REST Framework et le frontend prévu avec Vue.js + Vite. PostgreSQL sera utilisé pour les données persistantes ; SQLite reste disponible pour lancer le squelette local sans serveur de base.

## Semaine 1 — dépôt et lancement

```bash
cp .env.example .env
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python backend/manage.py migrate
python backend/manage.py test core
python backend/manage.py runserver 8000
```

Vérification : `curl http://127.0.0.1:8000/health/` doit renvoyer `{"status":"ok",...}`.

## Structure

- `backend/` : projet Django et application `core`.
- `frontend/` : futur client Vue/Vite.
- `docs/` : conception, diagrammes et décisions d'architecture.
- `fixtures/` : données fictives uniquement.

## Organisation Git proposée

- `main` : version stable et démontrable.
- `develop` : intégration de l'équipe.
- `feature/<nom-court>` : une fonctionnalité par branche.
- Une Pull Request et une relecture par les deux membres suivants dans l'ordre défini sont requises avant fusion.

Exemples : `feature/health-endpoint`, `feature/order-stock-validation`, `docs/mcd-mld`.

## Règles de sécurité

Ne jamais committer `.env`, mots de passe, clés API ou données personnelles réelles. Les comptes, numéros et paiements de démonstration sont fictifs. Les paiements MTN MoMo, Orange Money et à la livraison sont simulés et ne déclenchent aucune transaction financière réelle.

## Prochaines étapes

1. Ajouter les modèles et migrations du MCD/MLD.
2. Exposer les endpoints catalogue, panier, commande et paiement simulé.
3. Ajouter authentification, permissions par rôle et au moins huit tests métier/API.
4. Intégrer le frontend Vue au parcours client et aux tableaux vendeur/admin.
