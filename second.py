year = int(input('Введите номер года: '))

match year % 12:
    case 0:
        animal_of_year = 'обезьяны'
    case 1:
        animal_of_year = 'петуха'
    case 2:
        animal_of_year = 'собаки'
    case 3:
        animal_of_year = 'свиньи'
    case 4:
        animal_of_year = 'крысы'
    case 5:
        animal_of_year = 'коровы'
    case 6:
        animal_of_year = 'тигра'
    case 7:
        animal_of_year = 'зайца'
    case 8:
        animal_of_year = 'дракона'
    case 9:
        animal_of_year = 'змеи'
    case 10:
        animal_of_year = 'лошади'
    case 11:
        animal_of_year = 'овцы'

print(f'{year} г. - год {animal_of_year}')
