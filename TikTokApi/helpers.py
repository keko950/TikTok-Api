import TikTokApi
from TikTokApi.browser_utilities.browser import browser
from urllib.parse import quote, urlencode
from .exceptions import *

import re
import requests


def extract_tag_contents(html):
    if "__NEXT_DATA__" in html:
        j_raw = html.split('<script id="__NEXT_DATA__" type="application\/json" nonce="[\w-]+" crossorigin="anonymous">')[1].split("</script>")[0]
        return j_raw
    else:
        try:
            splitted = html.split('<script id="SIGI_STATE" type="application/json">')[1].split('</script>')[0]
            return splitted
        except:
            raise CaptchaException(0, None,
            "TikTok blocks this request displaying a Captcha \nTip: Consider using a proxy or a custom_verify_fp as method parameters"
        )


def extract_video_id_from_url(url, headers={}):
    url = requests.head(url=url, allow_redirects=True, headers=headers).url
    if "@" in url and "/video/" in url:
        return url.split("/video/")[1].split("?")[0]
    else:
        raise TypeError(
            "URL format not supported. Below is an example of a supported url.\n"
            "https://www.tiktok.com/@therock/video/6829267836783971589"
        )
