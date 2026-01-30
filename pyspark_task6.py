cat > /tmp/pyspark_task6.py <<'EOF'
> from pyspark.sql import SparkSession
> from pyspark.sql.types import StructType, StructField, IntegerType, StringType
>
> print("="*60)
> print("Task 6: PySpark - Reading and Processing Data")
> print("="*60)
>
> # Create Spark Session
> spark = SparkSession.builder \
>     .appName("BigData-Assignment5-Task6") \
>     .getOrCreate()
>
> spark.sparkContext.setLogLevel("ERROR")
>
> # Define schema for users data
> schema = StructType([
>     StructField("id", IntegerType(), True),
>     StructField("name", StringType(), True),
>     StructField("age", IntegerType(), True)
> ])
>
> # Read data from HDFS
> print("\n1. Reading data from HDFS...")
> df_users = spark.read.csv("/user/bigdata/users/part-m-00000", schema=schema)
>
> print("\n2. Showing users data:")
> df_users.show()
>
> print("\n3. Data Statistics:")
> print(f"Total Records: {df_users.count()}")
> df_users.describe().show()
>
> print("\n4. Age Analysis:")
> df_users.groupBy("age").count().orderBy("age").show()
>
> print("\n5. Users above age 25:")
> df_users.filter(df_users.age > 25).show()
>
> # Create new data
> print("\n6. Creating new records to export:")
> new_data = [
>     (7, "Ali", 24),
>     (8, "Nour", 31),
>     (9, "Heba", 26)
> ]
>
> df_new = spark.createDataFrame(new_data, schema)
> print("\nNew users to add:")
> df_new.show()
>
> # Save new data to HDFS
> print("\n7. Saving new data to HDFS...")
> df_new.write.mode("overwrite").csv("/user/bigdata/pyspark_export", header=False)
> print("✓ Data saved to /user/bigdata/pyspark_export")
>
> print("\n" + "="*60)
> print("✓ Task 6 Completed Successfully!")
> print("="*60)
>
> spark.stop()
> EOF