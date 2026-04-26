# IA Locale, Open Source et Agents RAG 🚀 (Version Stack Podman)

Présentation technique réalisée pour **3W Québec** à l'**UQAM** le **23 Avril 2026**.

## 📝 Description du Projet
Ce dépôt est une infrastructure IA souveraine orchestrée par **Podman**. Il permet de faire tourner des LLMs localement, d'automatiser des tâches via des agents, et d'utiliser un système de RAG (Retrieval-Augmented Generation) pour interroger vos propres documents.

## 🏗️ Schéma d'Architecture Global

```mermaid
graph TD
    subgraph "Interface Utilisateur & Dev"
        OWUI[Open WebUI - Port 3000]
        OC[OpenCode GUI - Port 6080]
    end

    subgraph "Orchestration & Intelligence"
        HRAG[Hermes RAG - Port 5000]
        ORP[OpenRouter Proxy - Port 4000]
    end

    subgraph "Moteurs d'Inférence"
        OLL[Ollama API]
        LCPP[Llama.cpp - Port 8080]
    end

    subgraph "Stockage Souverain"
        MODELS[(Volume: /models)]
    end

    OWUI --> OLL
    OWUI --> HRAG
    OC --> HRAG
    ORP --> OLL
    HRAG --> MODELS
    OLL --> MODELS
    LCPP --> MODELS
```

> **Note :** Tous les services communiquent via le réseau isolé `ai-net` de Podman.

## 🛠️ Services Inclus
1.  **Ollama** : Backend principal pour l'exécution des modèles (GGUF, Safetensors).
2.  **Open WebUI** : Interface de chat moderne et gestion du RAG.
3.  **Hermes RAG** : Moteur de connaissance basé sur vos documents locaux.
4.  **OpenCode GUI** : Environnement de développement accessible par navigateur (VNC).
5.  **Llama.cpp** : Inférence haute performance optimisée pour le format GGUF.
6.  **OpenRouter Proxy** : Passerelle unifiée pour le routage des requêtes.

## 🏛️ Architecture des Agents IA
Voici une visualisation stylisée de l'interaction des agents :

<p align="center">
  <img src="documentation/architecture_agents_AI.png" alt="Architecture des Agents IA" width="50%"/>
</p>

## 🚀 Déploiement
1. **Pré-requis** : Podman et Podman-Compose installés.
2. **Lancement** :
   ```bash
   podman-compose up -d
   ```
3. **Administration** : Pilotez vos conteneurs sur [http://localhost:9090](http://localhost:9090) (Cockpit).

---
*Refactorisation effectuée pour optimiser la souveraineté des données et la légèreté des outils.*
