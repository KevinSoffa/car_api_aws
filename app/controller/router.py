from fastapi import APIRouter

# routers
from app.controller.controller_create_car import router_create_car
from app.controller.controller_delete_car import router_delete_car
from app.controller.controller_update_car import router_update_car
from app.controller.controller_list_car import router_list_car
from app.controller.controller_get_car import router_get_car


router = APIRouter()

router.include_router(router_create_car)
router.include_router(router_get_car)
router.include_router(router_list_car)
router.include_router(router_update_car)
router.include_router(router_delete_car)
