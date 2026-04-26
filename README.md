# IA Locale, Open Source et Agents RAG 🚀 (Version Stack Podman)

Présentation technique réalisée pour **3W Québec** à l'**UQAM** le **23 Avril 2026**.

## 📝 Description du Projet
Infrastructure IA modulaire et souveraine. Chaque service est un conteneur Podman indépendant, tous reliés à un dossier de modèles centralisé et un réseau privé.

## 🏗️ Schéma d'Architecture Global

```mermaid
graph TD
    subgraph "Interfaces & Proxy"
        OWUI[Open WebUI - Port 3000]
        OC[OpenCode GUI - Port 6080]
        ORP[OpenRouter Proxy - Port 4000]
    end

    subgraph "Services & RAG"
        HRAG[Hermes RAG - Port 5000]
    end

    subgraph "Moteurs d'Inférence"
        OLL[Ollama API]
        LCPP[Llama.cpp - Port 8080]
    end

    subgraph "Stockage Centralisé"
        MODELS[(Volume Physique: /models)]
    end

    %% Connexion Directe au Volume de Modèles (Demande Utilisateur)
    MODELS === OLL
    MODELS === LCPP
    MODELS === HRAG
    MODELS === OC
    MODELS === ORP

    %% Interactions Logiques
    OWUI -.-> OLL
    OWUI -.-> HRAG
    ORP -.-> OLL
    OC -.-> HRAG
```

> **Souveraineté :** L'accès direct au volume `/models` (représenté par les lignes pleines `===`) garantit que chaque outil travaille sur la même base de connaissance locale sans duplication.

## 🛠️ Détail des Services
- **Ollama, Llama.cpp, Hermes RAG, OpenCode, OpenRouter** : Tous sont configurés avec un montage de volume sur le dossier des modèles de l'hôte.
- **Open WebUI** : Sert de point d'entrée unique pour l'interaction utilisateur.

## 🏛️ Architecture des Agents IA
Visualisation de la logique des agents :

<p align="center">
  <img src="documentation/architecture_agents_AI.png" alt="Architecture des Agents IA" width="50%"/>
</p>

## 🚀 Lancement Rapide
```bash
cd /media/sacha/datas/3w_quebec_23_avril_2026
podman-compose up -d
```
Visualisation système : [http://localhost:9090](http://localhost:9090) (Cockpit)

---
*Architecture optimisée pour le partage de ressources locales.*
