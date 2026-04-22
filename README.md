# IA Locale, Open Source et Agents RAG 🚀

Présentation technique réalisée pour **3W Québec** à l'**UQAM** le **23 Avril 2026**.

## 📝 Description du Projet
Ce dépôt contient les ressources et les scripts de démonstration pour une architecture d'IA locale souveraine. L'objectif est de montrer comment orchestrer des modèles de langage (LLM) en local, utiliser le protocole **MCP** (Model Context Protocol) pour l'accès aux outils, et implémenter une recherche sémantique (**RAG**) performante.

## 📅 Détails de la Présentation
- **Titre :** IA Locale, Open Source et Agents RAG : Souveraineté et Performance
- **Lieu :** UQAM - 3W Québec
- **Date :** 23 Avril 2026
- **Auteur :** Sacha Emmanuel Torres

## 🛠️ Architecture Technique
L'agent utilise plusieurs composants clés :
- **Ollama :** Serveur de LLM local pour l'exécution des modèles.
- **Modèles utilisés :** 
  - `phi3:mini` (Réflexion et Planification)
  - `qwen2.5:3b` (Rédaction et Synthèse)
  - `mxbai-embed-large` (Embeddings pour le RAG)
- **MCP (Model Context Protocol) :** Intégration de serveurs Puppeteer pour la navigation web automatisée.
- **ChromaDB :** Base de données vectorielle locale pour le stockage des connaissances métier.

## 📂 Structure du Dépôt
- `agent_rag.py` : Démonstration de base (RAG sur les normes ISO).
- `agent_rag_v2.py` : Agent de veille technologique avancé (Focus sur Claude/Anthropic).
- `pre-requis.md` : Guide d'installation complet (Ubuntu 24.04).
- `presentation_3w_quebec.pptx` : Support visuel de la présentation.
- `requirements.txt` : Dépendances Python nécessaires.

## 🚀 Installation Rapide
1. Clonez le dépôt : `git clone https://github.com/SachaEmmanuelTorres/3w_quebec_2026.git`
2. Installez les dépendances : `pip install -r requirements.txt`
3. Configurez Ollama en suivant les instructions du fichier [pre-requis.md](./pre-requis.md).

---
*Projet réalisé dans le cadre de la conférence 3W Québec à l'UQAM.*
