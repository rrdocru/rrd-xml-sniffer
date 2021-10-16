# coding: utf-8
from lxml import etree
from lxml.etree import QName


class Sniffer:
    """
    Класс для получения типа и версии xml-документа
    """
    def __init__(self,  xml):
        self.__xml = xml
        self.__type = None
        self.__code = None

    def get_type(self):
        """
        Получение типа документа

        Допустимые возвращаемые значения:
            * region_cadstr, kpt, extract_cadastral_plan_territory -- кадастровый план территории
            * region_cadastr_vidimus_kp, kpzu -- кадастровый паспорт земельного участка
            * region_cadastr_vidimus_kv, kvzu -- кадастровая выписка земельного участка
            * kpoks -- кадастровый паспорт объекта капитального строительства
            * kvoks -- кадастровая выписка объекта капитального строительства
            * mp -- межевой план
            * tp -- технический план
            * extract_about_boundaries -- выписка о границе между субъектами РФ, муниципального образования, населенного
              пункта
            * extract_about_property_build, extract_about_property_car_parking_space, extract_about_property_construction,
              extract_about_property_land, extract_about_property_property_complex, extract_about_property_room,
              extract_about_property_under_construction, extract_about_property_unified_real_estate_complex --
              выписка из ЕГРН об объекте недвижимости
            * extract_about_zone -- выписка о различных зонах
            * extract_base_params_build, extract_base_params_car_parking_space, extract_base_params_construction,
              extract_base_params_land, extract_base_params_property_complex, extract_base_params_room,
              extract_base_params_under_construction, extract_base_params_unified_real_estate_complex  --
              выписка из ЕГРН об основных характеристиках и зарегистрированных правах на объект недвижимости
            * schemaparcels -- схема располжения земельного участка на кадастровом плане территории

        :return: тип документа
        :rtype: str
        """
        if self.__type:
            return str(self.__type).lower()

        context = iter(etree.iterparse(self.__xml, events=('start', 'end',)))
        try:
            event, element = next(context)
            self.__type = QName(element.tag).localname
        finally:
            del context
        return str(self.__type).lower()

    def get_version(self):
        """
        Получение версии документа

        :return: версия документа
        :rtype: str
        """
        context = iter(etree.iterparse(self.__xml, events=('start', 'end',)))
        try:
            event, root = next(context)
            # Получение значения по ключу None из словаря Namespaces.
            # kvzu_06, kvzu_07, kpzu_05, kpzu_06, kvoks_03, kvokslinear_03, kposk_04, kposklinear_04, kpt_09, kpt_10
            if root.nsmap and None in root.nsmap.keys():
                self.__code = root.nsmap[None]
            # Получение версии из атрибута корневого элемента
            # mp_06, mp_08, tp_03, tp_06
            elif root.get('Version', None):
                self.__code = root.get('Version')
            else:
                # Получение версии из первого дочернего элемента
                # schemaparcels_01
                event, element = next(context)
                if element.get('Version', None):
                    self.__code = element.get('Version')
                # Все остальные случаи
                else:
                    self.__code = str(self.get_type()).lower()
        finally:
            del context
        return self.__code
