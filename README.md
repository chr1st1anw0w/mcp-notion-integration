# MCP 設定格式差異分析 - Notion 整合工具

## 🎯 專案目的

此工具可以自動將 **MCP (Model Context Protocol) 設定格式差異分析** 文件建立到您的 Notion 資料庫中，包含完整的格式比較、程式碼範例和使用建議。

## 📋 功能特色

- ✅ **自動化建立 Notion 頁面**：一鍵將分析報告加入資料庫
- ✅ **完整格式支援**：包含表格、程式碼區塊、標題層級
- ✅ **四種 IDE 比較**：Cursor、VS Code、Trae、Claude Desktop
- ✅ **視覺化呈現**：emoji 圖示、高亮文字、摺疊區塊
- ✅ **安全性考量**：支援環境變數儲存 Token

## 🚀 快速開始

### 前置準備

1. **Python 3.6+** 環境
2. **Notion Integration Token**（格式：`secret_...`）
3. **目標 Notion 資料庫** 已共享給 Integration

### 安裝依賴

```bash
pip install requests
```

### 設定 Token

**方式一：環境變數（推薦）**
```bash
export NOTION_TOKEN="secret_your_actual_token_here"
```

**方式二：執行時輸入**
```bash
python create_mcp_analysis_page.py
# 程式會提示您輸入 Token
```

### 執行腳本

```bash
python create_mcp_analysis_page.py
```

## 📊 執行結果

成功執行後，您將在 Notion 資料庫中看到新建立的頁面：

```
🎉 執行成功！
==================================================
✅ 頁面已建立完成
📄 頁面連結：https://www.notion.so/...
🆔 頁面 ID：...
🗂️ 資料庫 ID：20ede957-d4e5-8033-b64d-fb4f53111611

📝 頁面內容包含：
   • 📋 MCP 格式總覽
   • 🔧 各 IDE 設定範例
   • 📊 格式比較矩陣
   • 🎯 關鍵發現與結論
   • 💡 使用建議
```

## 📖 頁面內容預覽

建立的 Notion 頁面將包含：

### 🔧 設定格式範例
- **Cursor MCP 設定**：`mcpServers` 格式 + AI 參數
- **VS Code MCP 設定**：`servers` 格式 + 環境變數
- **Trae MCP 設定**：`projectAwareServers` 格式 + 效能優化
- **Claude Desktop MCP 設定**：標準化 MCP 協議實作

### 📊 格式比較矩陣
| IDE | 根鍵 | 相容性 |
|-----|------|--------|
| Cursor | `mcpServers` | 🟢 完全相容 |
| VS Code | `servers` | 🟡 需要轉換 |
| Claude Desktop | `mcpServers` | 🟢 原生支援 |

### 🎯 關鍵發現
> 💡 **Claude Desktop 使用與 Cursor 幾乎相同的格式！**

## ⚙️ 自訂設定

### 修改目標資料庫

在腳本中修改 `DATABASE_ID` 變數：

```python
DATABASE_ID = "your_database_id_here"
```

### 自訂頁面屬性

修改 `_get_page_properties()` 方法來適應您的資料庫結構：

```python
def _get_page_properties(self) -> Dict[str, Any]:
    return {
        "標題": {  # 您的標題欄位名稱
            "title": [...]
        },
        "類型": {  # 您的類型欄位名稱
            "select": {"name": "技術文件"}
        }
        # 加入更多欄位...
    }
```

## 🔧 故障排除

### 常見錯誤

| 錯誤代碼 | 原因 | 解決方案 |
|----------|------|----------|
| **401** | Token 無效 | 檢查 Token 格式是否正確 |
| **403** | 權限不足 | 確認 Integration 已共享給資料庫 |
| **404** | 資料庫不存在 | 檢查 Database ID 是否正確 |

### 除錯模式

在腳本中加入除錯資訊：

```python
print(f"Database ID: {DATABASE_ID}")
print(f"Token 前 10 字符: {NOTION_TOKEN[:10]}...")
```

## 📋 系統需求

- **Python**: 3.6 或更高版本
- **網路連線**: 需要存取 Notion API
- **權限**: Notion Integration 需要對目標資料庫有寫入權限

## 🤝 貢獻指南

歡迎提交 Issue 或 Pull Request！

## 📄 授權條款

MIT License

## 👤 作者

**Christian Wu**
- GitHub: [@chr1st1anw0w](https://github.com/chr1st1anw0w)
- Email: christian.wu@araizen.com

---

**⭐ 如果這個工具對您有幫助，請給個星星支持！**
