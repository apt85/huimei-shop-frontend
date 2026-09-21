import os
import requests

# 缺失的图片列表
missing_images = [
    {'url': 'https://images.unsplash.com/photo-1601784551446-20a1159689b1?w=400&h=300&fit=crop', 'filename': 'cellphone_3.jpg'},
    {'url': 'https://images.unsplash.com/photo-1593435162379-1d7257791cd3?w=400&h=300&fit=crop', 'filename': 'furniture_3.jpg'},
    {'url': 'https://images.unsplash.com/photo-1551298376-118d06f5d5d9?w=400&h=300&fit=crop', 'filename': 'furniture_4.jpg'},
    {'url': 'https://images.unsplash.com/photo-1587831990284-cd24b78a66b6?w=400&h=300&fit=crop', 'filename': 'homeappliances_1.jpg'},
    {'url': 'https://images.unsplash.com/photo-1605296862277-1e51d390f289?w=400&h=300&fit=crop', 'filename': 'homeappliances_2.jpg'},
    {'url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&h=300&fit=crop', 'filename': 'homeappliances_5.jpg'},
    {'url': 'https://images.unsplash.com/photo-1574717020297-09138d39e1d6?w=400&h=300&fit=crop', 'filename': 'homeappliances_6.jpg'},
    {'url': 'https://images.unsplash.com/photo-1594007650960-89d0d0d9d120?w=400&h=300&fit=crop', 'filename': 'homeappliances_7.jpg'},
    {'url': 'https://images.unsplash.com/photo-1545127398-322e4fef3e60?w=400&h=300&fit=crop', 'filename': 'numericalcode_3.jpg'},
    {'url': 'https://images.unsplash.com/photo-1541963463532-d68292c34d19?w=400&h=300&fit=crop', 'filename': 'snacks_6.jpg'},
    {'url': 'https://images.unsplash.com/photo-1552689431-9e3a8d63f48b?w=400&h=300&fit=crop', 'filename': 'snacks_8.jpg'}
]

success_count = 0
failed_list = []

print("开始下载缺失的图片...")
for item in missing_images:
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

print(f"\n缺失图片下载完成！")
print(f"成功下载: {success_count}/{len(missing_images)}")
if failed_list:
    print(f"下载失败的文件: {failed_list}")
else:
    print("所有缺失图片下载成功！")