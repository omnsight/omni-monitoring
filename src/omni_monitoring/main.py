from contextlib import asynccontextmanager

from fastapi import FastAPI
from omni_python_library import init_omni_library

from omni_monitoring.routers import (
    health_router,
    monitor_trigger_router,
    monitoring_source_router,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_omni_library()
    yield


app = FastAPI(title="Omni Monitoring", lifespan=lifespan)

# Include routers
app.include_router(health_router)
app.include_router(monitoring_source_router)
app.include_router(monitor_trigger_router)
