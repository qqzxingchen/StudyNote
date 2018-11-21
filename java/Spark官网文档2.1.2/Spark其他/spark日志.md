# Spark日志相关

## spark.eventLog.enabled

* 针对当前最新版本的 Spark-Streaming 程序，默认情况下一个配置 `spark.eventLog.enabled` 是开启着的
    * 该配置的开启会导致 SparkListener 的执行日志写入 `hdfs:/spark2-history/${app_id}.inprogress` 目录下
    * 而如果 steaming 程序比较复杂，job个数较多的时候，它就会产生大量的事件日志，导致hdfs集群压力过大
        * 按照当前ID拉通的一个实例，大概 1 小时产生了 5G 的事件日志

* 粗暴的处理方案（已验证）
    * spark-submit 时，指定配置 `--conf spark.eventLog.enabled=false`

* 优雅的处理方案（未验证）
    * 在ambari里 Custom spark2-defaults 添加以下参数
        * spark.history.fs.cleaner.enabled true
        * spark.history.fs.cleaner.maxAge  12h
        * spark.history.fs.cleaner.interval 1h
    * 重启spark history

