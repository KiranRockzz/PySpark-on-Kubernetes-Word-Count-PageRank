from pyspark import SparkContext

if __name__ == "__main__":
    sc = SparkContext("local", "PySpark Word Count Example")

    words = sc.textFile("/home/kgolla98119/week-7/words.txt").flatMap(lambda li>
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a +>
    
    wordCounts.saveAsTextFile("/home/kgolla98119/week-7/output/")
