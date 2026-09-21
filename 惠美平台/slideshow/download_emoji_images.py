import requests
import os

# 创建images文件夹（如果不存在）
os.makedirs('images', exist_ok=True)

# 家具专场需要的图片
furniture_emoji_images = [
    {
        "url": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=800",
        "filename": "emoji_couch.jpg",
        "description": "沙发表情对应的真实图片"
    },
    {
        "url": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=800",
        "filename": "emoji_home.jpg",
        "description": "房子表情对应的真实图片"
    }
]

# 零食专场需要的图片
snacks_emoji_images = [
    {
        "url": "https://images.unsplash.com/photo-1541701494587-cb58502866ab?w=800",
        "filename": "emoji_candy.jpg",
        "description": "糖果表情对应的真实图片"
    },
    {
        "url": "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=800",
        "filename": "emoji_fireworks.jpg",
        "description": "烟花表情对应的真实图片"
    }
]

def download_image(url, filename):
    """下载图片到指定文件夹"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        file_path = os.path.join('images', filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        print(f"✅ {filename} 下载完成")
    except Exception as e:
        print(f"❌ {filename} 下载失败: {str(e)}")

print("开始下载家具专场表情图片...")
for img in furniture_emoji_images:
    download_image(img["url"], img["filename"])

print("\n开始下载零食专场表情图片...")
for img in snacks_emoji_images:
    download_image(img["url"], img["filename"])

print("\n所有表情图片下载完成！")