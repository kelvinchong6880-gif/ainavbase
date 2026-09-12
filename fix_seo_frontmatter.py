import os

pages = {
    r"c:\Users\USER\Desktop\ainavbase.com\index.md": {
        "title": "AI工具导航站 - 顶级 AI 工具与科学上网资源",
        "description": "全面收录全球前沿 AI 写作、绘画、编程等效率神器，并提供高质量流媒体观影、数字账号合租及科学上网（机场）资源，一站式赋能您的数字生活与副业变现。"
    },
    r"c:\Users\USER\Desktop\ainavbase.com\airport\ranking\index.md": {
        "title": "2026 最新机场排行榜：稳定好用机场推荐",
        "description": "为您精选 2026 年最新翻墙机场排行榜，涵盖最稳定、速度最快的优质代理节点服务商，支持 Clash, Shadowrocket, v2rayN 等全平台客户端。"
    },
    r"c:\Users\USER\Desktop\ainavbase.com\airport\cheap\index.md": {
        "title": "便宜机场推荐：低价大流量代理节点",
        "description": "精选市面上便宜且好用的高性价比机场，提供低价大流量订阅套餐，适合学生党及轻度科学上网用户。"
    },
    r"c:\Users\USER\Desktop\ainavbase.com\airport\classic\index.md": {
        "title": "老牌机场推荐：运营多年不跑路的稳定节点",
        "description": "收集并评测运营三年以上的老牌翻墙机场，技术底蕴深厚，抗封锁能力强，为您提供永不失联的稳定代理服务。"
    },
    r"c:\Users\USER\Desktop\ainavbase.com\airport\oneyuan\index.md": {
        "title": "一元机场推荐：一元白嫖试用好帮手",
        "description": "为您寻找月付一元甚至提供免费试用节点的便宜机场，适合仅需临时科学上网或偶尔查阅海外资料的用户。"
    },
    r"c:\Users\USER\Desktop\ainavbase.com\airport\premium\index.md": {
        "title": "优质机场推荐：高端 IPLC 专线极致体验",
        "description": "追求极致速度与延迟？为您推荐全线采用 IPLC/IEPL 国际内网专线的优质高端机场，晚高峰 4K/8K 视频秒开，游戏不丢包。"
    },
    r"c:\Users\USER\Desktop\ainavbase.com\airport\stable\index.md": {
        "title": "稳定机场推荐：晚高峰不限速不卡顿",
        "description": "经过长期测速与稳定性追踪，为您推荐 2026 年表现最稳定的机场节点，确保在晚高峰等拥堵时段依然流畅出海。"
    },
    r"c:\Users\USER\Desktop\ainavbase.com\airport\value\index.md": {
        "title": "性价比机场推荐：兼顾价格与速度的完美选择",
        "description": "为您寻找价格亲民且速度不俗的性价比机场，不仅支持流媒体解锁，还拥有充足的节点冗余，是日常办公娱乐的首选。"
    }
}

for path, meta in pages.items():
    if not os.path.exists(path):
        continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if frontmatter exists
    if content.startswith("---"):
        fm_end = content.find("---", 3)
        if fm_end != -1:
            fm = content[3:fm_end]
            body = content[fm_end+3:]
            
            # Remove old title/description if they exist
            lines = fm.split("\n")
            new_lines = [l for l in lines if not l.startswith("title:") and not l.startswith("description:")]
            
            # Add new title and description
            new_fm = f"title: {meta['title']}\ndescription: {meta['description']}\n" + "\n".join(new_lines)
            
            new_content = "---\n" + new_fm.strip() + "\n---" + body
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {path}")
    else:
        # Create basic frontmatter if not exists
        new_content = f"---\ntitle: {meta['title']}\ndescription: {meta['description']}\n---\n\n" + content
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Added FM to {path}")
