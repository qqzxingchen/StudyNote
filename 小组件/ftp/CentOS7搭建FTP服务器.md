
### CentOS7 搭建 FTP 服务器

```bash

# 安装 vsftpd
$ yum install -y vsftpd

# 备份 vsftpd 的配置文件( /etc/vsftpd/vsftpd.conf )

# 修改 vsftpd 的配置文件
$ vim /etc/vsftpd/vsftpd.conf
>>> # 不允许匿名访问
>>> anonymous_enable=NO
>>> # 允许使用本地帐户进行FTP用户登录验证
>>> local_enable=YES
>>> # 使用户不能离开主目录
>>> chroot_local_user=YES
>>> chroot_list_enable=YES
>>> chroot_list_file=/etc/vsftpd/chroot_list
>>> # 最后再添加一项配置
>>> allow_writeable_chroot=YES

# 保证 /etc/vsftpd/chroot_list 文件存在
$ touch /etc/vsftpd/chroot_list

# 重启 vsftpd 服务
$ systemctl restart vsftpd.service


# 添加用户，并设置密码
$ useradd -d /home/ftpuser -g ftp ftpuser
$ passwd ftpuser

# 这时候，即可通过 ftp 命令进行访问
$ ftp ftpuser@localhost

# 也可以通过 web 来进行访问
# ftp://username:password@localhost
```



