import aiohttp
import asyncio


class APIClient:

    def __init__(self, base_url):
        self.__base_url = base_url

    async def __get_url(self, endpoint):
        return f"{self.__base_url}{endpoint}"

    async def get_data(self, endpoint):
        url = await self.__get_url(endpoint)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientError as e:
            print(f"Ошибка при GET-запросе к API: {e}")
            return None
        except asyncio.TimeoutError:
            print("Превышено время ожидания GET-запроса к API.")
            return None


class JSONPlaceholderClient(APIClient):
    pass


