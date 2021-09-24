from sklearn.model_selection import train_test_split
import os
import pandas as pd
from argparse import ArgumentParser
from get_data import get_config
def load_processed(config_path):
    config=get_config(config_path)
    train_path=config['split_data']['train_path']
    test_path=config['split_data']['test_path']
    raw_data_path=config['load_data']['raw_dataset']
    target=config['base']['target']
    r=config['split_data']['test_size']
    rs=config['base']['random_state']
    data=pd.read_csv(raw_data_path)
    train,test,=train_test_split(data,test_size=r,random_state=rs)
    train.to_csv(train_path,sep=',',index=False)
    test.to_csv(test_path,sep=',',index=False)

if __name__=='__main__':
    arg=ArgumentParser()
    arg.add_argument('--config',default='param.yaml')
    parsed=arg.parse_args()
    load_processed(parsed.config)