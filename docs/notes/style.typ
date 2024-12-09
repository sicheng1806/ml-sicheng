// 数学建模竞赛的typst模板, 借鉴于cumcm-muban:0.3.0
/* 更新日志:
- ...
- 使页面指向标题，支持快速跳转
*/
#import "@preview/ctheorems:1.1.2":*
// 文本和代码的字体
#let songti = "SimSun"
#let heiti = "SimHei"
#let kaiti = "SimKai"
#let text-font = "Times New Roman"
#let code-font = "DejaVu Sans Mono"

#let conf(
  title: "全国大学生数学建模竞赛 Typst 模板",
  authors: (),//姓名列表
  abstract: [],
  keywords: (),
  outline: [],
  abstract_page: false,
  body,
) = {
  // 设置正文和代码的字体 
  set text(font: (text-font, songti), size: 12pt, lang: "zh", region: "cn")
  show strong: it => {
    show regex("[\p{hani}\s]+"): set text(stroke: 0.02857em)
    it
  }
  show raw: set text(font: code-font, 8pt)

  // 设置文档元数据和参考文献格式
  set document(title: title)

  // 设置章节标题 
  set heading(numbering: "1.1 ")

  show heading: it => box(width: 100%)[
    #set text(font: (text-font, heiti))
    #if it.numbering != none { counter(heading).display() }
    #it.body
    #v(8pt)
  ]

  show heading.where(
    level: 1
  ): it => box(width: 100%)[
    #set text(size: 15pt)
    #set align(center)
    #set heading(numbering: "一、")
    #v(4pt)
    #it
  ]

  show heading.where(
    level: 2
  ): it => box(width: 100%)[
    #set text(size: 13pt)
    #it
  ]
  // 配置公式的编号、间距和字体
  set math.equation(numbering: "(1.1)")
  show math.equation: eq => {
    set block(spacing: 0.65em)
    eq
  }
  show math.equation: it => {
    show regex("[\p{hani}\s]+"): set text(font: songti)
    it
  }

  show figure: it => [
    #v(4pt)
    #it
    #v(4pt)
  ]

  show figure.where(
    kind: raw
  ): it => {
    set block(width: 100%, breakable: true)
    it
  }
  
  // 段落配置
  set par(
    first-line-indent: 2em,
    linebreaks: "optimized",
    justify: true
  )

  // 配置列表
  set list(tight: false, indent: 1em, marker: ([•], [◦], [•], [◦]))
  show list: set text(top-edge: "ascender")

  set enum(tight: false, indent: 1em)
  show enum: set text(top-edge: "ascender")

  // 设置页面
  set page(
    paper: "a4",
    margin: (top: 1in, bottom: 0.75in, left: 1in, right: 1in),
    footer: align(center)[#text(context {counter(page).display("1")}, font: songti, size: 12pt)]
  )

  // 标题、作者、摘要、目录
  set page(
    header: align(left)[#text(10pt)[#link(<title>)[#title]]#v(-10pt)#line(length: 100%, stroke: 0.6pt)]
    ) if outline == []
  align(center)[
    #set text(font: (text-font, heiti))
    #text(size: 16pt)[#title<title>] 
    #if authors != () {
      v(1pt)
      authors.join(",")
    }
    #v(2pt)
    #if abstract != [] {text(size: 14pt)[摘 要]}
  ]
  if abstract != [] {
    abstract
    if keywords != () [
      #v(5pt)
      #h(-2em)#text("关键字：", font: heiti)
      #keywords.join(h(1em))
    ]
    if abstract_page { pagebreak()}
  }
  if outline != [] [#outline]
  set page(
    header: align(left)[#text(10pt)[#link(<title>)[#title]]#v(-10pt)#line(length: 100%, stroke: 0.6pt)]
    ) if outline != []
  
  body
}

#let bib(bibliography-file) = {
  show bibliography: set text(10.5pt)
  set bibliography(title: "参考文献", style: "gb-7714-2015-numeric")
  bibliography-file
  v(12pt)
}

#let appendix-num = counter("appendix")

#let appendix(title,use-table:true, body) = {
  appendix-num.step()
  if not use-table {
    text[*附录 #appendix-num.display()：*]
    align(center,text[*#title*])
    body
  } 
  else {
    table(
      fill: (_, row) => if row == 0 or row == 1 {luma(200)} else {none},
      rows: 3,
      columns: 1fr,
      text[*附录 #appendix-num.display()：*],
      align(center,text[*#title*]),
      body
    )
  }
}

// 定理环境
#let envbox = thmbox.with(
  base: none,
  breakable: true,
  base_level: 1, 
  inset: 0.5em
)

#let plainbox = thmplain.with(
  base: none, 
  inset: .5em, 
  stroke: luma(50%), 
  titlefmt: strong
)

#let notation = thmbox(
  "notaion",
  "注意",
  inset: 0.5em,
  titlefmt: title => {text(red)[#title]}
).with(fill: cmyk(0%, 8.05%, 48.73%, 7.45%),stroke:luma(72.11%) , numbering: none)

#let definition = envbox(
  "definition",
  "定义",
  //breakable: false,
  base: "heading",
).with(stroke: luma(50%))

#let axiom = envbox(
  "axiom",
  "公理",
)

#let theorem = envbox(
  "theorem",
  "定理",
).with(fill: rgb("#eeffee")) 

#let lemma = envbox(
  "lemma",
  "引理",
).with(fill: rgb("#eeffee")) 

#let corollary = envbox(
  "corollary",
  "推论",
)

#let assumption = envbox(
  "assumption",
  "假设",
)

#let conjecture = envbox(
  "conjecture",
  "猜想",
).with(fill: rgb("#eeffee")) 

#let problem = plainbox(
  "problem",
  "问题",
).with(base: "heading", base_level: 1)

#let example = plainbox(
  "example",
  "例",
).with(base: "heading", base_level: 1)

#let proof = plainbox(
  "proof",
  "证明",
  bodyfmt: body => [#body #h(1fr) $square$ ], 
  stroke: none
).with(numbering: none)

#let solution = plainbox(
  "solution",
  "解",
  stroke: none,
).with(numbering: none)
