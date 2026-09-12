import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "AI工具导航站",
  description: "汇总 Linux、Docker、VPS 中文技术文档，提供流媒体、AI 工具及账号使用指南。",
  cleanUrls: true,
  
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
      { text: '机场推荐', link: '/airport/recommend/sogo' },
      { text: '机场排行榜', link: '/airport/ranking/' },
      { text: '稳定机场', link: '/airport/stable/' },
      { text: '老牌机场', link: '/airport/classic/' },
      { text: '性价比机场', link: '/airport/value/' },
      { text: '优质机场', link: '/airport/premium/' },
      { text: '便宜机场', link: '/airport/cheap/' },
      { text: '一元机场', link: '/airport/oneyuan/' },
      {
        text: '🤖 AI 工具导航',
        items: [
          { text: 'AI 工具汇总', link: '/ai/summary' },
          { text: 'AI 副业变现', link: '/ai/sidehustle/' },
          { text: 'AI 写作工具', link: '/ai/writing/' },
          { text: 'AI 图像工具', link: '/ai/image/' },
          { text: 'AI 视频工具', link: '/ai/video/' },
          { text: 'AI 编程辅助', link: '/ai/coding/' },
          { text: 'AI 提示词指令', link: '/ai/prompts/' }
        ]
      },
      {
        text: '🍿 流媒体与账号',
        items: [
          { text: '账号合租指南', link: '/serve/sharing/account-sharing-guide' }
        ]
      }
    ],

    sidebar: {
      '/airport/': [
        {
          text: '✈️ 科学上网',
          items: [
            { text: '机场排行榜', link: '/airport/ranking/' },
            { text: 'sogo云 深度评测', link: '/airport/recommend/sogo' },
            { text: '稳定机场', link: '/airport/stable/' },
            { text: '老牌机场', link: '/airport/classic/' },
            { text: '性价比机场', link: '/airport/value/' },
            { text: '优质机场', link: '/airport/premium/' },
            { text: '微风 (Weifeng) 深度评测', link: '/airport/recommend/weifeng' }
          ]
        }
      ],
      '/serve/': [
        {
          text: '🍿 影音合租与低价账号',
          items: [
            { text: '账号合租指南', link: '/serve/sharing/account-sharing-guide' }
          ]
        }
      ],
      '/ai/': [
        {
          text: '🤖 AI 创作与办公',
          items: [
            { text: 'AI 工具汇总', link: '/ai/summary' },
            { text: 'Ai写作工具', link: '/ai/writing/' },
            { text: 'Ai图像工具', link: '/ai/image/' },
            { text: 'Ai视频工具', link: '/ai/video/' },
            { text: 'Ai办公工具', link: '/ai/office/' },
            { text: 'Ai聊天助手', link: '/ai/chat/' },
            { text: 'Ai智能体', link: '/ai/agent/' }
          ]
        },
        {
          text: '💻 AI 开发与设计',
          items: [
            { text: 'Ai编程工具', link: '/ai/coding/' },
            { text: 'Ai开发平台', link: '/ai/dev/' },
            { text: 'Ai设计工具', link: '/ai/design/' },
            { text: 'Ai音频工具', link: '/ai/audio/' },
            { text: 'Ai搜索引擎', link: '/ai/search/' },
            { text: 'Ai学习网站', link: '/ai/learning/' }
          ]
        },
        {
          text: '🚀 AI 模型与拓展',
          items: [
            { text: 'Ai副业变现指南', link: '/ai/sidehustle/' },
            { text: 'Ai训练模型', link: '/ai/models/' },
            { text: 'Ai模型评测', link: '/ai/evaluation/' },
            { text: 'Ai内容检测', link: '/ai/detection/' },
            { text: 'Ai提示词指令', link: '/ai/prompts/' }
          ]
        }
      ]
    },

    footer: {
      message: `
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
            <a href="https://findjichang.com" target="_blank" rel="noopener noreferrer">找机场</a>
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
          <div class="footer-column">
            <div class="footer-title">🤖 AI 创作与办公</div>
            <a href="/ai/writing/">Ai写作工具</a>
            <a href="/ai/image/">Ai图像工具</a>
            <a href="/ai/video/">Ai视频工具</a>
            <a href="/ai/office/">Ai办公工具</a>
            <a href="/ai/chat/">Ai聊天助手</a>
            <a href="/ai/agent/">Ai智能体</a>
          </div>
          <div class="footer-column">
            <div class="footer-title">💻 AI 开发与设计</div>
            <a href="/ai/coding/">Ai编程工具</a>
            <a href="/ai/dev/">Ai开发平台</a>
            <a href="/ai/design/">Ai设计工具</a>
            <a href="/ai/audio/">Ai音频工具</a>
            <a href="/ai/search/">Ai搜索引擎</a>
            <a href="/ai/learning/">Ai学习网站</a>
          </div>
          <div class="footer-column">
            <div class="footer-title">🚀 AI 模型与拓展</div>
            <a href="/ai/models/">Ai训练模型</a>
            <a href="/ai/evaluation/">Ai模型评测</a>
            <a href="/ai/detection/">Ai内容检测</a>
            <a href="/ai/prompts/">Ai提示词指令</a>
            <a href="/ai/sidehustle/">Ai副业工具</a>
          </div>
        </div>
      `,
      copyright: 'Copyright © 2026-present AI工具导航站'
    }
  }
})
