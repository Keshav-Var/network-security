from pymongo import MongoClient
uri = "mongodb+srv://varshunix2023_db_user:db_user_2026@cluster0.mxurxah.mongodb.net/?appName=Cluster0&compressors=zlib"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)