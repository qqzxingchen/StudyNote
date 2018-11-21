# jstat

* 使用 jstat 命令，查看 FGC 列，确认指定进程的 FULLGC 次数
    * 命令: `jstat -gcutil ${pid} 1000`
    * 查看 FGC 列，确认指定进程的 FULLGC 次数
        * 一般来说，如果进程执行期间， FGC 的值不停地涨，这说明进程的执行导致频繁的 FGC ，问题需要解决
        
