# Spark 调优相关

* spark.storage.memoryFraction

```
如前面所说 spark.executor.memory 决定了每个 Executor 可用内存的大小，
而 spark.storage.memoryFraction 则决定了在这部分内存中有多少可以用于Memory Store管理RDD Cache数据，
剩下的内存用来保证任务运行时各种其它内存空间的需要。
spark.executor.memory 默认值为0.6，官方文档建议这个比值不要超过 JVM Old Gen 区域的比值。
这也很容易理解，因为 RDD Cache 数据通常都是长期驻留内存的，理论上也就是说最终会被转移到Old Gen区域（如果该RDD还没有被删除的话），
如果这部分数据允许的尺寸太大，势必把Old Gen区域占满，造成频繁的FULL GC。如何调整这个比值，取决于你的应用对数据的使用模式和数据的规模，
粗略的来说，如果频繁发生Full GC，可以考虑降低这个比值，
这样RDD Cache可用的内存空间减少（剩下的部分Cache数据就需要通过Disk Store写到磁盘上了），会带来一定的性能损失，
但是腾出更多的内存空间用于执行任务，减少Full GC发生的次数，反而可能改善程序运行的整体性能
```

