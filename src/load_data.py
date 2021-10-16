## read the data from the data source
## save it in the data/raw for future process

import os
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path,sep=",", index = False,header=df.columns)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")  ## to fill information about argument and turns them into object
    parsed_args = args.parse_args()  ## storing the arguments
    load_and_save(config_path=parsed_args.config)