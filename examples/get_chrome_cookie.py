from pyfuncs import ChromeCookie

with ChromeCookie() as chrome:
    cookies = chrome.get_cookie_by_host("https://github.com")