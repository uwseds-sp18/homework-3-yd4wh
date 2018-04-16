#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Yumeng Ding
"""
import pandas as pd
import sqlite3
import os

def create_dataframe (db_arg):
    if os.path.isfile(db_arg):
        db = sqlite3.connect(db_arg)
        df = pd.read_sql_query("""
                       SELECT video_id AS video_id, category_id AS category_id,
                       'ca' AS language FROM CAvideos
                       UNION
                       SELECT video_id AS video_id, category_id AS category_id,
                       'de' AS language FROM DEvideos
                       UNION 
                       SELECT video_id AS video_id, category_id AS category_id,
                       'fr' AS language FROM FRvideos
                       UNION 
                       SELECT video_id AS video_id, category_id AS category_id,
                       'gb' AS language FROM GBvideos
                       UNION 
                       SELECT video_id AS video_id, category_id AS category_id, 
                       'us' AS language FROM USvideos;
                       """, db)
        return df
    else:
        raise ValueError("path to the database is not valid")