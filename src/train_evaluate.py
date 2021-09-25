from sklearn.ensemble import RandomForestRegressor
from get_data import get_config
from argparse import ArgumentParser
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
import pandas as pd
import numpy as np
import os
import pickle
import json

def evl_metric(ytest,predicted):
    rmse=np.sqrt(mean_squared_error(ytest,predicted))
    mae=mean_absolute_error(ytest,predicted)
    r2=r2_score(ytest,predicted)
    return rmse,mae,r2
def train(config_path):
    config=get_config(config_path)
    train_path=config['split_data']['train_path']
    test_path=config['split_data']['test_path']
    y=config['base']['target']
    n_e=config['estimator']['Random_forest_regressor']['params']['n_estimators']
    rs=config['estimator']['Random_forest_regressor']['params']['random_state']
    model_path=config['model_dir']
    param_path=config['reports']['params']
    scores_path=config['reports']['scores']
    train_data=pd.read_csv(train_path)
    y_train=train_data[y]
    train_data=train_data.drop([y],axis=1)
    test_data=pd.read_csv(test_path)
    y_test=test_data[y]
    test_data=test_data.drop([y],axis=1)
    reg=RandomForestRegressor(n_estimators=n_e,random_state=rs)
    reg.fit(train_data,y_train)
    predicted=reg.predict(test_data)
    rmse,mae,r2=evl_metric(y_test,predicted)
    m_p=os.path.join(model_path,'model.pkl')
    pickle.dump(reg,open(m_p,'wb'))

    with open(scores_path,'w') as f:
        score={
            'rmse':rmse,
            'mae':mae,
            'r2':r2
        }
        json.dump(score,f,indent=4)

    with open(param_path,'w') as f:
        param={
                'n_estimator':n_e,
                'random_state':rs
            }
        json.dump(param,f,indent=4)
    

if __name__=='__main__':
    arg=ArgumentParser()
    arg.add_argument('--config',default='param.yaml')
    parsed=arg.parse_args()
    train(parsed.config)