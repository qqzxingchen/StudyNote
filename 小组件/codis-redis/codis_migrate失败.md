# Codis migrate 操作失败的处理

* Codis migrate 可能会因为多种原因（比如 proxy 当掉，codis节点网络故障等原因）导致失败。
    而如果失败之后，你会发现即使重启 dashboard ，页面上仍然会显示 migrate 任务正在运行中，且仍旧卡在失败的一个 slot 迁移上。

* 这时候需要根据失败 slot 的状态，确定该 slot 的迁移是否已经开始
    * 查看 dashboard 的日志，找到问题所在并解决，之后 codis 迁移任务将会继续执行(如果不处理，则该 migrate 任务将会一直重试下去，直到成功执行)
    * 在 zookeeper 中强制停止该任务，如下:

```bash
# 连接 zk
$ ./bin/zkCli.sh

# 找到 codis 在 zookeeper 中注册的地址
>>> ls /zk/codis/db_xxx

# 查看 migrate 任务列表
>>> ls /zk/codis/db_xxx/migrate_tasks

# 手动删除所有的 migrate 任务
# 注意，如果该 slot 的迁移已经开始，只是在迁移过程中发生错误导致终止，则删除该任务可能会导致丢失该 slot 的数据
>>> delete /zk/codis/db_xxx/migrate_tasks/0000000000
>>> delete /zk/codis/db_xxx/migrate_tasks/0000000002
>>> delete /zk/codis/db_xxx/migrate_tasks/0000000003
...

```
