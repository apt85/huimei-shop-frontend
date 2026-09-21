$productDetailsDir = "c:\Users\liuzhilang\Documents\HBuilderProjects\shoppingplatform\productdetails"
$files = Get-ChildItem -Path $productDetailsDir -Filter "*.html"

foreach ($file in $files) {
    $filePath = $file.FullName
    $content = Get-Content -Path $filePath -Raw
    
    # 检查addToCart函数是否包含图片信息获取代码
    if ($content -like "*function addToCart*" -and $content -notlike "*productImage*") {
        Write-Host "需要更新的文件: $($file.Name)"
        
        # 更新addToCart函数，添加图片信息获取代码
        $updatedContent = $content -replace 
            'function addToCart\(button\) \{\s*const productDetail = button\.closest\(''\.product-detail''\);\s*const product = \{\s*id: productDetail\.dataset\.productId,\s*name: productDetail\.dataset\.productName,\s*price: parseFloat\(productDetail\.dataset\.productPrice\)\s*\};',
            'function addToCart(button) {\n            const productDetail = button.closest(''.product-detail'');\n            const productImage = productDetail.querySelector(''.product-image'');\n            const product = {\n                id: productDetail.dataset.productId,\n                name: productDetail.dataset.productName,\n                price: parseFloat(productDetail.dataset.productPrice),\n                image: productImage ? productImage.src : ''''\n            };'
        
        Set-Content -Path $filePath -Value $updatedContent -Encoding UTF8
        Write-Host "已更新文件: $($file.Name)"
    }
}

Write-Host "所有文件检查和更新完成！"