from pathlib import Path

# urls
PEP_DOMAIN = "peps.python.org"

# other constants
DT_FORMAT = "%Y-%m-%d_%H-%M-%S"

# dirs
BASE_DIR = Path(__file__).parent.parent
RESULTS = "results"
RESULTS_DIR = BASE_DIR / RESULTS

# scrapy settins
BOT_NAME = "pep_parse"
NEWSPIDER_MODULE = "pep_parse.spiders"
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True
FEED_EXPORT_ENCODING = "utf-8"
FEEDS = {
    f"{RESULTS}/pep_%(time)s.csv": {
        "format": "csv",
        "fields": ["number", "name", "status"],
        "overwrite": True,
    },
}
ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}
