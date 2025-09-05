import requests
import concurrent.futures

# آدرس‌هایی که لیست سرورها توشونه
SOURCE_URLS = [
    "https://raw.githubusercontent.com/lagzian/SS-Collector/refs/heads/main/VLESS/VL100.txt",
    "https://raw.githubusercontent.com/AliDev-ir/FreeVPN/main/vpn"
]

def fetch_links(url):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return [line.strip() for line in resp.text.splitlines() if line.strip()]
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def test_server(server_url):
    try:
        resp = requests.get(server_url, timeout=5)
        if resp.status_code == 200:
            return server_url
    except:
        pass
    return None

def main():
    all_servers = []
    for src in SOURCE_URLS:
        all_servers.extend(fetch_links(src))

    print(f"Total servers found: {len(all_servers)}")

    valid_servers = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(test_server, s) for s in all_servers]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                valid_servers.append(result)

    print("Valid servers:")
    for s in valid_servers:
        print(s)

    with open("valid_servers.txt", "w") as f:
        f.write("\n".join(valid_servers))

if __name__ == "__main__":
    main()
