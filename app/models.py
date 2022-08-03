import math

from django.db import models
import requests
import json


class Client(models.Model):
    title = models.CharField(max_length=50, verbose_name='название', blank=True, null=True)
    image = models.ImageField(null=True, blank=True, verbose_name='картинка', upload_to='our_clients')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Наш клиент'
        verbose_name_plural = 'Наши клиенты'


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name='название', blank=True, null=True)
    image = models.ImageField(null=True, blank=True, verbose_name='картинка', upload_to='our_projects')
    description = models.CharField(max_length=120, verbose_name='описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Наш проект'
        verbose_name_plural = 'Наши проекты'


class Fuel(models.Model):
    title = models.CharField(max_length=15, verbose_name='Тип топлива', blank=True, null=True)

    def __str__(self):
        return self.title


class Execution(models.Model):
    title = models.CharField(max_length=15, verbose_name='Исполнение', blank=True, null=True)

    def __str__(self):
        return self.title


class StartSystem(models.Model):
    title = models.CharField(max_length=15, verbose_name='Система запуска', blank=True, null=True)

    def __str__(self):
        return self.title


class ReserveAutomat(models.Model):
    title = models.CharField(max_length=7, verbose_name='Наличие автомата ввода резерва (АВР)', blank=True, null=True)

    def __str__(self):
        return self.title


class GeneratorCategory(models.Model):
    title = models.CharField(max_length=10, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория генераторов'
        verbose_name_plural = 'Категории генераторов'


class EngineManufacturer(models.Model):
    title = models.CharField(max_length=20, verbose_name='Производитель двигателя')

    def __str__(self):
        return self.title


class CylindersPositioning(models.Model):
    title = models.CharField(max_length=20, verbose_name='Расположение цилиндров')

    def __str__(self):
        return self.title


class TurboEngine(models.Model):
    title = models.CharField(max_length=5, verbose_name='Турбонаддув')

    def __str__(self):
        return self.title


class CoolingSystem(models.Model):
    title = models.CharField(max_length=15, verbose_name='Система охлаждения')

    def __str__(self):
        return self.title


class RegulatorType(models.Model):
    title = models.CharField(max_length=20, verbose_name='Тип регулятора двигателя')

    def __str__(self):
        return self.title


class AlternatorManufacturer(models.Model):
    title = models.CharField(max_length=30, verbose_name='Производитель')

    def __str__(self):
        return self.title


class Generator(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название', blank=True, null=True)
    category = models.ForeignKey(GeneratorCategory, on_delete=models.CASCADE, verbose_name='Категория')
    engine_name = models.CharField(max_length=20, verbose_name='Двигатель', blank=True, null=True)
    fuel_type = models.ForeignKey(Fuel, on_delete=models.CASCADE, verbose_name='Тип топлива')
    voltage = models.CharField(max_length=15, verbose_name='Напряжение', blank=True, null=True)
    power = models.FloatField(max_length=7, verbose_name='Мощность, кВт', blank=True, null=True)

    price = models.FloatField(verbose_name='Цена, USD', blank=True, null=True)

    execution = models.ForeignKey(Execution, on_delete=models.CASCADE, verbose_name='Исполнение')
    max_power = models.FloatField(max_length=20, verbose_name='Мощность максимальная, кВт', blank=True, null=True)
    nominal_power = models.FloatField(max_length=20, verbose_name='Мощность номинальная, кВт', blank=True, null=True)
    power_coefficient = models.FloatField(max_length=20, verbose_name='Коэффициент мощности', blank=True, null=True)
    frequency = models.IntegerField(verbose_name='Частота, Гц', blank=True, null=True)
    start_system = models.ForeignKey(StartSystem, on_delete=models.CASCADE, verbose_name='Система запуска')
    reserve_automat = models.ForeignKey(ReserveAutomat, on_delete=models.CASCADE, verbose_name='Наличие автомата '
                                                                                               'ввода резерва (АВР)')

    image = models.ImageField(blank=True, verbose_name='Изображение на странице генераторов', upload_to='generators')

    def __str__(self):
        return self.title + ' (' + self.execution.title + ")"

    # @property
    # def get_price_KZT(self):
    #     url = "https://currency-exchange.p.rapidapi.com/exchange"
    #
    #     querystring = {"from": "USD", "to": "KZT", "q": "1.0"}
    #
    #     headers = {
    #         "X-RapidAPI-Key": "16d1315cf5msheaa92765cffe447p1f31b5jsnbdf27d45f845",
    #         "X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
    #     }
    #
    #     response = requests.request("GET", url, headers=headers, params=querystring)
    #     exchange_rate = float(response.text)
    #
    #     return math.ceil(exchange_rate * self.price)

    class Meta:
        verbose_name = 'Генератор'
        verbose_name_plural = 'Генераторы'


class Engine(models.Model):
    generator = models.OneToOneField(Generator, default=None, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(EngineManufacturer, on_delete=models.CASCADE,
                                     verbose_name='Производитель двигателя', help_text='Двигатель', default='')
    engine_model = models.CharField(max_length=10, verbose_name='Модель двигателя', blank=True, null=True)
    speed = models.IntegerField(verbose_name='Количество оборотов двигателя', blank=True, null=True)
    working_power = models.FloatField(max_length=5, verbose_name='Рабочая мощность двигателя', blank=True,
                                      null=True)
    max_power = models.FloatField(max_length=5, verbose_name='Максимальная мощность двигателя', blank=True,
                                  null=True)
    cylinders = models.IntegerField(verbose_name='Количество цилиндров', blank=True, null=True)
    cylinders_positioning = models.ForeignKey(CylindersPositioning, on_delete=models.CASCADE,
                                              verbose_name='Расположение цилиндров', default='')
    turbo = models.ForeignKey(TurboEngine, on_delete=models.CASCADE, verbose_name='Турбонаддув', default='')
    cooling_system = models.ForeignKey(CoolingSystem, on_delete=models.CASCADE,
                                       verbose_name='Система охлаждения', default='')
    regulator_type = models.ForeignKey(RegulatorType, on_delete=models.CASCADE,
                                       verbose_name='Тип регулятора двигателя', default='')
    volume = models.FloatField(max_length=7, verbose_name='Объём двигателя, л', blank=True, null=True)
    electric_system = models.FloatField(max_length=7, verbose_name='Электрическая система питания, В',
                                        blank=True, null=True)
    fuel_consumption_50 = models.FloatField(max_length=20, verbose_name='Расход топлива при 50% нагрузке',
                                            blank=True, null=True)
    fuel_consumption_75 = models.FloatField(max_length=20, verbose_name='Расход топлива при 75% нагрузке',
                                            blank=True, null=True)
    fuel_consumption_100 = models.FloatField(max_length=20, verbose_name='Расход топлива при 100% нагрузке',
                                             blank=True, null=True)

    def __str__(self):
        return self.manufacturer.title + " " + self.engine_model

    class Meta:
        verbose_name = 'Двигатель'
        verbose_name_plural = 'Двигатели'


class Alternator(models.Model):
    generator = models.OneToOneField(Generator, default=None, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(AlternatorManufacturer, on_delete=models.CASCADE,
                                     verbose_name='Производитель альтернатора', default='')
    type = models.TextField(verbose_name='Тип', blank=True, null=True)
    nominal_power = models.FloatField(max_length=20, verbose_name='Номинальная мощность', blank=True,
                                      null=True)
    overload = models.CharField(max_length=30, verbose_name='Перегрузка', blank=True, null=True)
    isolation_resistance = models.FloatField(max_length=20, verbose_name='Сопр. изоляции, vac', blank=True,
                                             null=True)
    isolation_level = models.CharField(max_length=2, verbose_name='Степень изоляции', blank=True, null=True)
    voltage = models.CharField(max_length=15, verbose_name='Напряжение, В', blank=True, null=True)
    voltage_regulator = models.CharField(max_length=10, verbose_name='Регулятор напряжения', blank=True,
                                         null=True)

    def __str__(self):
        return self.manufacturer.title + " " + str(self.nominal_power)

    class Meta:
        verbose_name = 'Альтернатор'
        verbose_name_plural = 'Альтернатор'


class GeneratorParameters(models.Model):
    generator = models.OneToOneField(Generator, default=None, on_delete=models.CASCADE)
    fuel_tank_volume = models.FloatField(max_length=20, verbose_name='Емкость топливного бака, л', blank=True,
                                         null=True)
    length = models.FloatField(max_length=20, verbose_name='Длина, мм', blank=True, null=True)
    width = models.FloatField(max_length=20, verbose_name='Ширина, мм', blank=True, null=True)
    height = models.FloatField(max_length=20, verbose_name='Высота, мм', blank=True, null=True)
    weight = models.FloatField(max_length=20, verbose_name='Масса, кг', blank=True, null=True)

    def __str__(self):
        return self.generator.__str__() + " parameters"

    class Meta:
        verbose_name = 'Параметры'
        verbose_name_plural = 'Параметры'


class GeneratorImage(models.Model):
    generator = models.ForeignKey(Generator, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='generators_description', verbose_name='Изображения')

    def __str__(self):
        return self.generator.title

    class Meta:
        verbose_name = 'Изображение генератора в описании'
        verbose_name_plural = 'Изображения генератора в описании'
