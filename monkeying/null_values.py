from pyhive import hive, presto
import json

CONFIG_FILE = 'config.json'

def get_config(key=None):
    with open(CONFIG_FILE) as config_file:
        config = json.load(config_file)
    return config[key] if key else config

hive_conn = hive.connect(**get_config('hive'))
presto_conn = presto.connect(**get_config('presto'))
