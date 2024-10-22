import asyncio
import json
import random
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

async def scrape_website(url):
    async with async_playwright() as p:
        browser = None
        try:
            browser = await p.chromium.launch()
            context = await browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/91.0.4472.124 Safari/537.36'
            )
            page = await context.new_page()
            await page.set_extra_http_headers({
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': ('text/html,application/xhtml+xml,application/xml;q=0.9,'
                           'image/avif,image/webp,image/apng,*/*;q=0.8,'
                           'application/signed-exchange;v=b3;q=0.9'),
            })
            await page.goto(url)
            delay = random.uniform(0.8, 2)
            await asyncio.sleep(delay)
            content = await page.content()
            print(f"Successfully scraped {url}")
            return content
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            return None
        finally:
            if browser:
                await browser.close()

def extract_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    body_content = soup.body
    if body_content:
        content = str(body_content)
    else:
        content = ""

    soup = BeautifulSoup(content, 'html.parser')
    for stuff in soup(["script", "style"]):
        stuff.extract()

    cleaned_stuff = soup.get_text(separator="\n")
    cleaned_stuff = "\n".join(
            line.strip() for line in cleaned_stuff.splitlines() if line.strip()
    )

    return cleaned_stuff

def split_dom(dom_stuff, max_length = 6969):
    return [dom_stuff[i: i + max_length] for i in range(0, len(dom_stuff), max_length)]


