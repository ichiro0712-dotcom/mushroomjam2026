import re

def update_jam2():
    with open('jam2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Combine BACKGROUND and VISION
    old_concept = """                            <div class="grid-2">
                                <div className="glass-panel feature-card hover-lift animate-fade-up delay-1">
                                    <div className="feature-icon">🎬</div>
                                    <h3 className="feature-title font-display">THE BACKGROUND</h3>
                                    <h4 style={{ color: '#fff', fontSize: '1.25rem', marginBottom: '1rem', fontWeight: 700 }}>数字の先にある「人間の熱量」</h4>
                                    <p style={{ color: 'var(--text-sub)' }}>
                                        YouTubeというプラットフォームで確かなコミュニティを築き上げてきた表現者たち。しかし、画面の中だけでは伝えきれない表現衝動や、まだ見ぬポテンシャルが彼らには眠っています。デジタルな繋がりを超え、クリエイターの「本気のパフォーマンス」をリアルな会場で解き放ち、ファンと共に新しい伝説を創る場所が必要です。
                                    </p>
                                </div>

                                <div className="glass-panel feature-card hover-lift animate-fade-up delay-2">
                                    <div className="feature-icon">🔥</div>
                                    <h3 className="feature-title font-display">THE VISION</h3>
                                    <h4 style={{ color: '#fff', fontSize: '1.25rem', marginBottom: '1rem', fontWeight: 700 }}>「情熱」を、ファンと共に可視化する</h4>
                                    <p style={{ color: 'var(--text-sub)' }}>
                                        普段の動画スタイルとは一線を画す「本気の一面」を30分間のステージに凝縮。<br /><br />
                                        クリエイターとファンが同じ空間で熱量を共有し、「リアル投げ銭（ボール）」という形で目に見える愛を届け合うことで、これまでにない深い絆を構築する「日本一距離が近い」プレミアムイベントです。
                                    </p>
                                </div>
                            </div>"""
    
    new_concept = """                            <div className="glass-panel feature-card hover-lift animate-fade-up delay-1" style={{ maxWidth: '900px', margin: '0 auto' }}>
                                <div className="feature-icon">🔥</div>
                                <h3 className="feature-title font-display">VISION</h3>
                                <h4 style={{ color: '#fff', fontSize: '1.25rem', marginBottom: '1rem', fontWeight: 700 }}>数字の先にある「人間の熱量」と情熱の可視化</h4>
                                <p style={{ color: 'var(--text-sub)', marginBottom: '1.5rem' }}>
                                    YouTubeというプラットフォームで確かなコミュニティを築き上げてきた表現者たち。しかし、画面の中だけでは伝えきれない表現衝動や、まだ見ぬポテンシャルが彼らには眠っています。デジタルな繋がりを超え、クリエイターの「本気のパフォーマンス」をリアルな会場で解き放ち、ファンと共に新しい伝説を創る場所が必要です。
                                </p>
                                <p style={{ color: 'var(--text-sub)' }}>
                                    普段の動画スタイルとは一線を画す「本気の一面」を30分間のステージに凝縮。<br />
                                    クリエイターとファンが同じ空間で熱量を共有し、「リアル投げ銭（ボール）」という形で目に見える愛を届け合うことで、これまでにない深い絆を構築する「日本一距離が近い」プレミアムイベントです。
                                </p>
                            </div>"""

    content = content.replace(old_concept, new_concept)

    # 2. EVENT OVERVIEW to OVERVIEW and combine
    old_overview_head = """<h2 className="section-title font-display text-gradient">EVENT OVERVIEW</h2>"""
    content = content.replace(old_overview_head, """<h2 className="section-title font-display text-gradient">OVERVIEW</h2>""")

    old_overview_cards = """                            <div className="grid-3">
                                <div className="glass-panel feature-card text-center hover-lift">
                                    <div className="feature-icon">📅</div>
                                    <h3 className="font-accent" style={{ color: 'var(--text-sub)', marginBottom: '0.5rem' }}>DATE & TIME</h3>
                                    <p className="font-display" style={{ fontSize: '1.5rem', color: '#fff' }}>2026年 某日</p>
                                    <p style={{ color: 'var(--primary)', fontWeight: 'bold', marginTop: '0.5rem' }}>19:30 開場 / 23:30 終了</p>
                                </div>

                                <div className="glass-panel feature-card text-center hover-lift">
                                    <div className="feature-icon">🎯</div>
                                    <h3 className="font-accent" style={{ color: 'var(--text-sub)', marginBottom: '0.5rem' }}>TARGET AUDIENCE</h3>
                                    <p className="font-display" style={{ fontSize: '1.25rem', color: '#fff' }}>出演クリエイターの<br />コアファン層</p>
                                    <p style={{ color: 'var(--primary)', fontWeight: 'bold', marginTop: '0.5rem' }}>熱狂的なライブを求める方へ</p>
                                </div>

                                <div className="glass-panel feature-card text-center hover-lift">
                                    <div className="feature-icon">🎙️</div>
                                    <h3 className="font-accent" style={{ color: 'var(--text-sub)', marginBottom: '0.5rem' }}>LINEUP</h3>
                                    <p className="font-display" style={{ fontSize: '1.5rem', color: '#fff' }}>本気の表現者たち</p>
                                    <p style={{ color: 'var(--primary)', fontWeight: 'bold', marginTop: '0.5rem' }}>4〜5組 ＋ 著名MC</p>
                                </div>
                            </div>"""
                            
    new_overview_card = """                            <div className="glass-panel feature-card hover-lift" style={{ maxWidth: '900px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '2rem' }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: '2rem', borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '2rem' }}>
                                    <div className="feature-icon" style={{ margin: 0, fontSize: '2.5rem' }}>📅</div>
                                    <div>
                                        <h3 className="font-accent" style={{ color: 'var(--text-sub)', marginBottom: '0.25rem', fontSize: '0.875rem' }}>DATE & TIME</h3>
                                        <p className="font-display" style={{ fontSize: '1.25rem', color: '#fff' }}>2026年 某日 <span style={{ color: 'var(--primary)', fontWeight: 'bold', marginLeft: '1rem', fontSize: '1rem' }}>19:30 開場 / 23:30 終了</span></p>
                                    </div>
                                </div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: '2rem', borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '2rem' }}>
                                    <div className="feature-icon" style={{ margin: 0, fontSize: '2.5rem' }}>🎯</div>
                                    <div>
                                        <h3 className="font-accent" style={{ color: 'var(--text-sub)', marginBottom: '0.25rem', fontSize: '0.875rem' }}>TARGET AUDIENCE</h3>
                                        <p className="font-display" style={{ fontSize: '1.25rem', color: '#fff' }}>出演クリエイターのコアファン層 <span style={{ color: 'var(--primary)', fontWeight: 'bold', marginLeft: '1rem', fontSize: '1rem' }}>熱狂的なライブを求める方へ</span></p>
                                    </div>
                                </div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: '2rem' }}>
                                    <div className="feature-icon" style={{ margin: 0, fontSize: '2.5rem' }}>🎙️</div>
                                    <div>
                                        <h3 className="font-accent" style={{ color: 'var(--text-sub)', marginBottom: '0.25rem', fontSize: '0.875rem' }}>LINEUP</h3>
                                        <p className="font-display" style={{ fontSize: '1.25rem', color: '#fff' }}>本気の表現者たち <span style={{ color: 'var(--primary)', fontWeight: 'bold', marginLeft: '1rem', fontSize: '1rem' }}>4〜5組 ＋ 著名MC</span></p>
                                    </div>
                                </div>
                            </div>"""

    content = content.replace(old_overview_cards, new_overview_card)

    # 3. STAGE CONTENTS -> CONTENTS
    content = content.replace("""<h2 className="section-title font-display text-primary-gradient">STAGE CONTENTS</h2>""", """<h2 className="section-title font-display text-primary-gradient">CONTENTS</h2>""")

    # 4. OSHI-BALL SYSTEM -> BALL SYSTEM
    content = content.replace("""<h2 className="section-title font-display text-gradient">OSHI-BALL SYSTEM</h2>""", """<h2 className="section-title font-display text-gradient">BALL SYSTEM</h2>""")

    # 5. Restore Oshi Items
    oshi_items_react = """            const oshiItems = [
                { name: "ピンポン", price: "100円", effect: "挨拶代わりの一投。" },
                { name: "カラーボール", price: "300円", effect: "応援の意思表示。" },
                { name: "ビーチボール", price: "1,500円", effect: "ステージを彩る。演者の視界に確実に入る。" },
                { name: "ビーチボール（大）", price: "3,000円", effect: "目立つ。転換時の回収で存在感を発揮。" },
                { name: "ピンポンバズーカ", price: "5,000円", effect: "ステージへ向けて射出。一気に会場を沸かせる。" },
                { name: "バランスボール", price: "10,000円", effect: "巨大な愛。演者が抱えるほどの大きさ。" },
                { name: "バランスボール（銀）", price: "30,000円", effect: "会場ライティングが変化。VIP演出発動。" },
                { name: "バランスボール（金）", price: "50,000円", effect: "特効＋会場BGMが豪華に変化。" }
            ];"""
            
    # Inject oshiItems and news variables into App React scope
    content = content.replace("""const applicationUrl = "https://docs.google.com/forms/d/e/1FAIpQLSeQCrP79MVOQz9JqYtHNsCCrRSKIbBkrTfLA3MmzWGqSacIxQ/viewform?usp=header";""", f"""const applicationUrl = "https://docs.google.com/forms/d/e/1FAIpQLSeQCrP79MVOQz9JqYtHNsCCrRSKIbBkrTfLA3MmzWGqSacIxQ/viewform?usp=header";

{oshi_items_react}

            const news = [
                {{ date: "2026.XX.XX", title: "出演クリエイター急募！", description: "「それだけでは食っていけないクリエイター祭り2026」の参加者を募集開始いたしました。本気の30分ステージを創り上げてくれるクリエイターを募集しています！" }},
                {{ date: "2026.XX.XX", title: "企画始動", description: "普段の動画スタイルとは一線を画す「本気の一面」をライブでお届けするイベント企画がスタートしました！" }}
            ];
""")

    old_table_body = """                                    <tbody>
                                        <tr className="pricing-row">
                                            <td style={{ fontWeight: 'bold', color: '#fff', display: 'flex', alignItems: 'center', gap: '1rem' }}>
                                                <span style={{ width: '10px', height: '10px', background: '#ccc', borderRadius: '50%', display: 'inline-block' }}></span>
                                                ノーマルボール
                                            </td>
                                            <td className="font-display" style={{ color: 'var(--primary)', fontSize: '1.25rem' }}>¥1,000</td>
                                            <td style={{ color: 'var(--text-sub)' }}>通常の投げ込み用ボール。基本の応援アイテムです。</td>
                                        </tr>
                                        <tr className="pricing-row">
                                            <td style={{ fontWeight: 'bold', color: '#fff', display: 'flex', alignItems: 'center', gap: '1rem' }}>
                                                <span style={{ width: '10px', height: '10px', background: 'var(--primary)', borderRadius: '50%', display: 'inline-block', boxShadow: '0 0 10px var(--primary-glow)' }}></span>
                                                光るカラーボール
                                            </td>
                                            <td className="font-display" style={{ color: 'var(--primary)', fontSize: '1.25rem' }}>¥5,000</td>
                                            <td style={{ color: 'var(--text-sub)' }}>クリエイターのイメージカラーで発光。サイン入りお礼カードを後日送付。</td>
                                        </tr>
                                        <tr className="pricing-row">
                                            <td style={{ fontWeight: 'bold', color: '#fff', display: 'flex', alignItems: 'center', gap: '1rem' }}>
                                                <span style={{ width: '16px', height: '16px', background: 'linear-gradient(135deg, #FFF76A 0%, #FF8C00 100%)', borderRadius: '50%', display: 'inline-block', boxShadow: '0 0 15px var(--primary-glow)' }}></span>
                                                特大バルーン
                                            </td>
                                            <td className="font-display" style={{ color: 'var(--primary)', fontSize: '1.25rem' }}>¥50,000</td>
                                            <td style={{ color: 'var(--text-sub)' }}>投入時、会場の照明・音響が専用の特別演出に変化。終演後の楽屋挨拶権付き。</td>
                                        </tr>
                                    </tbody>"""

    new_table_body = """                                    <tbody>
                                        {oshiItems.map((item, idx) => (
                                            <tr key={idx} className="pricing-row">
                                                <td style={{ fontWeight: 'bold', color: '#fff', display: 'flex', alignItems: 'center', gap: '1rem' }}>
                                                    <span style={{ width: '10px', height: '10px', background: idx > 4 ? 'linear-gradient(135deg, #FFF76A 0%, #FF8C00 100%)' : 'var(--primary)', borderRadius: '50%', display: 'inline-block', boxShadow: '0 0 10px var(--primary-glow)' }}></span>
                                                    {item.name}
                                                </td>
                                                <td className="font-display" style={{ color: 'var(--primary)', fontSize: '1.25rem' }}>{item.price}</td>
                                                <td style={{ color: 'var(--text-sub)' }}>{item.effect}</td>
                                            </tr>
                                        ))}
                                    </tbody>"""
                                    
    content = content.replace(old_table_body, new_table_body)

    # 6. Add Impact, MC, News, Requirements sections
    # They will be injected right before the CTA & FOOTER section
    cta_marker = """                    {/* CTA & FOOTER */}"""

    missing_sections = """                    {/* IMPACT */}
                    <section id="impact" className="section-padding" style={{ position: 'relative' }}>
                        <div className="container">
                            <div className="section-header">
                                <h2 className="section-title font-display text-gradient">IMPACT</h2>
                                <div className="section-line"></div>
                                <p style={{ color: 'var(--text-sub)', maxWidth: '600px', margin: '2rem auto 0', fontSize: '1.1rem' }}>単なる一過性のイベントではなく、クリエイターの今後の活動を強力にバックアップします。</p>
                            </div>
                            <div className="grid-3">
                                <div className="glass-panel feature-card hover-lift text-center">
                                    <h4 style={{ color: '#fff', fontSize: '1.25rem', marginBottom: '1rem', fontWeight: 700 }}>ファンとの深い交流</h4>
                                    <p style={{ color: 'var(--text-sub)' }}>画面越しではない濃密なコミュニケーションにより、コアなファンベースを固めます。</p>
                                </div>
                                <div className="glass-panel feature-card hover-lift text-center">
                                    <h4 style={{ color: '#fff', fontSize: '1.25rem', marginBottom: '1rem', fontWeight: 700 }}>新たな収益への道</h4>
                                    <p style={{ color: 'var(--text-sub)' }}>リアルと配信の両軸から集まる支援により、次なる企画のための軍資金を確保できます。</p>
                                </div>
                                <div className="glass-panel feature-card hover-lift text-center">
                                    <h4 style={{ color: '#fff', fontSize: '1.25rem', marginBottom: '1rem', fontWeight: 700 }}>プレミアム映像素材</h4>
                                    <p style={{ color: 'var(--text-sub)' }}>当日の舞台裏や共演シーンなど、自身のチャンネルで活用できる貴重な映像コンテンツが得られます。</p>
                                </div>
                            </div>
                        </div>
                    </section>
                    
                    {/* MC LIST */}
                    <section id="mc" className="section-padding" style={{ background: 'var(--bg-accent)' }}>
                        <div className="container text-center">
                            <div className="section-header">
                                <h2 className="section-title font-display text-primary-gradient">MC GUEST</h2>
                                <div className="section-line"></div>
                                <p style={{ color: 'var(--text-sub)', maxWidth: '600px', margin: '2rem auto 0', fontSize: '1.1rem' }}>予算50万円想定。この人のライブから入るのもあり</p>
                            </div>
                            <div className="glass-panel" style={{ display: 'inline-block', padding: '3rem 5rem' }}>
                                <h3 className="font-display" style={{ fontSize: '2.5rem', color: '#fff' }}>ジャンポケ斎藤</h3>
                            </div>
                        </div>
                    </section>

                    {/* NEWS */}
                    <section id="news" className="section-padding">
                        <div className="container">
                            <div className="section-header">
                                <h2 className="section-title font-display text-gradient">NEWS</h2>
                                <div className="section-line"></div>
                            </div>
                            <div className="glass-panel" style={{ padding: '3rem' }}>
                                <div className="space-y-8" style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
                                    {news.map((item, index) => (
                                        <div key={index} style={{ borderBottom: index < news.length - 1 ? '1px solid rgba(255,255,255,0.1)' : 'none', paddingBottom: index < news.length - 1 ? '2rem' : '0' }}>
                                            <h3 className="mb-2 font-bold font-display" style={{ color: 'var(--primary)', fontSize: '1.25rem', marginBottom: '0.5rem' }}>{item.date}　{item.title}</h3>
                                            <p style={{ color: 'var(--text-main)' }}>{item.description}</p>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </div>
                    </section>

                    {/* REQUIREMENTS */}
                    <section id="requirements" className="section-padding" style={{ background: 'var(--bg-accent)' }}>
                        <div className="container">
                            <div className="section-header">
                                <h2 className="section-title font-display text-primary-gradient">REQUIREMENTS</h2>
                                <div className="section-line"></div>
                                <p style={{ color: 'var(--text-sub)', maxWidth: '600px', margin: '2rem auto 0', fontSize: '1.1rem' }}>参加要項</p>
                            </div>
                            
                            <div className="glass-panel hover-lift" style={{ padding: '3rem', marginBottom: '2rem' }}>
                                <h3 className="font-bold mb-2" style={{ color: 'var(--primary)', fontSize: '1.25rem' }}>参加資格</h3>
                                <p style={{ color: 'var(--text-sub)' }}>演奏やパフォーマンス、そしてファンとのコミュニケーションをリアルで「本気で」したい配信者・クリエイター</p>
                            </div>
                            
                            <div className="grid-2">
                                <div className="glass-panel hover-lift" style={{ padding: '3rem' }}>
                                    <h3 className="font-bold mb-4" style={{ color: 'var(--primary)', fontSize: '1.25rem' }}>協力事項</h3>
                                    <ul style={{ color: 'var(--text-sub)', paddingLeft: '1.5rem', lineHeight: '2' }}>
                                        <li>イベント会議への参加</li>
                                        <li>30分の自身のステージの準備・練習</li>
                                        <li>動画等での告知協力（告知・練習風景などの配信）</li>
                                        <li>イベントや準備期間の映像の使用許可（内容確認可）</li>
                                        <li>アフターパーティー・VIPへの会席参加（可能であれば）</li>
                                    </ul>
                                </div>
                                <div className="glass-panel hover-lift" style={{ padding: '3rem' }}>
                                    <h3 className="font-bold mb-4" style={{ color: 'var(--primary)', fontSize: '1.25rem' }}>主催協力事項</h3>
                                    <ul style={{ color: 'var(--text-sub)', paddingLeft: '1.5rem', lineHeight: '2', marginBottom: '2rem' }}>
                                        <li>会場・機材・必要サポートスタッフの手配</li>
                                        <li>告知用MV・Webサイトの作成</li>
                                        <li>演出・進行のサポート</li>
                                    </ul>
                                    <div style={{ borderTop: '1px solid rgba(255,255,255,0.1)', paddingTop: '2rem' }}>
                                        <h3 className="font-bold mb-2" style={{ color: 'var(--primary)', fontSize: '1.25rem' }}>収益分配</h3>
                                        <p style={{ color: 'var(--text-sub)' }}>イベント収益および投げ銭（推しボール）による収益は、規定の割合で還元いたします。</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

"""
    content = content.replace(cta_marker, missing_sections + cta_marker)

    with open('jam2.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_jam2()
