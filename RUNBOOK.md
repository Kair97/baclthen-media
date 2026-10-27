# RUNBOOK — YouTube autopilot (read fully at the start of every scheduled run)

Owner: Kairzhan (writes in Russian; reply to him in Russian). Laptop "kozlaptop" (Windows) is usually ON weekdays 11:00–12:00 Asia/Qyzylorda.
Goal: two faceless US-audience channels that grow and reach monetization. Quality > quantity (YouTube demonetizes mass-produced, repetitive content).

## 0. Hard rules
- Never enter passwords, never create accounts, never complete captchas/verification codes. If a login/verification is needed → log it in PROGRESS and tell the owner.
- Every fact must come from a source you actually opened this run or one already cited in the episode file. No invented numbers, quotes or events. List sources in the description (plain text, no links until the channel is phone-verified).
- No real person's likeness in generated images; no brand logos; Costco-style brands may be named in narration only.
- Flow credits: ≤ 50 per day (Omni 1.1 Flash video = 12 credits per 8-s clip; Nano Banana images = 0).
- Don't spawn subagents. Don't repost the same video twice. Don't delete anything on the owner's laptop.
- Keep `state/queue.json` and `PROGRESS.md` truthful: update them after EVERY finished step (a run can die at any moment).

## 1. Start of run
1. `add_repo` Kair97/baclthen-media (access "push"), clone to /home/claude/baclthen-media, `bash pipeline/setup.sh`.
2. Read `state/queue.json`, `plan/topics.md`, `channels/*.md`. Read the Project doc `claude/PROGRESS.md` (Projects tool) if available.
3. Check the laptop: load `mcp__remote-devices__*` tools and call `Claude_Browser__tabs_context`. Laptop reachable = you can use Google Flow this run.

## 2. Decide what to do (buffer rule)
Target cadence (all times Asia/Qyzylorda; 21:00 = 12:00 ET before Nov 1 / 11:00 ET after; fine either way):
- **Back Then (BT)**: long video **Tue + Fri 21:00**; one Short **every day 21:00**.
- **Price Decoded (PD)**: long video **Mon + Thu 21:00**; one Short **every day 23:00**.
Buffer = long videos already scheduled (or ready to schedule) in the future. **Keep ≥ 4 per channel** and Shorts covered ≥ 7 days ahead.
Priority each run:
1. Anything `rendered` but not scheduled → schedule it (section 6).
2. PD episodes due for upload in the next 24 h (Zapier uploads immediately — see 6b) → upload.
3. Channel with the smallest buffer → advance its next episode one stage: `planned → scripted → assets → rendered → scheduled`.
   - Laptop reachable → do the `assets` stage (Flow) first, it's the bottleneck. Batch assets for 2 episodes if time allows (laptop window ≈ 1 h).
   - Laptop NOT reachable → do cloud-only stages: research + script + TTS for upcoming episodes, render episodes whose assets are in the repo, cut Shorts, schedule.
4. Fridays: weekly review (section 8).

## 3. Script (research → beats.py)
- Pick the next topic from `plan/topics.md` (mark it taken). Research with WebSearch/WebFetch; prefer primary/official sources; current figures must be looked up this run.
- Write `episodes/<channel>/<id>/beats.py` following the reference episodes (`episodes/backthen/bt02/beats.py`, `episodes/pricedecoded/pd02/beats.py`) and `channels/<channel>.md`.
- Length: **1,400–1,800 words** (≈ 9–12 min; must be ≥ 8:00 for mid-roll ads). Structure: 0–5 s grab, 5–15 s promise (open loop paid off at the end), stakes by 30 s, a pattern interrupt every ~30 s, CTA ≈1:00 and ≈ middle, comment question at the end, tease next episode.
- Also write `metadata.txt` (title ≤ 70 chars, description with `{CHAPTERS}` placeholder + sources, 12–15 tags) and `shorts.json` plan (3–4 Shorts of 20–58 s; each must work without context — strong first line).

## 4. Assets in Google Flow (laptop needed) — account dbatyr08 = `https://flow.google.com/u/1/`
- If `episodes/<channel>/<id>/flow_prompts.md` exists, paste its messages as-is (TOM and style already substituted).
- Open a NEW Flow project (button «Новый проект»). Flow now works through its side **agent chat**: put text into `[role=textbox][contenteditable=true]` with `document.execCommand('insertText',false,text)` and press **Return** (real key) to send.
- Images: one message per ≤ 9 prompts: "Generate exactly one image for EACH of the following N prompts (Nano Banana 2.1, 16:9 …). Use each prompt exactly as written … append this style: …" Images cost 0 and need no approval.
- Videos: one message listing [C01]…[C0n] prompts ("8-second video, Omni 1.1 Flash, 16:9, text-to-video"). The agent asks "Сгенерировать N видео за бонусы (12·N)?" → click the `.option-row` whose text is «Одобрить» via JS `.click()`. Max 4 clips/day (credit limit).
- Collect images: the grid is a CDK virtual scroller `.page-container`. Loop `sc.scrollTop=y; sc.dispatchEvent(new Event('scroll'))` in 300-px steps with 600 ms waits, collecting `img[alt^="Карточка"]` src (they're `flow.google.com/asb/...`, full-res 1376×768 WEBP). Download each with fetch→blob→`<a download="<ep>_raw_NN.jpg">`.
- Map images to keys by viewing a contact sheet (they are visually distinct) — never assume order.
- Videos: each card has a short English title. Real-click the card (opens /edit/…), then `document.querySelector('video').currentSrc` → fetch→blob download as `<ep>_<key>.mp4`; go back with the `arrow_back` button. Download clips ONE AT A TIME (parallel fetches fail on the slow network).
- Bring files into the container: `device_stage_files` from `~/Downloads/` (stage 1–4 files per call; if still `.tmp`, wait 30–60 s). Convert WEBP→JPG into `episodes/<channel>/<id>/img/<key>.jpg`, clips into `vid/<key>.mp4`.
- Commit assets to the repo right away (so another run can render them). Missing clip → make a Ken-Burns placeholder from its still (see PROGRESS notes) rather than block.

## 5. Render
- Copy the episode folder to `/home/claude/pipeline/<id>/`, run TTS (`python3 tts.py <id>`), then `python3 render_v2.py <id>` (BT) or `python3 render_pd2.py <id>` (PD). ~1.5× real time on 2 CPUs. Use `LIMIT=4` first for a quick test.
- Check ≥ 8 frames on a contact sheet (character on-model, no garbled text, subtitles readable).
- Fill `{CHAPTERS}` from `out/chapters.txt`. Two-pass encode if a < 30 MB copy is needed for the laptop; for publishing use `out/final.mp4` directly (GitHub file limit 100 MB → if bigger, two-pass to ~95 MB).
- Thumbnail 1280×720 (generate a Flow image with big empty area, add text with PIL; BT: hand-marker style, PD: Inter Black navy/lime). Make an A/B variant.
- Shorts: `python3 make_shorts.py /home/claude/pipeline/<id> shorts.json`.

## 6. Publish
Host files: commit to `media/<id>/` in this repo, push, URL = `https://raw.githubusercontent.com/Kair97/baclthen-media/main/media/<id>/<file>`. GitHub releases are NOT allowed in these sessions.
### 6a. Back Then → Metricool (`createScheduledPost`, blogId **7680884**, timezone Asia/Qyzylorda)
- Long video: providers `[{"network":"youtube"}]`, youtubeData {title, type:"video", privacy:"public", tags, category:"EDUCATION", madeForKids:false, isAiGeneratedContent:false}. Add `videoThumbnailUrl` only if the channel is verified (else omit).
- Shorts: providers youtube + tiktok (+ instagram REEL once connected), youtubeData type "short", tiktokData {privacyOption:"PUBLIC_TO_EVERYONE", isAigc:true, title}.
- Metricool copies media to static.metricool.com at scheduling time → after ALL posts of an item are scheduled, `git rm` the media and push.
### 6b. Price Decoded → Zapier YouTube (`YouTubeV4CLIAPI`)
- Zapier YouTube connections (verified 27.10 with channels?mine=true):
  - **Price Decoded** = connection_id `029408f4-f55a-85f0-bcf1-aa0acf68a877` (channel UCAvdyFFYSkZhXY12fYJd2lw)
  - **Back Then** = connection_id `02a941d2-04c8-812a-b7ee-9e26aef629ba` (channel UCNh5AC5k6i_8TyXZxJhZ3ng)
  ALWAYS pass `connection_id` explicitly — never rely on the default.
- Upload: `execute_zapier_write_action` action `upload_video` with params {title, description, video:<raw GitHub URL>, thumbnail:<raw URL, only if channel verified>, privacy_status, tags:[...], category_id:"27" (Education), made_for_kids:"false", default_language:"en", default_audio_language:"en"}.
  Try scheduling: privacy_status "private" + publish_at "<ISO datetime>". If YouTube rejects publish_at, upload on the publish day with privacy_status "public".
- Raw YouTube Data API is available: GET via `execute_zapier_read_action` action `_zap_raw_request` {method:"GET", url:"https://www.googleapis.com/youtube/v3/...", querystring:{...}, fail_on_errors:"false"}; POST/PUT via `execute_zapier_write_action` same action. Use it for: listing uploads (playlistItems, playlistId = "UU" + channelId[2:]), videos.update (status.publishAt, snippet), analytics checks.
- After a successful upload `git rm` the media and push. Record the videoId in state/queue.json.
- Back Then long videos may also go through Zapier (connection above) if Metricool fails.
- Instagram/TikTok for PD don't exist yet.

## 7. Bookkeeping (after every step)
- `state/queue.json`: status, file paths, publish dates, Metricool post ids / YouTube video ids.
- `PROGRESS.md` (repo) + Project doc `claude/PROGRESS.md`: append one dated line per step.
- Laptop copies when reachable: `Desktop\koz\YOUTUBE_CLAUDE\channels\<channel>\videos\<id>\` (video < 30 MB copy, thumbnail, metadata, srt) and the Obsidian vault `Desktop\koz\YOUTUBE_CLAUDE\youtube_claude_vault\Videos\<ID>.md`.
- End of run: send the owner a short Russian summary (what got scheduled, buffer per channel, anything he must do).

## 8. Weekly review (Fridays)
Metricool `getAnalyticsDataByMetrics` (YouTube/TikTok) + Zapier YouTube `get_report` for PD: views, CTR, average view duration per video. Write findings to the vault `Feedback/` and adjust `plan/topics.md` (more of what works). Report to the owner.
