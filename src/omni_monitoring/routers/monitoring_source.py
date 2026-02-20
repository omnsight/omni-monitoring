import logging
from typing import Dict, List

from fastapi import APIRouter, Depends, HTTPException
from omni_python_library.dal.monitoring_source_data_access_layer import MonitoringSourceDataAccessLayer
from omni_python_library.middleware.user_token import get_user_context
from omni_python_library.models import MonitoringSource, MonitoringSourceMainData
from omni_python_library.utils import NotFoundError, PermissionDeniedError

monitoring_source_router = APIRouter()
logger = logging.getLogger(__name__)


dal = MonitoringSourceDataAccessLayer()


@monitoring_source_router.post("/monitoring-sources", response_model=MonitoringSource, tags=["Monitoring Sources"])
def create_monitoring_source(data: MonitoringSourceMainData, user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.create_monitoring_source(data, user_ctx["user_id"], user_ctx["roles"])
    except PermissionDeniedError:
        logger.exception(f"User {user_ctx['user_id']} failed to create monitoring source {data}")
        raise HTTPException(status_code=403, detail="Only the owner can create this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to create monitoring source {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@monitoring_source_router.get("/monitoring-sources/{id:path}", response_model=MonitoringSource, tags=["Monitoring Sources"])
def get_monitoring_source(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        monitoring_source = dal.get_monitoring_source(id, user_ctx["user_id"])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to get monitoring source {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    if not monitoring_source:
        raise HTTPException(status_code=404, detail="Resource not found")
    return monitoring_source


@monitoring_source_router.get("/monitoring-sources", response_model=List[MonitoringSource], tags=["Monitoring Sources"])
def get_monitoring_sources_by_user(limit: int = 100, user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.get_monitoring_sources_by_user(user_ctx["user_id"], limit=limit)
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to get monitoring sources")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@monitoring_source_router.put("/monitoring-sources/{id:path}", response_model=MonitoringSource, tags=["Monitoring Sources"])
def update_monitoring_source(id: str, data: MonitoringSourceMainData, user_ctx: Dict = Depends(get_user_context)):
    try:
        return dal.update_monitoring_source(id, data, user_ctx["user_id"], user_ctx["roles"])
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to update monitoring source {id} with data {data}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@monitoring_source_router.delete("/monitoring-sources/{id:path}", status_code=204, tags=["Monitoring Sources"])
def delete_monitoring_source(id: str, user_ctx: Dict = Depends(get_user_context)):
    try:
        dal.delete_monitoring_source(id, user_ctx["user_id"])
        return {"message": "Monitoring source deleted successfully"}
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Resource not found")
    except PermissionDeniedError:
        raise HTTPException(status_code=403, detail="Insufficient permissions to access this resource")
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to delete monitoring source {id}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
