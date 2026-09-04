import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "AI工具导航站",
  description: "汇总 Linux、Docker、VPS 中文技术文档，提供流媒体、AI 工具及账号使用指南。",
  
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
        <div style="display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap; text-align: left; line-height: 1.8;">
          <div>
            <strong>VPN机场与线路</strong>
            <ul style="list-style: none; padding: 0; margin: 0.5rem 0;">
              <li><a href="/serve/airport/summary">机场推荐与评测</a></li>
              <li><a href="/serve/routing/">线路选择与避坑</a></li>
              <li><a href="/serve/client/">客户端教程</a></li>
            </ul>
          </div>
          <div>
            <strong>流媒体、账号与 AI</strong>
            <ul style="list-style: none; padding: 0; margin: 0.5rem 0;">
              <li><a href="/streaming/summary">流媒体观影指南</a></li>
              <li><a href="/serve/sharing/account-sharing-guide">账号合租与独享</a></li>
              <li><a href="/ai/summary">AI 综合使用汇总</a></li>
            </ul>
          </div>
          <div>
            <strong>站点信息</strong>
            <ul style="list-style: none; padding: 0; margin: 0.5rem 0;">
              <li><a href="/about/">关于本站</a></li>
              <li><a href="/privacy/">隐私政策</a></li>
              <li><a href="/serve/sms/">接码平台</a></li>
            </ul>
          </div>
        </div>
      `,
      copyright: 'Copyright © 2024-present AI工具导航站'
    }
  }
})
