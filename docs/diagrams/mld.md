# MLD — CamerShop

Notation : `PK` clé primaire, `FK` clé étrangère, `UQ` unicité, `NN` non nul.

```text
UTILISATEUR(
  id PK, email UQ NN, password_hash NN, role NN,
  first_name, last_name, is_active, created_at
)

BOUTIQUE(
  id PK, vendeur_id FK -> UTILISATEUR.id NN UQ,
  nom NN, description, ville, quartier, actif, created_at
)

CATEGORIE(
  id PK, nom NN UQ, slug NN UQ
)

PRODUIT(
  id PK, boutique_id FK -> BOUTIQUE.id NN,
  categorie_id FK -> CATEGORIE.id NN,
  nom NN, slug, description, prix NUMERIC(12,2) NN,
  stock INTEGER NN CHECK(stock >= 0), image_url, actif, created_at, updated_at
)
INDEX: (boutique_id, actif), (categorie_id, actif), slug.

PANIER(
  id PK, client_id FK -> UTILISATEUR.id NN UQ, updated_at
)

LIGNE_PANIER(
  id PK, panier_id FK -> PANIER.id NN,
  produit_id FK -> PRODUIT.id NN, quantite INTEGER NN CHECK(quantite > 0),
  UQ(panier_id, produit_id)
)

COMMANDE(
  id PK, client_id FK -> UTILISATEUR.id NN,
  reference UQ NN, statut NN, total NUMERIC(12,2) NN CHECK(total >= 0),
  created_at, updated_at
)
INDEX: (client_id, created_at), statut.

LIGNE_COMMANDE(
  id PK, commande_id FK -> COMMANDE.id NN,
  produit_id FK -> PRODUIT.id NN, boutique_id FK -> BOUTIQUE.id NN,
  quantite INTEGER NN CHECK(quantite > 0),
  prix_unitaire NUMERIC(12,2) NN CHECK(prix_unitaire >= 0),
  sous_total NUMERIC(12,2) NN CHECK(sous_total >= 0)
)

PAIEMENT_SIMULE(
  id PK, commande_id FK -> COMMANDE.id NN UQ,
  reference_paiement UQ NN, mode NN,
  statut NN, montant NUMERIC(12,2) NN, confirmed_at, created_at
)
INDEX: reference_paiement.

EXPEDITION(
  id PK, commande_id FK -> COMMANDE.id NN UQ,
  statut NN, quartier NN, point_repere NN,
  adresse_detail, created_at, updated_at
)
```

## Contraintes métier portées par le modèle et le service

- `PRODUIT.stock >= 0` et décrément dans une transaction atomique.
- Le prix de `LIGNE_COMMANDE.prix_unitaire` est une copie figée du catalogue.
- Une seule ligne par produit dans un panier (`UQ(panier_id, produit_id)`).
- Une seule confirmation par commande (`PAIEMENT_SIMULE.commande_id UQ`) et une référence de paiement unique.
- Le total est recalculé côté serveur à partir des lignes, jamais accepté depuis le navigateur.
