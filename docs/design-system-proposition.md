# CamerShop — proposition de design system

## Direction artistique : « Douceur tropicale premium »

CamerShop doit inspirer confiance sans paraître froid ni bancaire. La direction proposée associe la sobriété d'un produit SaaS premium à des accents chaleureux rappelant les marchés urbains de Douala et Yaoundé. L'interface utilise beaucoup d'espace, des cartes aérées, des photos produits lumineuses et une hiérarchie très lisible.

## Palette

| Usage | Couleur | Hex |
|---|---|---|
| Fond principal | Ivoire doux | `#F8F7F2` |
| Surface | Blanc cassé | `#FFFFFF` |
| Texte principal | Vert forêt | `#123C35` |
| Texte secondaire | Gris sauge | `#6F7F79` |
| Accent principal | Corail doux | `#E9815B` |
| Accent secondaire | Vert sauge | `#A8C3B2` |
| Succès | Vert validation | `#3E8B68` |
| Alerte | Ambre | `#D8A34A` |
| Erreur | Rouge brique | `#C9685B` |

Le corail est réservé aux actions importantes, aux prix et aux éléments sélectionnés. Le vert forêt sert aux titres, à la navigation et aux actions secondaires. Les statuts ne doivent pas dépendre de la couleur seule : ils utilisent aussi un libellé explicite.

## Typographie

- Titres : **Manrope**, poids 650 à 750, avec une taille généreuse et peu de mots.
- Texte courant : **Inter**, poids 400 à 500, pour la lisibilité des tableaux et formulaires.
- Prix : Inter semi-bold, chiffres bien espacés, suffixe `FCFA` visible.
- Échelle : 12, 14, 16, 20, 28, 36 et 48 px.

## Formes et espacements

Les cartes utilisent un rayon de 18 à 20 px. Les champs et boutons utilisent un rayon de 12 à 14 px. L'échelle d'espacement est basée sur 4 px : 4, 8, 12, 16, 24, 32 et 48 px. Les ombres doivent rester discrètes : elles servent à séparer les surfaces, pas à décorer.

## Composants essentiels

**Navigation.** Barre claire avec logo, recherche centrale, navigation courte, favoris, panier et avatar. Sur mobile, la navigation devient une barre inférieure à quatre entrées.

**Boutons.** Le bouton primaire est corail avec texte blanc. Le bouton secondaire est ivoire ou blanc avec contour vert forêt. Les boutons destructifs utilisent le rouge brique et demandent une confirmation.

**Cartes produit.** Image sur fond ivoire, catégorie, nom sur deux lignes maximum, vendeur, prix en FCFA, disponibilité et bouton d'ajout. L'utilisateur doit comprendre en moins de deux secondes ce qu'il peut acheter.

**Statuts.** `En attente`, `Confirmée`, `À préparer`, `Expédiée`, `Livrée` et `Annulée`. Chaque statut possède une pastille, un libellé et éventuellement une icône.

**Tableaux.** Utilisés pour les commandes et le stock côté vendeur/admin. Les actions principales restent dans la dernière colonne ; les filtres sont placés au-dessus du tableau.

## Parcours proposés

### Client

Accueil → recherche ou catégorie → fiche produit → panier multivendeur → livraison par quartier et point de repère → paiement simulé → confirmation → suivi de commande.

### Vendeur

Vue d'ensemble → alertes de stock faible → produits → commandes à préparer → mise à jour du statut → statistiques de vente.

### Administrateur

Vue globale → comptes et boutiques → modération des produits → supervision des commandes → statistiques et incidents.

## Principes d'expérience

L'interface doit toujours expliquer ce qui se passe, en particulier lors de la vérification du stock et du paiement simulé. Le total est présenté avant confirmation, les prix des lignes de commande sont figés au moment de la validation et les erreurs doivent proposer une action corrective claire. Les données de paiement sont explicitement marquées comme simulées.

## Adaptation au contexte Cameroun

Les adresses utilisent les champs `Ville`, `Quartier` et `Point de repère`, plutôt qu'une adresse postale supposée précise. Les montants sont affichés en FCFA. Les méthodes de paiement affichées sont `MTN MoMo simulé`, `Orange Money simulé` et `Paiement à la livraison`, sans connexion à une API financière réelle.
