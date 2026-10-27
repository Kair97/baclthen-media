# Price Decoded ep02 — How Costco Makes Money Selling $1.50 Hot Dogs
# Pipeline v2: each beat = narration + a list of shots (cut every ~3-5 s).
# Shot kinds: "i:key" full-bleed illustration (Ken Burns), "v:key" Flow video clip,
#             dict(type=...) motion graphic from render.py (title, chapter, quote, bigstat, compare, bars, readings, bullets, flow)
VOICE = "am_michael"; SPEED = 0.95

STYLE = ("Editorial flat illustration, clean vector shapes with subtle grain texture, deep navy blue background tones "
         "with bright lime-green (#C6F432) accents, warm skin tones, soft shadows, modern magazine explainer style, "
         "16:9 widescreen, no text, no letters, no logos, no brand names")

B = []
def beat(text, *shots, chapter=None, sfx=None):
    B.append(dict(text=text, shots=list(shots), chapter=chapter, sfx=sfx))

# ---------------- HOOK ----------------
beat("A hot dog and a soda at Costco costs a dollar fifty. In nineteen eighty-five, it also cost a dollar fifty.",
     "v:c01", dict(type="bigstat", value=1.50, fmt="${:.2f}", label="Hot dog + soda · same price since 1985", src="Costco / ABC News, 2024"),
     chapter="The $1.50 paradox", sfx="ding")
beat("Adjusted for inflation, that combo should cost about four and a half dollars today. Costco has refused to raise it for more than forty years.",
     dict(type="compare", left=("$1.50", "what you pay"), right=("~$4.50", "1985 price + inflation"), src="BLS CPI-U, author's calculation"))
beat("Former CEO Craig Jelinek says co-founder Jim Sinegal once told him: if you raise the effing hot dog, I will kill you. Figure it out.",
     dict(type="quote", kicker="JIM SINEGAL, CO-FOUNDER (as told by Craig Jelinek)", line="“If you raise the effing hot dog,\nI will kill you. Figure it out.”", img="p23", dim=0.55), sfx="scratch")
beat("So here's the puzzle. Costco sells a hot dog at a nineteen eighty-five price, a chicken that's widely believed to lose money, and it caps how much it marks things up. And last year it made nine point two billion dollars in profit.",
     "i:p03", dict(type="bigstat", value=9.2, fmt="${:.1f}B", label="Costco net income · fiscal 2026", src="Costco FY2026 results"))
beat("The answer is sitting in your wallet. Once you see it, you'll never look at that little card the same way. Let's decode it.",
     "i:p04", dict(type="title", title="THE $1.50 HOT DOG", sub="Price Decoded", img="p01", dim=0.5))

# ---------------- CH1 ----------------
beat("Chapter one. The hot dog is bait.",
     dict(type="chapter", n="01", title="The hot dog is bait", img="p05", dim=0.5), chapter="The hot dog is bait")
beat("Retailers have a name for this. A loss leader. You sell something famous so cheap that people come in for it, and then buy everything else while they're there.",
     "i:p06", dict(type="flow", steps=["Famous cheap item", "You walk in", "You fill the cart", "Store profits"]))
beat("Costco has two legendary ones. The dollar fifty hot dog. And the four ninety-nine rotisserie chicken, which has cost four ninety-nine since two thousand nine.",
     "v:c02", dict(type="compare", left=("$1.50", "hot dog + soda"), right=("$4.99", "rotisserie chicken"), src="Costco; The Hustle, 2024"))
beat("Costco sells around a hundred and six million of those chickens a year. Adjusted for inflation, each one would cost more than eight dollars.",
     "i:p07", dict(type="bigstat", value=106, fmt="{:.0f}M", label="Rotisserie chickens sold per year", src="The Hustle, 2024"))
beat("That's roughly one out of every eight rotisserie chickens sold in the whole country.",
     dict(type="bars", title="Rotisserie chickens sold per year, U.S.", unit="", items=[("Costco", 106), ("Everyone else", 794)], src="The Hustle, 2024 (millions)"))
beat("Now notice where the chicken is. Not by the door. All the way in the back. To reach it, you walk past the TVs, the patio furniture, and the forty-pack of paper towels.",
     "v:c03", "i:p08", sfx="whoosh")
beat("Costco even built its own four hundred and fifty million dollar chicken plant in Nebraska, partly to keep that price from moving.",
     "i:p09", dict(type="bigstat", value=450, fmt="${:.0f}M", label="Costco's own chicken plant · Nebraska, 2019", src="The Hustle, 2024"))
beat("That plant processes around two million chickens a week. Costco estimated it would save up to thirty-five cents on every rotisserie chicken. Thirty-five cents. That's how seriously they take a four ninety-nine price tag.",
     "v:c02", dict(type="bigstat", value=0.35, fmt="${:.2f}", label="Estimated saving per chicken", src="The Hustle, 2024"))
beat("But here's the thing. Even the bait doesn't explain nine billion dollars. Because Costco barely makes money on anything it sells.",
     "i:p10")

# ---------------- CH2 ----------------
beat("Chapter two. The tiny margin machine.",
     dict(type="chapter", n="02", title="The tiny-margin machine", img="p11", dim=0.5), chapter="The tiny-margin machine")
beat("Last fiscal year, Costco sold two hundred and ninety-seven billion dollars worth of stuff.",
     "v:c04", dict(type="bigstat", value=297.2, fmt="${:.1f}B", label="Costco net sales · fiscal 2026", src="Costco FY2026 results"))
beat("After paying for the merchandise itself, it kept about eleven percent. Eleven dollars out of every hundred, before paying a single worker or the electric bill.",
     dict(type="bigstat", value=11.1, fmt="{:.1f}%", label="Gross margin on sales · fiscal 2026", src="Costco FY2026 results"), "i:p12")
beat("Kroger, the biggest traditional supermarket chain in America, keeps about twenty-three.",
     dict(type="bars", title="Gross margin, % of sales", unit="%", items=[("Costco FY2026", 11.1), ("Kroger FY2025", 22.9)], src="Company reports"))
beat("Industry reports say Costco caps its markup at about fourteen percent on name brands, and fifteen percent on its own Kirkland Signature products.",
     dict(type="compare", left=("14%", "max markup · name brands"), right=("15%", "max markup · Kirkland"), src="RetailWire via TheStreet, 2026"))
beat("So how do you survive on margins that thin? You cut everything else. A Costco warehouse carries fewer than four thousand products. The average American supermarket carries more than thirty-three thousand.",
     "i:p13", dict(type="bars", title="Products on the shelf", unit="", items=[("Costco warehouse", 4000), ("Average supermarket", 33248)], src="Costco 10-K 2026; FMI 2025"))
beat("Fewer products means gigantic orders of each one. And when you're buying that much, suppliers fight for your shelf space, and they cut their prices to get it.",
     "i:p14")
beat("No fancy displays. Products sit on the pallets they arrived on. Almost no advertising. Bulk packs that fly off the shelves.",
     "v:c05", dict(type="bullets", title="How Costco cuts costs", items=["Fewer than 4,000 products", "Pallets, not displays", "Almost no advertising", "Bulk packs that sell fast"]))
beat("Do all of that, and you can sell almost at cost. But almost at cost isn't nine billion dollars. So where does the money actually come from?",
     "i:p10z", sfx="boing")

# ---------------- CH3 ----------------
beat("Here's how thin it gets. After every bill is paid, Costco keeps about three cents of profit from every dollar of revenue. The average grocery retailer keeps about two.",
     dict(type="bars", title="Net profit per $1 of revenue", unit="%", items=[("Costco FY2026", 3.0), ("Avg food retailer 2025", 2.1)], src="Costco FY2026; FMI 2025"))
beat("Chapter three. The card in your wallet.",
     dict(type="chapter", n="03", title="The card in your wallet", img="p15", dim=0.5), chapter="The card in your wallet")
beat("A basic Costco membership in the U.S. costs sixty-five dollars a year. The Executive membership costs a hundred and thirty.",
     "i:p15z", dict(type="compare", left=("$65", "Gold Star / year"), right=("$130", "Executive / year"), src="Costco 10-K 2026; TheStreet, 2026"))
beat("Last year, Costco collected five point nine billion dollars in membership fees.",
     dict(type="bigstat", value=5.9, fmt="${:.1f}B", label="Membership fees · fiscal 2026", src="Costco FY2026 results"), sfx="ding")
beat("Now put that next to the profit. Nine point two billion. The fees alone add up to almost two thirds of that number.",
     dict(type="bars", title="Costco, fiscal 2026", unit="$B", items=[("Membership fees", 5.9), ("Net income", 9.2)], src="Costco FY2026 results"))
beat("And unlike a hot dog, a membership fee costs almost nothing to deliver. There's no product, no shipping, no shelf. It's about as close to pure profit as retail gets.",
     "i:p16")
beat("Those fees come from eighty-four million paid members.",
     "v:c06", dict(type="bigstat", value=84.1, fmt="{:.1f}M", label="Paid Costco memberships · Aug 2026", src="Costco 10-K 2026"))
beat("Do the math per store. Costco runs nine hundred and thirty-nine warehouses. That's almost ninety thousand paying members per warehouse, and more than six million dollars in fees for each building, every year, before it sells a single hot dog.",
     "i:p15", dict(type="bigstat", value=6.3, fmt="${:.1f}M", label="Membership fees per warehouse per year", src="Costco FY2026; author's calculation"))
beat("And they keep coming back. Ninety-two percent renew in the U.S. and Canada. Almost ninety percent worldwide.",
     dict(type="bars", title="Membership renewal rate, 2026", unit="%", items=[("U.S. & Canada", 92.3), ("Worldwide", 89.8)], src="Costco 10-K 2026"))
beat("Most subscription businesses would kill for numbers like that. Costco isn't really a store that sells memberships. It's a membership that happens to come with a store.",
     dict(type="quote", kicker="THE REAL BUSINESS", line="Not a store that sells memberships.\nA membership that comes with a store.", img="p17", dim=0.6))
beat("Quick thing. If you like seeing the real math behind prices, hit subscribe. Next, we're decoding why an ambulance ride can cost more than a plane ticket.",
     "i:p18")

# ---------------- CH4 ----------------
beat("Chapter four. Why you keep paying.",
     dict(type="chapter", n="04", title="Why you keep paying", img="p19", dim=0.5), chapter="Why you keep paying")
beat("Here's the psychology. Once you've paid sixty-five dollars upfront, you want to get your money's worth. So you shop at Costco more, not less.",
     "i:p19z", dict(type="flow", steps=["Pay $65 upfront", "Want your money's worth", "Shop there more", "Renew next year"]))
beat("The Executive card adds another hook. Two percent back on most purchases, up to twelve hundred and fifty dollars a year. The more you spend, the more it feels like you're winning.",
     "i:p20", dict(type="bigstat", value=2, fmt="{:.0f}%", label="Executive reward · up to $1,250 a year", src="TheStreet, 2026"))
beat("And it works. About half of all paid members now pay for the Executive card. Forty-two million of them, each paying double.",
     dict(type="bars", title="Paid memberships, millions · 2026", unit="", items=[("Executive", 42.3), ("All paid", 84.1)], src="Costco Q4 FY2026 report"))
beat("Then there's the treasure hunt. Costco keeps rotating part of what it sells, so the thing you see today might be gone next week. That's a reason to come back often, and to grab it right now.",
     "v:c07", "i:p21")
beat("And there's Kirkland Signature. Launched in nineteen ninety-five, it's reported to bring in around eighty-six billion dollars a year. And you can only buy it at Costco.",
     "i:p22", dict(type="bigstat", value=86, fmt="${:.0f}B", label="Kirkland Signature sales per year", src="Wall Street Journal via TheStreet, 2026"))

# ---------------- CH5 ----------------
beat("Chapter five. The real reason the hot dog is a dollar fifty.",
     dict(type="chapter", n="05", title="The real reason it's $1.50", img="p01", dim=0.5), chapter="The real reason it's $1.50")
beat("So now the hot dog makes sense. It isn't really a product. It's a promise.",
     "v:c08", sfx="ding")
beat("Every time you see that price, Costco is telling you: we are not ripping you off. And that trust is exactly what makes you renew the card.",
     "i:p23")
beat("In twenty twenty-four, Costco raised its membership fee for the first time in seven years, from sixty dollars to sixty-five. But just a few months earlier, its CFO went out of his way on an earnings call to say: the dollar fifty hot dog price is safe.",
     dict(type="quote", kicker="CFO GARY MILLERCHIP · EARNINGS CALL, MAY 2024", line="“The $1.50 hot dog\nprice is safe.”", img="p03", dim=0.6))
beat("In fiscal twenty twenty-six, membership fee revenue grew by almost six hundred million dollars. Raise the fee, and you make hundreds of millions. Raise the hot dog, and you risk the trust that makes people pay the fee.",
     dict(type="bars", title="Membership fees, $ billions", unit="$B", items=[("Fiscal 2025", 5.323), ("Fiscal 2026", 5.907)], src="Costco FY2026 results"), "i:p25")

# ---------------- VERDICT ----------------
beat("So, how does Costco make money selling cheap hot dogs? It doesn't. It makes money selling you a card. The hot dog is how it keeps you buying it.",
     dict(type="quote", kicker="DECODED", line="Costco doesn't sell hot dogs.\nIt sells the card.", img="p04", dim=0.55), chapter="Decoded")
beat("What that means for you: a membership only pays off if you'd shop there anyway. Do the math on your own grocery bill, not on the hot dog. And no, this isn't financial advice.",
     "i:p26")
beat("Here's a simple rule for the Executive card. It costs sixty-five dollars more than the basic one, and pays two percent back. So it only pays for itself if you spend more than three thousand two hundred and fifty dollars a year at Costco.",
     dict(type="bigstat", value=3250, fmt="${:,.0f}", label="Yearly spend where Executive breaks even", src="$65 extra ÷ 2% reward · author's calculation"), "i:p26")
beat("What's your Costco must-buy? Tell me in the comments. I want to know if anyone actually goes just for the hot dog. This was Price Decoded.",
     "v:c01", dict(type="endcard", title="PRICE DECODED", next="Next: why an ambulance ride costs so much"))

BEATS = B

TOMLESS = True  # Price Decoded has no mascot
IMG = {
 "p01": "A juicy hot dog in a bun with mustard next to a paper soda cup on a red tray, food-court table in a big warehouse store, hero shot, dramatic lighting",
 "p02": "An older businessman with glasses and gray hair pointing a finger sternly, half-joking angry expression, standing in a warehouse store food court, portrait",
 "p03": "A huge stack of gold coins and dollar bills growing out of a tiny hot dog on a plate, surreal finance concept",
 "p04": "Close-up of a hand pulling a plain membership card with a lime-green stripe out of a leather wallet, glowing softly, no text on the card",
 "p05": "A hot dog on a fishing hook dangling in front of a crowd of shoppers with shopping carts, playful concept illustration",
 "p06": "A shopper walking into a giant warehouse store through big doors, small cheap item in hand, huge aisles of products ahead",
 "p07": "Rows and rows of golden rotisserie chickens in clear plastic domes on a long heated shelf in a warehouse store",
 "p08": "Top-down map-like view of a warehouse store floor plan, a dotted path from the entrance winding past TVs, furniture and paper towels to rotisserie chickens at the very back",
 "p09": "A large modern poultry processing plant on the Nebraska prairie with trucks, wide landscape, clean industrial building",
 "p10": "A puzzled shopper scratching his head next to a giant receipt that curls to the floor, question marks floating",
 "p11": "A tiny thin slice of a pie chart glowing lime green while the rest of the pie is dark navy, on a warehouse shelf",
 "p12": "A cashier handing a customer a small paper bag; behind them a large dollar bill being cut with scissors into a thin slice",
 "p13": "Split scene: left a sparse warehouse aisle with few huge pallets of products, right a crowded supermarket aisle with thousands of small colorful products",
 "p14": "Several suppliers in suits competing and pushing to place their product boxes on a single warehouse shelf, playful",
 "p15": "A giant membership card standing like a door in front of a warehouse entrance, shoppers lining up to walk through it",
 "p16": "A money printing machine shaped like a membership card printing dollar bills, minimal clean concept",
 "p17": "A shopping cart full of products balanced on top of a giant membership card like a stage",
 "p18": "An ambulance next to an airplane on a split background, price tags hanging from both, curious concept",
 "p19": "A shopper with a determined face pushing an overflowing shopping cart, thought bubble with a coin, getting my money's worth",
 "p20": "Shopper holding a long receipt while small coins rain back into their hand, cashback concept",
 "p21": "A treasure chest open in the middle of a warehouse aisle, shoppers rushing toward it with carts, sparkles",
 "p22": "Plain unbranded store-brand products, boxes and bottles with blank labels, lined up proudly on a warehouse shelf like a family portrait",
 "p23": "A handshake between a shopper and a store employee in a red vest with a hot dog on a tray between them, warm trust concept",
 "p24": "Business executive at a conference-call desk with microphone and earnings charts on screens, calm confident",
 "p25": "A balance scale with a membership card on one side heavily outweighing a small hot dog on the other",
 "p26": "A person at a kitchen table with a calculator, grocery receipts and a membership card, thinking, cozy evening light",
}
for k in [k for k in list(IMG) if False]: pass
VID = {
 "c01": "Animate: steam rises from the hot dog, the soda cup gets condensation drops, camera slowly pushes in, a shopper's hand reaches in and picks up the hot dog",
 "c02": "Animate: a store worker in a red vest places a fresh golden rotisserie chicken in a plastic dome onto a heated shelf, steam rising, camera slowly tracks sideways",
 "c03": "Animate: a shopper pushes a cart along a long warehouse aisle past TVs and furniture toward the back of the store, camera follows behind",
 "c04": "Animate: a forklift lifts a pallet of boxes high onto warehouse racking, shoppers walk below, camera slowly tilts up",
 "c05": "Animate: shoppers grab bulk packs from pallets, products disappear quickly, fast-paced busy warehouse",
 "c06": "Animate: a long line of shoppers holding up membership cards at the warehouse entrance, an employee checks each card with a smile",
 "c07": "Animate: shoppers rush to a pallet with a new surprise product, one grabs the last box and smiles, camera push in",
 "c08": "Animate: a hot dog on a tray with a soda glows softly, camera slowly orbits around it, warm cinematic light",
}
STILL_FOR_VID = {  # first-frame stills to animate
 "c01": "p01", "c02": "p07", "c03": "p06", "c04": "p13", "c05": "p13", "c06": "p15", "c07": "p21", "c08": "p01",
}
