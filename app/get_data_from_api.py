import aiohttp
import asyncio

async def fetch_data(url: str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.json()
    except aiohttp.ClientError as e:
        print(f"Ошибка при запросе к API: {e}")
        return None
    except asyncio.TimeoutError:
        print("Превышено время ожидания запроса к API.")
        return None

async def main():
    data = await fetch_data("https://jsonplaceholder.typicode.com/users")
    if data:
        print(data)

if __name__ == "__main__":
    asyncio.run(main())