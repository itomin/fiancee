from google.cloud import bigquery
import logging

logging.basicConfig(format='%(asctime)s: "%(name)s: >>  %(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class Persist():

    def __init__(self):
        self.client = bigquery.Client()
        self.job_config = bigquery.LoadJobConfig()
        self.job_config.autodetect = True
        
    # e.g bq.append("dataset", "table", [{"a" : 1, "b" : 2}])
    def append_df(self, datasetName, tableName, df):
        dataset  = self.client.dataset(datasetName)
        table = dataset.table(tableName)
        job = self.client.load_table_from_dataframe( df, table, job_config=self.job_config)
        logger.debug(job.result())

    def overwrite_df(self, datasetName, tableName, df):
        job_config = bigquery.LoadJobConfig()
        job_config.autodetect = True
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE

        dataset  = self.client.dataset(datasetName)
        table = dataset.table(tableName)
        job = self.client.load_table_from_dataframe( df, table, job_config=self.job_config)
        logger.debug(job.result())

    

    def append_json(self, datasetName, tableName, json):
        dataset  = self.client.dataset(datasetName)
        table = dataset.table(tableName)
        job = self.client.load_table_from_json( json, table, job_config=self.job_config)
        logger.debug(job.result())

    def load(self, qry):
        query_job = self.client.query(qry)  # API request
        df = query_job.to_dataframe()  # Waits for query to finish
        return df
    

    
    

    
