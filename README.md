＃20200624
1. 啟用 Radial 成功：的確是昨日發現的 bug 導致
2. 新問題，大概是因為文章數量太少，導致圖形都聚集在某個角落
3. 使用 forceManyBody().strength 來讓 node 散得更接近圓形，加上一點點 forceCollide 來讓 node 不要重疊

#20200623
1. 研究 forceRadial -> 發現問題（d.level if 判斷式進不去）
```javascript
.force("r", d3.forceRadial(function(d){
    console.log(d.level)
    if(d.level === "tag"){
        return 60
        console.log('fuck')
    }
    else if (d.level == 'article'){
        return 100
    }
    else if (d.level == 'media'){
        return 50
    }
}, width/2, height/2).strength(1))
```

#20200619
1. 撰寫 csvtojson
2. 測試 d3.force 各種變數
3. 測試 d3.forcebounce（需要再研究）

#20200617 
1. 創建json檔，撰寫開頭