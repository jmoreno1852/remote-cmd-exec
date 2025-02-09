import src.server

async def main(s):
    async with s.serve(server, "127.0.0.1",port=4444):
        await asyncio.Future()
if __name__ == "__main__":
    asyncio.run(main())
