import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

trusted_path = "s3://data-lake-andrey-amaral-1.1/Trusted/"

df_movies = spark.read.parquet(f"{trusted_path}/TMDB/JSON/ano=2024/mes=8/dia=10/")

df_fato_filme = df_movies.select(
    col("id").alias("id_filme"),
    col("original_title").alias("titulo_original"),
    col("genre_ids").alias("combinacao_generos"),
    col("popularity").alias("popularidade"),
    col("release_date").alias("lancamento")
).distinct()

df_fato_filme.write.mode("append").parquet("s3://data-lake-andrey-amaral-1.1/Refined/db_data-lake-andrey-amaral-1.1/fato_filme/")

job.commit()
