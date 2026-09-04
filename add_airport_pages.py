import os

pages = {
    "airport/recommend/index.md": "# 机场推荐\n\n最新、最全的机场推荐汇总。",
    "airport/stable/index.md": "# 稳定机场\n\n以稳定性为主的 VPN 机场评测。",
    "airport/cheap/index.md": "# 便宜机场\n\n低价、高性价比的平民机场推荐。",
    "airport/classic/index.md": "# 老牌机场\n\n运营时间长、信誉好的老牌机场。",
    "airport/value/index.md": "# 性价比机场\n\n兼顾价格与速度的高性价比机场。",
    "airport/ranking/index.md": "# 机场排行榜\n\n各大机场综合实力排行榜。",
    "airport/premium/index.md": "# 优质机场\n\n提供专线、全节点流媒体解锁的高端优质机场。"
}

for filepath, content in pages.items():
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Airport pages created successfully.")
