# import asyncio
# from sqlalchemy import text
# from db import engine

# async def test_connection():
#     async with engine.connect() as conn:
#         result = await conn.execute(text("SELECT 1"))
#         print(result.scalar())

#     # 🔥 IMPORTANT: close all connections cleanly
#     await engine.dispose()

# asyncio.run(test_connection())