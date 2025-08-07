import asyncio
import time

async def brew_coffee(order_id):
    print(f"Order {order_id}: Starting Brewing Coffee")
    await asyncio.sleep(3)
    print(f"Order {order_id}: Coffee Ready")

async def toast_bagel(order_id):
    print(f"Order {order_id}: Start Toasting Bagel")
    await asyncio.sleep(2)
    print(f"Order {order_id}: Bagel Ready")

async def prepare_order(order_id):
    await asyncio.gather(
        brew_coffee(order_id),
        toast_bagel(order_id)
    )

async def process_orders(orders):
    for order_id in orders:
        await prepare_order(order_id)

async def main():
    start = time.time()

    # Simulating multiple orders
    orders = [1, 2, 3]

    await process_orders(orders)

    end = time.time()
    print(f"Total Time: {end - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())