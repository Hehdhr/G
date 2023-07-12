
import requests

def search_tiktok_users():
    base_url = "https://api.tiktok.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        "Referer": "https://www.tiktok.com/"
    }
    
    for username in range(1000, 10000):  # تبدأ بالرقم 1000 وتنتهي بالرقم 9999
        url = f"{base_url}@{username}"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:  # تحقق مما إذا كان الاستجابة ناجحة
            print(f"تم العثور على مستخدم تيك توك: {username}")

search_tiktok_users() 
