# top

* 使用 top 命令，查看 load average 栏，它分别代表了 CPU 在 1分钟、5分钟、15分钟内系统的平均负荷
    * 单 CPU 的情况下
        * 当CPU完全空闲的时候，平均负荷为0
        * 当CPU工作量饱和的时候，平均负荷为1
        * 当CPU工作量饱和之后，继续有新的任务进来，那么新进的任务就需要排队
    * 多 CPU 的情况下
        * 假设系统有两个CPU，那么当CPU工作量完全饱和时，平均负荷为 2
        * n 个CPU工作量完全饱和时，平均负荷为 n

* 查看CPU信息
    * `cat /proc/cpuinfo`
        * 查看CPU信息
    * `grep -c 'model name' /proc/cpuinfo`
        * 返回CPU的总核心数

* http://www.ruanyifeng.com/blog/2011/07/linux_load_average_explained.html


