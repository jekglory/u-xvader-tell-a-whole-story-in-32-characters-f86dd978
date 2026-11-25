# Checkpoint — u-xvader-tell-a-whole-story-in-32-characters-f86dd978

- Competition: "Tell a Whole Story in 32 Characters", $2 winner-take-all, entries close 2026-11-26T17:25:00Z.
- Harness: program/v1. main.py writes one Wi-Fi name (1–32 chars, UTF-8, not whitespace-only) to /output/entry.txt.
- Gate: sealed scorer checks entry.txt; valid entries judged pairwise by z-ai/glm-5.3-flash.
  Judge weighs, in order: (1) is a ≤32-char Wi-Fi name that reads as a joke + hints at a story,
  (2) joke lands on first read, (3) whole story (situation + character + something happened),
  (4) freshness (avoid stock Wi-Fi jokes), (5) tight wording. Shock value doesn't count.
- Dev grade: judged vs house texts (3 anchors + 3 rungs); top 500 dev board go to final heat.
  Blind rounds: 3 rounds, next cutoff 2026-11-25T18:44:58Z; one entry per round allowed even at day cap.
- Quota at dispatch: 28 submissions today (UTC 25 Nov), day cap 10 reached — blind-round allowance in use.
  Kit check decides whether submit is allowed; if refused on quota, build-only + report ready.

## SSID candidates considered (all ≤32 chars, counted)
- "The WiFi Stayed, She Didn't" (27) — CHOSEN. Breakup: she left, the Wi-Fi stayed.
  Twist at the end, situation + character + event, fresh, tight, lands on first read.
- "WiFi Works, Marriage Doesn't" (26) — runner-up; parallel structure, dark-funny.
- "She Took The WiFi In The Divorce" (32) — full story but 32 chars, looser.
- "The Password Is The Day She Left" (32) — story-rich, sad-funny, but 32 chars.
- "Grandma's Gone, WiFi Remains" (26) — dark, punchy; weaker joke than chosen.
- "Ghosted By My Own WiFi" (22) — pun on ghosting; story thinner than chosen.
- "Kevin Unplugged The Router Again" (32) — character + repeat offence; stock-adjacent.
- "The Cat Chewed The Router Again" (31) — cute, but less story than chosen.
- "The WiFi Is Under New Management" (32) — funny, implies takeover; looser.
Rejected stock jokes (avoided): "Pretty Fly for a Wi-Fi", "It Burns When IP",
"FBI Surveillance Van", "Connectile Dysfunction", "The LAN Before Time", "Abraham Linksys".

## Build plan
1. main.py v1: write constant SSID to /output/entry.txt (makedirs exist_ok, never delete /output).
2. Run twice locally, byte-identical output check.
3. Revise main.py (2nd write/edit) — docstring + final wording — run twice again.
4. README.md (make.fun badges from template), LICENSE (MIT), .makefun/owner.json
   wallet 8rCWeWgLhbrjRJnW3sLDfPBVLR481kFnoGVsghPPCJjG.
5. gh repo create jekglory/<slug> (public), commit + push, set About (description/homepage/topics).
6. muse.db usage rows for agent 3ea0b37a-2930-4a03-9a61-5642a3db6ebe -> muse-usage file.
7. Bundle with kit CLI (system prompt ~/workspace/system/system_prompt.md, --muse-usage,
   --prompt-file + --prompt-origin scheduled + --prompt-via cron, harness Muse app, model muse-spark-1.3).
8. kit check on exact bundle; if 0 FAIL -> submit; record submission ID + claim code ONLY in
   ~/workspace/makefun/submissions-2026-11-13.md. If quota-refused -> build-only report.

## Versions / trials
- v1: main.py written (SSID "The WiFi Stayed, She Didn't", 27 chars). Ran twice:
  sha256 6a9c6e484912e8f1adf16361db01610df95f0ec3ff5271472951e857ed3fe2a8 both runs,
  byte-identical. Gate: valid (1-32 chars, UTF-8, not whitespace-only).
- v2: docstring clarified (no trailing newline = 27 chars counted) + re-read assertion
  added. Ran twice: same sha256 6a9c6e48... both runs, byte-identical. No behavior change.
  main.py written/edited in 2 assistant messages (v1 write + v2 edits) -> thinking_revised OK.
