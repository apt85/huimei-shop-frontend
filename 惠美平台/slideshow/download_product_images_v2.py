import os
import requests

# 创建images文件夹（如果不存在）
if not os.path.exists('images'):
    os.makedirs('images')

# 更新后的商品列表与可用的图片链接
products = [
    # 家具类
    {'name': '现代布艺沙发', 'filename': 'furniture_1.jpg', 'url': 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=800'},
    {'name': '实木茶几', 'filename': 'furniture_2.jpg', 'url': 'https://images.pexels.com/photo/3735361/pexels-photo-3735361.jpeg?auto=compress&cs=tinysrgb&w=800'},
    {'name': '简约电视柜', 'filename': 'furniture_3.jpg', 'url': 'https://images.pexels.com/photo/439317/pexels-photo-439317.jpeg?auto=compress&cs=tinysrgb&w=800'},
    {'name': '现代落地灯', 'filename': 'furniture_4.jpg', 'url': 'https://images.pexels.com/photo/902034/pexels-photo-902034.jpeg?auto=compress&cs=tinysrgb&w=800'},
    {'name': '实木双人床', 'filename': 'furniture_5.jpg', 'url': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800'},
    {'name': '四门衣柜', 'filename': 'furniture_6.jpg', 'url': 'https://images.pexels.com/photo/1618206/pexels-photo-1618206.jpeg?auto=compress&cs=tinysrgb&w=800'},
    {'name': '简约床头柜', 'filename': 'furniture_7.jpg', 'url': 'https://images.pexels.com/photo/381833/pexels-photo-381833.jpeg?auto=compress&cs=tinysrgb&w=800'},
    {'name': '梳妆台', 'filename': 'furniture_8.jpg', 'url': 'https://images.pexels.com/photo/1596717530792-42dd36a475f0?auto=compress&cs=tinysrgb&w=800'},
    # 零食类
    {'name': '香脆薯片大礼包', 'filename': 'snacks_1.jpg', 'url': 'https://images.pexels.com/photo/262978/pexels-photo-262978.jpeg?auto=compress&cs=tinysrgb&w=800'},
    {'name': '进口巧克力礼盒', 'filename': 'snacks_2.jpg', 'url': 'https://images.unsplash.com/photo-1511381939415-e44015466834?w=800'},
    {'name': '坚果混合装', 'filename': 'snacks_3.jpg', 'url': 'https://images.pexels.com/photo/1639562/pexels-photo-1639562.jpeg?auto=compress&cs=tinysrgb&w=800'},
    {'name': '果脯蜜饯组合', 'filename': 'snacks_4.jpg', 'url': 'https://images.pexels.com/photo/291528/pexels-photo-291528.jpeg?auto=compress&cs=tinysrgb&w=800'},
    {'name': '手工饼干礼盒', 'filename': 'snacks_5.jpg', 'url': 'https://images.unsplash.com/photo-1583394838336-acd977736f90?w=800'},
    {'name': '进口咖啡套装', 'filename': 'snacks_6.jpg', 'url': 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800'},
    {'name': '海鲜零食大礼包', 'filename': 'snacks_7.jpg', 'url': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800'},
    {'name': '网红零食组合', 'filename': 'snacks_8.jpg', 'url': 'https://images.unsplash.com/photo-1563245372-f21724e3856d?w=800'}
]

def download_image(url, filename, product_name):
    """从指定URL下载图片并保存"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        with open(f'images/{filename}', 'wb') as f:
            f.write(response.content)
        print(f'{filename} 下载成功 ({product_name})')
        return True
    except Exception as e:
        print(f'下载 {product_name} 失败: {str(e)}')
        return False

# 开始下载所有商品图片
print('开始下载商品图片...')
print('=' * 50)

success_count = 0
for product in products:
    if download_image(product['url'], product['filename'], product['name']):
        success_count += 1

print('\n' + '=' * 50)
print(f'下载完成！成功下载 {success_count}/{len(products)} 张图片')
