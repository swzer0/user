import requests
import time

# تحميل قائمة الأسماء من ملف
file_path = "usernames_500.txt"  # تأكد من وضع المسار الصحيح للملف
with open(file_path, "r") as file:
    usernames = [line.strip() for line in file.readlines()]

# رابط التحقق على إنستغرام
check_url = "https://www.instagram.com/accounts/web_create_ajax/attempt/"

# رؤوس الطلب (تحاكي متصفحًا حقيقيًا لتجنب الحظر)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.instagram.com/",
}

available_usernames = []

for username in usernames:
    try:
        response = requests.post(check_url, headers=headers, data={"email": "", "username": username, "first_name": "", "opt_into_one_tap": "false"})
        if '"available":true' in response.text:
            print(f"✅ {username} متاح!")
            available_usernames.append(username)
        else:
            print(f"❌ {username} غير متاح.")
        
        time.sleep(1)  # تجنب الحظر بإضافة تأخير بين الطلبات

    except Exception as e:
        print(f"خطأ أثناء التحقق من {username}: {e}")

# حفظ النتائج في ملف
with open("available_usernames.txt", "w") as file:
    for user in available_usernames:
        file.write(user + "\n")

print("\n✅ تم الانتهاء! تم حفظ الأسماء المتاحة في available_usernames.txt")
