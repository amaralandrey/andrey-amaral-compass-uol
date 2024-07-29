import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Definição dos caminhos de entrada e saída
input_path = "s3://data-lake-andrey-amaral/Raw/Local/CSV/"
output_path = "s3://data-lake-andrey-amaral/Trusted/"

# Extração dos dados
datasource0 = glueContext.create_dynamic_frame.from_options(
    format_options={"withHeader": True},
    connection_type="s3",
    format="csv",
    connection_options={"paths": [input_path]},
    transformation_ctx="datasource0"
)

# Transformação dos dados
applymapping1 = ApplyMapping.apply(
    frame=datasource0, 
    mappings=[("col1", "string", "col1", "string"), ("col2", "int", "col2", "int")],
    transformation_ctx="applymapping1"
)

# Conversão para o spark dataframe
df = applymapping1.toDF()

# Carregamento dos dados para o s3
df.write.mode("append").parquet(output_path)

job.commit()
