import asyncio
from dataclasses import dataclass
from typing import Iterable

import httpx
from fake_useragent import UserAgent
from tenacity import retry, stop_after_attempt, wait_exponential


@dataclass
class CertificateItem:
    name: str
    type: str | None = None
    industry: str | None = None
    price: float | None = None
    duration: str | None = None
    exam_period: str | None = None
    description: str | None = None


def build_headers() -> dict:
    ua = UserAgent()
    return {"User-Agent": ua.random}


@retry(wait=wait_exponential(multiplier=1, min=1, max=8), stop=stop_after_attempt(3))
async def fetch(client: httpx.AsyncClient, url: str) -> str:
    resp = await client.get(url, timeout=15)
    resp.raise_for_status()
    return resp.text


async def crawl_sources() -> Iterable[CertificateItem]:
    # 占位：这里应替换为真实目标站点的列表与解析逻辑
    urls = [
        "https://example.com/certificates/mock1",
        "https://example.com/certificates/mock2",
    ]
    items: list[CertificateItem] = []
    async with httpx.AsyncClient(headers=build_headers(), follow_redirects=True) as client:
        for url in urls:
            try:
                await fetch(client, url)
                items.append(
                    CertificateItem(
                        name=f"Mock Cert from {url}",
                        type="示例",
                        industry="样例行业",
                        price=1999.0,
                        duration="1-2个月",
                        exam_period="季度",
                        description="此为占位数据，需替换为真实解析结果",
                    )
                )
            except Exception:
                continue
    return items


async def run():
    items = await crawl_sources()
    for it in items:
        print("CRAWLED:", it)


if __name__ == "__main__":
    asyncio.run(run())


