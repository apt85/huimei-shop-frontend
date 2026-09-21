import os
import requests

# 最后3张失败图片的更新链接
final_missing_images = [
    {'url': 'https://images.unsplash.com/photo-1574717020297-09138d39e1d6?w=400&h=300&fit=crop', 'filename': 'homeappliances_1.jpg'},
    {'url': 'https://images.unsplash.com/photo-1581291518633-83b4ebd1d83e?w=400&h=300&fit=crop', 'filename': 'homeappliances_6.jpg'},
    {'url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop', 'filename': 'snacks_8.jpg'}
]

success_count = 0
failed_list = []

print("开始下载最后3张缺失的图片...")
for item in final_missing_images:
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

print(f"\n最后3张图片下载完成！")
print(f"成功下载: {success_count}/{len(final_missing_images)}")
if failed_list:
    print(f"下载失败的文件: {failed_list}")
else:
    print("所有缺失图片下载成功！")