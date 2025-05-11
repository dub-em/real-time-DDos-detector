from fastapi import APIRouter

from ddos_pred_service.app.api.v1.endpoints.ddos_pred import (
    router as cachehandler_router,
)

api_router = APIRouter()

api_router.include_router(
    cachehandler_router,
    prefix="/ddos",
    tags=["DDoS"],
)
