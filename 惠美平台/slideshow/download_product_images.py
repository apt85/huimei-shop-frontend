import os
import requests
from PIL import Image
from io import BytesIO

# 创建images文件夹（如果不存在）
if not os.path.exists('images'):
    os.makedirs('images')

# 商品列表与对应的图片文件名
products = [
    # 家具类
    {'name': '现代布艺沙发', 'filename': 'furniture_1.jpg'},
    {'name': '实木茶几', 'filename': 'furniture_2.jpg'},
    {'name': '简约电视柜', 'filename': 'furniture_3.jpg'},
    {'name': '现代落地灯', 'filename': 'furniture_4.jpg'},
    {'name': '实木双人床', 'filename': 'furniture_5.jpg'},
    {'name': '四门衣柜', 'filename': 'furniture_6.jpg'},
    {'name': '简约床头柜', 'filename': 'furniture_7.jpg'},
    {'name': '梳妆台', 'filename': 'furniture_8.jpg'},
    # 零食类
    {'name': '香脆薯片大礼包', 'filename': 'snacks_1.jpg'},
    {'name': '进口巧克力礼盒', 'filename': 'snacks_2.jpg'},
    {'name': '坚果混合装', 'filename': 'snacks_3.jpg'},
    {'name': '果脯蜜饯组合', 'filename': 'snacks_4.jpg'},
    {'name': '手工饼干礼盒', 'filename': 'snacks_5.jpg'},
    {'name': '进口咖啡套装', 'filename': 'snacks_6.jpg'},
    {'name': '海鲜零食大礼包', 'filename': 'snacks_7.jpg'},
    {'name': '网红零食组合', 'filename': 'snacks_8.jpg'}
]

# 使用Unsplash API搜索图片（需要API访问，这里使用免费的图片源）
def download_image(product_name, filename):
    """从Unsplash下载商品图片"""
    try:
        # 使用 Unsplash 免费图片，通过关键词搜索
        query = product_name.replace(' ', '+')
        # 使用公共的图片API或备用链接
        # 这里我们使用一些稳定的图片源
        image_urls = {
            '现代布艺沙发': 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=800',
            '实木茶几': 'https://images.unsplash.com/photo-1530018170808-2f73057849d8?w=800',
            '简约电视柜': 'https://images.unsplash.com/photo-1567538299760-968658de8a9c?w=800',
            '现代落地灯': 'https://images.unsplash.com/photo-1507473885765-99cf4574d083?w=800',
            '实木双人床': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800',
            '四门衣柜': 'https://images.unsplash.com/photo-1591356861116-6e5f31d0f191?w=800',
            '简约床头柜': 'https://images.unsplash.com/photo-1581417937921-3e50f1958d38?w=800',
            '梳妆台': 'https://images.unsplash.com/photo-1596717530792-42dd36a475f0?w=800',
            '香脆薯片大礼包': 'https://images.unsplash.com/photo-1565299585323-38d63d139974?w=800',
            '进口巧克力礼盒': 'https://images.unsplash.com/photo-1511381939415-e44015466834?w=800',
            '坚果混合装': 'https://images.unsplash.com/photo-1611591453043-588f7a778dd3?w=800',
            '果脯蜜饯组合': 'https://images.unsplash.com/photo-1541658184517-78a310437742?w=800',
            '手工饼干礼盒': 'https://images.unsplash.com/photo-1583394838336-acd977736f90?w=800',
            '进口咖啡套装': 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800',
            '海鲜零食大礼包': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800',
            '网红零食组合': 'https://images.unsplash.com/photo-1563245372-f21724e3856d?w=800'
        }

        if product_name in image_urls:
            url = image_urls[product_name]
            response = requests.get(url)
            response.raise_for_status()

            # 将图片保存到文件
            with open(f'images/{filename}', 'wb') as f:
                f.write(response.content)
            print(f'{filename} 下载成功 ({product_name})')
            return True
        else:
            print(f'无法找到 {product_name} 的图片链接')
            return False

    except Exception as e:
        print(f'下载 {product_name} 失败: {str(e)}')
        return False

# 开始下载所有商品图片
print('开始下载商品图片...')
print('=' * 50)

success_count = 0
for product in products:
    if download_image(product['name'], product['filename']):
        success_count += 1

print('\n' + '=' * 50)
print(f'下载完成！成功下载 {success_count}/{len(products)} 张图片')
