from sqlalchemy import create_engine
import pandas as pd
import os
from config import Config

engine = create_engine('postgresql://'+Config.username+':'+Config.password+'@localhost:5432/'+Config.db)
folder = os.path.join(os.getcwd(), 'csv')

for subdir, dirs, files in os.walk(folder):
    for file in files:
        print 'importing: ' + file
        df = pd.read_csv(os.path.join(folder, file),  encoding='utf-8')
        df.to_sql(file, engine, if_exists='replace')
        