import os
import requests

# 创建images文件夹（如果不存在）
if not os.path.exists('images'):
    os.makedirs('images')

# 使用更稳定的图片链接，包括免费可访问的图片源
products = [
    # 家具类
    {
        'name': '现代布艺沙发', 
        'filename': 'furniture_1.jpg', 
        'url': 'https://picsum.photos/800/600?random=1'
    },
    {
        'name': '实木茶几', 
        'filename': 'furniture_2.jpg', 
        'url': 'https://picsum.photos/800/600?random=2'
    },
    {
        'name': '简约电视柜', 
        'filename': 'furniture_3.jpg', 
        'url': 'https://picsum.photos/800/600?random=3'
    },
    {
        'name': '现代落地灯', 
        'filename': 'furniture_4.jpg', 
        'url': 'https://picsum.photos/800/600?random=4'
    },
    {
        'name': '实木双人床', 
        'filename': 'furniture_5.jpg', 
        'url': 'https://picsum.photos/800/600?random=5'
    },
    {
        'name': '四门衣柜', 
        'filename': 'furniture_6.jpg', 
        'url': 'https://picsum.photos/800/600?random=6'
    },
    {
        'name': '简约床头柜', 
        'filename': 'furniture_7.jpg', 
        'url': 'https://picsum.photos/800/600?random=7'
    },
    {
        'name': '梳妆台', 
        'filename': 'furniture_8.jpg', 
        'url': 'https://picsum.photos/800/600?random=8'
    },
    # 零食类
    {
        'name': '香脆薯片大礼包', 
        'filename': 'snacks_1.jpg', 
        'url': 'https://picsum.photos/800/600?random=9'
    },
    {
        'name': '进口巧克力礼盒', 
        'filename': 'snacks_2.jpg', 
        'url': 'https://picsum.photos/800/600?random=10'
    },
    {
        'name': '坚果混合装', 
        'filename': 'snacks_3.jpg', 
        'url': 'https://picsum.photos/800/600?random=11'
    },
    {
        'name': '果脯蜜饯组合', 
        'filename': 'snacks_4.jpg', 
        'url': 'https://picsum.photos/800/600?random=12'
    },
    {
        'name': '手工饼干礼盒', 
        'filename': 'snacks_5.jpg', 
        'url': 'https://picsum.photos/800/600?random=13'
    },
    {
        'name': '进口咖啡套装', 
        'filename': 'snacks_6.jpg', 
        'url': 'https://picsum.photos/800/600?random=14'
    },
    {
        'name': '海鲜零食大礼包', 
        'filename': 'snacks_7.jpg', 
        'url': 'https://picsum.photos/800/600?random=15'
    },
    {
        'name': '网红零食组合', 
        'filename': 'snacks_8.jpg', 
        'url': 'https://picsum.photos/800/600?random=16'
    }
]

def download_image(url, filename, product_name):
    """从指定URL下载图片并保存"""
    try:
        print(f'正在下载: {product_name} -> {filename}')
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        
        file_path = os.path.join('images', filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f'✓ {filename} 下载成功')
        return True
    except Exception as e:
        print(f'✗ 下载 {product_name} 失败: {str(e)}')
        return False

# 开始下载
print('开始下载所有商品图片...')
print('=' * 50)

success_count = 0
for product in products:
    if download_image(product['url'], product['filename'], product['name']):
        success_count += 1

print('\n' + '=' * 50)
print(f'下载完成！')
print(f'成功下载: {success_count}/{len(products)} 张图片')
print(f'保存位置: {os.path.abspath("images")}')
