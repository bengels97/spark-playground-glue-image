from pyspark.sql import SparkSession

if __name__ == "__main__":
    # Create Spark session
    spark = SparkSession.builder \
        .appName("Horse Racing Data") \
        .getOrCreate()
    
    # Read CSV file into DataFrame
    df = spark.read.csv("data.csv", header=True, inferSchema=True)
    
    # Show the data
    # If you set a debug point on line 14, you can inspect the DataFrame in the debugger using DataWrangler
    print(f"Total rows: {df.count()}")
    df.show(10)
    df.printSchema()
    
    # Stop the Spark session
    spark.stop()