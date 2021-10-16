# coding: utf-8
import logging
from rrd_xml_sniffer.sniffer import Sniffer

logger = logging.getLogger(__name__)


def createParser():
    """
    Объявление параметров командной строки

    :return: объект с определенными параметрами
    :rtype: argparse.ArgumentParser
    """
    import argparse  # noqa
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input',
                        help='Шаблон пути для поиска файлов',
                        type=str,
                        required=True
                        )
    parser.add_argument('-r', '--recursive',
                        help='Рекурсивный обход при поиске по паттерну',
                        action='store_false')
    return parser


def main():
    import os  # noqa
    from rrd_utils.utils import rrd_file_iterator_with_origin_name  # noqa
    parser = createParser()
    args = parser.parse_args()
    pattern = args.input
    type_version = dict()
    for xml, origin in rrd_file_iterator_with_origin_name(pattern, args.recursive):
        sniffer = Sniffer(xml)
        type_xml = sniffer.get_type()
        version_xml = sniffer.get_version()
        type_version.setdefault(type_xml, dict()).setdefault(version_xml, 0)
        type_version[type_xml][version_xml] += 1
        print('Документ: {:<100}. Тип документа: {:<50}. Версия документа: {}'.format(
            os.path.basename(origin), type_xml, version_xml)
        )
        del sniffer
    print(type_version)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
