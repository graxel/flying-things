import aiohttp
import asyncio
import time

camera_ips = ["192.168.0.17"]#, "192.168.0.64"]
resolution_val = 15
capture_interval = 1  # seconds between captures
capture_count = 3  # total number of capture iterations


async def set_resolution(session, camera_ip, resolution):
    url = f"http://{camera_ip}/control?var=framesize&val={resolution}"
    async with session.get(url) as resp:
        if resp.status == 200:
            print(f"Resolution set for {camera_ip}")
        else:
            print(f"Failed to set resolution for {camera_ip}, status: {resp.status}")


async def capture_image(session, camera_ip, iteration):
    url = f"http://{camera_ip}/capture"
    async with session.get(url) as resp:
        if resp.status == 200:
            content = await resp.read()
            filename = f"capture_{camera_ip.replace('.', '_')}_{iteration}.jpg"
            with open(filename, "wb") as f:
                f.write(content)
            print(f"Saved image {filename}")
        else:
            print(f"Failed to capture image from {camera_ip}, status: {resp.status}")


async def main():
    async with aiohttp.ClientSession() as session:
        # Set resolution for all cameras concurrently, once at startup
        await asyncio.gather(*(set_resolution(session, ip, resolution_val) for ip in camera_ips))
        await asyncio.sleep(1)
        for i in range(capture_count):
        #########
        # Set resolution for all cameras concurrently, once at startup
        
        # for i in range(capture_count):
        #     await asyncio.gather(*(set_resolution(session, ip, capture_count) for ip in camera_ips))

            ########

            start_time = time.time()
            # Capture images from all cameras concurrently
            await asyncio.gather(*(capture_image(session, ip, i) for ip in camera_ips))

            elapsed = time.time() - start_time
            sleep_time = max(0, capture_interval - elapsed)
            await asyncio.sleep(sleep_time)
            

if __name__ == "__main__":
    asyncio.run(main())
