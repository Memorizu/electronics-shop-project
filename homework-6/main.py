from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    print(Item.instantiate_from_csv('./test1'))
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    print(Item.instantiate_from_csv('../test.csv'))
    # InstantiateCSVError: Файл item.csv поврежден
