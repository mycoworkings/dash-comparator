from utils.verifiers import check_existing_path
import pandas as pd


# If data is already created, we will append new values to the existing csv file.
# If data is not created, we will create the csv file in the path we have introduced.
def create_update_csv(df: pd.DataFrame, path: str):
    if check_existing_path(path):
        df.to_csv(path, mode="a", index=False)
    else:
        df.to_csv(path, index=False)

