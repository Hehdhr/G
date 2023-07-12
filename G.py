
import requests

def search_users():
    for i in range(1000, 10000):  # تبحث عن اليوزرات الرباعية من 1000 إلى 9999
        username = str(i)
        url = f"https://tiktok.com/@{username}"

        response = requests.get(url)
        if response.status_code == 404:
            print(f"اليوزر {username} غير متاح.")
        else:
            print(f"اليوزر {username} متاح.")
        
