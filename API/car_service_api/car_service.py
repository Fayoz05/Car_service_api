from fastapi import APIRouter
from database.carservice import add_car_db, change_car_info_db, delete_car_db, all_cars_db

service_router = APIRouter(prefix='/car_service', tags=['API for car service'])


@service_router.post('/add_car')
async def add_car(name: str, description: str, price: int, category_id: int):
    add = add_car_db(name, description, price, category_id)
    return add


@service_router.post('/edit_car')
async def edit_car(id: int, change_info: str, new_info):
    edit = change_car_info_db(id, change_info, new_info)
    return edit


@service_router.get('/all_cars')
async def get_all_cars():
    cars = get_all_cars()
    return cars


@service_router.post('/delete_car')
async def delete_car(id: int):
    car = delete_car_db(id)
    return car
