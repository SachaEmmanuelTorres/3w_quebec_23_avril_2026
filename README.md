# IA Locale, Open Source et Agents RAG 🚀 (Version Stack Podman)

Présentation technique réalisée pour **3W Québec** à l'**UQAM** le **23 Avril 2026**.

## 📝 Description du Projet
Ce dépôt a été refactorisé pour passer de scripts Python isolés à une architecture conteneurisée robuste sous **Podman**. L'objectif est de déployer une stack complète pour la gestion, la création d'agents IA complexes et l'implémentation de pipelines RAG avancés via des outils d'orchestration spécialisés.

## 📅 Détails de la Présentation
- **Titre :** IA Locale, Open Source et Agents RAG : Souveraineté et Performance
- **Lieu :** UQAM - 3W Québec
- **Date :** 23 Avril 2026
- **Auteur :** Sacha Emmanuel Torres

## 🛠️ Stack Technique (Infrastructure Podman)
L'architecture repose désormais sur l'orchestration de plusieurs services souverains :
- **Podman & Podman-Compose :** Environnement d'exécution conteneurisé (alternative open-source à Docker).
- **Ollama :** Backend d'inférence local pour l'exécution des LLMs (`phi3`, `qwen2.5`, etc.).
- **Open WebUI :** Interface de management centralisée, gestion de l'historique et RAG intégré.
- **Dify :** Plateforme d'orchestration "Low-Code" pour la création d'agents autonomes, workflows complexes et gestion fine du RAG.
- **ChromaDB / PostgreSQL :** Stockage vectoriel et persistance des données applicatives.

## 📂 Structure du Dépôt
- `docker-compose.yaml` : Fichier de configuration pour lancer l'ensemble de la stack avec Podman.
- `volumes/` : Répertoires pour la persistance des modèles Ollama et des bases de données.
- `pre-requis.md` : Guide d'installation de Podman et configuration système.
- `presentation_3w_quebec.pptx` : Support visuel de la présentation.

## 🚀 Installation Rapide
1. Clonez le dépôt : `git clone https://github.com/SachaEmmanuelTorres/3w_quebec_2026.git`
2. Lancez l'infrastructure complète :
   ```bash
   podman-compose up -d
   ```
3. Accédez aux services :
   - **Interface Chat & RAG :** `http://localhost:3000` (Open WebUI)
   - **Création d'Agents IA :** `http://localhost:80` (Dify)

---
*Projet réalisé dans le cadre de la conférence 3W Québec à l'UQAM.*
