#!/bin/bash

base_path=$(cd "$(dirname "$0")"; pwd)
cd ${base_path}

pkill -f 'gitbook serve'

# 删除原来的 _book
cd .. 
rm -rf _book
rm -rf SUMMARY.md
echo 'gitbook studynote: delete old success'


# 生成新的
cd _auto_generate_summary_file
python2 AutoGenerate.py
echo 'gitbook studynote: autogenerate success'


# 启动服务
cd ..
nohup gitbook serve --port 3000 --lrport 35728 > _auto_generate_summary_file/gitbook_serve_log.log 2>&1 & 
# gitbook serve --port 3000 --lrport 35728
echo 'gitbook studynote: gitbook serve success at http://localhost:3000/'



