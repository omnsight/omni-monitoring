# Omni Monitoring
[![codecov](https://codecov.io/github/omnsight/omni-monitoring/graph/badge.svg?token=2LDW67VWXE)](https://codecov.io/github/omnsight/omni-monitoring)

Omni Monitoring is a service for monitoring data sources and triggering actions based on the data.

### 🚀 Features

- **Monitoring Sources**: Create, read, and manage monitoring sources.
- **Monitor Triggers**: Set up triggers to act on monitoring data.
- **Health Checks**: API endpoint for health checks.
- **OpenAPI Support**: Automatically generated OpenAPI documentation.

### 🛠 Tech Stack

- **Backend:** Python, FastAPI
- **Database:** ArangoDB, Redis
- **Frontend:** TypeScript
- **Tooling:** uv, Docker, Pydantic

## 📦 Getting Started

### Prerequisites

- Python 3.10+
- Docker
- `uv`

### Installation

Clone the repo:

```bash
git clone https://github.com/omnsight/omni-monitoring.git
cd omni-monitoring
```

Install dependencies:

```bash
uv lock --upgrade
uv sync --extra dev
```

Install client dependencies:

```bash
cd client
npm install
cd ..
```

## ⚙️ Configuration

Update configurations in [`.env`](.env)

## 📖 Usage

### Running the Service

Start the backend services:

```bash
docker-compose up -d --build --wait
```

Stop the backend services when you're done:

```bash
docker-compose down
```

### Using the Client

Refer to [client/README.md](client/README.md) for [client](https://www.npmjs.com/package/omni-monitoring-client) setup and usage.

## Local Development

Refer to [DEVELOPMENT.md](DEVELOPMENT.md) for local development setup.

## 📄 License

Distributed under the Apache-2.0 License. See [LICENSE](./LICENSE) for more information.
