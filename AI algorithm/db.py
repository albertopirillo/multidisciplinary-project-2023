"""
    This script contains functions to interact with the database.
    It is used by the API to retrieve the data it needs its operations.
"""

import os
import numpy as np
import pandas as pd
import psycopg
import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy import create_engine


def alchemy_engine() -> sqlalchemy.Engine:
    """ Return an object to connect to the DB using SQLAlchemy """
    load_dotenv()
    return create_engine(os.getenv("DATABASE_URL"))


def psycopg_engine() -> psycopg.Connection:
    """ Return an object to connect to the DB using psycopg3 """
    load_dotenv()
    return psycopg.connect(os.getenv("DATABASE_URL"))


def get_worker_embedding(worker_id: int) -> pd.DataFrame:
    """ Retrieve the ID and the embedding of one worker in the DB """
    with alchemy_engine().connect() as conn:
        df = pd.read_sql_query("""
            SELECT worker_id, embedding FROM worker
            WHERE worker_id = %(worker_id)s
            """, conn, params={'worker_id': str(worker_id)})
        df["embedding"] = df["embedding"].apply(lambda x: np.array(x, dtype="float32"))
        return df


def get_offer_embedding(offer_id: int) -> pd.DataFrame:
    """ Retrieve the ID and the embedding of one worker in the DB """
    with alchemy_engine().connect() as conn:
        df = pd.read_sql_query("""
            SELECT offer_id, embedding FROM job_offer
            WHERE offer_id = %(offer_id)s
            """, conn, params={'offer_id': str(offer_id)})
        df["embedding"] = df["embedding"].apply(lambda x: np.array(x, dtype="float32"))
        return df


def get_all_cv_embeddings() -> pd.DataFrame:
    """ Retrieve the ID and the embedding of every worker in the DB """
    with alchemy_engine().connect() as conn:
        df = pd.read_sql_query("SELECT worker_id, embedding FROM worker", conn)
        df["embedding"] = df["embedding"].apply(lambda x: np.array(x, dtype="float32"))
        return df


def get_all_jobs_embeddings() -> pd.DataFrame:
    """ Retrieve the ID and the embedding of every job offer in the DB """
    with alchemy_engine().connect() as conn:
        df = pd.read_sql_query("SELECT offer_id, embedding FROM job_offer", conn)
        df["embedding"] = df["embedding"].apply(lambda x: np.array(x, dtype="float32"))
        return df


def get_offer_embeddings(offer_id: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    """ Retrieve the ID and the embedding of the workers that applied to a specific job offer"""
    with alchemy_engine().connect() as conn:
        # Get the embedding of the job offer
        df_offer = pd.read_sql_query("""
            SELECT offer_id, embedding FROM job_offer
            WHERE offer_id = %(offer_id)s
            """, conn, params={'offer_id': str(offer_id)})

        # Get the embeddings of the CV of the workers that applied
        df_workers = pd.read_sql_query("""
            SELECT worker.worker_id, worker.embedding 
            FROM worker JOIN applies_to
            ON applies_to.worker_id = worker.worker_id 
            AND offer_id =  %(offer_id)s
            """, conn, params={'offer_id': str(offer_id)})

        # Pre-process the embeddings
        df_offer["embedding"] = df_offer["embedding"].apply(lambda x: np.array(x, dtype="float32"))
        df_workers["embedding"] = df_workers["embedding"].apply(lambda x: np.array(x, dtype="float32"))

        return df_offer, df_workers
