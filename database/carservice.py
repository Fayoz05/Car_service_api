from .models import CategoryCars, Cars
from database import get_db


def add_car_db(name, description, price, category_id):
    db = next(get_db())
    new_car = Cars(name=name, description=description, price=price, category_id=category_id)
    db.add(new_car)
    db.commit()
    return f'Машина {name} была добавлена.'


def delete_car_db(id):
    db = next(get_db())
    car_delete = db.query(Cars).filter_by(id=id).first()
    if car_delete:
        db.delete(car_delete)
        db.commit()
        return 'Машина удалена'
    return 'Нет такой машины'


def change_car_info_db(id, change_info, new_info):
    db = next(get_db())
    car = db.query(Cars).filter_by(id=id).first()
    if car:
        try:
            if change_info == 'name':
                car.name = new_info
            elif change_info == 'description':
                car.description = new_info
            elif change_info == 'price':
                car.price = new_info
            elif change_info == 'category_id':
                car.category_id = new_info
            db.commit()
            return 'Данные машины изменены'
        except:
            return 'Нет ID такой машины'
    return False


def all_cars_db():
    try:
        db = next(get_db())
        cars = db.query(Cars).all()
        return cars
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        db.close()
