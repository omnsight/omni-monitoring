# Omni Sentinel
[![codecov](https://codecov.io/github/omnsight/omni-monitoring/graph/badge.svg?token=2LDW67VWXE)](https://codecov.io/github/omnsight/omni-monitoring)

## Overview

Omni Sentinel is a robust monitoring service designed to track and manage various information sources. It provides a flexible API to create, configure, and manage monitoring sources and set up triggers based on specific conditions.

The backend is built with Python using the FastAPI framework, leveraging ArangoDB for data persistence and Redis for caching. A TypeScript client is also provided for easy integration with frontend applications.

## Usage

### API Call Using Typescript Client

To use this client in your project, add the following to your `package.json`:

```json
{
  "dependencies": {
    "omni-monitoring-client": "github.com/omnsight/omni-monitoring#main"
  }
}
```

Here is a sample code snippet demonstrating how to use the client to invoke API calls.

```typescript
import { HealthService, OpenAPI } from 'omni-monitoring-client';

async function main() {
  // Configure the base URL and a static token
  OpenAPI.BASE = 'http://localhost:8000';
  OpenAPI.TOKEN = 'your-static-jwt-token-here';

  try {
    const health = await HealthService.healthCheckHealthGet();
    console.log('Health check result:', health);
  } catch (error) {
    console.error('Error fetching health check:', error);
  }
}
```

## Local Development

Refer to [DEVELOPMENT.md](DEVELOPMENT.md) for local development setup.
