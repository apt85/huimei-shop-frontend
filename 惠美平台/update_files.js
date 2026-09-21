const fs = require('fs');
const path = require('path');

const productDetailsDir = path.join(__dirname, 'productdetails');
const files = fs.readdirSync(productDetailsDir).filter(file => file.endsWith('.html'));

files.forEach(file => {
    const filePath = path.join(productDetailsDir, file);
    const content = fs.readFileSync(filePath, 'utf8');
    
    if (content.includes('function addToCart') && !content.includes('productImage')) {
        console.log(`需要更新的文件: ${file}`);
        const updatedContent = content.replace(
            /function addToCart\(button\) \{\s*const productDetail = button\.closest\('\.product-detail'\);\s*const product = \{\s*id: productDetail\.dataset\.productId,\s*name: productDetail\.dataset\.productName,\s*price: parseFloat\(productDetail\.dataset\.productPrice\)\s*\};/g,
            'function addToCart(button) {\n            const productDetail = button.closest(\'.product-detail\');\n            const productImage = productDetail.querySelector(\'.product-image\');\n            const product = {\n                id: productDetail.dataset.productId,\n                name: productDetail.dataset.productName,\n                price: parseFloat(productDetail.dataset.productPrice),\n                image: productImage ? productImage.src : \'\'\n            };'    
        );
        
        fs.writeFileSync(filePath, updatedContent, 'utf8');
        console.log(`已更新文件: ${file}`);
    }
});

console.log('所有文件检查和更新完成！');