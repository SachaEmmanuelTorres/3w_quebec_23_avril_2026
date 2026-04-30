

# IA Locale, Open Source et Agents RAG

### Bâtir une infrastructure souveraine avec Podman


## 🏗️ Architecture : La Force du Volume Partagé

- **Un seul dossier `/models`** pour tous les services.

- **Interopérabilité** : Ollama (modèles simples) + Llama.cpp (GGUF avancés).

- **Persistance** : Logs, Données et Entraînement isolés.


## 🛠️ Automatisation et Interaction

- **`add\_model.sh`** : Un pont interactif entre Hugging Face et votre stack locale.

- **Écosystème Python (uv)** :

  - Scripts d'interaction rapides.

  - Intégration LangChain & Pydantic-AI.

  - Connexion transparente aux API Hugging Face.


## 🥊 Docker Model Runner vs Podman

- **DMR** : Standardisation OCI, "Zéro Config", parfait pour le dev rapide.

- **Podman (Notre stack)** :

  - Flexibilité totale des backends.

  - Sécurité Rootless native.

  - Souveraineté complète sur les moteurs d'inférence.


## 🚀 Démo : Du modèle à l'interaction

1. **Démarrage** : `podman-compose up -d`

2. **Installation** : `./add\_model.sh`

3. **Inférence** : `uv run test\_ai.py`


## 🌐 Conclusion : L'IA est un microservice

En traitant l'IA comme un conteneur standard, on gagne :
- **Portabilité** : Dev -> Prod sans friction.
- **Contrôle des coûts** : Pas de facturation au token.
- **Confidentialité** : 100% Hors-ligne si nécessaire.

### Une stack prête pour le futur de l'Open Source.
**Merci de votre attention !**
*Questions ?*
*Accès stack : http://localhost:8080*

