import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, monotonically_increasing_id

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

refined_path = "s3://data-lake-andrey-amaral-1.1/Refined/"

df_movies = spark.read.parquet(f"{refined_path}/db_data-lake-andrey-amaral-1.1/dim_genero/")

df_movies = df_movies.withColumn("id_combinacao_generos", monotonically_increasing_id())

df_dim_combinacao_generos = df_movies.select(
    col("id_combinacao_generos"),
    col("id_genero")
).distinct()

df_dim_combinacao_generos.write.mode("append").parquet("s3://data-lake-andrey-amaral-1.1/Refined/db_data-lake-andrey-amaral-1.1/dim_combinacao_generos/")

job.commit()
