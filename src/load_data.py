import os
from argparse import ArgumentParser
import pandas as pd
from get_data import get_data,get_config


def load_data_save(config_):
    config=get_config(config_)
    data=get_data(config_)
    raw_path=config['load_data']['raw_dataset']
    columns=[i.replace(" ","_") for i in data.columns]
    data.to_csv(raw_path,sep=',',index=False,header=columns)

if __name__=='__main__':
    arg=ArgumentParser()
    arg.add_argument('--config',default='param.yaml')
    parsed=arg.parse_args()
    load_data_save(parsed.config)
