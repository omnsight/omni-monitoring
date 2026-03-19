import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from omni_python_library import init_omni_library

from omni_monitoring.routers import (
    health_router,
    monitor_trigger_router,
    monitoring_source_router,
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_omni_library()
    yield


app = FastAPI(title="Omni Monitoring", lifespan=lifespan)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTPException: {exc.status_code} {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

# Include routers
app.include_router(health_router)
app.include_router(monitoring_source_router)
app.include_router(monitor_trigger_router)
