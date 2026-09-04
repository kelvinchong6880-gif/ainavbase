import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "AI工具导航站",
  description: "汇总 Linux、Docker、VPS 中文技术文档，提供流媒体、AI 工具及账号使用指南。",
  
  head: [
    ['style', {}, `
      .VPNavBarTitle .logo { 
        height: 48px !important; 
        width: auto !important;
        margin-right: 10px !important;
      }
      .VPNavBar .content {
        flex-grow: 1 !important;
      }
      .VPNavBarMenu {
        flex-grow: 1 !important;
        justify-content: center !important;
      }
      /* 自定义页脚样式 */
      .custom-footer {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 3rem;
        max-width: 900px;
        margin: 1rem auto;
        text-align: left;
      }
      .footer-column {
        display: flex;
        flex-direction: column;
        gap: 0.8rem;
      }
      .footer-title {
        font-weight: 700;
        font-size: 1.1rem;
        color: var(--vp-c-text-1);
        margin-bottom: 0.5rem;
        border-bottom: 2px solid var(--vp-c-brand);
        padding-bottom: 0.4rem;
        width: fit-content;
      }
      .footer-column a {
        color: var(--vp-c-text-2) !important;
        text-decoration: none !important;
        transition: color 0.2s ease, transform 0.2s ease;
        font-size: 0.95rem;
        display: inline-block;
      }
      .footer-column a:hover {
        color: var(--vp-c-brand) !important;
        transform: translateX(4px);
      }
    `]
  ],

  themeConfig: {
    logo: '/logo.png',
    search: {
      provider: 'local'
    },
    
    nav: [
      { text: '机场推荐', link: '/airport/recommend/' },
      { text: '稳定机场', link: '/airport/stable/' },
      { text: '便宜机场', link: '/airport/cheap/' },
      { text: '老牌机场', link: '/airport/classic/' },
      { text: '性价比机场', link: '/airport/value/' },
      { text: '机场排行榜', link: '/airport/ranking/' },
      { text: '优质机场', link: '/airport/premium/' }
    ],

    sidebar: {
      '/airport/': [
        {
          text: '机场推荐',
          items: [
            { text: '推荐汇总', link: '/airport/recommend/' },
            { text: '微风 (Weifeng) 深度评测', link: '/airport/recommend/weifeng' }
          ]
        }
      ]
    },

    footer: {
      message: \`
        <div class="custom-footer">
          <div class="footer-column">
            <div class="footer-title">📌 站点信息</div>
            <a href="/about/">关于我们</a>
            <a href="/contact/">联系我们</a>
            <a href="/privacy/">隐私政策</a>
            <a href="/terms/">使用条款</a>
            <a href="/disclaimer/">免责声明</a>
          </div>
          <div class="footer-column">
            <div class="footer-title">🤝 友情链接</div>
            <a href="https://clash-vpn.org" target="_blank" rel="noopener noreferrer">Clash VPN</a>
            <a href="https://clashjiedian.org" target="_blank" rel="noopener noreferrer">Clash 节点</a>
            <a href="https://findjichang.com" target="_blank" rel="noopener noreferrer">发现机场</a>
            <a href="https://jichangdog.com" target="_blank" rel="noopener noreferrer">机场狗</a>
            <a href="https://haoyongjichang.com" target="_blank" rel="noopener noreferrer">好用机场</a>
          </div>
          <div class="footer-column">
            <div class="footer-title">🌐 推荐资源</div>
            <a href="https://github.com" target="_blank" rel="noopener noreferrer">GitHub</a>
            <a href="https://github.com/MetaCubeX/mihomo" target="_blank" rel="noopener noreferrer">Clash Meta</a>
            <a href="https://openai.com" target="_blank" rel="noopener noreferrer">OpenAI</a>
            <a href="https://huggingface.co" target="_blank" rel="noopener noreferrer">Hugging Face</a>
          </div>
        </div>
      \`,
      copyright: 'Copyright © 2024-present AI工具导航站'
    }
  }
})
