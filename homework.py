from turtle import window_height


class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
    
    def get_message(self) -> str:
        """Возвращает строку сообщения."""
        return (f'Тип тренировки: {self.training_type};'
                f'Длительность: {self.duration} ч.;'
                f'Дистанция: {self.distance} км;'
                f'Ср. скорость: {self.speed} км/ч;'
                f'Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
    action: int
    duration: float
    weight: float
    LEN_STEP: float 
    M_IN_KM: int 
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP: float,
                 M_IN_KM: int 
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = LEN_STEP
        self.M_IN_KM = M_IN_KM

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM  

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories()
        )


class Running(Training):
    """Тренировка: бег."""
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

