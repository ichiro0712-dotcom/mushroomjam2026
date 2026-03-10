import re
import os

with open("jam.html", "r", encoding="utf-8") as f:
    jam_html = f.read()

# Extract fonts/scripts from jam.html to construct the head
head_base = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>それだけでは食っていけないクリエイター祭り2026</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&family=Noto+Sans+JP:wght@400;500;700;900&family=Oswald:wght@700&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">

    <script src="https://unpkg.com/react@17/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
"""

css_base = """    <style>
        :root {
            --bg-color: #050505;
            --bg-accent: #111111;
            --primary: #FFF76A;
            --primary-glow: rgba(255, 247, 106, 0.4);
            --text-main: #FFFFFF;
            --text-sub: #A0A0A0;
            --glass-bg: rgba(20, 20, 20, 0.6);
            --glass-border: rgba(255, 255, 255, 0.08);
            
            --font-display: 'Montserrat', 'Noto Sans JP', sans-serif;
            --font-body: 'Noto Sans JP', sans-serif;
            --font-accent: 'Oswald', sans-serif;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: var(--font-body);
            background-color: var(--bg-color);
            color: var(--text-main);
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* Typography Utilities */
        .font-display {
            font-family: var(--font-display);
            font-weight: 900;
            letter-spacing: -0.02em;
        }

        .font-accent {
            font-family: var(--font-accent);
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }

        .text-gradient {
            background: linear-gradient(135deg, #FFFFFF 0%, #888888 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .text-primary-gradient {
            background: linear-gradient(135deg, #FFF76A 0%, #FF8C00 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* Premium UI Components */
        .glass-panel {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 24px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        }

        .hover-lift {
            transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease, border-color 0.4s ease;
        }

        .hover-lift:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.8), 0 0 20px var(--primary-glow);
            border-color: rgba(255, 215, 0, 0.3);
        }

        /* Buttons */
        .btn-super {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 1.25rem 3rem;
            background: linear-gradient(135deg, #FFF76A 0%, #FFB300 100%);
            color: #000;
            font-family: var(--font-display);
            font-size: 1.25rem;
            font-weight: 900;
            text-decoration: none;
            border-radius: 50px;
            border: none;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px var(--primary-glow);
        }

        .btn-super::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
            transition: left 0.5s ease;
        }

        .btn-super:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 30px var(--primary-glow);
        }

        .btn-super:hover::before {
            left: 100%;
        }

        .btn-outline {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.75rem 2rem;
            background: transparent;
            color: var(--primary);
            font-family: var(--font-display);
            font-weight: 700;
            text-decoration: none;
            border-radius: 50px;
            border: 2px solid var(--primary);
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .btn-outline:hover {
            background: var(--primary);
            color: #000;
            box-shadow: 0 0 15px var(--primary-glow);
        }

        /* Layout Utilities */
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .section-padding {
            padding: 8rem 0;
        }

        /* Nav */
        .nav-header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 100;
            background: rgba(5, 5, 5, 0.8);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--glass-border);
            transition: all 0.3s ease;
        }

        .nav-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 80px;
        }

        .nav-links {
            display: none;
            gap: 2rem;
        }

        @media (min-width: 1024px) {
            .nav-links {
                display: flex;
            }
        }

        .nav-link {
            color: var(--text-main);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 700;
            transition: color 0.2s ease;
            position: relative;
        }

        .nav-link:hover {
            color: var(--primary);
        }

        .nav-link::after {
            content: '';
            position: absolute;
            bottom: -4px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--primary);
            transition: width 0.3s ease;
        }

        .nav-link:hover::after {
            width: 100%;
        }

        /* Hero Section */
        .hero {
            position: relative;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding-top: 80px;
            overflow: hidden;
        }

        .hero-bg {
            position: absolute;
            inset: 0;
            z-index: 0;
            background: radial-gradient(circle at 50% 50%, #2a2a00 0%, var(--bg-color) 70%);
            opacity: 0.5;
        }

        .hero-particles {
            position: absolute;
            inset: 0;
            z-index: 1;
            background-image: radial-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px);
            background-size: 50px 50px;
            opacity: 0.3;
        }

        .hero-content {
            position: relative;
            z-index: 10;
            text-align: center;
            max-width: 900px;
            padding: 2rem;
        }

        .badge {
            display: inline-block;
            padding: 0.5rem 1.5rem;
            border-radius: 50px;
            border: 1px solid rgba(255, 215, 0, 0.3);
            background: rgba(255, 215, 0, 0.1);
            color: var(--primary);
            font-weight: 700;
            font-size: 0.875rem;
            letter-spacing: 0.1em;
            margin-bottom: 2rem;
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.1);
        }

        .hero-title {
            font-size: clamp(3rem, 8vw, 6.5rem);
            line-height: 1.1;
            margin-bottom: 1.5rem;
            text-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
        }

        .hero-subtitle {
            font-size: clamp(1.1rem, 2.5vw, 1.5rem);
            color: var(--text-sub);
            margin-bottom: 4rem;
            font-weight: 500;
        }

        /* Section Headers */
        .section-header {
            text-align: center;
            margin-bottom: 5rem;
        }

        .section-title {
            font-size: clamp(2.5rem, 5vw, 4rem);
            margin-bottom: 1rem;
        }

        .section-line {
            width: 80px;
            height: 4px;
            background: var(--primary);
            margin: 0 auto;
            border-radius: 2px;
            box-shadow: 0 0 15px var(--primary-glow);
        }

        /* Grids */
        .grid-2 {
            display: grid;
            grid-template-columns: 1fr;
            gap: 2rem;
        }

        .grid-3 {
            display: grid;
            grid-template-columns: 1fr;
            gap: 2rem;
        }

        .grid-4 {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }

        @media (min-width: 768px) {
            .grid-2 {
                grid-template-columns: repeat(2, 1fr);
                gap: 3rem;
            }

            .grid-3 {
                grid-template-columns: repeat(3, 1fr);
            }

            .grid-4 {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (min-width: 1024px) {
            .grid-4 {
                grid-template-columns: repeat(4, 1fr);
            }
        }

        /* Cards */
        .feature-card {
            padding: 3rem 2rem;
            position: relative;
            overflow: hidden;
        }

        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1.5rem;
            display: inline-block;
            filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.2));
        }

        .feature-title {
            font-size: 1.5rem;
            color: var(--primary);
            margin-bottom: 1rem;
        }

        /* Stage specialized cards */
        .stage-box {
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 1.5rem;
            transition: all 0.3s ease;
        }

        .stage-box:hover {
            background: rgba(255, 215, 0, 0.05);
            border-color: rgba(255, 215, 0, 0.3);
        }

        /* Pricing/Table */
        .pricing-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
        }

        .pricing-table th,
        .pricing-table td {
            padding: 1.5rem;
            border-bottom: 1px solid var(--glass-border);
            text-align: left;
        }

        .pricing-table th {
            font-family: var(--font-accent);
            color: var(--text-sub);
            font-size: 0.875rem;
            letter-spacing: 0.1em;
        }

        .pricing-row {
            transition: background 0.2s;
        }

        .pricing-row:hover {
            background: rgba(255, 255, 255, 0.03);
        }

        /* Timeline */
        .timeline {
            position: relative;
            max-width: 800px;
            margin: 0 auto;
        }

        .timeline::before {
            content: '';
            position: absolute;
            top: 0;
            bottom: 0;
            left: 24px;
            width: 2px;
            background: var(--glass-border);
        }

        @media (min-width: 768px) {
            .timeline::before {
                left: 50%;
                transform: translateX(-50%);
            }
        }

        .timeline-item {
            position: relative;
            margin-bottom: 3rem;
            padding-left: 70px;
        }

        @media (min-width: 768px) {
            .timeline-item {
                padding-left: 0;
                width: 50%;
            }

            .timeline-item:nth-child(odd) {
                padding-right: 50px;
                text-align: right;
            }

            .timeline-item:nth-child(even) {
                left: 50%;
                padding-left: 50px;
            }
        }

        .timeline-dot {
            position: absolute;
            left: 16px;
            top: 20px;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: var(--bg-color);
            border: 4px solid var(--primary);
            box-shadow: 0 0 15px var(--primary-glow);
            z-index: 2;
        }

        @media (min-width: 768px) {
            .timeline-item:nth-child(odd) .timeline-dot {
                left: auto;
                right: -9px;
            }

            .timeline-item:nth-child(even) .timeline-dot {
                left: -9px;
            }
        }

        /* Animations */
        @keyframes fadeUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .animate-fade-up {
            animation: fadeUp 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        .delay-1 { animation-delay: 0.2s; }
        .delay-2 { animation-delay: 0.4s; }
    </style>
</head>
<body>
    <div id="root"></div>
"""

react_script = """    <script type="text/babel">
        const { useState, useEffect } = React;

        const App = () => {
            const [scrolled, setScrolled] = useState(false);
            const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
            const applicationUrl = "https://docs.google.com/forms/d/e/1FAIpQLSeQCrP79MVOQz9JqYtHNsCCrRSKIbBkrTfLA3MmzWGqSacIxQ/viewform?usp=header";

            const oshiItems = [
                { name: "ピンポン", price: "100円", effect: "挨拶代わりの一投。" },
                { name: "カラーボール", price: "300円", effect: "応援の意思表示。" },
                { name: "ビーチボール", price: "1,500円", effect: "ステージを彩る。演者の視界に確実に入る。" },
                { name: "ビーチボール（大）", price: "3,000円", effect: "目立つ。転換時の回収で存在感を発揮。" },
                { name: "ピンポンバズーカ", price: "5,000円", effect: "ステージへ向けて射出。一気に会場を沸かせる。" },
                { name: "バランスボール", price: "10,000円", effect: "巨大な愛。演者が抱えるほどの大きさ。" },
                { name: "バランスボール（銀）", price: "30,000円", effect: "会場ライティングが変化。VIP演出発動。" },
                { name: "バランスボール（金）", price: "50,000円", effect: "特効＋会場BGMが豪華に変化。" }
            ];

            const news = [
                { date: "2026.XX.XX", title: "出演クリエイター急募！", description: "「それだけでは食っていけないクリエイター祭り2026」の参加者を募集開始いたしました。本気の30分ステージを創り上げてくれるクリエイターを募集しています！" },
                { date: "2026.XX.XX", title: "企画始動", description: "普段の動画スタイルとは一線を画す「本気の一面」をライブでお届けするイベント企画がスタートしました！" }
            ];

            useEffect(() => {
                const handleScroll = () => setScrolled(window.scrollY > 50);
                window.addEventListener('scroll', handleScroll);
                return () => window.removeEventListener('scroll', handleScroll);
            }, []);

            const navLinks = [
                { name: 'VISION', href: '#vision' },
                { name: 'OVERVIEW', href: '#overview' },
                { name: 'CONTENTS', href: '#stage' },
                { name: 'BALL SYSTEM', href: '#oshiball' },
                { name: 'TIMETABLE', href: '#timetable' },
            ];

            return (
                <div className="app-wrapper">
                    {/* Header */}
                    <header className={`nav-header ${scrolled ? 'shadow-lg' : ''}`} style={{ background: scrolled ? 'rgba(5,5,5,0.95)' : 'rgba(5,5,5,0.5)' }}>
                        <div className="container nav-content">
                            <div className="font-display" style={{ fontSize: '1.25rem', fontWeight: 900 }}>
                                <span className="text-primary-gradient">CREATOR FES</span> <span className="text-gray-500">2026</span>
                            </div>

                            <nav className="nav-links">
                                {navLinks.map(link => (
                                    <a key={link.name} href={link.href} className="nav-link font-accent">{link.name}</a>
                                ))}
                            </nav>

                            <div className="hidden lg:block" style={{ display: 'none' /* hidden on mobile, handle via media query conceptually */ }}>
                                <a href={applicationUrl} target="_blank" rel="noopener noreferrer" className="btn-outline" style={{ display: 'inline-flex', padding: '0.5rem 1.5rem', fontSize: '0.875rem' }}>
                                    ENTRY
                                </a>
                            </div>

                            {/* Mobile menu button */}
                            <button
                                className="lg:hidden"
                                style={{ background: 'transparent', border: 'none', color: 'white', fontSize: '2rem', display: 'block' }}
                                onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
                            >
                                ≡
                            </button>
                        </div>
                        {/* Mobile Menu Dropdown */}
                        {mobileMenuOpen && (
                            <div style={{ background: '#111', padding: '1rem 2rem', borderBottom: '1px solid #333' }}>
                                {navLinks.map(link => (
                                    <a key={link.name} href={link.href} onClick={() => setMobileMenuOpen(false)} style={{ display: 'block', padding: '1rem 0', color: 'white', textDecoration: 'none', fontWeight: 'bold' }}>
                                        {link.name}
                                    </a>
                                ))}
                                <a href={applicationUrl} target="_blank" rel="noopener noreferrer" style={{ display: 'block', padding: '1rem 0', color: '#FFF76A', textDecoration: 'none', fontWeight: 'bold' }}>
                                    出演応募はこちら &rarr;
                                </a>
                            </div>
                        )}
                    </header>

                    {/* Hero Section */}
                    <section id="home" className="hero">
                        <div className="hero-bg"></div>
                        <div className="hero-particles"></div>
                        <div className="hero-content animate-fade-up">
                            <div className="badge">GUEST CREATORS WANTED</div>
                            <h1 className="hero-title font-display">
                                <span style={{ display: 'block', color: '#fff' }}>それだけでは</span>
                                <span style={{ display: 'block', color: '#fff' }}>食っていけない</span>
                                <span className="text-primary-gradient" style={{ display: 'block', marginTop: '0.5rem' }}>クリエイター祭り2026</span>
                            </h1>
                            <p className="hero-subtitle">
                                画面の向こう側の「本気」を、リアルな空間で解き放て。<br />
                                ファンと創り上げる、一夜限りのプレミアムライブステージ。
                            </p>
                            <div style={{ marginTop: '2rem' }}>
                                <a href={applicationUrl} target="_blank" rel="noopener noreferrer" className="btn-super">
                                    出演応募はこちら
                                </a>
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

                    {/* VISION */}
                    <section id="vision" className="section-padding" style={{ position: 'relative' }}>
                        <div className="container">
                            <div className="section-header animate-fade-up">
                                <h2 className="section-title font-display text-primary-gradient">VISION</h2>
                                <div className="section-line"></div>
                            </div>
                            
                            <div className="glass-panel feature-card hover-lift animate-fade-up delay-1" style={{ maxWidth: '900px', margin: '0 auto' }}>
                                <h4 style={{ color: '#fff', fontSize: '1.25rem', marginBottom: '1rem', fontWeight: 700 }}>数字の先にある「人間の熱量」と情熱の可視化</h4>
                                <p style={{ color: 'var(--text-sub)', marginBottom: '1.5rem' }}>
                                    YouTubeというプラットフォームで確かなコミュニティを築き上げてきた表現者たち。しかし、画面の中だけでは伝えきれない表現衝動や、まだ見ぬポテンシャルが彼らには眠っています。デジタルな繋がりを超え、クリエイターの「本気のパフォーマンス」をリアルな会場で解き放ち、ファンと共に新しい伝説を創る場所が必要です。
                                </p>
                                <h4 style={{ color: '#fff', fontSize: '1.25rem', marginBottom: '1rem', fontWeight: 700, marginTop: '2.5rem' }}>普段の動画スタイルとは一線を画す「本気の一面」を30分間のステージに凝縮。</h4>
                                <p style={{ color: 'var(--text-sub)' }}>
                                    クリエイターとファンが同じ空間で熱量を共有し、「リアル投げ銭（ボール）」という形で目に見える愛を届け合うことで、これまでにない深い絆を構築する「日本一距離が近い」プレミアムイベントです。
                                </p>
                            </div>
                        </div>
                    </section>

                    {/* OVERVIEW */}
                    <section id="overview" className="section-padding" style={{ background: 'var(--bg-accent)' }}>
                        <div className="container">
                            <div className="section-header">
                                <h2 className="section-title font-display text-gradient">OVERVIEW</h2>
                                <div className="section-line"></div>
                            </div>

                            <div className="glass-panel feature-card hover-lift" style={{ maxWidth: '900px', margin: '0 auto', display: 'flex', flexDirection: 'column', gap: '2rem' }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: '2rem', borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '2rem' }}>
                                    <div className="feature-icon" style={{ margin: 0, fontSize: '2.5rem' }}>📅</div>
                                    <div>
                                        <h3 className="font-accent" style={{ color: 'var(--text-sub)', marginBottom: '0.25rem', fontSize: '0.875rem' }}>DATE & TIME</h3>
                                        <p className="font-display" style={{ fontSize: '1.25rem', color: '#fff' }}>2026年 某日 <span style={{ color: 'var(--primary)', fontWeight: 'bold', marginLeft: '1rem', fontSize: '1rem' }}>19:30 開場 / 23:30 終了</span></p>
                                    </div>
                                </div>
                                <div style={{ display: 'flex', alignItems: 'center', gap: '2rem' }}>
                                    <div className="feature-icon" style={{ margin: 0, fontSize: '2.5rem' }}>🎙️</div>
                                    <div>
                                        <h3 className="font-accent" style={{ color: 'var(--text-sub)', marginBottom: '0.25rem', fontSize: '0.875rem' }}>LINEUP</h3>
                                        <p className="font-display" style={{ fontSize: '1.25rem', color: '#fff' }}>本気の表現者たち <span style={{ color: 'var(--primary)', fontWeight: 'bold', marginLeft: '1rem', fontSize: '1rem' }}>4〜5組 ＋ 著名MC</span></p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    {/* CONTENTS */}
                    <section id="stage" className="section-padding">
                        <div className="container">
                            <div className="section-header">
                                <h2 className="section-title font-display text-primary-gradient">CONTENTS</h2>
                                <div className="section-line"></div>
                            </div>

                            <div style={{ display: 'flex', flexDirection: 'column', gap: '4rem' }}>
                                {/* Main Stage */}
                                <div className="glass-panel" style={{ padding: '4rem', position: 'relative', overflow: 'hidden' }}>
                                    <div style={{ position: 'absolute', right: '-5%', top: '-20%', fontSize: '20rem', opacity: 0.03, pointerEvents: 'none' }}>🎤</div>

                                    <div style={{ marginBottom: '3rem' }}>
                                        <span className="badge" style={{ marginBottom: '1rem' }}>MAIN STAGE (30min)</span>
                                        <h3 className="font-display" style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>本気のクリエイターステージ</h3>
                                        <p style={{ color: 'var(--text-sub)', fontSize: '1.1rem', maxWidth: '800px' }}>
                                            「普段の動画とは違う一面」をテーマに、この日のためだけに準備された本気のパフォーマンス。
                                            1ヶ月前から圧倒的な練習を積み重ねたクリエイティビティをステージで爆発させます。
                                        </p>
                                    </div>

                                    <div className="grid-3">
                                        <div className="stage-box">
                                            <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>🎸</div>
                                            <h4 className="font-bold text-white mb-2" style={{ fontSize: '1.2rem' }}>音楽・バンド</h4>
                                            <p style={{ color: 'var(--text-sub)', fontSize: '0.9rem' }}>画面越しではなく、直接心に響かせる魂の生演奏。</p>
                                        </div>
                                        <div className="stage-box">
                                            <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>🎭</div>
                                            <h4 className="font-bold text-white mb-2" style={{ fontSize: '1.2rem' }}>演劇・コント</h4>
                                            <p style={{ color: 'var(--text-sub)', fontSize: '0.9rem' }}>徹底的に練り上げられた脚本による、新しいキャラクターの開拓。</p>
                                        </div>
                                        <div className="stage-box">
                                            <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>🗣️</div>
                                            <h4 className="font-bold text-white mb-2" style={{ fontSize: '1.2rem' }}>トークライブ</h4>
                                            <p style={{ color: 'var(--text-sub)', fontSize: '0.9rem' }}>編集の壁を取り払い、その瞬間の空気感で紡ぐ言葉。</p>
                                        </div>
                                    </div>
                                </div>

                                {/* Collab */}
                                <div className="glass-panel" style={{ padding: '4rem', position: 'relative', overflow: 'hidden', background: 'rgba(30, 25, 5, 0.4)' }}>
                                    <div style={{ position: 'absolute', left: '-5%', bottom: '-20%', fontSize: '20rem', opacity: 0.03, pointerEvents: 'none' }}>🤝</div>

                                    <div style={{ marginBottom: '3rem', position: 'relative', zIndex: 10 }}>
                                        <span className="badge" style={{ marginBottom: '1rem', borderColor: 'rgba(255,255,255,0.3)', color: '#fff', background: 'rgba(255,255,255,0.1)' }}>COLLAB (15min)</span>
                                        <h3 className="font-display" style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>サイドコンテンツ</h3>
                                        <p style={{ color: 'var(--text-sub)', fontSize: '1.1rem', maxWidth: '800px' }}>
                                            出演クリエイター達とMCによる、ステージの熱狂を引き継ぐ特別な交流コーナー。
                                        </p>
                                    </div>

                                    <div className="grid-4" style={{ position: 'relative', zIndex: 10 }}>
                                        <div style={{ borderLeft: '3px solid var(--primary)', paddingLeft: '1.5rem' }}>
                                            <h4 className="text-white font-bold mb-2">太客と話そう</h4>
                                            <p style={{ color: 'var(--text-sub)', fontSize: '0.85rem' }}>熱烈な応援を送ったファンを指名し直接対話。</p>
                                        </div>
                                        <div style={{ borderLeft: '3px solid var(--primary)', paddingLeft: '1.5rem' }}>
                                            <h4 className="text-white font-bold mb-2">推しポイント客観評価</h4>
                                            <p style={{ color: 'var(--text-sub)', fontSize: '0.85rem' }}>MCがプロ視点でまだバレていない魅力を深掘り。</p>
                                        </div>
                                        <div style={{ borderLeft: '3px solid var(--primary)', paddingLeft: '1.5rem' }}>
                                            <h4 className="text-white font-bold mb-2">公開案件化</h4>
                                            <p style={{ color: 'var(--text-sub)', fontSize: '0.85rem' }}>企業関係者に対し次の一歩への情熱をピッチ。</p>
                                        </div>
                                        <div style={{ borderLeft: '3px solid var(--primary)', paddingLeft: '1.5rem' }}>
                                            <h4 className="text-white font-bold mb-2">ライブ配信対決</h4>
                                            <p style={{ color: 'var(--text-sub)', fontSize: '0.85rem' }}>各クリエイターが自分のchで同時生配信を実施。</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    {/* BALL SYSTEM */}
                    <section id="oshiball" className="section-padding" style={{ background: '#0a0a0a' }}>
                        <div className="container">
                            <div className="section-header">
                                <h2 className="section-title font-display text-gradient">BALL SYSTEM</h2>
                                <div className="section-line"></div>
                                <p style={{ color: 'var(--text-sub)', maxWidth: '600px', margin: '2rem auto 0', fontSize: '1.1rem' }}>
                                    デジタルの「スーパーチャット」を物理化。<br />
                                    会場全体の熱量を可視化し、一体となって盛り上がる究極の演出装置。
                                </p>
                            </div>

                            <div className="grid-2" style={{ marginBottom: '4rem' }}>
                                <div className="glass-panel" style={{ padding: '2.5rem' }}>
                                    <div style={{ width: '60px', height: '60px', background: 'var(--primary)', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.5rem', marginBottom: '1.5rem', boxShadow: '0 0 20px var(--primary-glow)' }}>⚾</div>
                                    <h3 className="font-display text-white" style={{ fontSize: '1.5rem', marginBottom: '1rem' }}>ステージへ直接投げ込む</h3>
                                    <p style={{ color: 'var(--text-sub)' }}>
                                        ステージ演奏中・演技中、観客は購入した「推しボール」をステージに投げ込むことで直接応援が可能。演者に当たってもOK。溢れる気持ちを物理的に「投げつける」ことで熱量を届けます。
                                    </p>
                                </div>
                                <div className="glass-panel" style={{ padding: '2.5rem' }}>
                                    <div style={{ width: '60px', height: '60px', background: 'var(--primary)', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.5rem', marginBottom: '1.5rem', boxShadow: '0 0 20px var(--primary-glow)' }}>💰</div>
                                    <h3 className="font-display text-white" style={{ fontSize: '1.5rem', marginBottom: '1rem' }}>リアルタイム演出＆還元</h3>
                                    <p style={{ color: 'var(--text-sub)' }}>
                                        巨大ボール投入時は会場のライティングや音響がダイナミックに変化。回収されたボールの数・種類に応じて、クリエイターへ即座に収益が還元されます。
                                    </p>
                                </div>
                            </div>

                            <div className="glass-panel" style={{ overflowX: 'auto' }}>
                                <table className="pricing-table">
                                    <thead>
                                        <tr>
                                            <th>ITEM</th>
                                            <th>PRICE</th>
                                            <th>EFFECTS / REWARDS</th>
                                        </tr>
                                    </thead>
                                    <tbody>
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
                                    </tbody>
                                </table>
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
                                <p style={{ color: 'var(--text-sub)', maxWidth: '600px', margin: '2rem auto 0', fontSize: '1.1rem' }}>この人のライブから入るのもあり</p>
                            </div>
                            <div className="glass-panel" style={{ display: 'inline-block', padding: '3rem 5rem' }}>
                                <h3 className="font-display" style={{ fontSize: '2.5rem', color: '#fff' }}>ジャンポケ斎藤</h3>
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
                                            <div className="font-accent" style={{ color: 'var(--primary)', fontWeight: 'bold', fontSize: '1.25rem' }}>{item.time}</div>
                                            <div style={{ color: '#fff', fontWeight: item.highlight ? 'bold' : 'normal' }}>{item.action}</div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </section>

                    {/* CTA & FOOTER */}
                    <section className="section-padding text-center" style={{ position: 'relative', overflow: 'hidden' }}>
                        <div style={{ position: 'absolute', inset: 0, background: 'radial-gradient(circle at center, rgba(255, 215, 0, 0.1) 0%, transparent 60%)', zIndex: 0 }}></div>
                        <div className="container relative z-10">
                            <h2 className="font-display" style={{ fontSize: 'clamp(2rem, 5vw, 3rem)', marginBottom: '2rem' }}>
                                本気のステージを共に創る<br />
                                仲間を待っています。
                            </h2>
                            <a href={applicationUrl} target="_blank" rel="noopener noreferrer" className="btn-super" style={{ fontSize: '1.5rem', padding: '1.5rem 4rem' }}>
                                出演に応募する
                            </a>
                        </div>
                    </section>

                    <footer style={{ background: '#000', padding: '3rem 0', textAlign: 'center', borderTop: '1px solid #222' }}>
                        <div className="font-display text-primary-gradient" style={{ fontSize: '1.5rem', fontWeight: 900, marginBottom: '1rem' }}>
                            CREATOR FES 2026
                        </div>
                        <p style={{ color: 'var(--text-sub)', fontSize: '0.875rem' }}>&copy; 2026 実行委員会 All Rights Reserved.</p>
                    </footer>
                </div>
            );
        };

        ReactDOM.render(<App />, document.getElementById('root'));
    </script>
</body>
</html>
"""

full_html = head_base + css_base + react_script

with open("jam2.html", "w", encoding="utf-8") as f:
    f.write(full_html)
print("Restored jam2.html successfully.")
