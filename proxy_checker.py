import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import logging
import sys

MAX_THREADS = 60
TIMEOUT = 20
CHECK_URLS = ['https://icanhazip.com', 'https://api.ip.sb/ip']
SAVE_PATH = "live_https_proxies.txt"
LOG_FILE = "proxy_checker.log"

logging.basicConfig(
    filename=LOG_FILE,
    filemode='w',
    format='%(asctime)s [%(levelname)s] %(message)s',
    level=logging.WARNING  # Only show source errors
)

def get_from_proxyscrape():
    try:
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all"
        r = requests.get(url, timeout=10)
        lines = r.text.strip().split('\n')
        return [(line.strip(), 'Unknown', 'ProxyScrape') for line in lines if ':' in line]
    except Exception as e:
        logging.error(f"ProxyScrape error: {e}")
        return []

def check_proxy(proxy_info, index, total):
    ip_port, country, source = proxy_info
    proxies = {
        "http": f"http://{ip_port}",
        "https": f"http://{ip_port}"
    }
    for check_url in CHECK_URLS:
        try:
            r = requests.get(check_url, proxies=proxies, timeout=TIMEOUT)
            if r.status_code == 200:
                with open(SAVE_PATH, "a") as f:
                    ip, port = ip_port.split(":")
                    f.write(f"{ip},{port},HTTPS\n")
                break
        except Exception:
            continue

    percent = round((index + 1) / total * 100, 2)
    sys.stdout.write(f"\r🔎 Checked: {index + 1}/{total} ({percent}%)")
    sys.stdout.flush()

def main():
    proxies = get_from_proxyscrape()
    total = len(proxies)

    print(f"ProxyScrape source: {total} proxies")

    if total == 0:
        print("❌ No proxies found. Exiting.")
        return

    with open(SAVE_PATH, "w") as f:
        f.write("IP,Port,Type\n")

    print("⚙ Starting check...")

    start = time.time()
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(check_proxy, proxy, i, total) for i, proxy in enumerate(proxies)]
        for _ in as_completed(futures):
            pass
    end = time.time()

    print(f"\n✅ Done in {round(end - start, 2)} seconds.")
    print(f"Live proxies → {SAVE_PATH}")
    print(f"Errors → {LOG_FILE}")

if __name__ == "__main__":
    main()
