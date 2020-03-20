


Ubuntu下系统默认自带Python环境，升级到最新版本后，系统会出现多个版本。以Python2.7-->Python3.7为例：

    1、安装路径：/usr/bin/python3
    2、在/usr/bin目录下使用 ls -l | grep python 查询 Python版本对应信息：
            python -> /etc/alternatives/python
            python2 -> python2.7
            python2.7
            python3 -> /etc/alternatives/python3
            python3.7
    3、在/etc/alternatives目录下使用 ls -l | grep python 查询 Python版本对应信息：
            python -> /usr/bin/python3
            python3 -> /usr/bin/python3.7
    4、需手动将系统自带的python2环境切换至python3环境


Python环境下lib目录：

    1、/usr/lib/python3.7：Python自带lib目录
    2、/usr/lib/python3/dist-packages：系统安装第三方lib的目录
    3、/usr/local/lib/python3.7/dist-packages：pip模块安装目录
    4、/home/xxx/.local/lib/python3.7/site-packages：当前用户手动安装第三方lib的目录
    5、/xx/xx/venv/lib/python3.7/site-packages：IDE环境下安装第三方lib包目录


Ubuntu下通过python命令直接运行代码：

    提示以下错误：
        import xxx
        ModuleNotFoundError: No module named 'xxxx'
    产生原因：
        1、在系统环境中当前项目父路径没有被添加到sys.path中，默认只有文件的当前路径，而在IDE环境下会显示所有路径
        2、系统环境中没有项目venv目录中的第三方lib包
    解决办法：
        1、手动在文件头部导入当前文件父路径，必须在其他import之前导入
            # import sys,os
            # sys.path.append(os.path.dirname(sys.path[0]))  # 保证系统环境下可以调用其他module中的文件
        2、创建xxx.pth文件，将此文件添加到系统目录下/usr/lib/python3/dist-packages中
            添加当前项目路径-->解决通过python命令执行代码时无法调用其他module中的文件
            添加当前项目下的/xx/xx/venv/lib/python3.7/site-packages路径-->解决通过python命令执行代码时无法使用venv中的第三方lib包
        3、使用pip命令在系统环境下安装第三方lib包，目录/home/xxx/.local/lib/python3.7/site-packages

注意事项：

    1、pip模块
        pip list 查询所有第三方lib包
        pip install --upgrade xx 升级第三方lib包
        pip show xx 查询第三方lib包所在路径
        os.path.abspath(__file__) # 返回绝对路径
        os.path.basename(__file__)# 返回文件名
        os.path.dirname(__file__) # 返回文件路径

    2、系统环境下用户使用第三方lib包
        /usr/local/lib：所有用户可以使用lib包
        /home/pc190559/.local/lib：只有当前用户可以使用lib包

    3、查询第三方lib包目录
        from distutils.sysconfig import get_python_lib
        print(get_python_lib())
        在IDE中运行获取的是项目中/venv/xx/site-packages目录
        在系统环境通过python命令运行获取的是/usr/lib/python3/dist-packages目录

    4、不同环境运行sys.path

        Ubuntu运行sys.path：

        ['/home/pc190559/demo/PythonDemo/python/auto', '/usr/lib/python37.zip', '/usr/lib/python3.7',
         '/usr/lib/python3.7/lib-dynload', '/home/pc190559/.local/lib/python3.7/site-packages', '/usr/local/lib/python3.7/dist-packages',
         '/usr/lib/python3/dist-packages']


        IDE运行sys.path：

        ['/home/pc190559/demo/PythonDemo/python/auto', '/home/pc190559/demo/PythonDemo/python',
        '/home/pc190559/develop/pycharm/plugins/python/helpers/pycharm_display', '/usr/lib/python37.zip', '/usr/lib/python3.7',
         '/usr/lib/python3.7/lib-dynload', '/home/pc190559/demo/PythonDemo/python/venv/lib/python3.7/site-packages',
         '/home/pc190559/develop/pycharm/plugins/python/helpers/pycharm_matplotlib_backend']

    5、升级系统自带的第三方lib包，或设置IDE中的Project Interpreter环境
    　