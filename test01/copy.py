import requests
from bs4 import BeautifulSoup


# pip install requests beautifulsoup4

# 目标网站的URL
url = "https://docs.python.org/zh-cn/3/tutorial/introduction.html"

# 发送HTTP GET请求
try:
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
    exit()

# 解析HTML内容
soup = BeautifulSoup(response.text, 'html.parser')

# 提取网页标题
title = soup.title.string
print(f"网页标题: {title}")

# 提取所有链接
links = soup.find_all('a', href=True)
print("网页中的链接:")
for link in links:
    print(f"{link.text}: {link['href']}")