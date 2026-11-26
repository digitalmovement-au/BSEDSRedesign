# Page content for the Bright Sparks Electrical & Data Services redesign.
# Copy is taken from the live site (bseds.com.au), shortened and lightly tidied for the prototype.

W = "https://www.bseds.com.au/wp-content/uploads/"
IG = W + "sb-instagram-feed-images/"

PHONE = "0433 909 889"
TEL = "0433909889"
EMAIL = "josh@bseds.com.au"
FACEBOOK = "https://www.facebook.com/p/Bright-Sparks-Electrical-Data-Services-61561684244842/"
INSTAGRAM = "https://www.instagram.com/bright.sparks.electrical/"
LOGO = W + "2026/08/cropped-Logo.png"

# ---------------------------------------------------------------- FAQs (from the live homepage)
FAQ = {
  "general": [
    ("What services does Bright Sparks Electrical & Data Services offer?", [
      "We’re a trusted Sunshine Coast electrician, serving local homes and businesses for more than two decades. Our work spans six main areas: residential electrical, commercial electrical, general electrical installations, maintenance and repairs, data and fibre cabling, and round-the-clock emergency call-outs.",
      "Because the same team handles both electrical work and structured data and network cabling, you can use one contractor for a full property fit-out rather than coordinating separate trades."]),
    ("What makes Bright Sparks different from other local electricians?", [
      "Three things: affordability without cutting corners on safety, a fully licensed and locally based team, and a strong track record of reliable, high-quality workmanship built up over 20+ years. That combination is why so many repeat customers and referrals come our way."]),
    ("How do I get a quote, and what areas do you service?", [
      f"Call the team directly on {PHONE} or send a request through the quote form. Quotes are detailed and upfront, with no hidden charges.",
      "We cover the Sunshine Coast and hinterland, including Maroochydore, Mooloolaba, Caloundra, Noosa, Buderim, Nambour, Kawana, Coolum, Palmwoods and Montville, along with many surrounding suburbs."]),
  ],
  "residential": [
    ("What residential electrical work do you handle for new builds and renovations?", [
      "Full house wiring and rewiring, switchboard installation, lighting and power design, energy-efficient solutions, and NBN, data and communications wiring. We work in partnership with homeowners, builders and developers, and install smoke alarms to meet current safety compliance requirements."]),
    ("What about existing homes and investment properties?", [
      "For existing homes we install ceiling fans, upgrade hot water systems, add power points, fit safety switches (RCDs) and set up security cameras.",
      "There’s also a dedicated service for landlords and investment properties, covering safety checks, electrical upgrades and fast turnarounds between tenancies."]),
  ],
  "commercial": [
    ("What commercial electrical services are available for business owners?", [
      "Electrical fit-outs for new or refurbished spaces, general installations, scheduled preventative maintenance, fault-finding and repairs, test and tag, and three-phase power for higher-demand setups.",
      "We regularly work with resorts, offices, shopping centres, strata complexes, medical facilities, cafés, restaurants and schools, with an emphasis on minimal disruption to daily operations."]),
    ("What compliance standards does commercial work follow?", [
      "All our work adheres to AS/NZS electrical standards, and we offer RCD testing and energy audits designed to help businesses reduce power costs. Emergency and fault response is available 24/7 for urgent commercial issues."]),
  ],
  "data": [
    ("Do you install data cabling and network points?", [
      "Yes. Data and fibre is its own dedicated service alongside our electrical work. It covers structured data cabling, network cabling design for offices and homes, data point installation, phone wiring and fibre-optic cabling for residential and commercial properties."]),
    ("Are you licensed to install NBN and fibre connections?", [
      "Yes. Our team is ACMA-approved and registered as an NBN contractor, in addition to holding standard electrical licensing. Cabling and NBN connection work in Australia needs this separate registration, and we also offer testing, certification and fault-finding for existing networks."]),
  ],
  "emergency": [
    ("What happens if I have an electrical emergency?", [
      "We provide a 24-hour, 7-day emergency electrician service for homes and businesses, covering power outages, faulty switchboards, sparking outlets, damaged wiring and overloaded circuits.",
      "Emergency work is carried out in line with the AS/NZS 3000 wiring standard, with the focus on fast, accurate troubleshooting so the fault is fixed properly the first time."]),
  ],
}
FAQ_ALL = [q for k in ("general", "residential", "commercial", "data", "emergency") for q in FAQ[k]]

# ---------------------------------------------------------------- Google reviews (from the live site)
REVIEWS = [
  ("Teagan Gardiner", "3 weeks ago", "We have had Josh and his team do work for our business and our home and we have nothing but good things to say. Communication is fantastic, as is the efficiency. These guys will always be our go to."),
  ("Cassandra Loh", "3 weeks ago", "Josh is fantastic, always quick to respond and great at communicating exactly what needs to be done. He came out promptly to fix our light and had it sorted in no time. Highly recommend!"),
  ("Julian Tebay", "3 weeks ago", "Josh, Hudson and his team have been great to work with and have assisted me in renovating my house… they have done so much and can highly recommend them."),
  ("Nicole Allan", "3 weeks ago", "Josh and the team are amazing! They helped my son achieve his 80 hours of work experience for his cert 2 in electrotechnology. They took the time to teach him and train him. Their professionalism is above and beyond."),
  ("Caz Brackett", "4 months ago", "After finding our meter was not safe late at night, he was there to help in a heartbeat. He was friendly, professional and such a nice person to deal with. For all your electrical needs I would highly recommend Bright Sparks."),
  ("Errol Ross", "10 months ago", "Josh attended our units on behalf of our body corporate to deal with an emergency pump system failure. Very professional, courteous and informative. We were up and running in minimal time. Highly recommended!"),
  ("Chris Moore", "4 months ago", "Josh and his team are the best on the sunny coast for their work and prices. Highly recommend using them and will only use them in the future. Thanks guys."),
  ("Mitchell Edwards", "7 months ago", "Josh has done a number of jobs for us since we moved to the Sunshine Coast. His work is always excellent and the rates are very reasonable. I would highly recommend him."),
  ("Fab50s Coffee Group", "11 months ago", "Arrived on time, worked efficiently, were very pleasant and did an excellent job. Would thoroughly recommend."),
  ("Sylvia Wightman", "3 months ago", "On time. Clean, neat and tidy, thank you."),
]

SUBURBS = ["Beerwah", "Buddina", "Buderim", "Caloundra", "Coolum", "Cooroy", "Currimundi", "Diamond Valley", "Doonan", "Dulong",
           "Eumundi", "Flaxton", "Glass House Mountains", "Glenview", "Golden Beach", "Hunchy", "Ilkley", "Kawana", "Kawana Islands", "Kenilworth",
           "Lake Macdonald", "Landsborough", "Little Mountain", "Maleny", "Maroochydore", "Minyama", "Moffat Beach", "Montville", "Mooloolaba", "Mooloolah Valley",
           "Mountain Creek", "Nambour", "Noosa", "Noosa Heads", "Noosaville", "Palmview", "Palmwoods", "Pelican Waters", "Peregian Beach", "Sippy Downs",
           "Tewantin", "Woombye", "Wurtulla", "Yandina"]

# Recent work, from the business's Instagram feed (cached on the live site)
INSTAGRAM_POSTS = [
  "707592326_18102350926935902_3422286671380539816_nfull.webp",
  "775494791_18117525487935902_1395040587930437987_nfull.webp",
  "707668743_18102350608935902_972946133791542895_nfull.webp",
  "707617855_18102349810935902_6053190241315930172_nfull.webp",
  "706317807_18102349195935902_5653754426201534242_nfull.webp",
  "706549682_18102348910935902_2739272914738147418_nfull.webp",
  "693634850_18100094695935902_5806446292488042226_nfull.webp",
  "684514011_18098426932935902_163503999499675504_nfull.webp",
]

WHY = [
  ("Affordable electrical & data solutions", "A wide range of electrical and data services that meet the highest safety and quality standards, without breaking the bank."),
  ("Local electricians, 24/7", "Peace of mind knowing a local electrician can be at your door to solve electrical and data issues, 24 hours a day, 7 days a week."),
  ("Precision, reliability & workmanship", "We’ve earned the trust of countless home and business owners for our precision, reliability and workmanship."),
]

# ---------------------------------------------------------------- Services
# blocks: (eyebrow, h2, [paragraphs], [bullets], [img, img])
SERVICES = [
  dict(
    slug="residential-electrician", nav="Residential", key="residential",
    title="Residential Electrician Sunshine Coast | Licensed & Insured",
    eyebrow="Residential electrician",
    h1="Electrical work for a more efficient, <em>connected</em> home",
    lead="Lower power bills, better lighting and reliable internet all start with good electrical work.",
    banner=W + "2025/10/Residential-banner.jpg",
    panel=W + "2026/08/homepage-banner-img-2a.webp",
    card_img=W + "2025/10/Residential-service.jpg",
    card_text="Lighting, smoke alarms, security cameras, switchboard and hot water upgrades, through to complete fit-outs.",
    intro_h2="Your local residential electrician",
    intro=[
      "Bright Sparks Electrical & Data Services helps Sunshine Coast homeowners make their homes more efficient, comfortable and connected.",
      "From LED lighting and ceiling fans to data points, switchboard upgrades and smoke alarms, our licensed team has more than 20 years of experience and makes sure every job meets Australian safety and quality standards.",
    ],
    intro_imgs=[W + "2025/11/residential-electricians-content-img-1.webp", W + "2025/11/residential-electricians-content-img-2.webp"],
    subs_h2="Residential services we offer",
    subs=[
      ("Electrical Fit-Outs", W + "2025/11/Ele-Outs-service-1.jpg"),
      ("Lighting Installations", W + "2025/11/Local-service-1.jpg"),
      ("Security Cameras", W + "2025/11/Cameras-service-1.jpg"),
      ("Local Residential Electrician", W + "2025/11/local-elex-box-img.png"),
      ("Switchboard Installations", W + "2025/10/Switchboard-service.jpg"),
      ("Switchboard Upgrades", W + "2025/10/S-Upgrades-service.jpg"),
      ("Smoke Alarm Installations", W + "2025/11/Smo-Alarms-service-1.jpg"),
      ("Ceiling Fan Installations", W + "2025/10/Ceiling-Fans-service.jpg"),
      ("Hot Water Systems", W + "2025/10/hot-systems-service.jpg"),
    ],
    list_h2="New builds & renovations",
    list_lead="We partner with homeowners, builders and developers to deliver reliable electrical systems that meet today’s standards and tomorrow’s needs.",
    list=["Full house wiring and rewiring", "Switchboard installations", "Lighting and power design", "Energy-efficient solutions", "NBN, data and communications", "Smoke alarms and safety compliance"],
    blocks=[
      ("Efficiency", "Lighting and ceiling fans", ["LED lighting and efficient ceiling fans can noticeably lower household power bills. We upgrade indoor and outdoor lighting and install quiet, efficient fans in bedrooms and living areas.", "We’ll recommend options that suit your home and budget, and every job is quoted upfront."],
       ["LED lighting, indoors and out", "Quiet ceiling fans with low running costs", "Energy-efficient design to suit your budget"], [W + "2025/11/light-installation-sunshine-coast-electrical.jpg", W + "2025/11/feature-downlights.jpg"]),
      ("Connected & safe", "Data points, power points and safety switches", ["We install and repair telephone, data and NBN points so every room has strong, reliable internet, whether you work from home or stream in the evenings.", "Extra power and USB points mean fewer overloaded power boards and double adaptors, and we add safety switches (RCDs) to older homes that are missing protection."],
       ["Telephone, data and NBN points", "Power points and USB outlets", "Safety switches (RCDs) on every circuit"], [W + "2025/11/residential-electricians-content-img-3.webp", W + "2025/10/data-service.jpg"]),
    ],
    prices=[],
    faqs=FAQ["residential"] + FAQ["emergency"],
    closing_h2="Need a residential electrician? <em>Let’s talk.</em>",
    closing="Tell us what you need and we’ll come back with a detailed, upfront quote.",
  ),
  dict(
    slug="commercial-electrician", nav="Commercial", key="commercial",
    title="Commercial Electrician Sunshine Coast | Licensed & Reliable",
    eyebrow="Commercial electrician",
    h1="Keep your business <em>safe</em>, compliant and trading",
    lead="Local commercial electricians Sunshine Coast business owners trust to protect them from downtime and electrical hazards.",
    banner=W + "2025/10/Commercia-banner.jpg",
    panel=W + "2026/08/homepage-banner-img-3a-1.webp",
    card_img=W + "2025/10/Commercial-servicer.jpg",
    card_text="Installations, troubleshooting, repairs, maintenance, test and tag and full commercial fit-outs.",
    intro_h2="Commercial electrical work you can rely on",
    intro=[
      "We keep business electrical systems safe, energy efficient, code compliant and sustainable for the long term, with a proven track record of precision, reliability and workmanship.",
      "From resorts and shopping centres to offices, strata complexes, medical facilities and cafés, our commercial electricians keep Sunshine Coast businesses safe, compliant and trading.",
    ],
    intro_imgs=[W + "2025/10/Left-image-4.jpg", W + "2025/11/comm-fitout.png"],
    subs_h2="Commercial services we offer",
    subs=[
      ("Commercial Fit-Outs", W + "2025/11/comm-fitout.png"),
      ("Electrical Installations", W + "2025/10/Com-Installations-service.jpg"),
      ("Electrical Maintenance", W + "2025/10/Com-Maintenance-service.jpg"),
      ("Electrical Repairs", W + "2025/10/Com-Repairs-service.jpg"),
      ("Testing & Tagging", W + "2025/10/Test-service.jpg"),
      ("3-Phase Power", W + "2025/10/Phase-Power-service.jpg"),
    ],
    list_h2="Offices, shops and medical facilities",
    list_lead="Fit-outs for offices, cafés, restaurants, schools and other commercial spaces, planned alongside your builder and project manager.",
    list=["Power, lighting, data and switchboards for new or refurbished tenancies", "Efficient LED lighting that can significantly cut power bills", "Test and tag, with records for workplace safety obligations", "Fast diagnosis and repairs to get you trading again"],
    blocks=[
      ("Strata & resorts", "Strata complexes, resorts and holiday accommodation", ["Shared buildings have complex, always-on electrical systems. We maintain common areas, plant and lighting, test emergency and exit lighting every six months, and provide clear records for body corporates and property managers."],
       ["Common areas, plant and lighting", "Six-monthly emergency and exit light testing", "Priority 24/7 response for maintenance clients"], [W + "2025/11/commercial-cabinet-lighting-install.jpg", W + "2025/11/commercial-LED-installs.jpg"]),
    ],
    prices=[("$90–$140", "per hour", "Typical commercial electrician rate in business hours"), ("After hours", "higher rates", "Priority after-hours response for commercial call-outs"), ("24/7", PHONE, "Call any time when power fails and every hour costs money")],
    faqs=FAQ["commercial"] + FAQ["emergency"],
    closing_h2="Need a commercial electrician? <em>Let’s talk.</em>",
    closing="Whether it’s a fit-out, a maintenance plan or a fault, we’ll keep your business running.",
  ),
  dict(
    slug="electrical-installations", nav="Installation", key="installation",
    title="Electrical Installations Sunshine Coast | Licensed Team",
    eyebrow="Electrical installations",
    h1="Installations done safely, neatly and <em>to standard</em>",
    lead="Building, renovating or just need more power where you live and work? Our licensed team installs it right.",
    banner=W + "2025/10/Installation-banner.jpg",
    panel=W + "2026/08/Electrical-Fit-Outs-image.jpg",
    card_img=W + "2025/10/Installation-servicer.jpg",
    card_text="All types, makes and models of electrical components and systems, for homes and businesses.",
    intro_h2="Every installation tested before handover",
    intro=[
      "Bright Sparks completes electrical installations for homes and businesses across the Sunshine Coast, safely and to Australian standards.",
      "With more than 20 years of experience, we quote every job upfront, use certified products and test every circuit before handover.",
    ],
    intro_imgs=[W + "2025/11/abt-us-content-img-1.webp", W + "2025/11/electrical-fit-outs-content-img-3.png"],
    subs_h2="What we install",
    subs=[
      ("Electrical Fit-Outs", W + "2025/11/Ele-Outs-service-1.jpg"),
      ("Lighting Installations", W + "2025/11/Local-service-1.jpg"),
      ("Security Cameras", W + "2025/11/Cameras-service-1.jpg"),
      ("Switchboard Installations", W + "2025/10/Switchboard-service.jpg"),
      ("Switchboard Upgrades", W + "2025/10/S-Upgrades-service.jpg"),
      ("Hot Water Systems", W + "2025/10/hot-systems-service.jpg"),
      ("Smoke Alarms", W + "2025/11/Smo-Alarms-service-1.jpg"),
      ("Ceiling Fans", W + "2025/10/Ceiling-Fans-service.jpg"),
      ("Data & Fibre", W + "2025/10/data-service.jpg"),
    ],
    list_h2="Home electrical installations",
    list_lead="For new builds and renovations we provide full house wiring and rewiring, plus lighting and power design.",
    list=["Power points and USB outlets", "LED lighting, ceiling and exhaust fans", "Switchboards with safety switches", "Appliance circuits for ovens, cooktops, air con and hot water", "Compliant smoke alarms", "Security cameras"],
    blocks=[
      ("Data & network", "Power and network, planned together", ["We also install data cabling, network cabling, data points, phone wiring and fibre-optic cabling, so your power and network can be planned at the same time.", "Our team is ACMA-approved and registered as an NBN contractor, in addition to holding standard electrical licensing."],
       ["ACMA-approved cablers", "Registered NBN contractor", "Fully licensed electricians"], [W + "2025/11/Residential-image-1.jpg", W + "2025/10/data-service.jpg"]),
    ],
    prices=[("$150–$300", "new power point", "Usual cost for a new power point"), ("$80–$150", "per LED downlight", "Each, supplied and installed"), ("$200–$400", "ceiling fan", "Typical installed price"), ("$300–$800", "dedicated circuit", "For ovens, air con and other appliances")],
    faqs=FAQ["residential"][:1] + FAQ["data"][1:] + FAQ["general"][2:],
    closing_h2="Planning an installation? <em>Get a quote.</em>",
    closing="Every job is quoted upfront, completed with certified products and tested before handover.",
  ),
  dict(
    slug="maintenance-repairs", nav="Maintenance & Repairs", key="maintenance",
    title="Electrical Maintenance & Repairs Sunshine Coast",
    eyebrow="Maintenance & repairs",
    h1="Protect people and property with <em>planned</em> maintenance",
    lead="Keep every electrical system compliant and in working order, and avoid costly downtime.",
    banner=W + "2025/10/Maintenance-banner.jpg",
    panel=W + "2026/08/Electrical-Repairs-image.jpg",
    card_img=W + "2025/10/Maintenance-service.jpg",
    card_text="Accurate troubleshooting, timely repairs and cost-effective maintenance of all electrical systems.",
    intro_h2="Safety compliance, kept on schedule",
    intro=[
      "Our maintenance electricians make sure your electrical systems are fully compliant with Australian safety and quality standards, so you avoid hazards, lessen downtime and extend the life of your equipment.",
      "Safeguarding life and property is our number one priority. With us maintaining your systems, you’ll have peace of mind for years to come.",
    ],
    intro_imgs=[W + "2025/11/com-maintenance-img.png", W + "2025/11/elec-maintenance-content-img-2.png"],
    subs_h2="Maintenance & repair services",
    subs=[
      ("Electrical Maintenance", W + "2025/10/Com-Maintenance-service.jpg"),
      ("Electrical Repairs", W + "2025/10/Com-Repairs-service.jpg"),
      ("Testing & Tagging", W + "2025/10/Test-service.jpg"),
    ],
    list_h2="Stay on top of safety testing",
    list_lead="For businesses, strata buildings and resorts across the Sunshine Coast. Missed tests create liability, so we keep them on schedule.",
    list=["RCD (safety switch) testing and documentation", "Six-monthly emergency and exit lighting tests", "Scheduled inspections of boards, lighting and equipment", "Thermal and load checks to find hot spots early", "Clear reports and recommendations after every visit", "Priority 24/7 response for maintenance clients"],
    blocks=[
      ("Efficiency", "Lower running costs through maintenance", ["Regular maintenance finds hot spots and overloads early, replaces failed fittings promptly and keeps equipment running efficiently. Reactive repairs cost far more than planned maintenance.", "LED upgrades, sensors and timers can also significantly cut power bills for businesses."],
       [], [W + "2025/11/test-tagging-content-img-1.png", W + "2025/11/Com-Repairs-3.jpg"]),
    ],
    prices=[("$90–$140", "per hour", "Typical maintenance electrician rate on the Sunshine Coast"), ("Per visit", "or per year", "Maintenance plans tailored to your property"), ("24/7", "priority", "Priority response for maintenance clients")],
    faqs=FAQ["commercial"][1:] + FAQ["emergency"] + FAQ["general"][2:],
    closing_h2="Keep your business <em>running</em>.",
    closing=f"Ask about a maintenance plan tailored to your property. Call {PHONE} to get started.",
  ),
  dict(
    slug="data-fibre", nav="Data & Fibre", key="data",
    title="Data & Fibre Installations Sunshine Coast | ACMA Approved",
    eyebrow="Data & fibre",
    h1="Seamless, hassle-free <em>connections</em>",
    lead="Structured cabling, fibre upgrades and end-to-end data solutions from local data electricians you can trust.",
    banner=W + "2025/10/Data-Electrician-banner.jpg",
    panel=W + "2026/08/Data-Fibre-image-1.jpg",
    card_img=W + "2025/10/data-service.jpg",
    card_text="Data points, network and fibre-optic cabling, and phone wiring for homes and businesses.",
    intro_h2="Reliable, high-performance networks",
    intro=[
      "We do everything from start to finish: structured cabling, fibre optic upgrades and end-to-end commercial data solutions across the Sunshine Coast.",
      "Whether it’s for your home or business, fully licensed data electricians deliver network installations tailored to your property. No shortcuts, no guesswork.",
    ],
    intro_imgs=[W + "2025/11/Cables-data-Buderim-Electrical-Noosa.jpg", W + "2025/10/Right-image-7.jpg"],
    subs_h2="Data & fibre installation services",
    subs=[
      ("Data Cable Installation", W + "2025/10/data-service.jpg"),
      ("Network Cabling", W + "2025/10/Network-cabling-service.jpg"),
      ("Data Point Installation", W + "2025/10/Data-points-service.jpg"),
      ("Phone Wiring", W + "2025/10/Phone-wiring-service.jpg"),
      ("Fibre Optic Cabling", W + "2025/10/F-Cabling-service.jpg"),
    ],
    list_h2="End-to-end data & fibre solutions",
    list_lead="For residential and commercial properties, from network design to testing and certification.",
    list=["Structured data cabling", "Office and commercial network design", "Fibre optic cabling and upgrades (FTTP, NBN)", "NBN cabling, registered and ACMA-approved", "Ethernet and network point installation", "Commercial Wi-Fi extension and coverage", "Server room and comms cabinet fit-outs", "Testing, certification and fault repairs"],
    blocks=[
      ("Licensed & compliant", "Fully licensed and registered under ACMA", ["We’re fully licensed and registered under ACMA to perform data and fibre cabling for residential and commercial projects. Whether you’re upgrading your network or building from scratch, every installation complies with the relevant standards (AS/NZS 11801, TIA/EIA) and is certified with test results."],
       ["ACMA-approved cablers", "Registered NBN contractors", "Fully licensed electricians"], [W + "2025/10/Left-image-8.jpg", W + "2025/11/electrical-trades-Noosa-maroochydore.jpg"]),
    ],
    prices=[],
    faqs=FAQ["data"] + FAQ["general"][2:],
    closing_h2="Upgrade your network. <em>Get a quote.</em>",
    closing="High-quality, competitively priced data and fibre solutions for your home or business.",
  ),
  dict(
    slug="emergency-electrician", nav="24/7 Emergency", key="emergency",
    title="24/7 Emergency Electrician Sunshine Coast | Fast Call-Outs",
    eyebrow="24/7 emergency electrician",
    h1="Emergency? <em>We’re on our way.</em>",
    lead="A licensed electrician for homes, rentals and businesses, any hour of the day or night, from Caloundra to Noosa and the hinterland.",
    banner=W + "2025/11/test-tagging-banner.png",
    panel=W + "2026/08/emergency-elex-img-1.png",
    card_img=W + "2025/11/emergency-elex-img.png",
    card_text="On call 24 hours a day, 7 days a week, with fast and effective fixes for homes and businesses.",
    intro_h2="Fast, accurate fault finding",
    intro=[
      "When you call, we give safety advice while we’re on the way. On site, we isolate the hazard, test circuits and find the cause, so the fault is fixed properly the first time.",
      "With more than 20 years of experience, our licensed team makes dangerous faults safe and restores power quickly.",
    ],
    intro_imgs=[W + "2025/11/electrical-fit-outs-content-img-1.webp", W + "2025/11/electrical-fit-outs-content-img-2.webp"],
    subs_h2="",
    subs=[],
    list_h2="What we attend, 24/7",
    list_lead="Storms, ageing switchboards and overloaded circuits all cause electrical emergencies.",
    list=["Total or partial power loss", "Safety switches that won’t reset", "Sparking, smoke or burning smells", "Storm and water damage", "Faulty switchboards and damaged wiring", "Overloaded circuits"],
    blocks=[
      ("Compliance", "Safe, compliant repairs", ["Emergency work is carried out in line with the AS/NZS 3000 wiring standard.", "Landlords rely on us for fast, compliant repairs for tenants, and businesses get priority response for coolrooms, kitchens and trading equipment."],
       ["Homes and rental properties", "Priority response for businesses", "Coolrooms, kitchens and trading equipment"], [W + "2025/11/abt-us-content-img-1.webp", W + "2026/08/emergency-elex-img-1.png"]),
    ],
    prices=[("$200–$400", "after-hours call-out", "Typical cost, usually including the first 30 to 60 minutes on site"), ("Hourly", "after that", "Additional time charged hourly"), ("24/7", PHONE, "Call any time, day or night")],
    faqs=FAQ["emergency"] + FAQ["general"][2:],
    closing_h2="Power out? Switchboard tripping? <em>Call now.</em>",
    closing="A licensed electrician will head to you as quickly as possible, day or night.",
  ),
]
