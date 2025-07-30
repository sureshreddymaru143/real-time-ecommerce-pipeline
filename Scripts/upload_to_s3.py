import boto3

bucket_name = 'suresh-sales-data'
file_path = 'Ingestion/sales_data.csv'
s3_key = 'raw/sales_data.csv'  # This is the "folder" and file name in S3

# Upload to S3
s3 = boto3.client('s3')

try:
    s3.upload_file(file_path, bucket_name, s3_key)
    print(f"✅ File uploaded successfully to s3://{bucket_name}/{s3_key}")
except Exception as e:
    print("❌ Upload failed:", e)
