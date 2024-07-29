import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import lit

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_path = "s3://data-lake-andrey-amaral/Raw/TMDB/"
output_path = "s3://data-lake-andrey-amaral/Trusted/"

datasource0 = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="json",
    connection_options={"paths": [input_path], "recurse": True},
    transformation_ctx="datasource0"
)

applymapping1 = ApplyMapping.apply(
    frame=datasource0, 
    mappings=[
        ("adult", "boolean", "adult", "boolean"),
        ("backdrop_path", "string", "backdrop_path", "string"),
        ("genre_ids", "array", "genre_ids", "array"),
        ("id", "int", "id", "int"),
        ("original_language", "string", "original_language", "string"),
        ("original_title", "string", "original_title", "string"),
        ("overview", "string", "overview", "string"),
        ("popularity", "double", "popularity", "double"),
        ("poster_path", "string", "poster_path", "string"),
        ("release_date", "string", "release_date", "string"),
        ("title", "string", "title", "string"),
        ("video", "boolean", "video", "boolean"),
        ("vote_average", "double", "vote_average", "double"),
        ("vote_count", "int", "vote_count", "int"),
        ("revenue", "int", "revenue", "int")
    ],
    transformation_ctx="applymapping1"
)

df = applymapping1.toDF()

df = df.withColumn("year", lit(2024)).withColumn("month", lit(7)).withColumn("day", lit(28))

df.write.mode("overwrite").partitionBy("year", "month", "day").parquet(output_path)

job.commit()

