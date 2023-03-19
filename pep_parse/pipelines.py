import csv
from collections import defaultdict
from csv import unix_dialect
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, DT_FORMAT, RESULTS


class PepParsePipeline:
    """Обработчик информации от парсера.
    После завершения парсинга сохраняет агрегированную
    информацию в файл.
    """
    def __init__(self):
        """Создании папки для хранения результатов
           при инициализации экземпляра класса.
        """
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        """После старта парсера создает словарь для хранения данных."""
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        """Добавляет ключи в словарь или увеличивает значение по ключу."""
        self.statuses[item.get("status")] += 1
        return item

    def close_spider(self, spider):
        """После завершения парсинга сохраняет агрегированную
        информацию в файл.
        """
        date_now = dt.now().strftime(DT_FORMAT)
        with open(
            f"{self.results_dir}/status_summary_{date_now}.csv",
            mode="w",
            encoding="utf-8",
        ) as file:
            csv.writer(
                file, dialect=unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows([
                ("Статус", "Количество"),
                *self.statuses.items(),
                ("Всего", sum(self.statuses.values())),
            ])
