import time
import requests
import threading
import multiprocessing
import asyncio
import aiohttp
import aiofiles
import argparse


def download_image(url):
    img_name = url.split('/')[-1]
    img_data = requests.get(url).content
    with open(img_name, 'wb') as handler:
        handler.write(img_data)
    print(f'{img_name} OK! in {time.time() - start_time:.3f}s')


async def async_download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            img_name = url.split('/')[-1]
            if response.status == 200:
                f = await aiofiles.open(img_name, mode='wb')
                await f.write(await response.read())
                await f.close()
    print(f'{img_name} OK! in {time.time() - start_time:.3f}s')


def image_thread(url_list):
    threads = []
    for i in range(len(url_list)):
        t = threading.Thread(target=download_image, args=(url_list[i],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


def image_process(url_list):
    processes = []
    for i in range(len(url_list)):
        p = multiprocessing.Process(target=download_image, args=(url_list[i],))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


async def image_async(url_list):
    tasks = []
    for url in url_list:
        task = asyncio.ensure_future(async_download_image(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


parser = argparse.ArgumentParser(description='Download image URLs.')
parser.add_argument('urls', metavar='U', type=str, nargs='+',
                    help='All image URLs')
parser.add_argument('-t', '--thr', dest='threads', action='store_const',
                    const=image_thread, help='Download using threads')
parser.add_argument('-p', '--pro', dest='processes', action='store_const',
                    const=image_process, help='Download using processes')
parser.add_argument('-a', '--asy', dest='asyncs', action='store_const',
                    const=image_async, help='Download using async')

start_time = time.time()

if __name__ == '__main__':
    args = parser.parse_args()
    if args.threads:
        args.threads(args.urls)
    elif args.processes:
        args.processes(args.urls)
    elif args.asyncs:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(args.asyncs(args.urls))
    else:
        print('You did not specify the method.')
    print(f'Finished in {time.time() - start_time:.3f}s')
