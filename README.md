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

To use the client in your Node.js project, you can install it directly from GitHub. Add the following to your `package.json`:

```json
{
  "dependencies": {
    "omni-monitoring": "github:omnsight/omni-monitoring"
  }
}
```

After installation, you can use the client in your application as shown below:

```typescript
import { OpenAPI, HealthService, HealthCheck } from 'omni-monitoring/client'; // Adjust path if needed

// Configure the API client
OpenAPI.BASE = 'http://localhost:8000'; // Adjust if your server runs on a different host/port
// Configure authentication (e.g., with a bearer token)
OpenAPI.TOKEN = 'your-bearer-token';

async function main() {
  try {
    console.log('Performing health check...');
    const healthStatus: HealthCheck = await HealthService.healthCheck();
    console.log('Health Check Status:', healthStatus);
  } catch (error) {
    console.error('Error during health check:', error);
  }
}

main();
```

## Local Development

Refer to [DEVELOPMENT.md](DEVELOPMENT.md) for local development setup.

## 📄 License

Distributed under the Apache-2.0 License. See [LICENSE](./LICENSE) for more information.
