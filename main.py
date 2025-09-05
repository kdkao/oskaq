import requests

# لینک فایل‌هایی که سرورهای VLESS داخلشون هستن
SOURCE_URLS = [
    "https://raw.githubusercontent.com/<username>/<repo>/main/servers1.txt",
    "https://raw.githubusercontent.com/<username>/<repo>/main/servers2.txt"
]

def fetch_links(url):
    """دریافت لینک‌ها از یک منبع"""
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        # جدا کردن خطوط خالی و بازگرداندن لیست لینک‌ها
        return [line.strip() for line in resp.text.splitlines() if line.strip()]
    except Exception as e:
        print(f"خطا در دریافت {url}: {e}")
        return []

def main():
    all_servers = []

    # جمع‌آوری همه لینک‌ها
    for src in SOURCE_URLS:
        all_servers.extend(fetch_links(src))

    print(f"تعداد کل سرورها: {len(all_servers)}")

    # ذخیره لینک‌ها داخل فایل
    with open("valid_servers.txt", "w") as f:
        f.write("\n".join(all_servers))

    print("تمام لینک‌ها ذخیره شدند: valid_servers.txt")

if __name__ == "__main__":
    main()
