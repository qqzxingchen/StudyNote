# encoding:utf-8

import os



# 基准目录。下面传入的目录、文件等配置，都必须基于该目录
def get_base_dir():
    cur_file = os.path.abspath(__file__)
    return os.path.dirname( os.path.dirname(cur_file) )

# 这些目录下的文件将会被处理
def get_executed_root_dirs():
    return [ 'component_elasticsearch','docker','java','测试方法','小组件' ]

def get_summary_file_path():
    return 'SUMMARY.md'



if __name__ == "__main__":
    print get_base_dir()
    print get_executed_root_dirs()


