# RRD-XML-SNIFFER

## Описание
Утитила проекта RRDoc которая извлекает из xml-документа его тип и версию

## Использование
Пакет rrd-xml-sniffer содержит экспортируемый класс Sniffer в котором реализованы функции получения типа и версии
документа.
```python
from rrd_xml_sniffer.sniffer import Sniffer

sniffer = Sniffer('полный путь к xml-документу')
type_xml = sniffer.get_type()
version_xml = sniffer.get_version()
``` 

### Возвращаемые типы документов
В пакете реализована поддержка предыдующих, актуальных и разрабатываемых типов докуметов получаемых из Росреестра
* region_cadstr, kpt, extract_cadastral_plan_territory -- кадастровый план территории
* region_cadastr_vidimus_kp, kpzu -- кадастровый паспорт земельного участка
* region_cadastr_vidimus_kv, kvzu -- кадастровая выписка земельного участка
* kpoks -- кадастровый паспорт объекта капитального строительства
* kvoks, kvokslinear -- кадастровая выписка объекта капитального строительства (и условная часть линейного)
* mp -- межевой план
* tp -- технический план
* extract_about_boundary -- выписка о границах
* extract_about_property_build, extract_about_property_car_parking_space, extract_about_property_construction,
  extract_about_property_land, extract_about_property_property_complex, extract_about_property_room,
  extract_about_property_under_construction, extract_about_property_unified_real_estate_complex --
  выписка из ЕГРН об объекте недвижимости
* extract_about_zone -- выписка о зонах
* extract_base_params_build, extract_base_params_car_parking_space, extract_base_params_construction,
  extract_base_params_land, extract_base_params_property_complex, extract_base_params_room,
  extract_base_params_under_construction, extract_base_params_unified_real_estate_complex  --
  выписка из ЕГРН об основных характеристиках и зарегистрированных правах на объект недвижимости
* schemaparcels -- схема разположения земельного(-ых) участка(-ов) на кадастровом плане территории
  
### Возвращаемые версии документов
Возвращаемые версии документов зависят от типа документа:
* Межевой план:
    * 06

* Технический план
    * 03

* Кадастровый паспорт объекта капитального строительства:
    * urn://x-artefacts-rosreestr-ru/outgoing/kpoks/3.0.7
    * urn://x-artefacts-rosreestr-ru/outgoing/kpoks/4.0.1

* Кадастровая выписка объекта капитального строительства:
    * urn://x-artefacts-rosreestr-ru/outgoing/kvoks/2.0.5
    * urn://x-artefacts-rosreestr-ru/outgoing/kvoks/3.0.1

* Кадастровая выписка объекта капитального строительства (условная часть линейного):
    * urn://x-artefacts-rosreestr-ru/outgoing/kvokslinear/2.0.5
    * urn://x-artefacts-rosreestr-ru/outgoing/kvokslinear/3.0.1

* Кадастровый паспорт земельного участка:
    * urn://x-artefacts-rosreestr-ru/outgoing/kpzu/5.0.8
    * urn://x-artefacts-rosreestr-ru/outgoing/kpzu/6.0.1
    
* Кадастровая выписка о земельном участке:
    * urn://x-artefacts-rosreestr-ru/outgoing/kvzu/6.0.9
    * urn://x-artefacts-rosreestr-ru/outgoing/kvzu/7.0.1

* Кадастровый план территории: 
    * urn://x-artefacts-rosreestr-ru/outgoing/kpt/9.0.3, 
    * urn://x-artefacts-rosreestr-ru/outgoing/kpt/10.0.1
    * extract_cadastral_plan_territory

* Выписка из ЕГРН об объекте недвижимости:
    * extract_about_property_build
    * extract_about_property_car_parking_space
    * extract_about_property_construction
    * extract_about_property_land
    * extract_about_property_property_complex
    * extract_about_property_room
    * extract_about_property_under_construction
    * extract_about_property_unified_real_estate_complex

* Выписка из ЕГРН об основных характеристиках и зарегистрированных правах на объект недвижимости:
    * extract_base_params_build
    * extract_base_params_car_parking_space
    * extract_base_params_construction
    * extract_base_params_land
    * extract_base_params_property_complex
    * extract_base_params_room
    * extract_base_params_under_construction
    * extract_base_params_unified_real_estate_complex

* Схема разположения земельного(-ых) участка(-ов) на кадастровом плане территории
    * 01

* Кадастровая выписка о границах
    * urn://x-artefacts-rosreestr-ru/outgoing/kv-bound/1.0.1

* Кадастровая выписка о зонах
    * urn://x-artefacts-rosreestr-ru/outgoing/kv-zone/1.0.1

* Высписка о границах
    * extract_about_boundary

* Выписка о зоне
    * extract_about_zone


## Тестирование
Зависимости для запуска тестов находятся в файле `tests/requirements.txt`

Запуск
```cmd
pytest
```

## Публикация пакета
### Twine
1. Изменить версию в файле `rrd_xml_sniffer/__init__.py`
2. Собрать и опубликовать пакет.
    1. В автоматическом режиме: пакет публикуется при помощи bitbucket-pipeline при коммите в ветку `master`
    2. В ручном режиме:
        ```cmd
        python setup.py sdist bdist_wheel
        twine upload --repository-url https://pypi.it-thematic.ru dist/*
        ``` 
### Poetry
1. Изменить версию
    ```cmd
    poetry version patch|minor|major|prepatch|preminor|premajor|prerelease
    ```
    правило увеличения версии выберается в зависимости от сделанных изменений
2. Собрать и опубликовать пакет.
    1. Добавить в конфигурационный файл poetry описание pypi-репозитория если он не был добавлен
    ```cmd
    poetry config repositories.itt https://pypi.it-thematic.ru
    ```
    2. Опубликовать пакет с его предварительной сборкой
    ```cmd
    poetry publish --build --repositry itt --username <имя пользователя в pypi-репозитории> --password <пароль>
    ```
