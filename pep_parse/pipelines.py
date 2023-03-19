from collections import defaultdict

from datetime import datetime as dt
from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item["status"]] += 1
        return item

    def close_spider(self, spider):
        print('BASE_DIR', BASE_DIR)
        with open(
            f'{BASE_DIR}/results/status_summary_{dt.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv', mode='w', encoding='utf-8'
        ) as f:
            f.write("Статус,Количество\n")
            for key, value in self.statuses.items():
                f.write(f"{key},{value}\n")
            f.write(f"Всего,{sum(self.statuses.values())}\n")


# status_summary_2029-01-31_23-55-00.csv