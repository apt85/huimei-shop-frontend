import os
import requests
from urllib.parse import urlparse

# 创建images文件夹（如果不存在）
if not os.path.exists('images'):
    os.makedirs('images')

# 各专场页面的图片信息
download_list = [
    # 手机专场
    {'url': 'https://images.unsplash.com/photo-1592750475338-74b7b88e03d9?w=400&h=300&fit=crop', 'filename': 'cellphone_1.jpg'},
    {'url': 'https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?w=400&h=300&fit=crop', 'filename': 'cellphone_2.jpg'},
    {'url': 'https://images.unsplash.com/photo-1601784551446-20a1159689b1?w=400&h=300&fit=crop', 'filename': 'cellphone_3.jpg'},
    {'url': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400&h=300&fit=crop', 'filename': 'cellphone_4.jpg'},
    {'url': 'https://images.unsplash.com/photo-1556656793-08538906a9f8?w=400&h=300&fit=crop', 'filename': 'cellphone_5.jpg'},
    {'url': 'https://images.unsplash.com/photo-1520923642038-b4259acecbd7?w=400&h=300&fit=crop', 'filename': 'cellphone_6.jpg'},
    {'url': 'https://images.unsplash.com/photo-1567532939604-b6b5b0db2604?w=400&h=300&fit=crop', 'filename': 'cellphone_7.jpg'},
    {'url': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400&h=300&fit=crop', 'filename': 'cellphone_8.jpg'},
    # 服饰专场
    {'url': 'https://images.unsplash.com/photo-1496747611176-843222e1e57c?w=400&h=300&fit=crop', 'filename': 'costume_1.jpg'},
    {'url': 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&h=300&fit=crop', 'filename': 'costume_2.jpg'},
    {'url': 'https://images.unsplash.com/photo-1583743814966-8936f338d207?w=400&h=300&fit=crop', 'filename': 'costume_3.jpg'},
    {'url': 'https://images.unsplash.com/photo-1523381294911-8d3cead13475?w=400&h=300&fit=crop', 'filename': 'costume_4.jpg'},
    {'url': 'https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=400&h=300&fit=crop', 'filename': 'costume_5.jpg'},
    {'url': 'https://images.unsplash.com/photo-1487215078519-e21cc028cb29?w=400&h=300&fit=crop', 'filename': 'costume_6.jpg'},
    {'url': 'https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=400&h=300&fit=crop', 'filename': 'costume_7.jpg'},
    {'url': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=400&h=300&fit=crop', 'filename': 'costume_8.jpg'},
    # 家具专场
    {'url': 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400&h=300&fit=crop', 'filename': 'furniture_1.jpg'},
    {'url': 'https://images.unsplash.com/photo-1557821552-17105176677c?w=400&h=300&fit=crop', 'filename': 'furniture_2.jpg'},
    {'url': 'https://images.unsplash.com/photo-1593435162379-1d7257791cd3?w=400&h=300&fit=crop', 'filename': 'furniture_3.jpg'},
    {'url': 'https://images.unsplash.com/photo-1551298376-118d06f5d5d9?w=400&h=300&fit=crop', 'filename': 'furniture_4.jpg'},
    {'url': 'https://images.unsplash.com/photo-1555041469-712d420e4e2e?w=400&h=300&fit=crop', 'filename': 'furniture_5.jpg'},
    {'url': 'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=400&h=300&fit=crop', 'filename': 'furniture_6.jpg'},
    {'url': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=400&h=300&fit=crop', 'filename': 'furniture_7.jpg'},
    {'url': 'https://images.unsplash.com/photo-1567016821344-cd79e388d303?w=400&h=300&fit=crop', 'filename': 'furniture_8.jpg'},
    # 家电专场
    {'url': 'https://images.unsplash.com/photo-1587831990284-cd24b78a66b6?w=400&h=300&fit=crop', 'filename': 'homeappliances_1.jpg'},
    {'url': 'https://images.unsplash.com/photo-1605296862277-1e51d390f289?w=400&h=300&fit=crop', 'filename': 'homeappliances_2.jpg'},
    {'url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&h=300&fit=crop', 'filename': 'homeappliances_3.jpg'},
    {'url': 'https://images.unsplash.com/photo-1581291518633-83b4ebd1d83e?w=400&h=300&fit=crop', 'filename': 'homeappliances_4.jpg'},
    {'url': 'https://images.unsplash.com/photo-1574717020297-09138d39e1d6?w=400&h=300&fit=crop', 'filename': 'homeappliances_5.jpg'},
    {'url': 'https://images.unsplash.com/photo-1584464716144-38a8e7040440?w=400&h=300&fit=crop', 'filename': 'homeappliances_6.jpg'},
    {'url': 'https://images.unsplash.com/photo-1594007650960-89d0d0d9d120?w=400&h=300&fit=crop', 'filename': 'homeappliances_7.jpg'},
    {'url': 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=400&h=300&fit=crop', 'filename': 'homeappliances_8.jpg'},
    # 数码专场
    {'url': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400&h=300&fit=crop', 'filename': 'numericalcode_1.jpg'},
    {'url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=300&fit=crop', 'filename': 'numericalcode_2.jpg'},
    {'url': 'https://images.unsplash.com/photo-1545127398-322e4fef3e60?w=400&h=300&fit=crop', 'filename': 'numericalcode_3.jpg'},
    {'url': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400&h=300&fit=crop', 'filename': 'numericalcode_4.jpg'},
    {'url': 'https://images.unsplash.com/photo-1593642632823-8f785190815e?w=400&h=300&fit=crop', 'filename': 'numericalcode_5.jpg'},
    {'url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=300&fit=crop', 'filename': 'numericalcode_6.jpg'},
    {'url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&h=300&fit=crop', 'filename': 'numericalcode_7.jpg'},
    {'url': 'https://images.unsplash.com/photo-1601662528567-526cd06f6582?w=400&h=300&fit=crop', 'filename': 'numericalcode_8.jpg'},
    # 零食专场
    {'url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop', 'filename': 'snacks_1.jpg'},
    {'url': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=400&h=300&fit=crop', 'filename': 'snacks_2.jpg'},
    {'url': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400&h=300&fit=crop', 'filename': 'snacks_3.jpg'},
    {'url': 'https://images.unsplash.com/photo-1541519227354-08fa5d50c44d?w=400&h=300&fit=crop', 'filename': 'snacks_4.jpg'},
    {'url': 'https://images.unsplash.com/photo-1546793665-c74683f339c1?w=400&h=300&fit=crop', 'filename': 'snacks_5.jpg'},
    {'url': 'https://images.unsplash.com/photo-1541963463532-d68292c34d19?w=400&h=300&fit=crop', 'filename': 'snacks_6.jpg'},
    {'url': 'https://images.unsplash.com/photo-1563245372-f21724e3856d?w=400&h=300&fit=crop', 'filename': 'snacks_7.jpg'},
    {'url': 'https://images.unsplash.com/photo-1552689431-9e3a8d63f48b?w=400&h=300&fit=crop', 'filename': 'snacks_8.jpg'}
]

success_count = 0
failed_list = []

print("开始下载图片...")
for item in download_list:
    url = item['url']
    filename = item['filename']
    filepath = os.path.join('images', filename)
    
    try:
        print(f"正在下载 {filename}...")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"✓ {filename} 下载完成")
            success_count += 1
        else:
            print(f"✗ {filename} 下载失败: HTTP {response.status_code}")
            failed_list.append(filename)
    except Exception as e:
        print(f"✗ {filename} 下载失败: {str(e)}")
        failed_list.append(filename)

print(f"\n下载完成！")
print(f"成功下载: {success_count}/{len(download_list)}")
if failed_list:
    print(f"下载失败的文件: {failed_list}")
else:
    print("所有文件下载成功！")