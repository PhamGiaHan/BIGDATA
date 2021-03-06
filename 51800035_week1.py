# -*- coding: utf-8 -*-
"""51800035.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U-r03c-kKRihWwo_CoyIc6CdhRpNg8wo
"""

!pip install pyspark

from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("Word Counting Example")
sc = SparkContext.getOrCreate(conf = conf)
text_File = sc.textFile('/content/example.txt')
files = (text_File.map(lambda line: line.split(' '))).reduce(lambda x: 1)

words = (sc.parallelize(files)).map(lambda word: (word, 1))
counts = words.count()
print("Văn bản trên có " + str(counts) + " từ")

words = words.reduceByKey(lambda x, y: x+y)
mostWord = (words.reduce(lambda a, b: a if a[1] > b[1] else b))
counts_1 = [x[0] for x in words.collect() if (x[1] == mostWord[1])]

print("Các từ '" + ', '.join(map(str, counts_1)) + "' có tần suất xuất hiện nhiều nhất với " + str(mostWord[1]) + " lần")

