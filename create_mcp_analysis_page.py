#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MCP 設定格式差異分析 - Notion 資料庫整合腳本
Author: Christian Wu
Date: 2025-06-11
"""

import requests
import json
import os
from datetime import datetime
from typing import Dict, List, Any

class NotionMCPIntegration:
    def __init__(self, token: str):
        """初始化 Notion API 客戶端"""
        self.token = token
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28'
        }
        
    def create_mcp_analysis_page(self, database_id: str) -> Dict[str, Any]:
        """建立 MCP 設定格式差異分析頁面"""
        
        # 頁面基本屬性
        properties = self._get_page_properties()
        
        # 頁面內容區塊
        content_blocks = self._get_content_blocks()
        
        payload = {
            "parent": {
                "database_id": database_id
            },
            "properties": properties,
            "children": content_blocks
        }
        
        try:
            print("📤 正在發送請求到 Notion API...")
            response = requests.post(
                f"{self.base_url}/pages",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                print("✅ 成功建立 MCP 分析頁面！")
                return response.json()
            else:
                print(f"❌ 建立失敗: {response.status_code}")
                print(f"錯誤詳情: {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ 網路請求錯誤: {e}")
            return None
    
    def _get_page_properties(self) -> Dict[str, Any]:
        """取得頁面屬性設定"""
        return {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": "MCP 設定格式差異分析指南"
                        }
                    }
                ]
            }
        }
    
    def _get_content_blocks(self) -> List[Dict[str, Any]]:
        """取得頁面內容區塊"""
        return [
            # 標題與總覽
            {
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "📋 總覽 | Overview"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "本文件分析 "
                            }
                        },
                        {
                            "type": "text",
                            "text": {
                                "content": "Cursor、VS Code、Trae 和 Claude Desktop"
                            },
                            "annotations": {
                                "bold": True
                            }
                        },
                        {
                            "type": "text",
                            "text": {
                                "content": " 在 MCP (Model Context Protocol) 設定格式上的核心差異。"
                            }
                        }
                    ]
                }
            },
            
            # 分隔線
            {
                "object": "block",
                "type": "divider",
                "divider": {}
            },
            
            # 關鍵發現
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "🎯 關鍵發現"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "callout",
                "callout": {
                    "icon": {
                        "emoji": "💡"
                    },
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Claude Desktop 使用與 Cursor 幾乎相同的格式，採用 mcpServers 根鍵！"
                            },
                            "annotations": {
                                "bold": True
                            }
                        }
                    ]
                }
            },
            
            # 各 IDE 設定格式範例
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "🔧 設定格式範例"
                            }
                        }
                    ]
                }
            },
            
            # Cursor 設定
            {
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Cursor MCP 設定"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "code",
                "code": {
                    "language": "json",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": """{
  "mcpServers": [
    {
      "name": "figma-ai-bridge",
      "url": "http://localhost:3000/figma",
      "description": "Figma 設計稿解析服務"
    }
  ],
  "aiParameters": {
    "temperature": 0.7,
    "maxTokens": 2048
  }
}"""
                            }
                        }
                    ]
                }
            },
            
            # Claude Desktop 設定
            {
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Claude Desktop MCP 設定 ⭐"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "配置檔案位置："
                            }
                        },
                        {
                            "type": "text",
                            "text": {
                                "content": "~/Library/Application Support/Claude/claude_desktop_config.json"
                            },
                            "annotations": {
                                "code": True
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "code",
                "code": {
                    "language": "json",
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": """{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}"""
                            }
                        }
                    ]
                }
            },
            
            # 格式比較
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "📊 格式比較"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "table",
                "table": {
                    "table_width": 3,
                    "has_column_header": True,
                    "has_row_header": False,
                    "children": [
                        {
                            "object": "block",
                            "type": "table_row",
                            "table_row": {
                                "cells": [
                                    [{"type": "text", "text": {"content": "IDE"}}],
                                    [{"type": "text", "text": {"content": "根鍵"}}],
                                    [{"type": "text", "text": {"content": "相容性"}}]
                                ]
                            }
                        },
                        {
                            "object": "block",
                            "type": "table_row",
                            "table_row": {
                                "cells": [
                                    [{"type": "text", "text": {"content": "Cursor"}}],
                                    [{"type": "text", "text": {"content": "mcpServers"}}],
                                    [{"type": "text", "text": {"content": "🟢 完全相容"}}]
                                ]
                            }
                        },
                        {
                            "object": "block",
                            "type": "table_row",
                            "table_row": {
                                "cells": [
                                    [{"type": "text", "text": {"content": "VS Code"}}],
                                    [{"type": "text", "text": {"content": "servers"}}],
                                    [{"type": "text", "text": {"content": "🟡 需要轉換"}}]
                                ]
                            }
                        },
                        {
                            "object": "block",
                            "type": "table_row",
                            "table_row": {
                                "cells": [
                                    [{"type": "text", "text": {"content": "Claude Desktop"}}],
                                    [{"type": "text", "text": {"content": "mcpServers"}}],
                                    [{"type": "text", "text": {"content": "🟢 原生支援"}}]
                                ]
                            }
                        }
                    ]
                }
            },
            
            # 結論
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "💡 結論與建議"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "最佳遷移路徑：Cursor ↔ Claude Desktop（零成本）"
                            },
                            "annotations": {
                                "bold": True
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "企業級應用：VS Code 提供最佳安全性"
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "高效能需求：Trae 提供專案感知功能"
                            }
                        }
                    ]
                }
            },
            
            # 頁尾
            {
                "object": "block",
                "type": "divider",
                "divider": {}
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "📅 建立日期：2025-06-11 | 📝 版本：v1.0 | 👤 作者：Christian Wu"
                            },
                            "annotations": {
                                "italic": True,
                                "color": "gray"
                            }
                        }
                    ]
                }
            }
        ]

def main():
    """主要執行函數"""
    print("🚀 MCP 設定格式差異分析 - Notion 整合工具")
    print("=" * 50)
    
    # 設定參數
    DATABASE_ID = "20ede957-d4e5-8033-b64d-fb4f53111611"
    
    # 從環境變數或直接輸入取得 Token
    NOTION_TOKEN = os.getenv('NOTION_TOKEN')
    
    if not NOTION_TOKEN:
        print("💡 請輸入您的 Notion Integration Token:")
        NOTION_TOKEN = input("Token (secret_...): ").strip()
        
    if not NOTION_TOKEN or not NOTION_TOKEN.startswith('secret_'):
        print("❌ Token 格式不正確，應該以 'secret_' 開頭")
        return
    
    print(f"🎯 目標資料庫 ID: {DATABASE_ID}")
    print(f"🔑 使用 Token: {NOTION_TOKEN[:10]}...")
    
    # 建立 Notion 客戶端
    notion = NotionMCPIntegration(NOTION_TOKEN)
    
    # 執行建立頁面
    print("\n📤 開始建立 MCP 分析頁面...")
    result = notion.create_mcp_analysis_page(DATABASE_ID)
    
    if result:
        page_url = result.get('url', '未取得頁面連結')
        page_id = result.get('id', '未取得頁面 ID')
        
        print("\n🎉 執行成功！")
        print("=" * 50)
        print(f"✅ 頁面已建立完成")
        print(f"📄 頁面連結：{page_url}")
        print(f"🆔 頁面 ID：{page_id}")
        print(f"🗂️ 資料庫 ID：{DATABASE_ID}")
        print("\n📝 頁面內容包含：")
        print("   • 📋 MCP 格式總覽")
        print("   • 🔧 各 IDE 設定範例")
        print("   • 📊 格式比較矩陣")
        print("   • 🎯 關鍵發現與結論")
        print("   • 💡 使用建議")
    else:
        print("\n❌ 頁面建立失敗")
        print("請檢查：")
        print("1. Token 是否正確")
        print("2. Integration 是否已共享給資料庫")
        print("3. 資料庫 ID 是否正確")

if __name__ == "__main__":
    main()
