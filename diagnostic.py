import os
import glob
import re

print("--- DIAGNOSTIC SCRIPT START ---")

# Check config.mts for sitemap and favicon
config_path = r"c:\Users\USER\Desktop\ainavbase.com\.vitepress\config.mts"
with open(config_path, "r", encoding="utf-8") as f:
    config = f.read()

if "sitemap" not in config:
    print("[SEO] MISSING: sitemap configuration in config.mts")
if "rel=" not in config and "favicon" not in config:
    print("[BRAND] MISSING: favicon configuration in head")

# Check markdown files for missing frontmatter title/description
md_files = glob.glob(r"c:\Users\USER\Desktop\ainavbase.com\**\*.md", recursive=True)
missing_frontmatter = []
missing_title = []
missing_desc = []

for md in md_files:
    # Skip node_modules or dist
    if "node_modules" in md or "dist" in md:
        continue
    
    with open(md, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if it starts with ---
    if not content.startswith("---"):
        missing_frontmatter.append(md)
    else:
        # Extract frontmatter
        fm_end = content.find("---", 3)
        if fm_end != -1:
            fm = content[3:fm_end]
            if "title:" not in fm:
                missing_title.append(md)
            if "description:" not in fm:
                missing_desc.append(md)

print(f"\n[SEO] Files missing frontmatter: {len(missing_frontmatter)}")
print(f"[SEO] Files missing title: {len(missing_title)}")
print(f"[SEO] Files missing description: {len(missing_desc)}")
if len(missing_title) > 0:
    print("Example missing title:", missing_title[:3])
if len(missing_desc) > 0:
    print("Example missing desc:", missing_desc[:3])

print("--- DIAGNOSTIC SCRIPT END ---")
