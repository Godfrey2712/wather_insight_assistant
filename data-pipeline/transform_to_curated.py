# Welcome to your new notebook
# Type here in the cell editor to add code!
# Read raw table from Lakehouse
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
df = spark.read.load("Tables/dbo/raw_weather_data", format="delta")

# Inspect schema to confirm nesting
df.printSchema()

# Transform into curated schema
# Select columns using col() to safely access dot-named fields
curated = df.select(
    col("`data.time`").alias("time"),
    col("`data.temp`").alias("temperature"),
    col("`data.rhum`").alias("humidity"),
    col("`data.wspd`").alias("windspeed")
)

# Save curated DataFrame as a new Lakehouse table
curated.write.mode("overwrite").saveAsTable("curated_weather_data")