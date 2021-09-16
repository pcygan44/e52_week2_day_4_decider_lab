


def preferences(task1, task2):
    if task1.description == "Wash Dishes" and task2.description == "Cook Dinner":
        return task1.description
    if task1.description == "Cook Dinner" and task2.description == "Clean Windows":
        return task1.description
    if task1.description == "Clean Windows" and task2.description == "Wash Dishes":
        return task1.description
    if task1.description == "Wash Dishes" and task2.description == "Wash Clothes":
        return task1.description
    if task1.description == "Cook Dinner" and task2.description == "Do Ironing":
        return task1.description
    if task1.description == "Clean Windows" and task2.description == "Do Ironing":
        return task1.description
    if task1.description == "Do Ironing" and task2.description == "Wash Clothes":
        return task1.description
    if task1.description == "Do Ironing" and task2.description == "Wash Dishes":
        return task1.description
    if task1.description == "Wash Clothes" and task2.description == "Cook Dinner":
        return task1.description
    if task1.description == "Wash Clothes" and task2.description == "Clean Windows":
        return task1.description