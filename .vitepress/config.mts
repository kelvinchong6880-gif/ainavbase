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

    footer: {
      message: `
        <div style="display: flex; justify-content: center; gap: 4rem; flex-wrap: wrap; text-align: left; line-height: 1.8; margin-top: 1rem;">
          <div>
            <strong>站点信息</strong>
            <ul style="list-style: none; padding: 0; margin: 0.5rem 0;">
              <li><a href="/about/">关于我们</a></li>
              <li><a href="/contact/">联系我们</a></li>
              <li><a href="/privacy/">隐私政策</a></li>
              <li><a href="/terms/">使用条款</a></li>
              <li><a href="/disclaimer/">免责声明</a></li>
            </ul>
          </div>
          <div>
            <strong>友情链接</strong>
            <ul style="list-style: none; padding: 0; margin: 0.5rem 0;">
              <li><a href="https://clash-vpn.org" target="_blank" rel="noopener noreferrer">Clash VPN</a></li>
              <li><a href="https://clashjiedian.org" target="_blank" rel="noopener noreferrer">Clash 节点</a></li>
              <li><a href="https://findjichang.com" target="_blank" rel="noopener noreferrer">发现机场</a></li>
              <li><a href="https://jichangdog.com" target="_blank" rel="noopener noreferrer">机场狗</a></li>
              <li><a href="https://haoyongjichang.com" target="_blank" rel="noopener noreferrer">好用机场</a></li>
            </ul>
          </div>
          <div>
            <strong>推荐资源</strong>
            <ul style="list-style: none; padding: 0; margin: 0.5rem 0;">
              <li><a href="https://github.com" target="_blank" rel="noopener noreferrer">GitHub</a></li>
              <li><a href="https://github.com/MetaCubeX/mihomo" target="_blank" rel="noopener noreferrer">Clash Meta</a></li>
              <li><a href="https://openai.com" target="_blank" rel="noopener noreferrer">OpenAI</a></li>
              <li><a href="https://huggingface.co" target="_blank" rel="noopener noreferrer">Hugging Face</a></li>
            </ul>
          </div>
        </div>
      `,
      copyright: 'Copyright © 2024-present AI工具导航站'
    }
  }
})
