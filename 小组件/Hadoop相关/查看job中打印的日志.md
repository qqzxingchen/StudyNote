# 查看 job 中打印的日志

* 如果向 hadoop 提交的任务在 map/reduce 各个阶段有打印日志，会发现在提交的控制台完全看不到这些日志信息，可以通过下面方法来查看
    * 首先向 hadoop 集群提交该 job ，然后查看控制台的日志输出，找到 applicationId ，如
    ```
    17/12/05 14:52:42 INFO util.RegionSizeCalculator: Calculating region sizes for table "btw_v1_3_1_demo_rongmei_hbase:OfflineUserProfileV3".
    17/12/05 14:52:43 INFO mapreduce.JobSubmitter: number of splits:64
    17/12/05 14:52:44 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1510880316990_0051
    17/12/05 14:52:44 INFO impl.YarnClientImpl: Submitted application application_1510880316990_0051    // applicationId
    17/12/05 14:52:44 INFO mapreduce.Job: The url to track the job: http://bjlg-3p41-opvm-bdos-name-02.bfdabc.com:8088/proxy/application_1510880316990_0051/
    17/12/05 14:52:44 INFO mapreduce.Job: Running job: job_1510880316990_0051
    17/12/05 14:52:59 INFO mapreduce.Job: Job job_1510880316990_0051 running in uber mode : false
    17/12/05 14:52:59 INFO mapreduce.Job:  map 0% reduce 0%
    17/12/05 14:53:33 INFO mapreduce.Job:  map 8% reduce 0%
    ```
    * 等待该 job 执行完毕，则可以在命令行通过下面命令进行聚合
    ```bash
    yarn logs -applicationId application_1510880316990_0051 > app.log
    ```

* 注意，上述方法要求 yarn 开启日志聚合特性，即 `Enable Log Aggregation = true`
