# Back Then — EP03: How Did Vikings Survive Winter?  (pipeline v2)
# Status: scripted 27.10.2026 (cloud run). Needs Flow assets: IMG s01..s34 (+z crops) and VID v01..v04 (4 clips = 48 credits).
VOICE = "am_puck"
SPEED = 0.92
STYLE = ("Hand-drawn doodle cartoon, thick black ink outlines, flat soft watercolor colors, warm cream paper texture background, "
         "simple funny explainer style, 16:9, no text, no letters, no words.")
TOM = ("Tom, a simple doodle character with a perfectly round white head, two big black dot eyes, tiny expressive mouth, no nose, "
       "thin black stick arms and legs, wearing a thick brown wool Viking tunic, grey wool trousers, a fur-lined cloak pinned at one shoulder "
       "and a simple grey wool cap")
VSTYLE = ("Animated hand-drawn doodle cartoon, thick black ink outlines, flat soft watercolor colors on warm cream paper texture, "
          "gentle line boil like traditional 2D animation, static camera, no text.")

# shot types: v=<flow video key>, i=<flow image key>, t=<kinetic title>
# Each beat: text, shots (list), cap (sticky caption), sfx ('whoosh','pop','ding','scratch','boing'), chapter
BEATS = [
  # ---------------- HOOK ----------------
  dict(text="It's January in Norway, around the year nine hundred. The sun barely clears the mountains before it sets again. It's freezing. And Tom has months of winter still ahead of him.", shots=["v:v01", "i:s01"], sfx="whoosh", chapter="The hook"),
  dict(text="No heating. No supermarket. No electric light. Just a wooden house, a fire, and whatever food he managed to store before the snow came.", shots=["i:s02", "t:NO HEAT. NO SHOPS. NO LIGHT."], sfx="scratch"),
  dict(text="And in the far north of Norway it's even worse. At the peak of the polar night, the sun doesn't rise at all. Not for a few hours. For whole days.", shots=["i:s01z"], cap="Polar night"),
  dict(text="So how did Vikings actually survive winter? By the end of this video, you'll know what they ate, how they stayed warm, what they did all day in the dark, and a Viking winter word you probably say every single year.", shots=["i:s03", "t:A VIKING WORD YOU STILL USE"], sfx="ding"),

  # ---------------- WINTER BEGINS ----------------
  dict(text="First, to a Viking, winter wasn't just a season. It was half of the year.", shots=["t:HALF THE YEAR"], sfx="pop", chapter="Winter was half the year"),
  dict(text="The Old Norse year had only two seasons. Summer and winter. And when Vikings counted years, they usually counted winters. A Viking wouldn't say he was twenty years old. He'd say he had lived twenty winters.", shots=["i:s04", "i:s04z"], cap="Age = winters survived"),
  dict(text="Winter began in late October, with a festival called the winter nights. And the month that followed had a brutal job.", shots=["i:s05"]),
  dict(text="In the old Icelandic calendar, its name refers to the half-digested contents of animal guts. Because this was slaughter month.", shots=["i:s06", "t:SLAUGHTER MONTH"], sfx="scratch"),
  dict(text="Here's why. Every animal that stayed alive all winter had to be fed with hay. And hay was the most precious thing on the farm.", shots=["v:v02"], cap="Hay = life"),
  dict(text="Hayfields were walled in and kept close to the house. If the hay ran out before spring, the animals starved. And then, so could you.", shots=["i:s07"]),
  dict(text="So in autumn, farmers made a hard choice. Keep the best animals to breed and milk. Slaughter the rest, and turn them into food for the dark months.", shots=["i:s08", "i:s08z"]),

  # ---------------- LONGHOUSE ----------------
  dict(text="Now, let's step inside Tom's house. Because the Viking longhouse was basically a survival machine.", shots=["t:THE SURVIVAL MACHINE"], sfx="whoosh", chapter="Inside the longhouse"),
  dict(text="A typical longhouse was five to seven meters wide and anywhere from fifteen to seventy-five meters long. The reconstructed chieftain's house at the Lofotr Viking Museum is over eighty meters long.", shots=["i:s09", "i:s09z"], cap="Up to 80 m long"),
  dict(text="Where timber was scarce, like in Iceland, the walls were built from thick blocks of turf. That's basically insulation you could cut out of the ground.", shots=["i:s10"], cap="Turf = insulation"),
  dict(text="Down the middle of the house burned a long hearth. That one fire did everything. It cooked the food, heated the room, and gave most of the light.", shots=["v:v03"]),
  dict(text="There was no chimney. The smoke just drifted up and out through a hole in the roof. So in winter, the inside of a longhouse was warm, dark, and very, very smoky.", shots=["i:s11"], sfx="boing"),
  dict(text="And here's a twist. Tom wasn't alone in there.", shots=["t:WHO'S IN THE HOUSE?!"], sfx="scratch"),
  dict(text="In many longhouses, one end was reserved for the animals in winter. Cows, sheep, all under the same roof as the family. Their body heat helped keep everyone warm.", shots=["i:s12", "i:s12z"], cap="Cows = central heating"),
  dict(text="Families slept on wide wooden benches that ran along the walls, close together. Privacy? Not really a thing.", shots=["i:s13"]),
  dict(text="And for light after dark, they burned oil lamps, little pots with a wick, filled with cod liver oil, or seal or whale oil. Candles were too expensive for most families.", shots=["i:s14"], cap="Fish-oil lamps"),

  # ---------------- CTA 1 ----------------
  dict(text="Quick thing. If you're enjoying Tom's trip through history, hit subscribe. It's free, and it keeps Tom warm.", shots=["i:s15"], sfx="ding", cta=True),

  # ---------------- PANTRY ----------------
  dict(text="So, what did a Viking eat when the fields were buried under snow?", shots=["t:THE WINTER PANTRY"], sfx="pop", chapter="The winter pantry"),
  dict(text="Lots of fish. Herring and salmon were dried, or packed in salt. And in the far north, there was the ultimate winter food: stockfish.", shots=["i:s16"], cap="Salt · smoke · dry"),
  dict(text="Stockfish is cod, hung on wooden racks in the freezing, dry air of northern Norway until all the water is gone. One historian compared it to beef jerky, only fishy.", shots=["v:v04", "i:s17"], cap="Fish jerky"),
  dict(text="And it lasted. Some medieval accounts say stockfish was still edible ten years after it was dried.", shots=["t:STILL EDIBLE AFTER 10 YEARS"], sfx="ding"),
  dict(text="It travelled, too. DNA from cod bones found at Haithabu, a Viking trading town in what's now northern Germany, shows the fish came from the Arctic waters off Lofoten. More than a thousand miles away.", shots=["i:s18", "i:s18z"]),
  dict(text="Then there was dairy. Butter, cheese, buttermilk, and in Iceland, skyr, a thick, sour, yogurt-like cheese that Icelanders still eat today.", shots=["i:s19"], cap="Skyr"),
  dict(text="Sheep's milk mattered more than you'd think. It's rich in vitamin C, which helped people fight scurvy in the dark months, when there was nothing fresh to eat.", shots=["i:s20"]),
  dict(text="Where you lived changed the menu. In Greenland, archaeologists found that poorer Viking farms ate a lot more seal, while richer farms ate more caribou. Winter food was also a sign of how rich you were.", shots=["i:s37"], cap="Poor = seal · rich = caribou"),
  dict(text="And no, it wasn't all bland. Cooks seasoned with onions, garlic, dill and coriander. Though, sadly, not a single original Viking recipe has survived.", shots=["i:s38"]),
  dict(text="By midwinter, the old Icelandic calendar even had a month whose name is about sucking fat. In the darkest weeks, families lived off stored fat and bone marrow.", shots=["i:s21", "t:THE FAT-SUCKING MONTH"], sfx="boing"),

  # ---------------- GETTING AROUND ----------------
  dict(text="But Vikings didn't just hide indoors. Snow and ice were also a highway.", shots=["t:ICE = HIGHWAY"], sfx="whoosh", chapter="Skates and skis"),
  dict(text="Archaeologists have found large numbers of Viking Age ice skates, made from the foot bones of horses and cattle, polished flat on the bottom.", shots=["i:s22", "i:s22z"], cap="Skates made of bone"),
  dict(text="You didn't lift your feet. You stood on the bones and pushed yourself along with a pole tipped with an iron spike. Kids used them. Adults used them. It was transport and fun.", shots=["i:s23"]),
  dict(text="And then, there were skis. In the mountains of southern Norway, melting ice gave up a pair of wooden skis about thirteen hundred years old, from just before the Viking Age. Still with their leather and birch-bark bindings.", shots=["i:s24", "i:s24z"], cap="1,300-year-old skis", sfx="ding"),
  dict(text="Skiing was so important that the Norse had a god for it. Ullr, the god of snow, hunting and the bow. Snorri Sturluson called him the ski-god.", shots=["i:s25"], cap="Ullr, the ski-god"),

  # ---------------- CTA 2 ----------------
  dict(text="By the way, if you've learned something already, a like really helps Tom get out of the snow and onto more screens.", shots=["i:s15b"], sfx="ding", cta=True),

  # ---------------- WORK & PLAY ----------------
  dict(text="So what did Vikings do with all those long, dark days? A lot of work, and a lot of games.", shots=["i:s26"], chapter="Long nights, games and stories"),
  dict(text="Winter was the time to spin wool, weave cloth, mend tools, and repair everything that broke over the summer.", shots=["i:s27"]),
  dict(text="And they played board games. One of them was hnefatafl, the king's table. One side protects a king and tries to sneak him off the board. The other side tries to trap him.", shots=["i:s28", "i:s28z"], cap="Hnefatafl"),
  dict(text="Games could get heated. One saga tells of a stepmother who threw a game piece at a player and knocked out his eye. Another feast in Denmark ended with a man flipping the board, and later being killed.", shots=["i:s29", "t:DON'T FLIP THE BOARD"], sfx="scratch"),
  dict(text="Even Viking raiders played. In the winter of eight seventy-two, the Great Viking Army camped at Torksey in England. Archaeologists there have found more than three hundred lead gaming pieces.", shots=["i:s30"], cap="300+ game pieces"),
  dict(text="Those warriors didn't just play, either. They melted down silver, made tools, sewed and fished in the river. A winter camp was a whole town.", shots=["i:s30z"]),
  dict(text="And then there were the stories. A verse in the Hávamál, the sayings of Odin, puts the winter rule simply: Fire he needs who with frozen knees has come from the cold without.", shots=["i:s31"], cap="Hávamál, stanza 3"),

  # ---------------- YULE ----------------
  dict(text="But the biggest moment of the whole winter came right in the middle of it.", shots=["t:YULE"], sfx="ding", chapter="Yule"),
  dict(text="Yule. A pagan festival that began around the winter solstice, when the sun was at its weakest, and lasted for several nights of feasting and drinking.", shots=["i:s32"]),
  dict(text="And the drinking was serious. According to a saga about King Hakon the Good, every free man had to drink about four gallons of booze over three nights.", shots=["i:s33", "t:4 GALLONS. 3 NIGHTS."], sfx="boing"),
  dict(text="Yule was also when Vikings swore solemn oaths, kind of like New Year's resolutions. Except breaking one was a very big deal, and some were sworn with a hand on a sacrificed boar.", shots=["i:s34"], cap="Oath on a boar"),
  dict(text="And Yule was a time to remember the dead. That's why, even today, many Scandinavians light candles in churchyards in the darkest weeks of the year.", shots=["i:s39"], cap="Candles for the dead"),

  # ---------------- PAYOFF ----------------
  dict(text="Okay. The Viking winter word I promised you. Actually, there are two.", shots=["t:THE WORDS"], sfx="ding", chapter="The words you still use"),
  dict(text="The first is Yule itself. People in the English-speaking world still sing about Yuletide and burn a Yule log, more than a thousand years later.", shots=["i:s32z"]),
  dict(text="The second one you'll say every time it snows. In Old Norse, a long snowshoe was called a skíð, which literally meant a stick of wood. English borrowed it from Norwegian in the eighteen-eighties. Ski.", shots=["t:SKÍÐ → SKI"], sfx="boing"),

  # ---------------- OUTRO ----------------
  dict(text="So, how did Vikings survive winter? Hay for the animals, salt and stockfish for the family, cows for central heating, bone skates for the commute, and one giant party in the darkest week of the year.", shots=["i:s35"], chapter="The verdict"),
  dict(text="Could you survive a winter in a smoky longhouse with a cow for a roommate? Tell us in the comments. And next time on Back Then, Tom goes to work on the pyramids of Egypt.", shots=["i:s36"], cta=True),
]

IMG = {
  "s01": "a snowy Norwegian fjord in midwinter, a tiny pale sun just above the dark mountains, a small wooden Viking farm with smoke rising, very short winter day",
  "s02": "TOM standing in deep snow outside a wooden house, holding an empty basket, shivering, big snowflakes, no shops anywhere",
  "s03": "TOM sitting by a crackling fire inside a dark wooden hall, looking curious at a glowing closed wooden chest",
  "s04": "TOM proudly counting on his stick fingers in front of a row of small snowflake symbols drawn on a wooden wall, birthday cake with candles nearby",
  "s05": "a Viking farm at dusk in autumn, villagers lighting torches and a bonfire, first snowflakes falling, festive but chilly mood",
  "s06": "TOM looking nervous next to a farmer with a wooden bucket and a cow, autumn leaves, a smokehouse in the background, cartoonish not gory",
  "s07": "a small stone-walled hayfield right next to a Viking longhouse, big haystacks, TOM guarding the hay with a pitchfork",
  "s08": "TOM choosing between a few cows and sheep in a pen, scratching his head, a small storehouse with hanging sausages behind him, cartoonish not gory",
  "s09": "a very long Viking longhouse with a curved roof covered in grass turf, snow on the ground, smoke rising from the roof hole, TOM tiny in front of it for scale",
  "s10": "cut-away view of a thick Icelandic turf wall made of stacked grass blocks, warm inside, cold blizzard outside, TOM inside giving a thumbs up",
  "s11": "inside a dark Viking longhouse, smoke curling up toward a hole in the roof, TOM coughing and waving smoke away from his face",
  "s12": "inside a longhouse in winter, cows and sheep in stalls at one end of the room, family sitting by the fire at the other end, warm wavy heat lines rising from the animals",
  "s13": "a Viking family sleeping squeezed together on a wide wooden bench along the wall of a longhouse under fur blankets, TOM squashed in the middle",
  "s14": "a small clay oil lamp with a tiny flame on a wooden shelf, a little cod fish doodle next to it, TOM reading the flame in the dark, cozy",
  "s15": "TOM in his Viking cloak pointing up at a big red subscribe-style button shape with a bell next to it, no text, smiling, snow falling",
  "s15b": "TOM in his Viking cloak giving a big thumbs up next to a giant glowing heart shape, no text, happy, snow falling",
  "s16": "wooden barrels full of salted herring and a rack of drying salmon outside a Viking storehouse, snowy ground",
  "s17": "huge wooden A-frame racks covered with hanging dried cod fish on a snowy Arctic coast, TOM biting a stiff dried fish like jerky",
  "s18": "a doodle map of Scandinavia with a dotted line and a small Viking ship carrying dried fish from the northern coast of Norway down to a trading town on the Baltic, TOM waving from the ship",
  "s19": "a wooden table with a bowl of thick white skyr, a round cheese, a crock of butter and a jug of buttermilk, TOM eating skyr with a wooden spoon",
  "s20": "TOM milking a fluffy sheep into a wooden bucket inside a cozy barn, a tiny sparkling lemon-shaped vitamin symbol floating above the bucket",
  "s21": "TOM happily sucking marrow from a big bone at the fire, his family grinning, deep blue night outside the smoke hole",
  "s22": "two flat polished ice skates made from animal leg bones lying on a museum stand, TOM leaning in amazed",
  "s23": "TOM gliding across a frozen lake standing on bone skates and pushing with a long wooden pole between his legs, kids skating behind him, snowy pine trees",
  "s24": "a pair of long old wooden skis with leather straps lying on melting mountain ice, archaeologists in warm jackets carefully lifting one, TOM peeking over their shoulders",
  "s25": "a tall bearded doodle Norse god on wooden skis holding a hunting bow, gliding down a snowy mountain, TOM watching in awe",
  "s26": "a Viking longhouse at night in a snowstorm, warm orange light glowing from the smoke hole, tiny silhouettes of people inside",
  "s27": "TOM sitting by the fire spinning wool with a drop spindle while a woman weaves on a tall upright loom with stone weights, cozy",
  "s28": "a square wooden board game with a king piece in the center and small round pieces around it, two Vikings concentrating hard, TOM watching",
  "s29": "a furious doodle Viking flipping a wooden game board, game pieces flying through the air, TOM ducking, comic chaos",
  "s30": "a big Viking winter camp beside a river in England, tents and fires, warriors playing board games on barrels, a few men fishing, snowy",
  "s31": "an old storyteller with a long beard telling a story by the fire while TOM and children listen wide-eyed, TOM's knees covered in frost",
  "s32": "a giant Viking Yule feast in a longhouse, long tables full of food, drinking horns raised, candles and a glowing fire, the low winter sun outside",
  "s33": "TOM at a Yule feast staring at an enormous drinking horn bigger than his head, other Vikings cheering, comic exaggeration",
  "s34": "a Viking standing on a bench making a solemn promise with one hand raised and the other hand on a big cartoon boar, the hall silent, TOM watching",
  "s35": "TOM sitting happily by the fire in the longhouse with a cow beside him, a dried fish in one hand, bone skates hanging on the wall",
  "s37": "split scene on a snowy Greenland coast: a small poor turf farm with a family eating seal meat by the fire, and a bigger farm with a family eating caribou, TOM looking between them",
  "s38": "TOM chopping onions and garlic with a tear in his eye next to bunches of dill and coriander, a bubbling pot behind him",
  "s39": "a quiet snowy churchyard at night with many small candles glowing on the snow, TOM holding a little candle, peaceful and gentle mood",
  "s36": "TOM in a white linen kilt standing in the desert sun waving at the viewer, pyramids under construction behind him",
}
# zoomed variants reuse the base image with a tighter crop (handled by the renderer)
for k in ["s01", "s04", "s08", "s09", "s12", "s18", "s22", "s24", "s28", "s30", "s32"]:
    IMG[k + "z"] = None

# 4 clips max (Flow credit limit 50/day = 4 x 12)
VID = {
  "v01": "TOM wakes up under fur blankets on a wooden bench in a dark smoky longhouse, shivers, looks at the tiny sliver of daylight through the smoke hole and pulls the blanket up to his nose",
  "v02": "TOM carries a huge bundle of hay through the snow into the barn end of a longhouse and feeds a hungry cow, which happily munches",
  "v03": "TOM sits by the long central hearth in a longhouse, stirs a bubbling pot hanging over the fire and warms his hands, smoke drifting up to the roof hole",
  "v04": "TOM hangs a cod fish on a tall wooden drying rack on a snowy Arctic shore, then pulls down a stiff dried fish, bites it and chews proudly",
}
