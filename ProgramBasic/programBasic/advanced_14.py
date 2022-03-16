import time
import asyncio


def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))


def main1(urls):
    for url in urls:
        crawl_page(url)


async def crawl_page_await(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    # 声明异步函数
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main2(urls):
    for url in urls:
        # 声明异步函数
        await crawl_page_await(url)


async def crawl_page_async(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    tasks = [asyncio.create_task(crawl_page_async(url)) for url in urls]
    # await asyncio.gather(*tasks)
    for task in tasks:
        await task


# 常规执行：10s
main1(['url_1', 'url_2', 'url_3', 'url_4'])
# 同步执行：10s
asyncio.run(main2(['url_1', 'url_2', 'url_3', 'url_4']))
# 异步执行: <10s
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
