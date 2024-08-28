def add_mileage(car, distance):
    """
    Returns a new Car instance with updated mileage and possibly an updated service date.
    """
    #todo: Implementiere die Funktion
    pass


def check_service(car):
    """
    Checks if the car's mileage exceeds 10,000 km.
    """
    #todo: Implementiere die Funktion
    pass


if __name__ == '__main__':
    my_car = Car(brand='Toyota', mileage=9500)
    print(f'Vor der Fahrt: {my_car}')

    my_car = add_mileage(my_car, 600)  # Sollte den Service hinzufügen
    print(f'Nach der ersten Fahrt: {my_car}')

    if check_service(my_car):
        print('Service benötigt!')

    my_car = add_mileage(my_car, 100)  # Keine Änderung bei Service-Daten
    print(f'Nach der zweiten Fahrt: {my_car}')
    print(f'Service-Daten: {my_car.service_dates}')