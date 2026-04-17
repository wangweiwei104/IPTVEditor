#!/bin/sh

# 先输出HTTP头
echo "Content-type: text/plain"
echo ""

# 定义文件存储路径
WEB_ROOT="/www/iptv"

# 从查询参数获取文件名
FILENAME=""
if [ -n "$QUERY_STRING" ]; then
    # 从查询字符串中提取filename参数
    QUERY="$QUERY_STRING"
    # 解码URL编码（处理空格等特殊字符）
    QUERY=$(printf "$(echo "$QUERY" | sed 's/+/ /g; s/%/\\x/g')")
    
    # 提取filename参数
    for param in $(echo "$QUERY" | tr '&' ' '); do
        if echo "$param" | grep -q "filename="; then
            FILENAME=$(echo "$param" | cut -d'=' -f2-)
            break
        fi
    done
fi


# 读取POST内容
if [ -n "$CONTENT_LENGTH" ] && [ "$CONTENT_LENGTH" -gt 0 ]; then
    # 保存目标文件路径
    TARGET_FILE="$WEB_ROOT/$FILENAME"
    
    # 创建临时文件
    TMP_FILE="$TARGET_FILE.tmp.$$"
    
    # 读取POST数据
    dd bs=1 count=$CONTENT_LENGTH 2>/dev/null > "$TMP_FILE"
    
    # 检查临时文件是否为空
    if [ ! -s "$TMP_FILE" ]; then
        echo "错误：接收到的内容为空"
        rm -f "$TMP_FILE"
        exit 1
    fi
    
    # 将临时文件移动到目标位置
    mv "$TMP_FILE" "$TARGET_FILE"
    
    # 更新修改时间记录
    TIME_FILE="$WEB_ROOT/last_modified_$FILENAME.txt"
    CURRENT_TIME=$(date '+%Y年%m月%d日 %H:%M:%S')
    echo "$CURRENT_TIME" > "$TIME_FILE"
    
    echo "success"
else
    echo "错误：未接收到数据或数据长度为0"
    exit 1
fi

exit 0