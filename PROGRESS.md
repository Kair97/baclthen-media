# PROGRESS — журнал шагов (читать ПЕРВЫМ при продолжении работы)
_Обновляется после каждого шага. Последнее обновление: 22.10.2026 15:10 (Кызылорда)_

## Как продолжить, если сессия прервалась
1. Прочитай этот файл (он же лежит в Project «youtube» как `claude/PROGRESS.md` и на ноутбуке `Desktop\koz\YOUTUBE_CLAUDE\PROGRESS.md`).
2. Найди первую строку со статусом ⏳ или ❌ в «Текущие задачи» — с неё и продолжай.
3. Технические детали — `claude/working-notes.md` и vault `youtube_claude_vault/Lessons/Problems & Fixes.md`.

## Где что лежит
- Ноутбук: `Desktop\koz\YOUTUBE_CLAUDE\channels\01_PriceDecoded\` и `\02_BackThen\` (videos/epXX_*/video.mp4, thumbnail.jpg, metadata.txt, subtitles_en.srt).
- Контейнер Claude (пропадает при новой сессии!): `/home/claude/pipeline/` — рендеры `render_v2.py` (Back Then), `render_pd2.py` (Price Decoded v2), эпизоды `bt02/`, `pd02/`.
- Studio: Back Then = аккаунт dbatyr08 (`?authuser=1`), канал UCNh5AC5k6i_8TyXZxJhZ3ng. Price Decoded = glovopromo4 (`authuser=0`), канал UCAvdyFFYSkZhXY12fYJd2lw.
- Flow: `flow.google.com/u/1/` (dbatyr08, Pro). Проект PD ep02: `/u/1/project/749209f6-4332-4e69-886f-7ad5f38b533e`. Проект BT ep02: `/u/1/project/78bc0dc1-7976-4e5e-bf2e-7f988de52876`.

## Текущие задачи
| # | Задача | Статус |
|---|---|---|
| 1 | BT ep02 «What Did Romans Actually Eat for Breakfast?» — опубликовать | ⏳ 14:45 черновика нет (обрыв на 81%). Окно загрузки открыто снова, ждём, когда пользователь выберет `ep02_roman_breakfast\video.mp4`; потом я заполняю поля по metadata.txt (заголовок, описание, теги, не для детей, ИИ-контент «нет», English US, Образование) и довожу до шага «Доступ». НЕ нажимать Escape в окне загрузки — открывает «Отменить загрузку». |
| 2 | PD ep02 «How Costco Makes Money Selling $1.50 Hot Dogs» | ⏳ Сценарий ✅, озвучка 8:09 ✅, 26 картинок ✅ (`pd02/img`), рендер с заглушками ✅, превью ✅ (thumbnail.jpg / thumbnail_B.jpg). Клипы: 14:55 скачиваются в ~/Downloads как pd02_c01..c08.mp4 (сопоставление по названию карточки: grab items=c05, pushes cart=c03, rotisserie=c02, forklift=c04, membership card=c06, rush to product=c07, hot dog and soda=c08, picks up hot dog=c01). Осталось: дождаться загрузки клипов → `pd02/vid/` → перерендер → сжать <30 МБ → сохранить в `01_PriceDecoded\videos\ep02_costco_hot_dog\` → отправить пользователю → загрузка в Studio PD. |
| 3 | PD ep01 «Car Insurance…» | ⏳ черновик в Studio: нужно поставить категорию «Образование» и расписание. |
| 4 | Подтверждение телефона на обоих каналах | ⏳ делает пользователь (нужно для своих превью, субтитров, ссылок). |

## Журнал шагов
- 16–17.10: созданы каналы PD и BT, брендинг, PD ep01 и BT ep01 смонтированы. BT ep01 опубликован (47 просмотров за 4 дня, CTR 1,6%, ср. просмотр 2:27/5:40).
- 18.10: BT ep02 смонтирован (pipeline v2: живой Том, караоке-субтитры, SFX), сохранён на ноутбук.
- 22.10 11:51: пользователь попросил опубликовать BT ep02 и сделать новый ролик для PD.
- 22.10 12:00–12:20: PD ep02 — исследование (Costco FY2026 10-K/отчёт, ABC, The Hustle, FMI, Kroger), сценарий 49 битов, озвучка, 26 картинок Flow (через нового агента Flow), 8 видео заказаны (96 кредитов).
- 22.10 12:10: BT ep02 — пользователь выбрал файл, я заполнил все поля до шага «Доступ». Субтитры требуют подтверждения личности — пропущено.
- 22.10 ~12:20: связь с ноутбуком пропала, вкладки Studio/Flow закрылись.
- 22.10 14:38: пользователь вернулся, просит продолжить и вести этот журнал.
- 22.10 14:45: BT ep02 — черновика в Studio нет, окно загрузки открыто заново.
- 22.10 14:55: PD ep02 — 8 клипов найдены во Flow, скачиваются (медленная сеть).
- 22.10 15:00: Studio (dbatyr08) требует повторной проверки личности при открытии окна загрузки. Пароль + 2 подтверждения на iPhone сделаны пользователем, но страница studio.youtube.com/reauth во встроенном браузере зависает на «Идет обработка» (ждёт всплывающее окно-opener, которого в панели нет) → цикл. ВЫВОД: загрузку BT ep02 делать в обычном Chrome (вход dbatyr08), не во встроенном браузере. Не просить пользователя подтверждать снова в панели.
- 22.10 15:00: PD клипы c01,c02(скачан, не застейджен),c03,c04,c05 есть; c06,c07,c08 — ошибка загрузки, повторить по одному.
- 27.10 00:35: пользователь просит полный автопилот (создание + публикация без него). Сделано: `autopilot/uploader.py` (YouTube Data API, очередь queue/<channel>/ → published/), `autopilot/НАСТРОЙКА.md`, `meta_example.json`. Ноутбук был офлайн — файлы лежат только в контейнере, при подключении скопировать в Desktop\koz\YOUTUBE_CLAUDE\autopilot\. Дальше: пользователь делает client_secret.json + `--login` для обоих каналов + schtasks; я создаю регулярную задачу «завод» (требует ноутбук для Flow).
- 27.10 11:15: АВТОПИЛОТ ЗАПУЩЕН. Metricool (бренд blogId 7680884, владелец dbatyr08, tz Asia/Qyzylorda): YouTube Back Then + TikTok @backthen.doodles подключены. Хостинг видео: публичный репо GitHub Kair97/baclthen-media (raw.githubusercontent.com/Kair97/baclthen-media/main/<path>); релизы GitHub запрещены сессией — класть файлы коммитом, после планирования удалять (Metricool копирует видео в static.metricool.com). Запланированы 3 Shorts BT ep02 (YouTube Shorts + TikTok, 21:00 Кызылорда = 12:00 ET): 27.10 garum (id 407467809), 28.10 vomitorium (407467973), 29.10 French toast (407467983). Instagram и Price Decoded в Metricool ещё не подключены. Zapier подключён, но не нужен.
