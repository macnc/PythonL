
import pysftp as sftp

# Another solution for upload file to remote server
# 另外一种实现从本地上传文件到远程服务器的方式
try:
    s = sftp.Connection(host='beta.menpuji.com', username='root', password='dfy!3fxxk%0JSI^s')

    remotepath = '/home/mpj/app/menpuji.war'
    localpath = 'menpuji-webapp/target/menpuji.war'
    s.put(localpath, remotepath)

    s.close()

except Exception as e:
    print(str(e))