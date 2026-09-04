import os

pages = {
    "docs/index.md": "# 文档记录\n\n这里是文档记录的汇总页面。",
    "frontend/index.md": "# 前端文档\n\n这里是前端开发相关的文档说明。",
    "vmware/index.md": "# VMware ESXi\n\nVMware ESXi 的使用教程与排错指南。",
    "server/index.md": "# 把玩服务器\n\nVPS 与独立服务器的折腾记录。",
    "asus/index.md": "# ASUS\n\n华硕路由器与固件折腾指南。",
    "streaming/summary.md": "# 流媒体观影指南\n\nNetflix、Disney+、Spotify等平台的使用与解锁指南。",
    "ai/summary.md": "# AI 使用汇总\n\n主流 AI 工具的最佳实践与使用技巧。",
    "ai/chatgpt.md": "# ChatGPT\n\nChatGPT 注册、升级与高阶提示词指南。",
    "ai/gemini.md": "# Gemini\n\nGoogle Gemini 模型的接入与使用教程。",
    "serve/airport/summary.md": "# VPN 机场评测与套餐比较\n\n主流机场的详细评测、价格对比及流媒体解锁情况。",
    "serve/sharing/account-sharing-guide.md": "# 账号合租与数字账号\n\nNetflix、ChatGPT 等流媒体与 AI 账号的安全合租指南。",
    "serve/routing/index.md": "# 线路选择与避坑\n\n科学上网线路解析、专线与直连的区别及避坑指南。",
    "serve/client/index.md": "# VPN/代理客户端教程\n\nClash、V2ray、Surge 等主流客户端的配置教程。",
    "serve/sms/index.md": "# 接码平台\n\n海外手机号接码平台推荐及使用方法。",
    "about/index.md": "# 关于本站\n\n关于 Eoht 的建站初衷与联系方式。",
    "privacy/index.md": "# 隐私政策\n\n本站的隐私保护与数据收集政策声明。"
}

for filepath, content in pages.items():
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Skeleton pages created successfully.")
