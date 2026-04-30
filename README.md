# IA Locale, Open Source et Agents RAG 🚀 (Version Stack Podman)

Présentation technique réalisée pour **3W Québec** à l'**UQAM**.

## 🏗️ Architecture Globale
Infrastructure IA modulaire et souveraine. Chaque service est un conteneur Podman indépendant, partageant un volume centralisé pour les modèles.

### Services de la Stack :
- **Ollama** : Moteur d'inférence simplifié.
- **Llama.cpp** : Serveur haute performance pour fichiers GGUF (avec support entraînement et logs).
- **Hermes RAG** : Pipeline de Retrieval Augmented Generation.
- **Open WebUI** : Interface utilisateur unifiée (Port 3000).
- **OpenCode-GUI** : IDE assisté par IA.

## 📂 Structure du Projet
- `ollama/`, `llamacpp-gui/` : Configurations et documentations spécifiques aux moteurs.
- `script-interaction-model/` : Écosystème **Python (uv)** pour interagir avec les API (Ollama, HF, LangChain).
- `models/` (externe) : Volume partagé `/media/sacha/.../models` mappé en `:rw`.
- `logs/`, `training/`, `data_io/` : Dossiers de travail pour l'entraînement et le debug de llama.cpp.

## 🛠️ Outils d'automatisation
- **`add_model.sh`** : Script interactif pour ajouter des modèles à Ollama ou llama.cpp (support local et Hugging Face).
- **`uv`** : Gestionnaire de paquets ultra-rapide pour les scripts Python d'interaction.

## 🚀 Lancement Rapide
```bash
# Lancer la stack complète
podman-compose up -d

# Accéder à la page d'accueil unifiée
# http://localhost:8080

# Ajouter un modèle (ex: Gemma 2)
./add_model.sh "google/gemma-2-2b-it"

# Tester les API (Python)
cd script-interaction-model
uv run test_ai.py
```

## 🎯 Conclusion & Points Forts
Cette stack démontre qu'il est possible de bâtir un écosystème IA complet, performant et **100% privé** en utilisant uniquement des outils Open Source et des standards ouverts (OCI, GGUF).

- **Souveraineté Totale** : Vos données et vos modèles ne quittent jamais votre infrastructure.
- **Interopérabilité** : Accès simultané via WebUI, API OpenAI compatible, ou scripts Python personnalisés.
- **Productivité** : Déploiement en une commande, ajout de modèles simplifié et interface d'accueil unifiée (Port 8080).

---
*Documentation comparative disponible dans `docker_model_runner_vs_podman.md`.*
