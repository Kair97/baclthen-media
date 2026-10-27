# Back Then — EP02: What Did Romans Actually Eat for Breakfast?  (pipeline v2)
VOICE = "am_puck"
SPEED = 0.92
STYLE = ("Hand-drawn doodle cartoon, thick black ink outlines, flat soft watercolor colors, warm cream paper texture background, "
         "simple funny explainer style, 16:9, no text, no letters, no words.")
TOM = ("Tom, a simple doodle character with a perfectly round white head, two big black dot eyes, tiny expressive mouth, no nose, "
       "thin black stick arms and legs, wearing a short off-white ancient Roman tunic with a red belt and simple brown sandals")
VSTYLE = ("Animated hand-drawn doodle cartoon, thick black ink outlines, flat soft watercolor colors on warm cream paper texture, "
          "gentle line boil like traditional 2D animation, static camera, no text.")

# shot types: v=<flow video key>, i=<flow image key>, t=<kinetic title>, n=<big number dict>
# Each beat: text, shots (list), cap (sticky caption), sfx ('whoosh','pop','ding','scratch','boing'), chapter
BEATS = [
  # ---------------- HOOK ----------------
  dict(text="It's six in the morning. Rome, the year 79. Tom just woke up, and he is starving.", shots=["v:v01"], sfx="whoosh", chapter="The hook"),
  dict(text="But what's on a Roman breakfast plate might surprise you. Bread dipped in wine. A fistful of olives. And a sauce made from fish guts that have been rotting in the sun for weeks.", shots=["i:s01", "i:s02", "v:v05"], sfx="scratch"),
  dict(text="By the end of this video, you'll know what Romans really ate first thing in the morning, why most of them barely ate breakfast at all, and the one Roman recipe you've probably eaten yourself.", shots=["i:s03", "t:THE ONE RECIPE YOU'VE EATEN TOO"], sfx="ding"),

  # ---------------- SCHEDULE ----------------
  dict(text="First, forget three big meals a day. Romans had three meals, but only one of them really mattered.", shots=["t:3 MEALS. 1 MATTERS.", "i:s04"], sfx="pop", chapter="The Roman meal schedule"),
  dict(text="There was ientaculum, a tiny breakfast. Prandium, a light snack around midday. And cena, the big dinner in the late afternoon. That was the meal Romans actually cared about.", shots=["i:s05"], cap="ientaculum · prandium · cena"),
  dict(text="So breakfast? For a lot of Romans, it was barely a meal. More like a snack you grabbed on your way out the door.", shots=["i:s06", "i:s06z"], sfx="boing"),
  dict(text="And for a lot of men in Rome, the morning wasn't about food at all. It was about the salutatio.", shots=["t:THE MORNING VISIT"], sfx="pop", chapter="The morning hustle"),
  dict(text="At dawn, crowds of clients would line up outside the house of a rich patron, just to greet him and show their loyalty.", shots=["i:s29", "i:s29z"]),
  dict(text="In return, the patron might hand out a small gift of food or a little money. So for some Romans, breakfast was literally whatever the boss handed them at the door.", shots=["i:s30"], cap="Breakfast from the boss"),

  # ---------------- WHAT WAS IN IT ----------------
  dict(text="So what was in that snack? Mostly bread. Often just a chunk of bread with a bit of salt.", shots=["v:v02"], cap="Breakfast = bread", chapter="What was on the plate"),
  dict(text="If you wanted to feel fancy, you'd dip it in wine. Yes, wine. At breakfast. Though Romans usually mixed their wine with water.", shots=["i:s07", "t:WINE. AT BREAKFAST."], sfx="pop"),
  dict(text="Add a few olives, some cheese, maybe raisins or a little honey, and that's a respectable Roman breakfast.", shots=["i:s08"], cap="+ olives, cheese, honey"),
  dict(text="And Romans got up early. The poet Martial wrote it like an alarm clock: Get up! The baker is already selling breakfast to the boys, and the birds of dawn are singing everywhere.", shots=["v:v03", "i:s09"], cap="Bakers at dawn"),

  # ---------------- CTA 1 ----------------
  dict(text="Quick thing. If you're enjoying Tom's trip through history, hit subscribe. Next time he's surviving a Viking winter, and it does not go well.", shots=["i:s10"], sfx="ding", cta=True),

  # ---------------- THE POOR ----------------
  dict(text="Now, that's breakfast for a regular city Roman. But most Romans were not rich. And for them, the real everyday food was puls.", shots=["i:s11"], chapter="What the poor ate"),
  dict(text="Puls was a thick porridge made from grain, like spelt or emmer, boiled in water with a pinch of salt. Ancient writers said early Romans lived on puls long before bread was common.", shots=["i:s12", "i:s12z"], cap="Puls = porridge"),
  dict(text="Rome also handed out free grain. Under the emperor Augustus, around two hundred thousand citizens in the city were on the grain dole.", shots=["i:s31", "t:200,000 PEOPLE. FREE GRAIN."], sfx="ding"),
  dict(text="That grain became bread, and Roman bread was serious business. Archaeologists have found loaves turned to charcoal by Vesuvius, still showing the eight slices the baker scored into the top.", shots=["i:s32", "i:s32z"], cap="2,000-year-old bread"),
  dict(text="And here's a twist. Many poor families in Rome didn't even have a kitchen.", shots=["t:NO KITCHEN?!"], sfx="scratch"),
  dict(text="They lived in crowded apartment blocks called insulae, where cooking over an open fire was a fire risk. So they ate out. A lot.", shots=["i:s13", "i:s14"]),

  # ---------------- STREET FOOD ----------------
  dict(text="Enter the thermopolium. Basically, ancient Roman fast food.", shots=["v:v04"], cap="Roman fast food", chapter="Roman fast food"),
  dict(text="A stone counter facing the street, with big clay jars built right into it, full of hot food you could grab and go.", shots=["i:s15"]),
  dict(text="Pompeii alone had around eighty of them. And in 2020, archaeologists uncovered one so well preserved it was still painted with bright pictures of ducks, a rooster and a dog on a leash.", shots=["i:s16", "i:s16z"], sfx="ding"),
  dict(text="Inside the jars, they found traces of duck, pig, goat, fish and even snails. Someone's lunch, frozen in time by the eruption of Vesuvius.", shots=["i:s17"], cap="duck · pig · goat · snails"),

  # ---------------- GARUM ----------------
  dict(text="And now, the sauce. Remember the fish guts?", shots=["t:THE FISH SAUCE"], sfx="scratch", chapter="Garum"),
  dict(text="Garum was made by packing fish and fish guts in salt and leaving them to ferment for months.", shots=["i:s18", "i:s18z"]),
  dict(text="It sounds disgusting, but Romans loved it. They put it on almost everything, a bit like how we use ketchup or soy sauce today.", shots=["v:v05", "i:s19"], cap="Roman ketchup"),
  dict(text="The best garum was a luxury product. Cheap versions were everywhere, from tavern counters to soldiers' camps.", shots=["i:s20"]),

  # ---------------- SOLDIERS ----------------
  dict(text="Speaking of soldiers, a legionary's breakfast was even simpler.", shots=["v:v06"], chapter="A soldier's breakfast"),
  dict(text="Hard, twice-baked bread called bucellatum, that could last for weeks on the march. And to drink? Posca. Sour wine mixed with water.", shots=["i:s21", "t:POSCA: SOUR WINE + WATER"], sfx="pop"),
  dict(text="It tasted rough, but it was cheap, it quenched thirst, and the vinegar may even have helped make dodgy water a little safer.", shots=["i:s22"]),

  # ---------------- CTA 2 ----------------
  dict(text="By the way, if you've learned something already, a like really helps Tom get out of the ancient world and onto more screens.", shots=["i:s10b"], sfx="ding", cta=True),

  # ---------------- RICH ----------------
  dict(text="What about the rich? Surprisingly, even wealthy Romans kept breakfast small. They were saving themselves for dinner.", shots=["i:s23"], chapter="Breakfast of the rich"),
  dict(text="And Roman dinner parties could get wild. Guests reclined on couches, eating course after course.", shots=["v:v07"]),
  dict(text="Dinner even had a running order. Romans said ab ovo usque ad mala, from the egg to the apples. Eggs to start, fruit to finish.", shots=["i:s33"], cap="From egg to apples"),
  dict(text="And no, they did not have special rooms for throwing up so they could keep eating. That's a myth.", shots=["t:THE VOMITORIUM MYTH"], sfx="scratch"),
  dict(text="A vomitorium was actually a passageway in a stadium or theater, the exits that let huge crowds pour out quickly. Spewing people, not spewing food.", shots=["i:s34", "i:s34z"], cap="Vomitorium = exit"),
  dict(text="One famous delicacy was the dormouse. Rich Romans fattened them in special clay jars, then served them stuffed or dipped in honey.", shots=["i:s24", "i:s24z"], cap="Yes. Dormice."),

  # ---------------- PAYOFF ----------------
  dict(text="Okay. The recipe I promised you.", shots=["t:THE RECIPE"], sfx="ding", chapter="The recipe you've eaten"),
  dict(text="A Roman cookbook called Apicius describes taking white bread, cutting off the crust, soaking it in milk, frying it in oil, and pouring honey over the top.", shots=["v:v08", "i:s25"]),
  dict(text="Bread, soaked in milk, fried, and covered in something sweet. Sound familiar?", shots=["i:s26"], cap="Sound familiar?"),
  dict(text="It's basically French toast. Two thousand years before brunch was a thing.", shots=["t:FRENCH TOAST, 2,000 YEARS AGO"], sfx="boing"),

  # ---------------- OUTRO ----------------
  dict(text="So, what did Romans actually eat for breakfast? Not much. Bread, a splash of wine, a few olives, and they saved the real feast for later.", shots=["i:s27"], chapter="The verdict"),
  dict(text="Would you trade your cereal for bread and wine? Tell us in the comments. And next time on Back Then, Tom tries to survive a Viking winter.", shots=["i:s28"], cta=True),
]

IMG = {
  "s01": "close-up of a wooden Roman table at dawn with a rough round loaf of bread, a small clay cup of red wine and a little bowl of olives, warm morning light",
  "s02": "TOM sniffing a small clay jar labeled with nothing, green stink lines rising from the jar, Tom making a disgusted face",
  "s03": "TOM standing in front of a big closed wooden treasure chest glowing with light, looking curious, Roman columns in the background",
  "s04": "TOM holding up three fingers in front of three plates on a table: a tiny plate, a small plate, and a huge feast platter",
  "s05": "a doodle sundial with three meal icons around it: a small bread roll at dawn, a small snack at noon, and a big roast chicken feast at sunset",
  "s06": "TOM jogging out of the door of a Roman apartment building holding a piece of bread in his mouth, busy street in the morning",
  "s07": "TOM dipping a piece of bread into a cup of red wine at a small table, looking pleased with himself",
  "s08": "a Roman breakfast spread on a wooden board: bread, olives, a wedge of cheese, raisins, and a small pot of honey with a dipper",
  "s09": "a grumpy doodle Roman man leaning out of an upstairs window in his nightcap, covering his ears, while a baker below shouts and sells bread to schoolboys at dawn",
  "s10": "TOM pointing up at a big red subscribe-style button shape with a bell next to it, no text, smiling",
  "s10b": "TOM giving a big thumbs up next to a giant glowing heart shape, no text, happy",
  "s11": "a crowded ancient Roman street full of ordinary doodle Romans in plain tunics, TOM in the middle looking around",
  "s12": "TOM stirring a big bubbling pot of thick grain porridge over a small fire, steam rising",
  "s13": "a tall crowded ancient Roman apartment building, many small windows with laundry and flower pots, people leaning out",
  "s14": "inside a tiny cramped Roman apartment room with no kitchen, TOM looking at an empty corner with a small brazier and a fire warning sign symbol, worried",
  "s15": "a Roman street food counter made of stone facing the street, with big round clay jars built into the counter top, steam rising, customers waiting",
  "s16": "a colorful painted Roman fresco on a food counter showing two ducks and a rooster, archaeologists with brushes gently cleaning it",
  "s17": "cut-away view of clay jars inside a stone counter, little doodle icons of a duck, a pig, a goat, a fish and a snail floating above the jars",
  "s18": "big clay vats full of small fish and salt fermenting under the hot sun, flies buzzing, a worker holding his nose",
  "s19": "TOM drizzling sauce from a small jug over a plate of food, delighted, a ketchup bottle silhouette and a soy sauce bottle silhouette floating nearby",
  "s20": "a busy Roman tavern counter with small jugs of fish sauce lined up, merchants and soldiers buying them",
  "s21": "TOM as a Roman legionary with a helmet trying to bite a rock-hard square biscuit, cartoon crack lines, other soldiers laughing",
  "s22": "TOM as a Roman legionary drinking from a metal cup and making a sour face, a water jug and a vinegar bottle beside him",
  "s23": "a rich Roman villa dining room, a wealthy doodle Roman in a toga waving away a breakfast tray with only bread, looking at a clock-like sundial",
  "s24": "a Roman dinner table with a silver plate holding cute cartoon dormice dipped in honey, a guest reclining on a couch looking excited, TOM shocked",
  "s25": "an old open Roman scroll cookbook on a table next to bread, a jug of milk, a frying pan with oil and a pot of honey",
  "s26": "a golden fried slice of bread on a plate drizzled with honey, TOM looking at it with big sparkling eyes",
  "s27": "TOM sitting on Roman steps at sunrise eating a piece of bread with a cup, calm and happy, the Colosseum in the distance",
  "s28": "TOM in a Viking helmet and fur cloak shivering in the snow, waving at the viewer, snowy village behind him",
}
# zoomed variants reuse the base image with a tighter crop (handled by the renderer)
for k in list(IMG):
    IMG[k + "z"] = None

VID = {
  "v01": "TOM wakes up on a simple wooden bed in a small Roman apartment at dawn, sits up, stretches, then rubs his belly hungrily and looks at the camera",
  "v02": "TOM sits at a small wooden table and takes a big bite of a hard round loaf of bread, chewing slowly with a funny face",
  "v03": "TOM runs down a busy ancient Roman street at dawn toward a baker's counter, buys a loaf of bread and happily holds it up",
  "v04": "TOM walks up to a Roman stone street food counter with clay jars, the vendor ladles hot stew into a bowl and hands it to Tom, who grins",
  "v05": "TOM sniffs a small clay jar of fish sauce, recoils with a disgusted face, then cautiously tastes it and his face lights up with delight",
  "v06": "TOM as a Roman legionary with a red helmet and shield marches on a dirt road with other soldiers, chewing a hard biscuit",
  "v07": "TOM reclines on a Roman dining couch at a lavish dinner party while servants bring plates of food, guests laughing",
  "v08": "TOM fries a slice of bread in a pan over a fire, flips it, pours honey on top and gives a happy thumbs up",
}

IMG.update({
  "s29": "a long line of doodle Romans in plain tunics waiting at dawn outside the big wooden door of a rich villa, TOM in the line yawning",
  "s30": "a rich doodle Roman patron in a white toga handing a small basket of bread and coins to TOM at the villa door, Tom grateful",
  "s31": "doodle Romans lining up at a stone counter where officials pour grain from large sacks into their baskets, TOM holding a basket",
  "s32": "a round Roman loaf of bread divided into eight wedges on top, partly blackened like charcoal, displayed on a museum stand, TOM leaning in amazed",
  "s33": "a Roman dinner table with a bowl of eggs at one end and a bowl of red apples at the other, a dotted arrow drawn between them",
  "s34": "a crowd of doodle Romans pouring out of a wide arched exit tunnel of a Roman amphitheater, cheerful and chaotic",
})
for k in ["s29", "s32", "s34"]:
    IMG[k + "z"] = None
