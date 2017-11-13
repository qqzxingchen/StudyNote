# Codis/Redis 数据备份

* 由于 codis 是由多个 redis 节点构成的，因此这里备份 codis 数据的方法就是单独备份多个 redis

```bash

172.18.1.46:6900> config get dir                # redis 数据备份文件存储的目录
   "dir"
   "/opt/bfd/codis/serverconf/data"
172.18.1.46:6900> config get dbfilename         # redis 数据备份文件的文件名
   "dbfilename"
   "dump6900.rdb"
172.18.1.46:6900> save                          # 进行数据备份，备份数据将会被写入 ${dir}/${dbfilename} 文件中
   OK

```

* 备份完成之后，要留意 dir 和 dbfilename 是否需要恢复到初始值
