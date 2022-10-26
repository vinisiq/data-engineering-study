import boto3
import pandas as pd

# #Criar um cliente para interagir com o AWS S3

s3_client = boto3.client('s3')

#s3Client.download_file('myBucketName', 'objectName','objectName here')
# s3_client.download_file("datalake-vinisiq", 
#                        "data/country_vaccinations.csv",
#                        "data/country_vaccinations.csv")

# s3_client.upload_file("data/estatistica_pais.csv",
#                       "datalake-vinisiq",
#                       "data/estatistica_pais.csv")

s3_client.download_file("datalake-vinisiq",
                        "data/estatistica_pais.csv",
                        "data/estatistica_pais.csv")
#df = pd.read_csv('data/country_vaccinations.csv', sep=",")
df = pd.read_csv('data/estatistica_pais.csv', sep=";")
print(df)

