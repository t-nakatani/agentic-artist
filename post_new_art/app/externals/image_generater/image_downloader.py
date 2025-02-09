from playwright.sync_api import sync_playwright
from PIL import Image
import io


class ImageDownloader:
    def __init__(self, user_agent: str = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"):
        self.user_agent = user_agent

    def download(self, url: str, output_path: str):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            context = browser.new_context(user_agent=self.user_agent)
            page = context.new_page()
            # page.set_extra_http_headers({"User-Agent": self.user_agent})

            response = page.goto(url)
            if response and response.status == 200:
                Image.open(io.BytesIO(response.body())).save(output_path)
                print(f"保存完了: {output_path}")
            else:
                raise Exception(f"ダウンロードに失敗しました: {response.status}")

            browser.close()
