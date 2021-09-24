import os
from argparse import ArgumentParser
import pandas as pd
import yaml

def get_config(config_):
    with open(config_) as yamlfile:
        config=yaml.safe_load(yamlfile)
    return config
def get_data(config_):
    config=get_config(config_)
    data=pd.read_csv(config['data_source']['s3_source'])
    return data
if __name__=='__main__':
    arg=ArgumentParser()
    arg.add_argument('--config',default='param.yaml')
    parsed=arg.parse_args()
    get_data(parsed.config)