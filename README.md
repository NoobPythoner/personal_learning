# Myspider
                                    pass
                                    
 1 scrapy的使用流程
- 创建项目 scrapy startproject 项目名
- 创建爬虫 scrapy genspider spider_name allow_domain
- 完善爬虫
  - start_url,response --> parse
  - 数据yield 通过传递给管道
  - 能够yield 的数据类型:dict，request，Item，None
- 管道
  - 开启管道
    - 开启管道，键:位置，值：距离引擎的远近，越小越近，数据会按这个权值的由小到大的依次经过每个pipline
2 crawlspider如何使用
-创建爬虫 scarpy genspider -t crawl spider_name allow_domain
-完善spider
--1 start_url：指定start_url，对应的响应会进过rules提取url地址
--2 完善rules ：添加Rule(LinkExtractor(allow=r'/web/site/info\d+.htm'), callback='parse_item')
----元组
---Rule(LinkExtractor,callback，follow)
-----LinkExtractor 连接提取器，提取url
-----callback url的响应会交给该callback处理
-----follow= True url的响应会继续被Rule提取地址
--3.完善callback
-注意点:
--url地址不完整，crawlspider会自动补充完整之后在请求
--parse函数不能定义，他有特殊的功能需要实现
--callback：连接提取器提取出来的url地址对应的响应交给他处理
--follow：连接提取器提取出来的url地址对应的响应是否继续被rules来过滤
