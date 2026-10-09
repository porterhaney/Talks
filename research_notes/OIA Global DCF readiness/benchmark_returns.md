# Public-Market and PE Benchmark Returns: Lacy (LDI) / OIA Global, 2010–2011 Entry to 2026 Exit

Data as of **October 8, 2026** (last market close available on October 9, 2026). All index and stock levels come from Yahoo Finance historical data, pulled through the finance-pricing MCP tool (`finance_get_historical`): monthly bars for 2010–2025 month-ends and daily bars to confirm 10/8/2026. Calculations: multiple = end level / start level, and CAGR = multiple^(1/years) − 1, with years = actual days / 365.25.

**Labeling convention:**
- **TR** means total return, with dividends reinvested.
- **Price** means price-only, with no dividends.
- For ETF proxies, TR uses Yahoo "adj_close". That figure is dividend- and split-adjusted and net of the ETF's expense ratio, so it slightly understates the gross index TR. The fees are IWM ~0.19%, IJH ~0.05%, XLI ~0.08% and IYT ~0.39%.

---

## Q1. What is the exact entry date for Lacy's (LDI's) acquisition of OIA Global?

### Takeaway
OIA's own press release is dated **August 31, 2011**. It describes LDI as having "recapitalized and acquired majority control" of Oregon International Air Freight Co. and OIA Global Logistics‑SCM, Inc. The Indianapolis Business Journal, however, reported the same deal on **September 16, 2010**, and the coordinator notes that OIA and LDI themselves date the deal to 2010. **The base case here uses August 31, 2011**, with two 2010 bookends: **September 30, 2010**, the month-end nearest the IBJ report, and **December 31, 2010**, which proxies "January 1, 2011". December 30, 2011 is the year-end bookend.

### Cited Findings
- OIA company news item dated "31 August 2011": LDI (LDI Ltd., LLC), a private Indianapolis holding company, "recapitalized and acquired majority control" of OIA. Founder Junki Yoshida stays as Chairman and Charles Hornecker becomes CEO. No price, financing or stake percentage was disclosed beyond "majority control." — [OIA Global company news](https://www.oiaglobal.com/?p=394); see also [OIA: Lacy Diversified LDI acquisition](https://www.oiaglobal.com/lacy-diversified-ldi-acquisition/)
- IBJ, "Lacy company takes stake in Oregon logistics firm," publication date **September 16, 2010**, as rendered by the fetch tool. It reports the same facts (recapitalization, majority stake, Yoshida stays chairman, Hornecker becomes CEO), with price and terms undisclosed. — [IBJ](https://ibj.com/?p=20502)
- LDI has kept investing in add-ons through OIA. Examples are U.S. Worldwide Logistics (Kentucky, 2013) and American Cargo Express. — [Inside Indiana Business: LDI acquires Kentucky company](https://www.insideindianabusiness.com/articles/ldi-acquires-kentucky-company); [OIA: U.S. Worldwide Logistics acquisition](https://www.oiaglobal.com/acquisition-us-worldwide-logistics-inc/); [Transport Topics: OIA Global acquires American Cargo Express](https://www.ttnews.com/articles/oia-global-acquires-american-cargo-express)
- Coordinator note, from the company-profile research rather than independently verified here: there have been about 11 add-on deals, accelerating in 2024–2026.

### Inferences
- The sources conflict by about 11.5 months. The IBJ story probably reflects the original 2010 announcement or close, and the OIA web post (August 31, 2011) may be a later re-post or the formal close. The start date matters a great deal for the benchmark because the S&P 500 fell about 7.5% between June 30 and August 31, 2011. An August 31, 2011 start therefore gives a **higher** benchmark CAGR (~15.1% TR) than a December 2010 start (~14.3% TR), even though its multiple is similar.
- The owners should use the **actual dates and amounts of every equity check** from LDI's books, not a single press-release date. See Q5.

### Gaps
- The exact closing date, purchase price and equity amount were not found in any public source. The deal was private and the terms were undisclosed.

---

## Q2. What has the S&P 500 returned from the 2010–2011 entry dates to 2025–2026 (TR vs. price, annualized and cumulative)?

### Takeaway
From the **August 31, 2011 base date to October 8, 2026** (15.11 years), the S&P 500 returned **15.12%/yr total return, turning $1 into $8.39**. Price-only, it returned 13.04%/yr ($6.37). Through **December 31, 2025** the figures are 14.91%/yr TR (7.33x) and 12.79%/yr price (5.62x). With a 2010 start, TR runs from 14.3% to 14.8%/yr and the multiple from 8.2x to 9.1x.

### Cited Findings
**Index levels.** SPXTR is Yahoo ^SP500TR (the S&P 500 Total Return index). SPX is ^GSPC (price). Source: [Yahoo Finance ^SP500TR history](https://finance.yahoo.com/quote/%5ESP500TR/history/) and [Yahoo Finance ^GSPC history](https://finance.yahoo.com/quote/%5EGSPC/history/), via the finance-pricing MCP tool.

| Date (close) | SPXTR (TR) | SPX (price) |
|---|---|---|
| 2010‑09‑30 | 1,908.95 | 1,141.20 |
| 2010‑12‑31 | 2,114.29 | 1,257.64 |
| 2011‑06‑30 | 2,241.66 | 1,320.64 |
| **2011‑08‑31 (base)** | **2,076.78** | **1,218.89** |
| 2011‑12‑30 | 2,158.94 | 1,257.60 |
| 2025‑12‑31 | 15,220.45 | 6,845.50 |
| 2026‑06‑30 | 16,774.07 | 7,499.36 |
| 2026‑08‑31 | 17,219.94 | 7,686.14 |
| 2026‑09‑30 | 17,160.41 | 7,651.54 |
| **2026‑10‑08 (latest)** | **17,419.63** | **7,765.36** |

Data note: Yahoo's partial October 2026 monthly bar showed 17,501.21 / 7,801.77, which are the October 7 closes. The daily series confirms the October 8 closes of 17,419.63 / 7,765.36, and those are used here. The SPXTR all-time high in the window was 17,596.69 intraday on October 6, 2026. — [Yahoo ^SP500TR daily via MCP](https://finance.yahoo.com/quote/%5ESP500TR/history/)

**Returns.** Each cell shows CAGR and the multiple ($1 became $X).

| Start → End | Years | S&P 500 **TR** | S&P 500 **Price** |
|---|---|---|---|
| 2011‑08‑31 → 2025‑12‑31 | 14.34 | **14.91% (7.33x)** | 12.79% (5.62x) |
| 2011‑08‑31 → 2026‑06‑30 | 14.83 | **15.13% (8.08x)** | 13.03% (6.15x) |
| 2011‑08‑31 → 2026‑09‑30 | 15.08 | **15.03% (8.26x)** | 12.95% (6.28x) |
| 2011‑08‑31 → 2026‑10‑08 | 15.11 | **15.12% (8.39x)** | 13.04% (6.37x) |
| 2010‑09‑30 → 2025‑12‑31 | 15.25 | 14.58% (7.97x) | 12.46% (6.00x) |
| 2010‑09‑30 → 2026‑10‑08 | 16.02 | 14.80% (9.13x) | 12.71% (6.81x) |
| 2010‑12‑31 → 2025‑12‑31 | 15.00 | 14.06% (7.20x) | 11.96% (5.44x) |
| 2010‑12‑31 → 2026‑06‑30 | 15.50 | 14.30% (7.93x) | 12.21% (5.96x) |
| 2010‑12‑31 → 2026‑10‑08 | 15.77 | 14.31% (8.24x) | 12.24% (6.18x) |
| 2011‑06‑30 → 2025‑12‑31 | 14.50 | 14.12% (6.79x) | 12.01% (5.18x) |
| 2011‑06‑30 → 2026‑06‑30 | 15.00 | 14.36% (7.48x) | 12.27% (5.68x) |
| 2011‑06‑30 → 2026‑10‑08 | 15.27 | 14.37% (7.77x) | 12.30% (5.88x) |
| 2011‑12‑30 → 2025‑12‑31 | 14.00 | 14.97% (7.05x) | 12.86% (5.44x) |
| 2011‑12‑30 → 2026‑10‑08 | 14.77 | 15.18% (8.07x) | 13.11% (6.18x) |

**Cross-check.** OfficialData.org gives $100 at the start of 2011 growing to about $781 by its last data row (**August 2026**). That is **14.02%/yr with dividends reinvested** and **+12.62%/yr price-only** (+494.99%). — [OfficialData.org S&P 500 since 2011](https://www.officialdata.org/us/stocks/s-p-500/2011). Over the comparable window (December 31, 2010 → August 31, 2026), the Yahoo SPXTR/SPX levels give **14.33% TR (8.15x)** and **12.25% price (6.11x)**.

### Inferences
- The two sources differ by about 0.3–0.4 pts/yr. OfficialData uses monthly-average (Shiller-style) prices and its own dividend series, while Yahoo's SPXTR is the official S&P DJI daily total-return index. **Use the SPXTR figures** for a point-to-point comparison with a deal.
- **Headline benchmark for the owners:** a dollar of LDI equity put into OIA on August 31, 2011 would have had to be worth about **$8.39 by October 8, 2026** (about **$7.33 at December 31, 2025**) just to match a passive S&P 500 index fund with dividends reinvested, before taxes and fees.
- For an exit **after** October 8, 2026, take the multiple to date and grow it at the market's return over the remaining period. Example: a December 31, 2026 close is 0.23 years away. At 0% further market return the hurdle stays at **8.39x**. At an assumed 10%/yr it becomes 8.39 × 1.10^0.23 ≈ **8.57x**. This is illustrative arithmetic, not a forecast.

### Gaps
- I did not pull the official S&P DJI factsheet directly. The Yahoo ^SP500TR levels are the S&P DJI index values as redistributed. The December 31, 2010 level (2,114.29) and the December 30, 2011 level (2,158.94) imply a 2011 calendar-year TR of +2.11%, which matches the well-known 2011 S&P 500 TR of about 2.1%.
- Slickcharts and the dqydj calculator were not fetched, to stay within the tool-call budget.

---

## Q3. How did other public benchmarks (small/mid caps, industrials/transports, logistics peers) perform over the same period?

### Takeaway
Every other public benchmark **trailed the S&P 500**. From August 31, 2011 to October 8, 2026, TR was:
- Russell 2000: **~10.8%/yr** (4.7x)
- S&P MidCap 400: **~11.6%** (5.2x)
- S&P 500 Industrials (XLI): **~13.6%** (6.9x)
- DJ Transportation (IYT): **~10.5%** (4.5x)
- Expeditors (EXPD): **~11.5%** (5.2x)
- C.H. Robinson (CHRW): **~7.1%** (2.8x)

The closest "OIA-like" public comparables (small caps, transports, forwarders) therefore set a hurdle of roughly **4.5x–5.2x** over the base period, against **8.4x** for the S&P 500.

### Cited Findings
Sources: [Yahoo IWM](https://finance.yahoo.com/quote/IWM/history/), [Yahoo ^RUT](https://finance.yahoo.com/quote/%5ERUT/history/), [Yahoo IJH](https://finance.yahoo.com/quote/IJH/history/), [Yahoo XLI](https://finance.yahoo.com/quote/XLI/history/), [Yahoo IYT](https://finance.yahoo.com/quote/IYT/history/), [Yahoo ^DJT](https://finance.yahoo.com/quote/%5EDJT/history/), [Yahoo EXPD](https://finance.yahoo.com/quote/EXPD/history/) and [Yahoo CHRW](https://finance.yahoo.com/quote/CHRW/history/), all pulled through the finance-pricing MCP tool. Each cell shows CAGR and the multiple.

**Base: 2011‑08‑31 → 2026‑10‑08 (15.11 yrs)**

| Benchmark | Proxy | TR | Price-only |
|---|---|---|---|
| S&P 500 | ^SP500TR / ^GSPC | **15.12% (8.39x)** | 13.04% (6.37x) |
| Russell 2000 | IWM adj (TR, net of ETF fee); ^RUT (price) | **10.79% (4.70x)** | 9.32% (3.84x) [^RUT 726.81 → 2,794.13] |
| S&P MidCap 400 | IJH | **11.56% (5.22x)** | 9.92% (4.17x) |
| S&P 500 Industrials | XLI | **13.62% (6.88x)** | 11.53% (5.20x) |
| Dow Jones Transportation Avg | IYT (TR); ^DJT (price) | **10.51% (4.52x)** | 10.04% (4.25x) [^DJT 4,666.96 → 19,809.07] |
| Expeditors (EXPD) | stock | **11.50% (5.18x)** | 10.07% (4.26x) |
| C.H. Robinson (CHRW) | stock | **7.14% (2.83x)** | 4.71% (2.01x) |

**Base start → 2025‑12‑31 (14.34 yrs)**

| Benchmark | TR | Price-only |
|---|---|---|
| S&P 500 | 14.91% (7.33x) | 12.79% (5.62x) |
| Russell 2000 (IWM / ^RUT) | 10.41% (4.14x) | 8.94% (3.42x) |
| S&P MidCap 400 (IJH) | 11.37% (4.68x) | 9.70% (3.77x) |
| Industrials (XLI) | 13.68% (6.29x) | 11.54% (4.79x) |
| DJ Transports (IYT / ^DJT) | 10.50% (4.18x) | 9.60% (3.72x) |
| EXPD | 10.08% (3.96x) | 8.63% (3.28x) |
| CHRW | 8.42% (3.19x) | 5.92% (2.28x) |

**Bookend: 2010‑12‑31 → 2026‑10‑08 (15.77 yrs), TR**

| Benchmark | TR |
|---|---|
| S&P 500 | 14.31% (8.24x) |
| Russell 2000 (IWM) | 9.83% (4.38x); ^RUT price 8.40% |
| MidCap 400 (IJH) | 10.84% (5.07x) |
| XLI | 12.55% (6.45x) |
| IYT | 9.44% (4.15x) |
| EXPD | 9.75% (4.34x) |
| CHRW | 6.04% (2.52x) |

**Bookend: 2010‑09‑30 → 2026‑10‑08 (16.02 yrs), TR**

| Benchmark | TR |
|---|---|
| S&P 500 | 14.80% (9.13x) |
| IWM | 10.71% (5.11x) |
| IJH | 11.54% (5.76x) |
| XLI | 13.14% (7.23x) |
| ^DJT price | 9.66% (4.38x) |
| EXPD | 10.76% (5.14x) |
| CHRW | 6.90% (2.91x) |

**Bookend: 2011‑12‑30 → 2026‑10‑08 (14.77 yrs), TR**

| Benchmark | TR |
|---|---|
| S&P 500 | 15.18% (8.07x) |
| IWM | 10.86% (4.59x) |
| IJH | 11.77% (5.18x) |
| XLI | 13.53% (6.52x) |
| IYT | 10.22% (4.21x) |
| EXPD | 12.53% (5.72x) |
| CHRW | 7.34% (2.85x) |

**Recent volatility that affects the exit-date comparison** (same Yahoo sources):
- Small caps and transports fell sharply in Q3 2026. ^RUT went from 3,024.37 (June 30, 2026) to 2,794.13 (October 8, 2026), and IWM is 9.0% below its August 2026 high.
- IYT went from 86.75 (June 30, 2026) to 79.94 and is 11.2% below its July 2026 high.
- CHRW fell from 188.34 (June 30, 2026) to 141.34.
- EXPD rose from 162.98 to 193.71 over the same period.

### Inferences
- The most relevant **"opportunity cost" benchmark** for a family holding company is the S&P 500 TR, because that is the passive alternative. The **"like-for-like risk" benchmarks** are small caps and transports/logistics: OIA is a small, private, cyclical freight forwarder, comparable to a sub-scale EXPD or CHRW. Those benchmarks set a much lower bar, at roughly 10–11.5%/yr and 4.5–5.2x.
- Because the Q3 2026 sell-off in small caps and transports was so sharp, the peer hurdle depends heavily on the exit date. For example, the 2011 → June 30, 2026 Russell 2000 TR was 11.57% (5.07x), against 10.79% (4.70x) at October 8. Freight-forwarder exit multiples also tend to move with these listed peers, so the sale price and the benchmark are partly correlated.
- XLI (Industrials) sits between the two groups at about 13.6% / 6.9x.

### Gaps
- No official total-return series was pulled for the Russell 2000 (^RUTTR) or the S&P 400 TR. The ETF adj_close values are slightly low because of expense ratios: about 0.19%/yr for IWM and about 0.05%/yr for IJH.
- IYT tracks the S&P Transportation Select Industry index, not the DJTA itself. It is used here as the TR proxy, and the ^DJT price index is shown alongside it.
- No index for private freight forwarders or logistics M&A was located.

---

## Q4. What did private equity (Cambridge Associates; vintage-2011 buyout funds) return, and what is the standard PE hurdle rate?

### Takeaway
- **15-year horizon:** the Cambridge Associates US PE Index returned **15.71%/yr net** over the 15 years to September 30, 2025, beating its Russell 3000 mPME (14.68%) by 103 bps and its Russell 2000 mPME (11.18%) by about 454 bps.
- **Vintage-2011 funds:** the only top-quartile net IRR found is **~19.2%** (Dakota, as of June 30, 2026). Medians are about **13.7%** (an older Buyouts snapshot) and **17.6%** (PitchBook, undated); they are not comparable.
- **Hurdle rate:** the standard PE preferred return is **8%**.

### Cited Findings
- **CA US PE Index**, pooled horizon IRR net to LPs, as of September 30, 2025:

  | Horizon | CA US PE Index | mPME MSCI ACWI | mPME Russell 3000 | mPME Russell 2000 |
  |---|---|---|---|---|
  | 1‑yr | 8.31% | 17.77% | 17.34% | 10.87% |
  | 5‑yr | 14.08% | 14.43% | 16.03% | 11.37% |
  | 10‑yr | 14.99% | 12.96% | 15.02% | 10.01% |
  | **15‑yr** | **15.71%** | 11.21% | **14.68%** | **11.18%** |
  | 20‑yr | 13.40% | 9.11% | 11.04% | 8.69% |
  | 25‑yr | 11.95% | 8.37% | 9.57% | 8.56% |

  The index covers 1,720 US PE funds from vintages 1986–2025. The 15-year mPME value-add is +450 bps vs. ACWI, +103 bps vs. Russell 3000 and +454 bps vs. Russell 2000. — [Cambridge Associates, US Private Equity Index and Selected Benchmark Statistics, Sept 30, 2025 (PDF)](https://www.cambridgeassociates.com/wp-content/uploads/2026/02/WEB-2025-Q3-USPE-Benchmark-Book.pdf)
- The free CA benchmark book does **not** include the since-inception-by-vintage-year table. CA says those reports are distributed only to clients and data contributors, or sold through IHS Markit (now S&P Global). — [same CA PDF](https://www.cambridgeassociates.com/wp-content/uploads/2026/02/WEB-2025-Q3-USPE-Benchmark-Book.pdf); [CA Private Investment Benchmarks](https://www.cambridgeassociates.com/private-investment-benchmarks/)
- **Vintage-2011 top-quartile net IRR: 19.2%.** The vintage-2010 figure is 18.8% and vintage-2012 is 18.0%. The source is "Dakota Marketplace Performance Benchmarks, as of June 30, 2026." No 2011 median is given; the article quotes a general mature-buyout median of "13 to 16% (Cambridge Associates US PE/VC Benchmark, 2024)." — [Dakota](https://www.dakota.com/resources/blog/top-quartile-private-equity-irr-benchmarks-by-vintage-year)
- **Vintage-2011 domestic buyout/turnaround funds:** top quartile 20.3%, median 13.7%, bottom quartile 7.6%. This is an **older snapshot** of interim IRRs, mostly through about 2015. — [Buyouts Insider: Cortec and Monomoy lead 2011 vintage All-Star funds](https://www.buyoutsinsider.com/cortec-and-monomoy-lead-2011-vintage-all-star-funds/)
- **PitchBook:** the 2011 vintage was a "particularly profitable crop," with a **median 17.6% IRR**. The date and the definition (net or gross, buyout or all PE) are unclear in the snippet. — [Institutional Investor](https://www.institutionalinvestor.com/article/2bsvsej8z8fel46jo3bb4/portfolio/platinum-equity-monomoy-capital-delivered-top-buyout-returns-in-past-decade-pitchbook-says)
- **The 8% hurdle rate:**
  - The ILPA Model LPA defines "Preferred Return" with a bracketed [8]% placeholder, compounded annually.
  - About 80% of buyout funds reportedly use exactly 8%, a figure attributed to the Goodwin terms database but not verified.
  - Worked example: $10M at an 8% hurdle requires about $14.69M after 5 years.
  - Sources: [Angel Investors Network](https://angelinvestorsnetwork.com/alternative-investments/hurdle-rate-private-equity-preferred-return-explained-2026); [Advisor Perspectives: How to assess PE waterfalls](https://www.advisorperspectives.com/articles/2019/07/01/how-to-assess-private-equity-waterfalls). These are secondary and marketing-grade sources, but the 8% norm is widely corroborated.

### Inferences
- **PE-style bar for a 15-year hold:** about **15–16% net** (the CA index at 15.71%) for a "median-ish" pooled outcome, and about **19–20%** for top-quartile 2011-vintage funds. A *net-to-LP* PE return is after fees and carry. A family office that owns OIA directly bears no fund fees, so its *gross* deal IRR should arguably beat these net figures, which makes them a reasonable "did we do as well as hiring a PE fund" comparison.
- The 8% preferred return is a **floor** (the point where GP carry starts), not a market benchmark. Over 2011–2026, 8% compounds to only about 3.2x, far below the 8.4x of the S&P 500 TR.
- An mPME versus the Russell 2000 of about 11.2% (15-year) agrees closely with the IWM point-to-point result (about 10.4–10.8%). That supports small caps as the "risk-matched public" bar.

### Gaps
- No primary (Cambridge, or Burgiss/MSCI Private Capital Solutions) **vintage-2011 buyout** median or top-quartile **net IRR and TVPI** as of 2025–2026 was obtainable for free; those tables are licensed. The figures above come from secondary sources with different datasets and dates.
- No reliable 2011-vintage TVPI was found. Secondary blogs cite 1.8–2.2x for 2010–2014 vintages without verifiable sourcing, so that range is not used here.

---

## Q5. What multiple must Lacy's 2026 sale proceeds reach to beat each benchmark, and how should dividends and add-on investments be handled?

### Takeaway
For a **single equity check on August 31, 2011** with no interim cash flows, the net equity proceeds at an October–December 2026 exit must exceed these multiples of the original check:
- about **8.4x** to beat the S&P 500 TR
- about **6.9x** to beat Industrials
- about **5.2x** to beat the MidCap 400, Expeditors or the CA-PE-like 12%
- about **4.5–4.7x** to beat small caps and transports
- about **3.2x** to clear an 8% hurdle

If there were interim dividends or follow-on equity for add-ons, compare using **IRR on all dated cash flows** against a **PME** (each cash flow invested in the index).

### Cited Findings
- The benchmark multiples to October 8, 2026 come from Q2 and Q3 above (Yahoo Finance via the MCP tool): S&P 500 TR 8.39x, XLI 6.88x, IJH 5.22x, EXPD 5.18x, IWM 4.70x, IYT 4.52x and CHRW 2.83x.
- The hurdle formula is **Required multiple = (1 + r)^t**, where t is years from the equity check to the exit. Values from August 31, 2011:

  | Exit date | t (yrs) | 8% | 10% | 11% | 12% | 13% | 14% | 15% | 16% | 20% |
  |---|---|---|---|---|---|---|---|---|---|---|
  | 2025‑12‑31 | 14.34 | 3.01x | 3.92x | 4.46x | 5.08x | 5.77x | 6.54x | 7.42x | 8.40x | 13.65x |
  | 2026‑06‑30 | 14.83 | 3.13x | 4.11x | 4.70x | 5.37x | 6.13x | 6.98x | 7.95x | 9.04x | 14.94x |
  | 2026‑10‑08 | 15.11 | 3.20x | 4.22x | 4.84x | 5.54x | 6.33x | 7.24x | 8.26x | 9.41x | 15.70x |
  | 2026‑12‑31 | 15.34 | 3.25x | 4.31x | 4.95x | 5.69x | 6.52x | 7.46x | 8.53x | 9.74x | 16.38x |

  Values from December 31, 2010, for the 2010 dating: to 2026‑12‑31 (16.0 yrs), 8% → 3.43x, 10% → 4.59x, 12% → 6.13x, 14% → 8.14x and 15% → 9.36x. These are computed directly; no external source is needed for the arithmetic.
- **PE-style bars converted to multiples** (August 31, 2011 → December 31, 2026):
  - CA US PE 15-year index rate of 15.71% → about **9.4x**
  - top-quartile 2011 vintage at 19.2% → about **14.8x**
  - median at about 13.7% → about **7.1x**
  - Rates: CA 15.71% from [CA PDF](https://www.cambridgeassociates.com/wp-content/uploads/2026/02/WEB-2025-Q3-USPE-Benchmark-Book.pdf); 19.2% from [Dakota](https://www.dakota.com/resources/blog/top-quartile-private-equity-irr-benchmarks-by-vintage-year); 13.7% from [Buyouts Insider](https://www.buyoutsinsider.com/cortec-and-monomoy-lead-2011-vintage-all-star-funds/). The multiples are computed as (1+r)^15.34.
- **The PME method** is what Cambridge uses: buy and sell index "shares" on the private fund's cash-flow dates, then compare. — [CA PDF methodology page](https://www.cambridgeassociates.com/wp-content/uploads/2026/02/WEB-2025-Q3-USPE-Benchmark-Book.pdf)

### Inferences

**How to build the real hurdle with interim cash flows.** This applies to dividends to LDI, management fees upstreamed, and follow-on equity for the roughly 11 add-ons.

1. **List every dated equity cash flow between LDI and OIA.**
   - Contributions: the initial 2010/2011 equity, any equity funding for add-ons (2013 U.S. Worldwide Logistics, American Cargo Express, and the 2024–2026 deals), and any capital injections. Record these as negative.
   - Distributions: dividends, recap dividends, and management or monitoring fees paid to LDI. Record these as positive.
   - Exclude add-ons funded by OIA's own cash flow or by OIA-level debt. Those are already reflected in exit equity value and are not new LDI capital.
2. **Actual deal IRR:** solve Σ CF_t / (1+IRR)^(t) + Exit Equity Proceeds / (1+IRR)^(T) = 0, for example with XIRR in Excel. Compare that IRR with the benchmark CAGRs above (15.1% S&P TR, about 10.8% Russell 2000, about 11.5% EXPD, and so on).
3. **PME-based dollar hurdle.** This is the exact figure the 2026 price must clear.
   - Hurdle exit proceeds = Σ Contributions_t × (I_exit / I_t) − Σ Distributions_t × (I_exit / I_t), where I is the total-return index level (for example SPXTR).
   - Each contribution is grown at the index's actual return from its own date. Each distribution is credited as if it had been reinvested in the index.
   - Kaplan–Schoar PME = [Σ Dist_t × (I_exit/I_t) + Exit proceeds] / [Σ Contrib_t × (I_exit/I_t)]. A PME above 1.0 means OIA beat the index.
4. **Why the timing of add-on capital matters.**
   - Capital invested in 2024–2026 has had little time to compound. A 2025 dollar needs only about 1.0–1.2x by exit to match the S&P 500, while the 2011 dollar needs about 8.4x.
   - A simple "total proceeds ÷ total invested" multiple (MOIC) therefore **understates** performance against the index when much of the capital went in late. A single-date (1+r)^15 test **overstates** the hurdle.
   - Conversely, dividends paid early count heavily. A $1 dividend in 2014 counts as roughly 5–6x at exit under a PME, because it is credited with S&P TR growth from 2014.
   - The IRR-vs-CAGR comparison is only exact for a single in/out cash flow. With multiple flows, use PME (or mPME) as the authoritative test and IRR vs. the index's IRR on the same cash-flow schedule.
5. **Apples to apples.**
   - The hurdle applies to **net equity proceeds to LDI**: enterprise value minus net debt, transaction fees, escrows and holdbacks, and any minority or rollover holders' share. LDI took "majority control," so founder Yoshida and others may have retained a stake.
   - Index returns are pre-tax. If the owners want an after-tax comparison, tax both sides consistently. Index dividends are taxed annually, while the private gain is taxed at exit.
6. **Illustrative example, with hypothetical numbers.** Assume $10M of LDI equity on August 31, 2011 and no other flows. The 2026 equity proceeds must exceed about $84M to beat the S&P 500 TR (8.39x as of October 8, 2026), about $47M to beat the Russell 2000 TR (4.70x), about $52M to beat EXPD TR (5.18x), and about $32M to clear an 8% compounding hurdle (3.20x).

### Gaps
- LDI's actual equity amounts, add-on funding sources and dividend history are not public. The dollar hurdle cannot be computed until the owners supply the cash-flow ledger.
- The index levels on a future closing date are unknowable. For a late-2026 close, use the October 8, 2026 multiple adjusted by the index's change between October 8 and the close date.
