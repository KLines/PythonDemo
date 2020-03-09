import random,logging

'''
headers使用

    1、urllib底层默认设置：
        headers["Connection"] = "close" 
        headers["User-Agent"] = "Python-urllib/%s" % __version__
    2、request header中Accept-Encoding中若包含gzip，response header通常会返回Content-Encoding: gzip
    3、response header中包含Content-Encoding: gzip，需要先解压再转码


HTTP内容编码：在http协议中，可以对内容（也就是body部分）进行编码

    1、可以采用压缩编码，比如gzip这样的从而达到压缩的目的，因此http压缩就是HTTP内容编码的一种
    2、可以使用其他的编码把内容搅乱或加密，以此来防止未授权的第三方看到文档的内容
   
        
HTTP压缩：采用通用的压缩算法，比如gzip来压缩HTML,Javascript, CSS文件，能大大减少网络传输的数据量，提高了用户显示网页的速度

    1、压缩过程：
        1、发送request包含Accept-Encoding: gzip, deflate。(告诉服务器， 浏览器支持gzip压缩)
        2、Web服务器接到request后，生成原始的response, 其中有原始的Content-Type和Content-Length
        3、Web服务器通过Gzip来对Response进行编码，编码后header中有Content-Type和Content-Length(压缩后的大小)，并且增加了Content-Encoding:gzip
        4、将response发送给浏览器，然后根据Content-Encoding:gzip来对response进行解码，获取到原始response后显示出网页 
    2、Content-Encoding值
        gzip：表明实体采用GNU zip编码，PEG这类文件用gzip压缩的不够好
            　简单来说， Gzip压缩是在一个文本文件中找出类似的字符串，并临时替换他们，使整个文件变小。这种形式的压缩对Web来说非常适合， 
            　因为HTML和CSS文件通常包含大量的重复的字符串，例如空格，标签
        compress：表明实体采用Unix的文件压缩程序
        deflate：表明实体是用zlib的格式压缩的
        identity：表明没有对实体进行编码。当没有Content-Encoding header时， 就默认为这种情况
        gzip, compress, 以及deflate编码都是无损压缩算法，用于减少传输报文的大小，不会导致信息损失，其中gzip通常效率最高， 使用最为广泛。

'''

USER_AGENTS =[
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
]


headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding':'gzip,deflate,br',  # 支持的压缩编码
    'Accept-language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'User-Agent':random.choice(USER_AGENTS)
}


'''配置日志'''
LOG_FORMAT = "%(asctime)s-->%(levelname)s-->HTTP-->%(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S %a"
logging.basicConfig(level=logging.DEBUG,
                    format= LOG_FORMAT,
                    datefmt= DATE_FORMAT)


def log_info(msg):
    logging.info(msg)


def log_error(msg):
    logging.error(msg)
