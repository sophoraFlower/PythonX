import jqdatasdk

jqdatasdk.auth('xxxxxx', 'xxxxxx')

# 获取平安银行按1分钟为周期以“2015-01-30 14:00:00”为基础前4个时间单位的数据
df = jqdatasdk.get_price('000001.XSHE',
                         end_date='2015-01-30 14:00:00',
                         count=4,
                         frequency='minute',
                         fields=['open', 'close', 'high', 'low', 'volume', 'money'])
print(df)
