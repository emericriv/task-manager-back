# Task Manager Backend

Mini gestionnaire de tâches collaboratif — Backend

## Stack technique

- **Django** (5.x)
- **Django REST Framework** (API REST)
- **SimpleJWT** (authentification JWT)
- **SQLite** (par défaut, facilement migrable vers Postgres)

## Fonctionnalités principales

- API CRUD pour les tâches (title, description, status, created_at, assigned_to)
- Authentification JWT (connexion, refresh)
- Inscription utilisateur via endpoint dédié
- Conversion automatique camelCase/snake_case pour le front JS
- CORS configuré pour le front Vite

## Structure du projet

```
back/
├── manage.py
├── requirements.txt
├── .env
├── db.sqlite3
├── taskmanager/
│   ├── settings.py      # Configuration principale
│   ├── urls.py          # Routing principal
│   └── ...
├── tasks/
│   ├── models.py        # Modèle Task
│   ├── serializers.py   # Sérialiseur Task
│   ├── views.py         # Vues API (CRUD, inscription)
│   ├── migrations/      # Migrations DB
│   └── ...
└── ...
```

## Installation & lancement

```bash
cd back
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Configuration

- Les variables sensibles (SECRET_KEY, DEBUG, etc.) sont dans `.env`.
- Les endpoints principaux :
  - `/api/token/` : connexion JWT
  - `/api/token/refresh/` : refresh du token
  - `/api/register/` : inscription utilisateur
  - `/api/tasks/` : CRUD des tâches
- CORS autorisé pour le front (`http://localhost:5173`)

## Fonctionnement

1. **Inscription** : POST `/api/register/` (username, email, password)
2. **Connexion** : POST `/api/token/` (username, password) → JWT
3. **CRUD tâches** : endpoints `/api/tasks/` (auth requis)

## Bonnes pratiques

- Utilise des permissions DRF pour sécuriser l’API
- Sérialise les données avec camelCase pour le front

---

Ce backend est conçu pour accompagner le front React/Vite dans un projet pédagogique fullstack.
