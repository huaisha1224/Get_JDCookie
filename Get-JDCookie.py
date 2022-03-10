import asyncio
# from gettext import find
from pyppeteer import launch


def find_cookie(cookies):
    """提取pt_key和pt_pin
    """
    for item in cookies.split('; '):
        if 'pt_pin' in item:
            pt_pin = item
        if 'pt_key' in item:
            pt_key = item
    jd_cookie = pt_pin+';'+pt_key+';'
    print("Cookie:", jd_cookie)
    return jd_cookie



async def main():
    browser = await launch(headless=False, dumpio=True, autoClose=False,
                           args=['--no-sandbox', '--window-size=800,700', '--disable-infobars'])   # 进入有头模式
    page = await browser.newPage()           # 打开新的标签页
    await page.setViewport({'width': 800, 'height': 700})      # 页面大小一致
    await page.goto('https://home.m.jd.com') # 访问主页

    await asyncio.sleep(60)
    cookie = await page.cookies()
    # print(cookie)
    # 格式化cookie
    cookies_temp = []
    for i in cookie:
        cookies_temp.append('{}={}'.format(i["name"], i["value"]))
    cookies = '; '.join(cookies_temp)
    find_cookie(cookies)
    # print("cookies:{}".format(await page.cookies()))


if __name__== "__main__":
    asyncio.get_event_loop().run_until_complete(main()) #调用