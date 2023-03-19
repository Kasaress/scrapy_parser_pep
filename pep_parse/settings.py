from pathlib import Path

# dirs
BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = "results"

# urls
PEP_URL = "https://peps.python.org/"
PEP_DOMAIN = "peps.python.org"

# other constants
DT_FORMAT = "%Y-%m-%d_%H-%M-%S"

# scrapy settins
BOT_NAME = "pep_parse"
SPIDER_MODULES = ["pep_parse.spiders"]
NEWSPIDER_MODULE = "pep_parse.spiders"
ROBOTSTXT_OBEY = True
FEED_EXPORT_ENCODING = "utf-8"
FEEDS = {
    "results/pep_%(time)s.csv": {
        "format": "csv",
        "fields": ["number", "name", "status"],
        "overwrite": True,
    },
}
ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}
