# Channel publishing playbook

## Ghost

**Publication name:** Market State Lab  
**One-line description:** Five market-moving developments, one regime map, and one testable quant idea—built for systematic traders using MATLAB and AI.  
**Editorial focus:** Finance, with Technology as a secondary theme  
**Subscription model:** Free Quant Market Brief; paid subscriptions off  
**Website:** https://market-state-lab.ghost.io/  
**Email signup:** [Subscribe free](https://market-state-lab.ghost.io/?utm_source=github&utm_medium=repository&utm_campaign=qmb_growth#/portal/signup)  
**Channel role:** Email delivery, public issue archive, and the canonical subscriber list.

### About copy

Market State Lab is a premarket intelligence publication for systematic traders, MATLAB users, and technically curious market practitioners. The free Quant Market Brief covers exactly five consequential developments, then translates them into market-state, factor, liquidity, options, execution, and model-risk implications. Every issue distinguishes fact from inference, timestamps market data, and links to a public methodology and GitHub companion.

Quant Lab—a deeper weekly reproducible research edition—will be added later. The daily brief remains free.

Research and education only; not individualized financial advice.

### Recommended Ghost settings and publication checks

- Keep Quant Market Brief posts publicly accessible and email subscriptions free.
- If Ghost member comments are enabled, moderate promotional trade calls.
- Publish each full issue on the Ghost website and send its newsletter edition to subscribed email recipients.
- Before sending, preview the web and email editions, verify source and companion links, and recheck the delivery warning and recipient count.
- Add GitHub methodology, disclosures, and editorial/corrections policy links to Ghost navigation or the About page.
- Use `masthead.png` as the wordmark and `social-card.png` as the share image.

## LinkedIn

Maintain the [Market State Lab newsletter](https://www.linkedin.com/newsletters/market-state-lab-7492957414569324544/) with the description:

> A five-story, decision-ready premarket brief on AI, systematic trading, SPY/QQQ and options, the Fed, and major technology—plus regime, factor, execution, MATLAB, and model-risk notes.

Publish a condensed native edition with the 60-second decision panel first, then link to the full Ghost issue and the matching dated GitHub companion. Include a free email signup link to `https://market-state-lab.ghost.io/#/portal/signup` in the newsletter and supporting post. Avoid posting only an outbound link; include enough native analysis to earn saves and discussion.

## GitHub

**Repository:** `market-state-lab`  
**Description:** Source-backed Quant Market Briefs, MATLAB companions, methods, and market-state research.  
**Topics:** `quantitative-finance`, `matlab`, `algorithmic-trading`, `market-microstructure`, `reinforcement-learning`, `options`, `market-regime`

Keep the default branch readable. Each issue should have one Markdown file, one source-data snapshot, original charts, and any MATLAB companion. Use commit history for corrections. Include the Ghost email signup link in each new companion; keep existing historical dated issues unchanged during channel-workflow updates.

## Cross-channel publication workflow

1. Prepare the Ghost issue, LinkedIn native newsletter and supporting post, and dated GitHub companion from the same verified brief. Match the edition date, title, facts, timestamps, and disclosures.
2. Commit the GitHub companion, publish the Ghost web/email edition after the delivery checks, and publish the LinkedIn newsletter and post. Link each channel to the matching edition or companion where appropriate.
3. Verify the published URLs and signup links. Use `https://market-state-lab.ghost.io/#/portal/signup` as the signup destination; add channel-specific UTM parameters before `#/portal/signup`, using the same edition campaign across channels.
4. Record publication and email-send status separately, and reconcile any corrections across the affected channels.

## Measurement

Track channel-specific metrics weekly:

- Ghost: net growth in email-subscribed members, recipients and delivery status per send, open rate and click-through where available, unsubscribes, and reader replies. Record counts alongside rates; treat opens as directional because email privacy features can distort them.
- LinkedIn: impressions, saves, meaningful comments, profile follows, and newsletter subscribers
- GitHub: unique visitors, stars, clones, issue discussions, and MATLAB file views

Optimize for reader trust and retained attention before monetization.
