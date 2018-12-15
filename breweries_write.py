from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String, Date,Float
from sqlalchemy import select
from sqlalchemy import func, asc
from datetime import datetime

import pandas as pd

engine = create_engine('mysql://root:Overfitting@localhost/brew', pool_recycle=3600)

meta = MetaData(engine)
#create table breweries (name VARCHAR(40), city VARCHAR(20), state CHAR(2),rating FLOAT, brewery_id INT);    

cols=['name','city','state','rating','brewery_id']

csv=pd.read_csv('breweries_sql.csv')
csv=csv[cols]
csv=csv.fillna("")
csv.to_sql('breweries', engine, if_exists='replace', index=False)
with engine.connect() as con:
    con.execute('ALTER TABLE `breweries` ADD PRIMARY KEY (`brewery_id`);') #couldnt figue out how to set this up with pandas sql write


regions=pd.read_csv('regions.csv')
regions.columns=regions.columns.str.lower()
regions.columns=[i.replace(" ","_") for i in regions.columns]
regions=regions.fillna("")
regions.to_sql('regions', engine, if_exists='replace', index=False)
with engine.connect() as con:
    con.execute('ALTER TABLE `regions` MODIFY `state_code` CHAR(2);')
    con.execute('ALTER TABLE `regions` ADD PRIMARY KEY (`state_code`);')

beers=pd.read_csv('beers.csv')
beers=beers[beers.columns[1:]]
beers.columns=beers.columns.str.lower()
beers.columns=[i.replace(" ","_") for i in beers.columns]
beers=beers.fillna("")
beers.to_sql('beers', engine, if_exists='replace', index=False)
