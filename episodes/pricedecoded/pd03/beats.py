# Price Decoded ep03 — Why an Ambulance Ride Can Cost More Than a Plane Ticket
# Status: scripted 27.10.2026 (cloud run). Needs Flow assets: IMG p01..p26 and VID c01..c04 (4 clips = 48 credits).
# Shot kinds: "i:key" full-bleed illustration (Ken Burns), "v:key" Flow video clip,
#             dict(type=...) motion graphic from render.py (title, chapter, quote, bigstat, compare, bars, readings, bullets, flow, endcard)
VOICE = "am_michael"; SPEED = 0.95

STYLE = ("Editorial flat illustration, clean vector shapes with subtle grain texture, deep navy blue background tones "
         "with bright lime-green (#C6F432) accents, warm skin tones, soft shadows, modern magazine explainer style, "
         "16:9 widescreen, no text, no letters, no logos, no brand names")

B = []
def beat(text, *shots, chapter=None, sfx=None):
    B.append(dict(text=text, shots=list(shots), chapter=chapter, sfx=sfx))

# ---------------- HOOK ----------------
beat("The average domestic plane ticket in America costs four hundred and forty-five dollars. That gets you a seat, a pilot, a jet, and hundreds of miles.",
     "v:c01", dict(type="bigstat", value=445, fmt="${:.0f}", label="Average U.S. domestic air fare · Q2 2026", src="Bureau of Transportation Statistics"),
     chapter="Ambulance vs. airplane", sfx="ding")
beat("The average ground ambulance bill for a patient with private insurance was about eleven hundred dollars. And that was back in twenty twenty-one. Often for a ride of just a few miles.",
     dict(type="compare", left=("$445", "plane ticket · 2026"), right=("$1,093", "ambulance bill · 2021"), src="BTS; Commonwealth Fund, 2026"))
beat("And unlike the plane, you didn't choose the ambulance. You didn't compare prices. You might not even have been conscious.",
     "i:p02", sfx="scratch")
beat("So why does a ten-minute ride in a van cost more than a flight across the country? The answer isn't the gas, and it isn't the stretcher. It's something you never see. Let's decode it.",
     "i:p03", dict(type="title", title="THE AMBULANCE BILL", sub="Price Decoded", img="p01", dim=0.5))

# ---------------- CH1 ----------------
beat("Chapter one. You don't get to pick.",
     dict(type="chapter", n="01", title="You don't get to pick", img="p04", dim=0.5), chapter="You don't get to pick")
beat("About three million people with private insurance ride in a ground ambulance every year. Almost none of them choose which company shows up.",
     "i:p04", dict(type="bigstat", value=3, fmt="{:.0f}M", label="Privately insured ground ambulance riders per year", src="Commonwealth Fund / Georgetown CHIR, 2026"))
beat("That's not a rare situation, either. About one in ten insured Americans who end up in the emergency room get there by ambulance.",
     "i:p02", dict(type="bigstat", value=10, fmt="1 in {:.0f}", label="Insured ER patients who arrive by ambulance", src="U.S. PIRG Education Fund"))
beat("You call nine one one, and whoever covers your area comes. That might be the fire department, a hospital, a nonprofit, or a private company.",
     "v:c02", dict(type="flow", steps=["You call 911", "Dispatch sends whoever covers the area", "You ride", "The bill arrives later"]))
beat("And here's the catch. That ambulance is often not in your insurance network.",
     "i:p05")
beat("Data from Elevance Health, one of the biggest insurers in the country, shows that between forty-four and fifty-one percent of emergency ground ambulance rides were out of network from twenty twelve to twenty twenty-five.",
     dict(type="bigstat", value=51, fmt="up to {:.0f}%", label="Emergency ambulance rides out of network · 2012–2025", src="Elevance Health Public Policy Institute, July 2026"))
beat("And it depends hugely on where you live. In California and Hawaii, nearly nine out of ten rides were out of network. In North Dakota, Nebraska, Mississippi and West Virginia, fewer than one in ten.",
     dict(type="bars", title="Ambulance rides out of network", unit="%", items=[("California / Hawaii", 90), ("ND, NE, MS, WV", 10)], src="Elevance Health PPI, 2026 (approx.)"))
beat("Out of network means there's no agreed price. The ambulance can bill its full charge, the insurer pays what it decides is fair, and the gap can land on you. That's called a balance bill.",
     "i:p06", dict(type="flow", steps=["Full charge", "Insurer pays its rate", "The gap", "Balance bill → you"]))

# ---------------- CH2 ----------------
beat("Chapter two. Paying for the waiting.",
     dict(type="chapter", n="02", title="Paying for the waiting", img="p07", dim=0.5), chapter="Paying for the waiting")
beat("Here's the part most people never think about. An ambulance doesn't cost money only when it's driving you. It costs money every hour it's ready to drive you.",
     "v:c03")
beat("A crew of trained paramedics, a vehicle full of equipment, fuel, insurance, a station. All of it has to be there at three in the morning on a Tuesday, whether anyone calls or not.",
     "i:p08", dict(type="bullets", title="What 'ready' costs", items=["Paramedics on shift 24/7", "Vehicle + equipment", "Fuel, insurance, station", "Dispatch & billing"]))
beat("Since twenty twenty-two, Medicare has been collecting real cost data from ambulance organizations across the country. And it shows how much that readiness matters.",
     "i:p09")
beat("For the services with the fewest transports, the cost per ride was about twenty-nine hundred dollars. For the busiest services, about nine hundred.",
     dict(type="bars", title="Cost per transport by volume", unit="$", items=[("Least busy quarter", 2878), ("Busiest quarter", 918)], src="MedPAC, June 2026 (GADCS 2022–23)"))
beat("Same equipment. Same crew. The difference is how many rides you split the cost across.",
     dict(type="quote", kicker="THE READINESS PROBLEM", line="An ambulance waiting\nis still an ambulance you pay for.", img="p07", dim=0.6))
beat("And the spread is enormous. In Medicare's data, a service at the expensive end, the ninetieth percentile, spent more than forty-one hundred dollars per transport. At the cheap end, the tenth percentile, about three hundred and seventy.",
     dict(type="compare", left=("$4,136", "90th percentile · cost per ride"), right=("$367", "10th percentile"), src="MedPAC, June 2026"))
beat("How crews are scheduled matters too. Services that keep the same number of ambulances staffed around the clock, no matter how busy it is, spent about fifteen hundred dollars a ride. Services that add and remove crews to match demand spent about six hundred and forty.",
     dict(type="bars", title="Cost per transport by staffing model", unit="$", items=[("Static (fixed 24/7)", 1524), ("Hybrid", 918), ("Dynamic (matches demand)", 636)], src="MedPAC, June 2026"), "i:p07")
beat("It also depends on who runs it. Government-owned services reported about sixteen hundred dollars per ride. For-profit companies, about five hundred and sixty.",
     dict(type="compare", left=("$1,626", "government · per ride"), right=("$563", "for-profit · per ride"), src="MedPAC, June 2026"))
beat("That's not because public services waste money. They often have to cover a whole area, including the quiet rural roads, and many also do fire and first response.",
     "i:p10")
beat("More than half of all ambulance organizations, about fifty-five percent, are government-owned. And for a typical one, what it collects covers only about seventy-two cents of every dollar it spends. Local taxes fill the gap.",
     dict(type="bigstat", value=0.72, fmt="${:.2f}", label="Collected per $1 of cost · median government service", src="MedPAC, June 2026"), "i:p11")
beat("And where you live changes the cost of being ready. Urban and rural services came out about the same, roughly a thousand dollars a ride. But in the most remote, super rural areas, it climbed to about twelve hundred and sixty.",
     dict(type="bars", title="Cost per transport by area", unit="$", items=[("Urban", 1018), ("Rural", 997), ("Super rural", 1263)], src="MedPAC, June 2026"), "i:p10")
beat("Quick thing. If you like seeing the real math behind prices, hit subscribe. There's a lot more where this came from.",
     "i:p12")

# ---------------- CH3 ----------------
beat("Chapter three. Three different prices for the same ride.",
     dict(type="chapter", n="03", title="Three prices, one ride", img="p13", dim=0.5), chapter="Three prices, one ride")
beat("So what does a ride actually cost? It depends on who's paying.",
     "i:p13")
beat("Medicare sets its own price. In twenty twenty-six, its base rate for an advanced life support emergency trip is about five hundred and forty dollars, plus nine dollars and fifteen cents for every mile with the patient on board.",
     dict(type="compare", left=("~$541", "Medicare base · ALS emergency"), right=("$9.15", "per mile"), src="MedPAC Payment Basics, Oct 2026"))
beat("In twenty twenty-four, Medicare paid about five point three billion dollars for around eleven point three million transports. That works out to roughly four hundred and seventy dollars a ride.",
     dict(type="bigstat", value=470, fmt="~${:.0f}", label="Average Medicare payment per transport · 2024", src="MedPAC, June 2026; author's calculation"))
beat("Private insurers pay more. In network, Elevance found they paid about a hundred and sixty percent of the Medicare price, on average.",
     "i:p14", dict(type="bigstat", value=161, fmt="{:.0f}%", label="In-network payment vs Medicare price", src="Elevance Health PPI, 2026"))
beat("Even the mileage is a lottery. In twenty twenty-two, the average in-network price per mile was about twenty-eight dollars in Utah. In Florida, under six.",
     dict(type="bars", title="Avg in-network price per mile · 2022", unit="$", items=[("Utah", 28.35), ("California", 20.63), ("Florida", 5.79)], src="FAIR Health, 2023"))
beat("And then there's the sticker price, what the ambulance actually charges. For out-of-network rides, those charges climbed to more than three times the Medicare price.",
     dict(type="bars", title="Ambulance charges, % of Medicare price · 2025", unit="%", items=[("In network", 263), ("Out of network", 314)], src="Elevance Health PPI, 2026"))
beat("And that gap is widening. Back in twenty twelve, out-of-network charges were a bit more than two times the Medicare price. Now they're over three times. Since twenty twenty-two alone, charges have grown about nine percent faster than medical inflation.",
     dict(type="bars", title="Out-of-network charges, % of Medicare price", unit="%", items=[("2012", 238), ("2025", 314)], src="Elevance Health PPI, 2026"))
beat("Between twenty twelve and twenty twenty-five, ambulance charges rose about thirty percent faster than medical inflation. What insurers actually paid barely moved.",
     dict(type="compare", left=("+30%", "charges, above inflation"), right=("+3–6%", "what insurers paid"), src="Elevance Health PPI, 2026"), "i:p15")
beat("So the sticker price keeps drifting away from what anyone really pays. And the person most exposed to that sticker price is the patient who ends up out of network.",
     "i:p16", sfx="boing")

# ---------------- CH4 ----------------
beat("Chapter four. The hole in the law.",
     dict(type="chapter", n="04", title="The hole in the law", img="p17", dim=0.5), chapter="The hole in the law")
beat("In January twenty twenty-two, the No Surprises Act took effect. It protects most patients from surprise bills from out-of-network doctors and hospitals in an emergency.",
     "i:p17")
beat("It even covers air ambulances, the helicopters and planes. But ground ambulances, the ones most people actually ride in, were left out.",
     dict(type="compare", left=("✓", "air ambulance · protected"), right=("✗", "ground ambulance · not covered"), src="No Surprises Act (2022)"), sfx="scratch")
beat("In twenty twenty-four, a federal advisory committee sent Congress a report recommending a ban on surprise ground ambulance bills, and limiting what patients pay to their normal cost sharing. As of early twenty twenty-six, Congress still hadn't acted.",
     "i:p18", dict(type="quote", kicker="FEDERAL ADVISORY COMMITTEE · 2024", line="Ban surprise ground\nambulance bills.", img="p18", dim=0.6))
beat("So states stepped in. By February twenty twenty-six, twenty-two states had some kind of protection.",
     dict(type="bigstat", value=22, fmt="{:.0f}", label="States with ground ambulance surprise-bill protections · Feb 2026", src="Commonwealth Fund; PIRG, 2026"), "v:c04")
beat("And they took very different approaches. North Dakota limits charges to two hundred and fifty percent of the Medicare rate. Utah makes insurers pay a rate set by the state, so the patient isn't billed for the rest. Illinois caps what the patient owes at their normal copay, or ten percent of the cost, whichever is less.",
     dict(type="bullets", title="How states protect patients", items=["North Dakota: charges capped at 250% of Medicare", "Utah: insurers pay the state-set rate", "Illinois: copay or 10%, whichever is less", "13 of 22 states also cover non-emergency rides"]), "i:p17")
beat("But there's a catch. State laws can't touch self-funded employer plans, the kind most American workers have. PIRG estimates about sixty percent of insured people aren't protected by those state laws.",
     dict(type="bigstat", value=60, fmt="~{:.0f}%", label="Insured people not protected by state ambulance laws", src="U.S. PIRG Education Fund, 2025"))
beat("The typical surprise ambulance bill, the part you're billed on top of what insurance paid, is around four hundred and fifty dollars. Across the country, insured patients pay roughly a hundred and twenty-nine million dollars a year in these bills.",
     dict(type="compare", left=("~$450", "median surprise bill"), right=("$129M", "paid by patients per year"), src="U.S. PIRG Education Fund"))
beat("And it changes behavior. In a YouGov poll, twenty-three percent of Americans said they had skipped an ambulance ride because of the cost.",
     dict(type="bigstat", value=23, fmt="{:.0f}%", label="Americans who skipped an ambulance because of cost", src="YouGov via Gray News, Oct 2024"), "i:p19")

# ---------------- CH5 ----------------
beat("Chapter five. Why the plane is cheaper.",
     dict(type="chapter", n="05", title="Why the plane is cheaper", img="p20", dim=0.5), chapter="Why the plane is cheaper")
beat("So now the comparison makes sense. A plane splits its costs across a whole cabin of passengers, and it flies trip after trip, all day long.",
     "i:p20", dict(type="flow", steps=["One jet", "A full cabin", "Many flights a day", "Cost split thin"]))
beat("An ambulance carries one patient at a time. And it spends a lot of its life waiting, so that when you call, it's there.",
     "i:p21")
beat("You're not really paying for a ride. You're paying for a crew that was ready before you knew you needed them. And when that bill is out of network, you can end up paying the sticker price on top.",
     dict(type="quote", kicker="DECODED", line="You're not paying for the ride.\nYou're paying for the waiting.", img="p21", dim=0.55), chapter="Decoded")

# ---------------- WHAT IT MEANS ----------------
beat("What does that mean for you? First: in a real emergency, call. Your health matters more than the bill, and a bill can often be fought.",
     "i:p22", chapter="What it means for you")
beat("If a big ambulance bill arrives, don't pay it right away. Check that your insurer has processed the claim first. Ask the ambulance for an itemized bill. And look up whether your state has a ground ambulance protection law.",
     "i:p23", dict(type="bullets", title="Got an ambulance bill?", items=["Wait for your insurer to process it", "Ask for an itemized bill", "Check your state's ambulance law", "Ask about payment plans or discounts"]))
beat("It's also worth asking whether they offer a payment plan or a financial hardship discount. You usually have to ask. And no, this isn't financial or legal advice. It's just the math.",
     "i:p24")
beat("Have you ever gotten an ambulance bill? How much was it? Tell me in the comments. And next time, we're decoding where your five dollar coffee actually goes. This was Price Decoded.",
     "v:c01", dict(type="endcard", title="PRICE DECODED", next="Next: where your $5 coffee actually goes"))

BEATS = B

TOMLESS = True  # Price Decoded has no mascot
IMG = {
 "p01": "A white ambulance van with lime-green stripes parked next to a commercial passenger jet on a tarmac at dusk, both with large blank price tags hanging from them, playful comparison concept",
 "p02": "A person lying on a stretcher being loaded into the back of an ambulance at night by two paramedics, the patient's eyes closed, calm cinematic lighting",
 "p03": "A very long paper bill unrolling from the back doors of an ambulance and trailing down a city street, surreal concept",
 "p04": "Top-down map of a city divided into colored zones, several different ambulances parked in different zones, a phone with a call icon in the center",
 "p05": "A patient holding an insurance card that doesn't fit into a puzzle-piece slot on the side of an ambulance, mismatched shapes concept",
 "p06": "A large stack of coins labeled with nothing splitting into two piles, a big gap between them with a small worried person standing in the gap holding an envelope",
 "p07": "An ambulance parked inside a quiet fire station at 3 a.m., a clock on the wall, two paramedics waiting at a table with coffee, ready",
 "p08": "An exploded-view diagram style illustration of an ambulance with its equipment floating around it: defibrillator, stretcher, oxygen tank, medical bags, fuel pump icon",
 "p09": "A government analyst at a desk sorting thousands of small folders into neat stacks, spreadsheets glowing on screens, data collection concept",
 "p10": "An ambulance driving alone on a long empty rural road through farmland at sunset, small houses far apart",
 "p11": "A small town hall building with a coin jar on the steps, coins flowing from houses into the jar and then into a parked ambulance",
 "p12": "A friendly hand pressing a large glowing lime-green button on a navy background, minimal concept, no text",
 "p13": "Three identical ambulances side by side, each with a different-sized blank price tag hanging from its mirror: small, medium and huge",
 "p14": "An insurance agent in a suit at a desk handing over a stack of money to an ambulance paramedic, neutral businesslike",
 "p15": "A thermometer-style gauge rising high on the left while a short flat line stays low on the right, abstract finance concept on navy background",
 "p16": "A patient at a kitchen table opening an envelope with a shocked expression, a big blank bill in their hands, evening light",
 "p17": "The dome of the U.S. Capitol building at dusk with a large rolled document and a shield floating in front of it, policy concept",
 "p18": "A committee of people around a large table handing a thick bound report across to a figure at a podium, no faces of real people, generic",
 "p19": "A person standing at a curb holding their side in pain, looking at their phone, an ambulance in the distance, hesitating, worried",
 "p20": "Cutaway of a passenger jet full of seated travelers, many small coins floating above each seat, cost-sharing concept",
 "p21": "Interior of an ambulance with a single patient on the stretcher and a paramedic beside them, one big coin floating above the patient",
 "p22": "A person calmly calling on their phone while a paramedic arrives at their door, reassuring warm light",
 "p23": "A person at a desk with a magnifying glass over an itemized bill, a phone on speaker and a checklist beside them",
 "p24": "A friendly billing office clerk across a counter sliding a smaller bill with a calendar to a relieved patient, handshake",
}
VID = {
 "c01": "Animate: a passenger jet takes off in the background while an ambulance with flashing lights drives past in the foreground, camera slowly pans",
 "c02": "Animate: an ambulance with flashing lights pulls out of a station and drives down a city street at night, cars move aside",
 "c03": "Animate: two paramedics wait in a quiet station at night, a call alarm lights up, they grab their bags and run to the ambulance",
 "c04": "Animate: a map of the United States where states light up one by one in lime green, camera slowly pushes in",
}
STILL_FOR_VID = {  # first-frame stills to animate
 "c01": "p01", "c02": "p04", "c03": "p07", "c04": "p17",
}
