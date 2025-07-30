Real-Time E-Commerce Sales Pipeline Project

This project shows how to build a complete data pipeline using AWS services and Power BI. It starts with raw sales data in CSV format and ends with a working dashboard that gives useful business insights.

Main Steps:

Uploaded raw sales data to S3 under the "raw" folder

Used AWS Glue Crawler to create a table from raw data

Created a Glue ETL job to clean the data and add a "total" column

Saved the cleaned data to the "processed" folder in S3 in Parquet format

Queried the processed data using Amazon Athena

Exported the Athena query result as CSV

Imported the CSV into Power BI and built a full dashboard

Exported the dashboard to PDF and saved the Power BI (.pbix) file

Tools Used:

AWS S3

AWS Glue Crawler

AWS Glue ETL Job (PySpark)

Amazon Athena

Power BI Desktop

Python (for triggering Glue job with boto3)

VS Code

Dashboard Features:

Total revenue (KPI card)

Sales by item (bar chart and pie chart)

Sales trend over time (line chart)

Customer vs product breakdown (matrix and stacked bar)

Filters using slicers

Project Structure:

Ingestion folder for raw CSV files

Scripts folder for Python scripts

Transform folder for Glue ETL code

exports folder with dashboard PDF

reports folder with Power BI .pbix file

README file describing the full pipeline

About Me:

I am a data engineer with hands-on experience in building cloud-based data pipelines using AWS and Azure, and in developing business dashboards in Power BI. I focus on creating scalable, end-to-end solutions that transform raw data into actionable insights.
This project demonstrates my ability to work across data ingestion, transformation, querying, and reporting layers using real-world tools and workflows.