import boto3

glue_cliente = boto3.client('glue',
    region_name='us-east-1',
    aws_access_key_id='ASIAZQ3DQ2REDGOYJPFF',
    aws_secret_access_key='MCcS42RIXBV7MYoX+sYM4JA0EgiqrMX1QARHusaP',
    aws_session_token = 'IQoJb3JpZ2luX2VjEJr//////////wEaCXVzLWVhc3QtMSJGMEQCIAZoubbobipKPuDLcapVrIZw63TOmYxdv5XPEvwOXc1FAiBbzgdu+mP2doHe6GJnOADJ2OAH7+EUvznwmIREMqJzISqqAwiT//////////8BEAAaDDY1NDY1NDM2MjY5NiIMzV6aeFYNX9PHFTZEKv4CU4fIYn8ZRlvh/EdYIAmPClvTldZqDGH6Tcb1y8FjbEG4KMw5WpENcqfGLI3VFtziMgeX7zBlPydUM7NaRulff7bov8FsIY3nw2cOgZNp4fBHiF4y2/Ox89/yj7Ob54OzsQz1b7EcUafY9vYbuOL8L8urQ63PJwHFpkY7Wr1QV3NLJSRJMgPgbqc97ZziJMu3Kyum59CESJSCJ9g12HoXT7s3NOgmzAawCWAtBpD7lTGOTBscO5xCwU3Asra5j+/fhsdq5P0Zz7FmcXyb4t9kzsPVdsfVIE32Ni3dJlkd9/gYdBE9YBuWityCNk5IJ3ICBHtoJ5KFnaHgg8QPVVuxuJRQAeDZmSmL2fq6p+5Yf+14jucKF1k+UO4nujyYAYpjLYAh1XlqGrdlr/2hKgB54gk/AWTCrsuC4ddl8gP9/DucP7yQ2+rYpxDo82LPRaYzlSC1GK+rZWhhpV7YJu6uVsMCGKkoUEjmj0qM3zvpqpWn3AXgbla0amdX/zb7wjDWjum1BjqnAfoXtyAmJJ1dKI6VF5enA+uhuLez7PTa7+fJTj1KehLbQrg8ZxdOePx0MQWeIqBF8Mhgt+cXSAKEH0DEOqrgKtZfxKnjYcDpQWNU37pVoy/D9psKkQILQu0HtVFRG7gHR3iEtIGwMpaJjC0VAVBgTn2mAc0VvKVqypdrQUJ9WnLnFrWjCCKNIlFM5uUVsMky4OK2Z2EEBKH3ENj/lRGvFMTU+4W1l25H'
)

database_name = 'db_data-lake-andrey-amaral-1.1'

glue_cliente.create_database(
        DatabaseInput={
            'Name': database_name,
            'Description': 'Banco de dados para armazenar as tabelas refinadas do data lake.',
        }
    )

glue_cliente.create_table(
    DatabaseName=database_name,
    TableInput={
        'Name': 'fato_filme',
        'StorageDescriptor': {
            'Columns': [
                {'Name': 'id_filme', 'Type': 'int'},
                {'Name': 'titulo_original', 'Type': 'string'},
                {'Name': 'id_combinacao_generos', 'Type': 'int'},
                {'Name': 'popularidade', 'Type': 'float'},
                {'Name': 'lancamento', 'Type': 'string'}
            ],
            'InputFormat': 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat',
            'OutputFormat': 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat',
            'Compressed': False
        },
        'TableType': 'EXTERNAL_TABLE'
    }
)

glue_cliente.create_table(
    DatabaseName=database_name,
    TableInput={
        'Name': 'dim_genero',
        'StorageDescriptor': {
            'Columns': [
                {'Name': 'id_genero', 'Type': 'int'}
            ],
            'InputFormat': 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat',
            'OutputFormat': 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat',
            'Compressed': False
        },
        'TableType': 'EXTERNAL_TABLE'
    }
)

glue_cliente.create_table(
    DatabaseName=database_name,
    TableInput={
        'Name': 'dim_combinacao_generos',
        'StorageDescriptor': {
            'Columns': [
                {'Name': 'id_combinacao_generos', 'Type': 'int'},
                {'Name': 'id_genero', 'Type': 'int'}
            ],
            'InputFormat': 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat',
            'OutputFormat': 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat',
            'Compressed': False
        },
        'TableType': 'EXTERNAL_TABLE'
    }
)

