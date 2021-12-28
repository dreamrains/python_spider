# python_spider
这是练习python数据分析与网络爬虫用的一个小程序，现在只有爬取阿拉丁网站的一个程序。  
爬虫爬取的是阿拉丁小程序指数公开的数据。这个爬虫程序性能还比较差，有兴趣的朋友可以用多线程等方法优化一下。
本次获取的数据分析的目的在于了解小程序生态换量的产品类型分布、交易合作方式以及价格等情况。但是小程序的换量有时效性，比如一款产品随着用户量的提升与成长在半年前和近期的交易可能从买量变成了卖量，因此针对这些复杂的情况，我在本地文件中做了以下的处理。
1. 使用了2019年10月1日以后的数据，因为9月算是暑假的结束，国庆节后衔接了双十一、双旦等重要阶段，所以选择十一为起点分析换量情况。
2. 同一款产品如果存在买量、卖量以及换量三种合作模式，在同一周的时间内，保留三条记录。若不同的合作模式超过了2个月，则仅保留最新的合作模式的记录。
3. 同一款产品如果存在买量或者卖量存在多种结算方式的情况，在同一周内，保留一种合作模式下最新结算方式的记录各一条。若不同的结算方式超过2个月，则仅保留最新一个结算方式的记录。
4. 一款产品买量或者卖量提供的单价如果为一个区间，则取最大值，表示该用户可接受的最高单价。
