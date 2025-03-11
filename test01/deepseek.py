
import requests

# ✅ 你的 DeepSeek API Key（从官网获取）
API_KEY = "sk-dc96286c2a78485b86ba5f8091895c5b"  # ⚠ 替换成你的实际 API Key

# ✅ DeepSeek API 地址
API_URL = "https://api.deepseekcom/v1/chat/completions"

# ✅ 请求头
headers = {
    "Authorization": f"Bearer {API_KEY}",  # 认证
    "Content-Type": "application/json"  # 请求格式
}

# ✅ 发送的消息
data = {
    "model": "deepseek-chat",  # 使用 DeepSeek Chat 模型
    "messages": [
        {"role": "system", "content": "你是一个智能 AI 助手"},
        {"role": "user", "content": "你好，DeepSeek！"}  # 用户输入
    ]
}

# ✅ 发送 API 请求
response = requests.post(API_URL, headers=headers, json=data)

# ✅ 打印返回结果
print(response.json())
