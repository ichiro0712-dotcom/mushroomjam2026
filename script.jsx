
            const { useState, useEffect } = Reac                const App =             {
            const [scrolled, setScrolled] = use            false);
            const [mobileMenuOpen, setMobileMenuOpen]            State(false);
            const applicationUrl = "https://docs.google.com/forms/d/e/1FAIpQLSeQCrP79MVOQz9JqYtHNsCCrRSKIbBkrTfLA3MmzWGqSacI            wform?usp=header";                      const oshiItems = [
                { name: "ピンポン", pri                円", effect: "挨拶代わりの一投。" },
                { name                ル", price: "300円", effect: "応援の意思表示。" },
                { name:             ル", price            00円", effect: "ステージ                界に確実に入る。" },
                { name: "ビ                ", price: "3,000円", effect: "目立つ。転換時の回収で存                },
                { name: "ピンポンバズー                e: "5,000円", effect: "ステージへ向けて射出。一気に会場を沸かせ                               { name: "バランスボール", price: "1            ", e             "巨大な愛。演者                きさ。" },
                { name                    （銀）", price: "3                    ffect: "会場ライティングが変化。VIP演出発動。" },
                { name: "バランスボール（金）", price: "50,000円", effect: "特効＋会場BGMが豪華に変化。" }
            ];

                              news = [
                { date: "2026.X                            "出演クリエイター急募！", description: "「それだけでは食っていけないクリエイター祭り2026」の参加者を募集開始いたしました。本気の30分ステ                                ーを募集しています！" },
                { date: "2026.XX.XX", title: "企画始動", description: "普段の動画スタイルとは一線を画す「本気の一                            ント企画がスタ                                        useEffect(() => {                                 const handleScroll = ()                                    ndow.scrollY > 50);
                window.addEventListener('scroll', handleScroll);
                                retu                            w.remov(                            leScroll);
            }, []);

            const navLinks = [
                { name: 'CONCEPT', href: '#concept' },
                                    me: 'OVERVIEW', href: '#overview' },
                { name: 'CONTENTS', href: '#stage' },
                { name: 'BALL SYSTEM', href: '#oshiball' },
                { name:                                      '#tim                                                                     ret                             assName="app-wrapper">
                                  {/* Ha                                            <header ca                                der ${scrolled ? 'shadow-lg' : ''}`} style={{ background: scrolled ? 'rgba(5,5,5,0.95)' : 'rgba(5,5,5,0.5)                                              <div className="container nav-content                                                              di                            ont-displa                        fontSiz                        , fontWeight: 900 }}>
                                            <span cl                            primary-gradient">CREATOR FES</span> <span className="text-gray-500">2026</span>
                                            </div>

                                                   className="nav-links">
                                {navLinks.map(link => (
                                    <a key={link.name} href={link.href} className="nav-link font-accent">{                                                                                        
                                                                                                <div className="hidden lg:block" style={{ display: 'none' /* hidden on mobile, handle via media query conceptually */ }}>
                                                                    onUrl} target="_                                ener                             assName                        e"                     isplay: 'in                    , padding: '0.5rem 1.                    tSize: '0.875rem' }}>
                                                ENTRY
                                            </a>
                            </d                                             {/* Mobile menu button */}                                           <button
                                                        "lg:hidden"
                                                             ground: 'transparent', border: 'none', color: 'white', fontSize:                                : 'block' }}
                                onClick={() => setMo                                bileMenuOpen)}
                            >
                                ≡
                            </b                                                              iv>
                        {/                                opdown */}
                                                      en && (
                                                 yle={                            '#111', padding: '1rem 2rem', border                                id #333' }}>
                                {navLinks.map(link => (
                                                         key={link                                k.hre                             => set                        en(fals                    {{ display:                     adding: '1rem 0', color: 'whi                    ecoration: 'none', fontWeight: 'bold' }}>
                                        {l                                                                                                             ))}
                                                <a href={applicationUrl} target="_blank" rel="noopener noreferrer" style={{ di                                padding: '1rem 0', color: '#FFF76A',                             : 'none                                                                                       &rarr;
                                </a>
                            </div                                            )}
                    </header                                         {/* Hero Section */}
                    <section id="home                                    >
                        <div className="hero-bg"></div>
                        <div className="hero-particl                                                     <div className="hero-con                                        ">
                            <div className="badge">GUEST CREATORS WANTED</div>
                            <h1 className="hero-title font-display">
                                                                             ={{ diso                                れだけでは</span>
                                <span style={{ display: 'block',                                     っていけない</span>
                                                             Name="text-primary-gradient" style={{ display: 'block', mar                                    }>クリエイター祭り2026</span>
                            </h1>
                            <p className="hero-subtitle">                                                   画面の向こう側の「本気」を、リアルな空間で解き放て。                                                           ファンと創り上げる、一夜限りのプレミアムラ イブステー ジ。
                                                </p>
                            <div style={{ marginTop: '2rem' }}>
                                                     href=                                 target                            "noopen                        r" clas                    -super">
                                                            はこちら
                                </a>
                            </div>
                                          
                    </secti                                       {/* BACKGROUND / CONCE                                           <section id="concept" className="section-padding" style={{ positio                                >
                        <div classN                            ">
                                 className="section-header                                ">
                                <h2 className="section-title fo                                    imary-gradient">CONCEPT</h2>
                                                  <div className="section-line"></div>
                            </div>

                            <                                    ss-panel feature-card hover-lift animate-fade-up delay-1" style={{ maxWidth: '900px', m                                    >
                                <div className="feature-icon">🔥</div>
                                                               featurel                                                                <h4 style={{ color: '#fff', fontSi                                    ginBottom: '1rem', fontWeight: 700 }}>数                                    視化</h4>
                                <p style={{ color: 'var(--text-sub)', marginBottom: '1.5rem' }}>
                                                      YouTubeというプラットフォームで確かなコミュニティを築き上げてきた表現者たち。しかし、画面の中だけでは伝えきれない表現衝動や、まだ見ぬポテンシ ャルが彼らには眠っています                                    ーの「本気のパフォーマンス」をリアルな会場で解き放ち、ファンと共に新しい伝説を創る場所が必要です。
                                </p>
                                                <p                                 ' }}>
                                    普段の動画スタイルとは一線を画す「本気の一面」を                                    >
                                    クリ                                    有し、「リアル投げ銭（ボール）」という形で目に見える愛を届け合うことで、これまでにない深い絆を構築する「日本一距離が近い」プレミアムイベントです。
                                                                                   </div>
                        </div>
                    </section                                         {/* OVERVIEW */}
                    <section id="overview" className="section-padding" sty                                : 'var(                            }}>
                                                      ssName="cont                                                               assName="section-header">
                                                className="section-title fo                            t-gradient">OVERVIEW</h2>
                                                <div className="section-line"></div>
                            </div>

                                            <div className="glass-panel                             over-lia                            ', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '2re                                                                                   { display: 'flex', alignItems: 'center', gap: '2rem', borderBottom: '1px solid rgba(255,255,255,0.1)                                    '2rem' }}>
                                    <div className="feature-icon" style={{ margin: 0, fontSize: '2.5rem' }}>📅</div>
                                        >
                                                                             nt-accent" style={{ color: 'var(--text-sub)', marginBottom: '0.25rem', fontSize: '0                                        IME</h3>
                                        <p className="font-display" style={{ fontSize: '1                                        f' }}>2026年 某日 <span style={{ color: 'var(--primary)', fontWeight: 'bold', margi                                            e: '1rem' }}>19:30 開場 / 23:30 終了</span></p>
                                                          </div>
                                                                                                             l                                    tems: 'center', gap: '2re                                        px solid rgba(255,255,255,0.                                            rem' }}>
                                    <div className="feat                                            gin: 0, fontSize: '2.5rem' }}>🎯</div>
                                    <div>
                                                              <h3 className="font-accent" style={{ color: 'var(--text-sub)', marginBotto                                        ze: '0.                                        DIENCE</h3>
                                                              <p className="font-display" style={{ fontSize: '1.25rem', color                                            アファン層 <span style={{ color: 'var(--primary)', fontWeight: 'bold', marginLeft: '1rem',                                            狂的なライブを求める方へ</span></p>
                                    </div>
                                                                                                                    style={{ display: 'flex', a                                            ap: '2rem' }}>
                                    <div className=                                            { margin: 0, fontSize: '2.5rem' }}>🎙️</div>
                                    <div                                                                <h3 className="font-accent" style={{ color: 'var(--text-sub)', margin                                        ontSize                                    NEUP</h                                                                           <p className                                style={{ fontSize: '1.25rem', color: '#fff' }}>本気の表現者たち <span style={{ color: 'var(--primary)', fontWeight: 'bold', marginLeft: '1rem',                                     }>4〜5組 ＋ 著名MC</span></p>
                                    </div>
                                </div>
                                                               v>
                    </section>

                    {/* STAGE & COLLAB                                             <section id="stage" className="section-padding">
                        <div className="container">
                            <div className="section-header">
                                                    <h2 className="section-title font-display text-primary-gradient">CONTENTS</h2>
                                                    <div className="section-line"></div>
                            </div>

                                                  <div style={{ display: 'flex', flexD                                        gap:                                            {                                                                    <div className="glass-panel" style={{                                         ition: 'relative', overflow: 'hidden' }}>
                                    <d                                            'absolute', right: '-5%', top: '-20%', fontSize: '20re                                            nterEvents: 'none' }}>🎤</div>

                                    <div style={{ margi                                                                                                    <span className="badge" style={{ marginBottom: '1rem' }}>MAIN STAGE                                                                              <h3 className="font-disp                                            : '2.5rem', marginBottom: '1rem' }}>本気のメインステージ</h3>
                                                                             : 'var(                                        ze: '1.1rem', maxWidth: '800px' }}>
                                                                                        のためだけに準備された本気のパフォーマンス。
                                                                          的な練習を積み重ねたクリエイティビティをステージで爆発させます。
                                        </p>
                                                                                                                        <div className="grid-3">
                                                                           e="stage-box">
                                                                                    Size: '2rem', marginBottom: '1rem' }}>🎸</div>
                                                                                  t-bold                                     tyle={{                                em' }}>                                                                                            <p sty                    r: 'var(--text-sub                    ze: '0.9rem' }}>画面越しではなく、直接心に響かせる魂の生演奏。</p>
                                        </                                                                                sName="stage-box">
                                                            <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>🎭</div>
                                                            <h4 class                                text-white mb-2" style={{ fontSize: '1.2rem' }}>演劇・コント</h4>
                                                                               : 'var(--text-sub)', fo ntS                                    底的に練り上げられた脚本による、新しいキャラクターの開拓。</p>                                                                       </                                                           <div className="stage-box">                                                             <div style={{ fontSize: '2rem',                                    em' }}>🗣️</div>
                                            <h4 className="font-bold text-white mb-2" style={{ fontSize: '1.2rem' }}>トークライブ</h4>
                                            <p style={{ color: 'var(--text-sub)', fontSize: '0.9rem' }}>編集の壁を取り払                                    p>
                                        </div>
                                    </div>
                                                     iv>

                                {/*                                                                <div className="glass-panel" style={{ padding: '4rem', position:                                     ow: '                                und: 'r                                .4)' }}>
                                    <div style={{ p                                    ', left: '-5%', bottom: '-20%', fontSize: '20rem', opacity: 0.03, pointerEvents: 'none' }}>🤝</div>

                                    <div style={{ marginBottom: '3rem', position: 'relative', zIndex: 10 }}>
                                        <span cla                                    le={{ marginBottom: '1rem', borderColor: 'rgba(255,255,255,0.3)', color: '#fff', background: 'rgba(255,255,255                                    15min)</span>
                                                                   ssName="font-display" style={{ fontSize: '2.5rem', marginBottom: '1rem'                                    
                                                                       p style=                            (--text-sub)', fontSize: '1.1rem', maxWidth: '800px' }}>
                                                            出演クリエイター達                                    ぐ特別な交流コー                                                                                         >
                                                          </div>

                                                          <div className="gr                                        ion: '                                     10 }}>
                                                                                     yle={{ borderLeft: '3px solid                                            ingLeft: '1.5rem' }}>
                                            <h4 className="text-white font-bold m                                                                                     <p style={{ color: 'var(--text-sub)', fontSize: '0.85rem' }}>熱烈な応援を送ったファンを指名し直接対話。</p                                                                                                                                                             <div style={{ borderLeft: '3px solid var(--primary)', paddingLeft: '1.5rem' }}>
                                                                  <h4 className="text-white font-bold mb-2">推しポイント客観評価</h4>
                                                                                        tyle={{ color: 'var(--text-su                                            m' }}>MCがプロ視点でまだバレていない魅力を深掘り。</p>
                                        </div>
                                                                      tyle={{ borderLeft: '3px solid var(--primary)', paddingLeft: '1.5rem' }}>
                                            <h4 className="text-white font-bold mb-2">公開案件化</h4>
                                                                                                         or: 'v                                            ize: '0.85rem' }}>企業関係者に対し次の一歩への情熱をピッチ。</p>
                                        </div>
                                                              <div style={{ borderLeft: '3px solid var(--primary)', paddingLeft: '1.                                                                                              <h4 className="text-w                                            イブ配信対決</h4>
                                            <p style={{ color: 'var(--text-sub)', fontSize:                                                のchで同時生配信を実施。</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </di                                                /sectio                                              {/*                                                         <section id="oshiball" className="section-padding" style={{ background: '#0a0a0a' }}>
                                              <div className="container">
                            <div className="section-he                                                                                  lassName=                                ont-displ                            nt">BAL                        >
                                                         className="section                    iv>
                                <p style={{ color: 'var(--text-sub)', maxWidth: '600px', mar                        uto 0', fontSize: '1.1rem' }                                                     デジタルの「スー                                />
                                    会場全体の熱量を可視化し、一体となって盛り上がる究極の演出装置。
                                                </p>
                                                                                        Name="grid-2" style={{ marg                                 }}                                                    <div className="gla                                     padding: '2.5rem' }}>
                                    <div sty                                    ', height: '60px', background: 'var(--prim                                    s: '50%', display: 'flex', alignItems: 'cente                                    : 'center', fontSize: '1.5rem', marginBott                                    hadow: '0 0 20px var(--primary-glow)' }}>⚾</d                                                          <h3 className="font-                                    " style={{ fontSize: '1.5rem', marginBottom:                                     げ込む</h3>
                                                                     or: 'var(--text-sub)' }}>
                                                          ステージ演奏中・演技中、観客は購入した「推しボール」をステージに投げ込むことで直接応援が可                                気持ちを物理的に「投げつける」ことで熱量を                                                            </p>
                                                    </div>
                                <div className="glass-panel" style={{ padding: '2.5rem' }}>
                                                        <div style={{ width: '60px', height: '60px', background: 'var(--primary)', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSiz                                            tom: '1.5rem', boxShadow: '0 0 20px var(--primary-glow)' }}>💰</div>
                                                                               isplay text-white" style={{ fontSize: '1.5rem', marginBottom: '1rem'                                        
                                                                                  col                            t-sub)'                                                                                   入時は会場のライティングや音響がダイナミッ                    ボールの数・種類に応じて、クリエイターへ即座に収益が還元されます。
                                    </p>
                                </div                                          </div>

                            <div className="glass-panel" style={{ overflowX: 'auto' }}>
                                <table classN                        -table">
                                    <thead>
                                                      <tr>
                                            <th>ITEM</th>
                                            <th>PRICE</th>
                                                          <th>EFFECTS / REWARDS</th>
                                        </tr>
                                                  </thead>
                                    <tbody>
                                                                   map((item,                                                                                           <tr c                    pricing-row">
                                                <td style={{ fontWeight: 'bold', color: '#fff',                        lex', alignItems: 'center',                             >
                                                    <span style={{ width: '10px', height: '10px', background: idx > 4                             ient(135deg, #FFF76A 0%, #FF8C00 100%)' : 'var(--primary)', borderRadius: '50%', display:                         k', box                     0 10px va                ary-glo            ></        >
                                                    {item.name}
                                             td>
                                                <td className="font-display" style={{ color: 'var(--primary)', fontSize: '1.25rem' }}>{item.price}</td>
                                                <td style={{ color: 'var(--text-sub)' }}>{item.effect}</td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </section>

                    {/* TIMETABLE */}
                    <section id="timetable" className="section-padding" style={{ background: 'var(--bg-accent)' }}>
                        <div className="container">
                            <div className="section-header">
                                <h2 className="section-title font-display text-primary-gradient">TIMETABLE</h2>
                                <div className="section-line"></div>
                            </div>

                            <div className="timeline">
                                {[
                                    { time: "19:30", action: "OPEN" },
                                    { time: "20:00", action: "オープニングアクト・企画説明（20分）", highlight: true },
                                    { time: "20:20", action: "第1ステージ（30分）" },
                                    { time: "20:50", action: "転換＆コラボトーク（15分）" },
                                    { time: "21:05", action: "第2ステージ（30分）" },
                                    { time: "21:35", action: "転換＆コラボトーク（15分）" },
                                    { time: "21:50", action: "第3ステージ（30分）" },
                                    { time: "22:20", action: "転換＆コラボトーク（15分）" },
                                    { time: "22:35", action: "第4ステージ（30分）" },
                                    { time: "23:05", action: "フィナーレ・物販交流" },
                                    { time: "23:30", action: "CLOSE", highlight: true }
                                ].map((item, i) => (
                                    <div className="timeline-item" key={i}>
                                        <div className="timeline-dot" style={item.highlight ? { background: 'var(--primary)' } : {}}></div>
                                        <div className="glass-panel" style={{ padding: '1.5rem', display: 'flex', alignItems: 'center', gap: '1rem', background: item.highlight ? 'rgba(255,215,0,0.1)' : 'var(--glass-bg)' }}>
                                            <div className="font-display" style={{ fontSize: '1.5rem', color: 'var(--primary)' }}>{item.time}</div>
                                            <div style={{ color: '#fff', fontWeight: 600 }}>{item.action}</div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </section>

                    {/* IMPACT */}
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

                    {/* CTA & FOOTER */}
                    <section className="section-padding" style={{ textAlign: 'center', position: 'relative', overflow: 'hidden' }}>
                        <div style={{ position: 'absolute', inset: 0, background: 'radial-gradient(circle at center, rgba(255, 215, 0, 0.1) 0%, transparent 60%)', zIndex: 0 }}></div>
                        <div className="container" style={{ position: 'relative', zIndex: 10 }}>
                            <h2 className="font-display" style={{ fontSize: 'clamp(2rem, 5vw, 3.5rem)', marginBottom: '1rem' }}>ARE YOU READY TO STAGE?</h2>
                            <p style={{ color: 'var(--text-sub)', marginBottom: '3rem', fontSize: '1.2rem' }}>本気の参加をお待ちしています。あなたの情熱を、ここで証明してください。</p>
                            <a href={applicationUrl} target="_blank" rel="noopener noreferrer" className="btn-super">
                                出演応募エントリー
                            </a>
                        </div>
                    </section>

                    <footer style={{ background: '#000', padding: '3rem 0', textAlign: 'center', borderTop: '1px solid #222' }}>
                        <div className="container">
                            <div className="font-display text-gradient" style={{ fontSize: '1.5rem', marginBottom: '1rem' }}>CREATOR FES 2026</div>
                            <p style={{ color: '#555', fontSize: '0.875rem' }}>© 2026 それだけでは食っていけないクリエイター祭り 実行委員会</p>
                        </div>
                    </footer>
                </div>
            );
        }

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    