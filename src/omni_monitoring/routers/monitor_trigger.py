import logging
from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from omni_python_library.dal.monitor_trigger_data_access_layer import MonitorTriggerDataAccessLayer
from omni_python_library.middleware.user_token import get_user_context
from omni_python_library.models import MonitorTrigger, MonitorTriggerMainData

monitor_trigger_router = APIRouter()
logger = logging.getLogger(__name__)


dal = MonitorTriggerDataAccessLayer()


@monitor_trigger_router.post("/monitor-triggers", response_model=MonitorTrigger, tags=["Monitor Triggers"])
def create_monitor_trigger(trigger: MonitorTriggerMainData, user_ctx: Dict = Depends(get_user_context)):
    try:
        trigger = MonitorTrigger(
            user_id=user_ctx["user_id"],
            **trigger.model_dump(exclude_unset=True),
        )
        dal.create_monitor_trigger(trigger)
        return trigger
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to create monitor trigger {trigger}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@monitor_trigger_router.get("/monitor-triggers", response_model=MonitorTrigger, tags=["Monitor Triggers"])
def get_monitor_trigger(user_ctx: Dict = Depends(get_user_context)):
    try:
        trigger = dal.get_monitor_trigger(user_id=user_ctx["user_id"])
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to get monitoring source")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    if trigger is None:
        raise HTTPException(status_code=404, detail="Monitor trigger not found")
    return trigger


@monitor_trigger_router.delete("/monitor-triggers", status_code=204, tags=["Monitor Triggers"])
def delete_monitor_trigger(user_ctx: Dict = Depends(get_user_context)):
    trigger = dal.get_monitor_trigger(user_id=user_ctx["user_id"])

    if not trigger:
        raise HTTPException(status_code=404, detail="Monitor trigger not found")

    try:
        dal.delete_monitor_trigger(user_id=user_ctx["user_id"])
        return {"message": "Monitor trigger deleted successfully"}
    except Exception:
        logger.exception(f"User {user_ctx['user_id']} failed to delete monitor trigger {trigger}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
