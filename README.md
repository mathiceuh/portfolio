# Portfolio Dynamique GitHub

Un portfolio moderne, réactif et totalement dynamique, intégralement contenu dans un seul fichier HTML. Ce projet se connecte automatiquement à l'API publique de GitHub pour récupérer et afficher en temps réel vos informations de profil, vos projets récents et vos langages de programmation les plus utilisés.

## Fonctionnalités

- **Synchronisation en temps réel** : Récupère instantanément vos données (profil et dépôts) depuis GitHub.
- **Design moderne ("Dark Mode")** : Interface soignée s'inspirant des standards actuels avec des couleurs élégantes et contrastées.
- **Skeleton Loading** : Affiche des "squelettes" de chargement animés offrant une expérience utilisateur fluide pendant l'appel à l'API.
- **Profil complet** : Mise en valeur de votre avatar, biographie, localisation, et statistiques (abonnés, dépôts publics).
- **Projets mis en avant** : Affichage sous forme de cartes élégantes de vos 6 dépôts les plus récemment mis à jour, incluant les étoiles, les forks et le langage principal.
- **Statistiques des langages** : Analyse automatique de vos récents dépôts pour générer des tags de vos langages dominants.
- **Responsive Design** : Parfaitement adapté à toutes les tailles d'écrans (mobiles, tablettes et ordinateurs de bureau).
- **100% Vanilla** : Aucune dépendance externe, pas de framework lourd. Uniquement du HTML sémantique, du CSS moderne et du JavaScript natif.

## Technologies utilisées

- **HTML5** : SVG intégrés (symboles) pour les icônes.
- **CSS3** : Variables CSS (`:root`), Flexbox, CSS Grid, animations (keyframes pour les shimmer effects et pulse).
- **JavaScript (ES6+)** : `fetch` API, `async/await`, promesses (`Promise.all`), manipulation avancée du DOM.
- **GitHub REST API** : Endpoints `/users/:username` et `/users/:username/repos`.

## Comment l'utiliser et le déployer

Grâce à son architecture mono-fichier, l'installation est immédiate et le déploiement gratuit.

### En local
1. Téléchargez le fichier `index.html` sur votre ordinateur.
2. Double-cliquez dessus pour l'ouvrir dans votre navigateur web favori (Chrome, Firefox, Safari, Edge...).

### Déploiement en ligne (GitHub Pages, Vercel, Netlify)
1. Créez un nouveau dépôt sur GitHub et placez-y le fichier `index.html`.
2. **Pour GitHub Pages** :
   - Allez dans les **Settings** (Paramètres) de ce nouveau dépôt.
   - Rendez-vous dans la section **Pages** (dans le menu latéral gauche).
   - Dans "Source", sélectionnez votre branche principale (ex: `main`) et cliquez sur Save.
   - En quelques minutes, votre portfolio sera accessible via une URL publique !

## Configuration et personnalisation

Pour connecter le portfolio à votre propre compte GitHub, vous n'avez qu'une seule variable à modifier :

1. Ouvrez `index.html` avec un éditeur de texte ou de code (VS Code, Notepad++, etc.).
2. Repérez le début de la balise `<script>` (vers la fin du fichier).
3. Modifiez la constante `GITHUB_USERNAME` :
   ```javascript
   const GITHUB_USERNAME = 'votre-pseudo-github';
   ```

*Astuce bonus :* Vous avez un langage préféré qui n'a pas la couleur que vous souhaitez ? Modifiez directement l'objet `languageColors` dans le script JavaScript pour définir vos propres codes couleurs hexadécimaux !

## 👨‍💻 Auteur

Développé par **Mathis Lefevre** ([@mathiceuh](https://github.com/mathiceuh)).
Lié au profil LinkedIn : [Mathis Lefèvre](https://www.linkedin.com/in/mathis-lefèvre-174744364/)
