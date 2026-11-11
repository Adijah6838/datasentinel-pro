# DataSentinel Pro

Enterprise Data Observability, Quality Intelligence, and Real-Time Pipeline Management Platform.

## 🚀 Overview
DataSentinel Pro is a full-stack, multi-tenant SaaS application designed to monitor data pipelines, validate data quality, and stream real-time events. It was built to solve critical data management challenges including incomplete records, duplicate data, and unexpected format changes.

## 🛠️ Technology Stack
*   **Backend:** Python, FastAPI, SQLAlchemy, Alembic
*   **Database:** PostgreSQL
*   **Caching & Message Broker:** Redis
*   **Background Workers:** Celery
*   **Frontend:** React, TypeScript, React Query, Recharts, React Router
*   **Testing:** Pytest (Backend), Vitest (Frontend)
*   **Infrastructure:** Docker, Docker Compose

## ✨ Key Features
*   **Multi-Tenant Architecture:** Complete tenant isolation. Users from one organization cannot access another's data.
*   **Role-Based Access Control (RBAC):** Admin, Engineer, Analyst, and Viewer roles with distinct permissions.
*   **Secure Credential Management:** Data source configurations are encrypted at rest using Fernet symmetric encryption and are never exposed via the API.
*   **Event-Driven Architecture:** Asynchronous data ingestion and quality rule evaluation powered by Celery and Redis.
*   **Real-Time WebSockets:** Live updates pushed directly to the React dashboard for pipeline events and rule evaluations.
*   **Interactive Dashboard:** Data visualization using Recharts and efficient data fetching with React Query.

## 🚦 Getting Started

### Prerequisites
*   Docker Desktop installed and running.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Adijah6838/datasentinel-pro.git
   cd datasentinel-pro