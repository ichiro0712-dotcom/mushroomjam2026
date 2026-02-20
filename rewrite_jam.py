import re

def main():
    with open('jam.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Title
    content = re.sub(r'<title>.*?</title>', '<title>それだけでは食っていけないクリエイター祭り2026</title>', content)

    # CSS addition
    css_addition = """    @media (min-width: 1024px) {
      .lg\\:grid-cols-3 {
        grid-template-columns: repeat(3, minmax(0, 1fr));
      }
    }

    .table-auto { table-layout: auto; }
    .w-full { width: 100%; }
    th, td { padding: 0.75rem 1rem; border-bottom: 1px solid #374151; }
    th { text-align: left; color: #fff76a; font-weight: bold; }
  </style>"""
    content = content.replace("    @media (min-width: 1024px) {\n      .lg\\:grid-cols-3 {\n        grid-template-columns: repeat(3, minmax(0, 1fr));\n      }\n    }\n  </style>", css_addition)

    # HomePage Component Replacement
    new_homepage = r"""    // HomePageコンポーネント
    const HomePage = ({ onNavigateToNews }) => {
      const applicationUrl = "https://docs.google.com/forms/d/e/1FAIpQLSeQCrP79MVOQz9JqYtHNsCCrRSKIbBkrTfLA3MmzWGqSacIxQ/viewform?usp=header";

      const news = [
        { date: "2026.XX.XX", title: "出演クリエイター急募！", description: "「それだけでは食っていけないクリエイター祭り2026」の参加者を募集開始いたしました。本気の30分ステージを創り上げてくれるクリエイターを募集しています！" },
        { date: "2026.XX.XX", title: "企画始動", description: "普段の動画スタイルとは一線を画す「本気の一面」をライブでお届けするイベント企画がスタートしました！" }
      ];

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

      const timetable = [
        { time: "19:30", desc: "開場・ボール販売" },
        { time: "19:45", desc: "オープニング（5分）" },
        { time: "19:50", desc: "全演者登場・決起集会（15分）" },
        { time: "20:05", desc: "第1ステージ（30分）" },
        { time: "20:35", desc: "転換＆コラボトーク（15分）" },
        { time: "20:50", desc: "第2ステージ（30分）" },
        { time: "21:20", desc: "転換＆コラボトーク（15分）" },
        { time: "21:35", desc: "第3ステージ（30分）" },
        { time: "22:05", desc: "転換＆コラボトーク（15分）" },
        { time: "22:20", desc: "第4ステージ（30分）" },
        { time: "22:50", desc: "フィナーレ（15分）" },
        { time: "23:05", desc: "物販・交流タイム" },
        { time: "23:30", desc: "完全撤収" }
      ];

      return (
        <>
          <section id="home" className="min-h-screen flex items-center justify-center px-6 pt-24">
            <div className="text-center">
              <h1 className="text-white mb-4" style={{ fontFamily: "ui-sans-serif, system-ui, sans-serif", fontSize: 'clamp(2rem, 5vw, 4.5rem)', fontWeight: '900', lineHeight: '1.2' }}>
                それだけでは<br />食っていけない<br /><span style={{ color: '#fff76a' }}>クリエイター祭り<br />2026</span>
              </h1>
              <p className="text-white mb-8 text-sm md:text-lg font-bold" style={{ color: '#fff76a' }}>
                – 画面を超え、本気で挑む30分<br />ファンと創り上げる一夜限りの最高到達点 –
              </p>
              <a href={applicationUrl} target="_blank" rel="noopener noreferrer">
                <Button className="text-black px-8 py-6 rounded-none text-lg" style={{ backgroundColor: '#fff76a' }} onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#ffe94d'} onMouseLeave={(e) => e.currentTarget.style.backgroundColor = '#fff76a'}>
                  <span className="font-bold">出演応募はこちら</span>
                </Button>
              </a>
            </div>
          </section>

          <section id="concept" className="bg-black/20 backdrop-blur-sm py-20 px-6">
            <div className="max-w-4xl mx-auto text-white space-y-8">
              <h2 className="mb-8 text-center" style={{ fontFamily: "'Architects Daughter', cursive", fontSize: 'clamp(2rem, 5vw, 3rem)', fontWeight: 'bold', color: '#fff76a' }}>企画背景・コンセプト</h2>
              <div>
                <h3 className="mb-4 text-xl font-bold" style={{ color: '#fff76a' }}>【背景】</h3>
                <p className="leading-relaxed">YouTubeというプラットフォームで確かなコミュニティを築き上げてきた表現者たち。しかし、画面の中だけでは伝えきれない表現衝動や、まだ見ぬポテンシャルが彼らには眠っています。デジタルな「数字」の先にある、クリエイターの「人間味」と「本気のパフォーマンス」をリアルな会場で解き放ち、ファンと共に新しい伝説を創る場所が必要です。</p>
              </div>
              <div>
                <h3 className="mb-4 text-xl font-bold" style={{ color: '#fff76a' }}>【コンセプト】</h3>
                <p className="leading-relaxed text-lg font-bold">「情熱」を、ファンと共に可視化する。</p>
                <p className="leading-relaxed mt-2">普段の動画スタイルとは一線を画す「本気の一面」を30分間のステージに凝縮。 クリエイターとファンが同じ空間で熱量を共有し、「リアル投げ銭（ボール）」という形で目に見える愛を届け合うことで、これまでにない深い絆を構築する「日本一クリエイターとファンの距離が近い」プレミアムイベントを目指します。</p>
              </div>
            </div>
          </section>

          <section id="overview" className="bg-black py-20 px-6">
            <div className="max-w-4xl mx-auto text-white space-y-8">
              <h2 className="mb-8 text-center" style={{ fontFamily: "'Architects Daughter', cursive", fontSize: 'clamp(2rem, 5vw, 3rem)', fontWeight: 'bold', color: '#fff76a' }}>開催概要</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div className="border border-gray-700 p-6 rounded-lg">
                  <h3 className="mb-2 font-bold" style={{ color: '#fff76a' }}>開催日・時間</h3>
                  <p>2026年 某日<br />19:30 開場 / 23:30 終了</p>
                </div>
                <div className="border border-gray-700 p-6 rounded-lg">
                  <h3 className="mb-2 font-bold" style={{ color: '#fff76a' }}>ターゲット層</h3>
                  <ul className="list-disc list-inside">
                    <li>出演クリエイターのコアファン層</li>
                    <li>「夢を追う人」を応援したいライブ好き</li>
                  </ul>
                </div>
                <div className="border border-gray-700 p-6 rounded-lg md:col-span-2">
                  <h3 className="mb-2 font-bold" style={{ color: '#fff76a' }}>出演者</h3>
                  <p>さらなる高みを目指す「本気の表現者」たち 4〜5組 ＋ 著名MC</p>
                </div>
              </div>
            </div>
          </section>

          <section id="stage" className="bg-black/30 backdrop-blur-sm py-20 px-6">
            <div className="max-w-4xl mx-auto text-white space-y-12">
              <h2 className="mb-8 text-center" style={{ fontFamily: "'Architects Daughter', cursive", fontSize: 'clamp(2rem, 5vw, 3rem)', fontWeight: 'bold', color: '#fff76a' }}>ステージコンテンツ詳細</h2>
              
              <div>
                <h3 className="mb-4 text-2xl font-bold border-b-2 border-yellow-300 inline-block pb-2" style={{ color: '#fff76a', borderColor: '#fff76a' }}>① 本気のメインステージ（各30分）</h3>
                <p className="mb-4 leading-relaxed">「普段の動画とは違う一面」をテーマに、この日のためだけに準備された本気のステージ。1ヶ月以上前から一生懸命に練習を積み重ねたクリエイティビティをステージで爆発させます。</p>
                <ul className="space-y-4 ml-4">
                  <li><strong style={{ color: '#fff76a' }}>バンド・音楽：</strong> 画面越しではなく、直接心に響かせる魂の生演奏。</li>
                  <li><strong style={{ color: '#fff76a' }}>演劇・コント：</strong> 徹底的に練り上げられた脚本による、新しいキャラクターの開拓。</li>
                  <li><strong style={{ color: '#fff76a' }}>トークライブ：</strong> 編集の壁を取り払い、その瞬間の空気感で紡ぐ真剣勝負の言葉。</li>
                </ul>
              </div>

              <div>
                <h3 className="mb-4 text-2xl font-bold border-b-2 border-yellow-300 inline-block pb-2" style={{ color: '#fff76a', borderColor: '#fff76a' }}>② クリエイターコラボコンテンツ（各15分）</h3>
                <p className="mb-4 leading-relaxed">出演クリエイター達とMCによる、ステージの熱狂を引き継ぐ特別な交流コーナー。</p>
                <ul className="space-y-4 ml-4">
                  <li><strong style={{ color: '#fff76a' }}>「太客と話そう」コーナー：</strong> 客席から熱烈な応援を送ったファンを指名し、直接対話。</li>
                  <li><strong style={{ color: '#fff76a' }}>「推しポイント客観評価」：</strong> MCがプロの視点から「まだ世間にバレていない魅力」を深掘り。</li>
                  <li><strong style={{ color: '#fff76a' }}>「ぶっちゃけどれくらい食えてないの？」：</strong> タイトルにちなんだユーモア溢れるトーク。</li>
                  <li><strong style={{ color: '#fff76a' }}>「公開案件化」コーナー：</strong> 会場に招かれたメディア・企業関係者に対し情熱をピッチ。</li>
                  <li><strong style={{ color: '#fff76a' }}>ライブ配信対決：</strong> 各クリエイターが自分のチャンネルで同時生配信を実施。</li>
                </ul>
              </div>
            </div>
          </section>

          <section id="oshiball" className="bg-black py-20 px-6">
            <div className="max-w-4xl mx-auto text-white space-y-8">
              <h2 className="mb-8 text-center" style={{ fontFamily: "'Architects Daughter', cursive", fontSize: 'clamp(2rem, 5vw, 3rem)', fontWeight: 'bold', color: '#fff76a' }}>会場を盛り上げる演出（推しボール）</h2>
              <p className="leading-relaxed">デジタルの「スーパーチャット」を物理化し、会場全体の熱量を可視化すると同時に、会場一体となって盛り上がる演出装置として機能させます。</p>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <div className="bg-gray-800 p-4 rounded-lg">
                  <h4 className="font-bold mb-2 text-xl" style={{ color: '#fff76a' }}>全力の応援</h4>
                  <p>ステージ演奏中・演技中、観客は購入した「推しボール」をステージに投げ込むことで直接応援が可能！</p>
                </div>
                <div className="bg-gray-800 p-4 rounded-lg">
                  <h4 className="font-bold mb-2 text-xl" style={{ color: '#fff76a' }}>推しにぶつけろ！</h4>
                  <p>演者にボールが当たってもOK。溢れる気持ちを物理的に「投げつける」ことで熱量を届けます。</p>
                </div>
              </div>

              <div className="overflow-x-auto">
                <table className="w-full text-sm text-left border border-gray-700 table-auto">
                  <caption className="text-xl font-bold mb-4 text-left" style={{ color: '#fff76a' }}>投げ銭アイテム一覧</caption>
                  <thead className="bg-gray-800">
                    <tr>
                      <th className="px-6 py-3 border-b border-gray-700">アイテム</th>
                      <th className="px-6 py-3 border-b border-gray-700">価格</th>
                      <th className="px-6 py-3 border-b border-gray-700">演出・特典</th>
                    </tr>
                  </thead>
                  <tbody>
                    {oshiItems.map((item, idx) => (
                      <tr key={idx} className="bg-black border-b border-gray-700">
                        <td className="px-6 py-4 font-medium whitespace-nowrap">{item.name}</td>
                        <td className="px-6 py-4">{item.price}</td>
                        <td className="px-6 py-4">{item.effect}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <section id="impact" className="bg-black/20 backdrop-blur-sm py-20 px-6">
            <div className="max-w-4xl mx-auto text-white space-y-8">
              <h2 className="mb-8 text-center" style={{ fontFamily: "'Architects Daughter', cursive", fontSize: 'clamp(2rem, 5vw, 3rem)', fontWeight: 'bold', color: '#fff76a' }}>活動へのポジティブな影響</h2>
              <p className="leading-relaxed mb-6">単なる一過性のイベントではなく、クリエイターの今後の活動を強力にバックアップします。</p>
              <ul className="space-y-6">
                <li><strong className="text-xl block mb-1" style={{ color: '#fff76a' }}>ファンとの深い交流機会：</strong>画面越しではない濃密なコミュニケーションにより、コアなファンベースを固めます。</li>
                <li><strong className="text-xl block mb-1" style={{ color: '#fff76a' }}>新たな収益機会の創出：</strong>リアルと配信の両軸から集まる支援により、次なる企画のための軍資金を確保できます。</li>
                <li><strong className="text-xl block mb-1" style={{ color: '#fff76a' }}>プレミアム映像素材の確保：</strong>当日の舞台裏や共演シーンなど、自身のチャンネルで活用できる貴重な映像コンテンツが得られます。</li>
              </ul>
            </div>
          </section>

          <section id="timetable" className="bg-black py-20 px-6">
            <div className="max-w-4xl mx-auto text-white">
              <h2 className="mb-12 text-center" style={{ fontFamily: "'Architects Daughter', cursive", fontSize: 'clamp(2rem, 5vw, 3rem)', fontWeight: 'bold', color: '#fff76a' }}>タイムテーブル詳細</h2>
              <div className="relative border-l border-gray-700 ml-4 md:ml-0">
                {timetable.map((item, idx) => (
                  <div key={idx} className="mb-8 ml-6">
                    <span className="absolute flex items-center justify-center w-4 h-4 rounded-full -left-2 ring-4 ring-black" style={{ backgroundColor: '#fff76a' }}></span>
                    <h3 className="flex items-center mb-1 text-lg font-bold" style={{ color: '#fff76a' }}>{item.time}</h3>
                    <p className="text-base font-normal text-white">{item.desc}</p>
                  </div>
                ))}
              </div>
            </div>
          </section>

          <section id="mc" className="bg-black/30 backdrop-blur-sm py-20 px-6">
            <div className="max-w-4xl mx-auto text-white text-center">
              <h2 className="mb-8" style={{ fontFamily: "'Architects Daughter', cursive", fontSize: 'clamp(2rem, 5vw, 3rem)', fontWeight: 'bold', color: '#fff76a' }}>MC候補リスト</h2>
              <p className="mb-4 text-gray-300">予算50万円。この人のライブから入るもあり</p>
              <div className="inline-block border border-gray-700 rounded-lg p-6 bg-black/50">
                <h3 className="text-2xl font-bold" style={{ color: '#fff76a' }}>ジャンポケ斎藤</h3>
              </div>
            </div>
          </section>

          <section id="news" className="bg-black py-20 px-6">
            <div className="max-w-4xl mx-auto text-white">
              <h2 className="mb-12 text-center" style={{ fontFamily: "'Architects Daughter', cursive", fontSize: 'clamp(2.5rem, 6vw, 4rem)', fontWeight: 'bold', color: '#fff76a' }}>NEWS</h2>
              <div className="space-y-8">
                {news.map((item, index) => (
                  <div key={index} className="border-b border-gray-700 pb-8">
                    <h3 className="mb-2 font-bold" style={{ fontFamily: 'Lulo Clean, sans-serif', color: '#fff76a' }}>{item.date} {item.title}</h3>
                    <p className="text-white">{item.description}</p>
                  </div>
                ))}
              </div>
              <div className="text-center mt-8">
                <button onClick={onNavigateToNews} className="transition-colors" style={{ color: '#fff76a', background: 'transparent', border: 'none' }} onMouseEnter={(e) => e.currentTarget.style.color = '#ffe94d'} onMouseLeave={(e) => e.currentTarget.style.color = '#fff76a'}>もっと読む →</button>
              </div>
            </div>
          </section>

          <section id="requirements" className="bg-black/30 backdrop-blur-sm py-20 px-6">
            <div className="max-w-4xl mx-auto text-white">
              <h2 className="mb-12 text-center" style={{ fontFamily: 'Lulo Clean, sans-serif', fontSize: 'clamp(2rem, 5vw, 3rem)', fontWeight: 'bold', color: '#fff76a' }}>参加要項</h2>
              <div className="space-y-8">
                <div>
                  <h3 className="mb-4 font-bold" style={{ color: '#fff76a' }}>参加資格</h3>
                  <p className="ml-4">演奏やパフォーマンス、そしてファンとのコミュニケーションをリアルで「本気で」したい配信者・クリエイター</p>
                </div>
                <div>
                  <h3 className="mb-4 font-bold" style={{ color: '#fff76a' }}>協力事項</h3>
                  <ul className="space-y-2 ml-4 list-disc list-inside">
                    <li>イベント会議への参加</li>
                    <li>30分の自身のステージの準備・練習</li>
                    <li>動画等での告知協力（告知・練習風景などの配信）</li>
                    <li>イベントや準備期間の映像の使用許可（内容確認可）</li>
                    <li>アフターパーティー・VIPへの会席参加（可能であれば）</li>
                  </ul>
                </div>
                <div>
                  <h3 className="mb-4 font-bold" style={{ color: '#fff76a' }}>主催協力事項</h3>
                  <ul className="space-y-2 ml-4 list-disc list-inside">
                    <li>会場・機材・必要サポートスタッフの手配</li>
                    <li>告知用MV・Webサイトの作成</li>
                    <li>演出・進行のサポート</li>
                  </ul>
                </div>
                <div>
                  <h3 className="mb-4 font-bold" style={{ color: '#fff76a' }}>収益分配</h3>
                  <p className="ml-4">イベント収益および投げ銭（推しボール）による収益は、規定の割合で還元いたします。</p>
                </div>
                <div className="text-center mt-12">
                  <a href={applicationUrl} target="_blank" rel="noopener noreferrer">
                    <Button className="text-black px-8 py-6 rounded-none text-lg" style={{ backgroundColor: '#fff76a' }} onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#ffe94d'} onMouseLeave={(e) => e.currentTarget.style.backgroundColor = '#fff76a'}><span className="font-bold">出演応募はこちら</span></Button>
                  </a>
                </div>
              </div>
            </div>
          </section>

          <footer className="bg-black py-8 px-6 border-t border-gray-800">
            <div className="max-w-7xl mx-auto text-center text-white">
              <p>©️2026 それだけでは食っていけないクリエイター祭り</p>
            </div>
          </footer>
        </>
      );
    };"""
    content = re.sub(r'    // HomePageコンポーネント\n    const HomePage =.*?(?=    // NewsPageコンポーネント)', new_homepage + '\n\n', content, flags=re.DOTALL)

    # Nav component changes
    content = re.sub(r'<button onClick=\{.*?\} className="text-white transition-colors" .*?>\s*About\s*</button>', '', content)
    content = re.sub(r'<button onClick=\{.*?\} className="text-white transition-colors" .*?>\s*Artist\s*</button>', '', content)
    content = re.sub(r'<button onClick=\{.*?\} className="text-white transition-colors" .*?>\s*イベント詳細\s*</button>', '', content)
    
    # Let's completely replace the App component navigation menus
    desktop_nav_old = r"""              <nav className="hidden md:flex gap-8">
                <button onClick={() => scrollToSection\('home'\)}.*?Home\s*</button>
.*?
              </nav>"""
              
    desktop_nav_new = r"""              <nav className="hidden md:flex gap-4 lg:gap-8 flex-wrap justify-center overflow-x-auto text-sm lg:text-base">
                <button onClick={() => scrollToSection('home')} className="text-white transition-colors whitespace-nowrap" style={{ color: 'white', background: 'transparent', border: 'none'}} onMouseEnter={(e) => e.currentTarget.style.color = '#fff76a'} onMouseLeave={(e) => e.currentTarget.style.color = 'white'}>Home</button>
                <button onClick={() => scrollToSection('concept')} className="text-white transition-colors whitespace-nowrap" style={{ color: 'white', background: 'transparent', border: 'none'}} onMouseEnter={(e) => e.currentTarget.style.color = '#fff76a'} onMouseLeave={(e) => e.currentTarget.style.color = 'white'}>コンセプト</button>
                <button onClick={() => scrollToSection('overview')} className="text-white transition-colors whitespace-nowrap" style={{ color: 'white', background: 'transparent', border: 'none'}} onMouseEnter={(e) => e.currentTarget.style.color = '#fff76a'} onMouseLeave={(e) => e.currentTarget.style.color = 'white'}>概要</button>
                <button onClick={() => scrollToSection('stage')} className="text-white transition-colors whitespace-nowrap" style={{ color: 'white', background: 'transparent', border: 'none'}} onMouseEnter={(e) => e.currentTarget.style.color = '#fff76a'} onMouseLeave={(e) => e.currentTarget.style.color = 'white'}>ステージ詳細</button>
                <button onClick={() => scrollToSection('oshiball')} className="text-white transition-colors whitespace-nowrap" style={{ color: 'white', background: 'transparent', border: 'none'}} onMouseEnter={(e) => e.currentTarget.style.color = '#fff76a'} onMouseLeave={(e) => e.currentTarget.style.color = 'white'}>推しボール</button>
                <button onClick={() => scrollToSection('timetable')} className="text-white transition-colors whitespace-nowrap" style={{ color: 'white', background: 'transparent', border: 'none'}} onMouseEnter={(e) => e.currentTarget.style.color = '#fff76a'} onMouseLeave={(e) => e.currentTarget.style.color = 'white'}>タイムテーブル</button>
                <button onClick={() => scrollToSection('requirements')} className="text-white transition-colors whitespace-nowrap" style={{ color: 'white', background: 'transparent', border: 'none'}} onMouseEnter={(e) => e.currentTarget.style.color = '#fff76a'} onMouseLeave={(e) => e.currentTarget.style.color = 'white'}>参加要項</button>
              </nav>"""

    mobile_nav_old = r"""              <nav className="md:hidden mt-4 pb-4 border-t border-gray-700 pt-4">
                <div className="flex flex-col gap-4">
                  <button onClick=\{\(\) => scrollToSection\('home'\)\}.*?Home\s*</button>
.*?
                </div>
              </nav>"""

    mobile_nav_new = r"""              <nav className="md:hidden mt-4 pb-4 border-t border-gray-700 pt-4">
                <div className="flex flex-col gap-4">
                  <button onClick={() => scrollToSection('home')} className="text-white text-left py-2 transition-colors" style={{ color: 'white', background: 'transparent', border: 'none' }}>Home</button>
                  <button onClick={() => scrollToSection('concept')} className="text-white text-left py-2 transition-colors" style={{ color: 'white', background: 'transparent', border: 'none' }}>コンセプト</button>
                  <button onClick={() => scrollToSection('overview')} className="text-white text-left py-2 transition-colors" style={{ color: 'white', background: 'transparent', border: 'none' }}>概要</button>
                  <button onClick={() => scrollToSection('stage')} className="text-white text-left py-2 transition-colors" style={{ color: 'white', background: 'transparent', border: 'none' }}>ステージ詳細</button>
                  <button onClick={() => scrollToSection('oshiball')} className="text-white text-left py-2 transition-colors" style={{ color: 'white', background: 'transparent', border: 'none' }}>推しボール</button>
                  <button onClick={() => scrollToSection('timetable')} className="text-white text-left py-2 transition-colors" style={{ color: 'white', background: 'transparent', border: 'none' }}>タイムテーブル</button>
                  <button onClick={() => scrollToSection('requirements')} className="text-white text-left py-2 transition-colors" style={{ color: 'white', background: 'transparent', border: 'none' }}>参加要項</button>
                </div>
              </nav>"""
              
    content = re.sub(desktop_nav_old, desktop_nav_new, content, flags=re.DOTALL)
    content = re.sub(mobile_nav_old, mobile_nav_new, content, flags=re.DOTALL)

    with open('jam.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
