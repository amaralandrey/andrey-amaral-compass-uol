import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, explode

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

trusted_path = "s3://data-lake-andrey-amaral-1.1/Trusted/"

df_movies = spark.read.parquet(f"{trusted_path}/TMDB/JSON/ano=2024/mes=8/dia=10/")

df_movies = df_movies.withColumn("genero_exploded", explode(col("genre_ids")))

df_dim_genero = df_movies.select(
    col("genero_exploded").alias("id_genero")
).distinct()

df_dim_genero.write.mode("append").parquet("s3://data-lake-andrey-amaral-1.1/Refined/db_data-lake-andrey-amaral-1.1/dim_genero/")

job.commit()
