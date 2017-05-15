# encoding:utf-8

import os

from AutoGenerateConfig import get_base_dir
from AutoGenerateConfig import get_executed_root_dirs
from AutoGenerateConfig import get_summary_file_path




# 判断文件是否是 markdown 文件
def check_is_markdown_file( file_path ):
    MDFILE_EXT_STR = '.md'
    return os.path.splitext( file_path )[1].lower() == MDFILE_EXT_STR

# 判断是不是readme文件
def check_is_readme_file( file_path ):
    README_FILE_NAME = 'readme.md'
    return os.path.split( file_path )[1].lower() == README_FILE_NAME
    

# 生成格式为 '    *[xxx](xxx)' 的字符串，该格式是 gitbook 要求的
def generate_summary_one_line_str( space_number,title,relative_file_path ):
    format_str = '{space_str}* [{title}]({relative_file_path})'
    format_obj = {
        'space_str': ' '*space_number,
        'title': title,
        'relative_file_path':relative_file_path
    }
    return format_str.format(**format_obj)

# 递归地遍历目录，将数状结构生成出来
def generate_summary_str_list( cur_executed_dir,str_list = [],deep = 0 ):
    cur_executed_dir_readme_file = ''
    cur_dir_dir_summary_str_list = []
    cur_dir_file_summary_str_list = []

    # 遍历目录该目录：对于该目录下的文件，直接生成 summary 字符串；对于该目录下的目录，则递归调用 generate_summary_str_list    
    child_deep = deep+1
    for path in os.listdir( cur_executed_dir ):
        child_path = os.path.join( cur_executed_dir,path )
        if os.path.isdir( child_path ):
            generate_summary_str_list( child_path,cur_dir_dir_summary_str_list,child_deep )
        else:
            if check_is_readme_file( child_path ):
                cur_executed_dir_readme_file = child_path
            elif check_is_markdown_file( child_path ):
                file_name = os.path.splitext( path )[0]
                s = generate_summary_one_line_str( child_deep*4,file_name,child_path )
                cur_dir_file_summary_str_list.append( s )

    cur_dir_file_summary_str_list.sort()
    
    # 生成当前目录对应的 summary 字符串
    cur_executed_dir_summary_str = generate_summary_one_line_str( 
        deep*4,
        os.path.split(cur_executed_dir)[1],
        cur_executed_dir_readme_file 
    )
    
    # 如果发现该目录下没有任何新生成的字符串信息，则该目录也不显示出来
    if len( cur_dir_file_summary_str_list ) + len( cur_dir_dir_summary_str_list ) > 0:
        str_list.append( cur_executed_dir_summary_str )
        str_list += cur_dir_file_summary_str_list
        str_list += cur_dir_dir_summary_str_list

def write_summary_str_to_file( summary_str_list,file_path ):
    with open( file_path,'w' ) as f:
        f.write( '# Summary\n' )
        for line_str in summary_str_list:
            f.write( line_str + '\n' )

def generate_summary():
    cur_dir = os.path.abspath(os.path.curdir)
    os.chdir( get_base_dir() )
    
    summary_str_list = []
    for root_dir in get_executed_root_dirs():
        generate_summary_str_list(root_dir,summary_str_list,0)
    
    summary_file_path = os.path.abspath( os.path.join( get_base_dir(),get_summary_file_path() ) )
    write_summary_str_to_file( summary_str_list,summary_file_path )

    os.chdir(cur_dir)
    return summary_str_list




if __name__ == '__main__':
    generate_summary()

    '''
    os.chdir( get_base_dir() )
    for path in os.listdir( get_executed_root_dirs()[0] ):
        print path
    '''
