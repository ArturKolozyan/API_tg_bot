import aiohttp
import asyncio


class JSONPlaceholderClient:

    def __init__(self, url):
        self.url = url

    async def get_data(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url) as response:
                    response.raise_for_status()
                    return await response.json()

        except aiohttp.ClientError as e:
            print(f"Ошибка при GET-запросе к API: {e}")
            return None

        except asyncio.TimeoutError:
            print("Превышено время ожидания GET-запроса к API.")
            return None
