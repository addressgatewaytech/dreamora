#!/usr/bin/env python3
"""Builds the static Dreamora website. Edit CONFIG, then run: python3 build.py"""
import os, json
ROOT = os.path.dirname(os.path.abspath(__file__))

CONFIG = {
  "legal_name": "Dreamora Interior Decoration W.L.L.",
  "brand": "Dreamora Decor",
  "cr": "254750",
  "phone": "+974 3164 2726",
  "phone2": "+974 3164 2727",
  "whatsapp": "+97431642726",
  "email": "Dreamora974@gmail.com",
  "address": "Doha, State of Qatar",
  "hours": "Saturday – Thursday, 9:00 AM – 9:00 PM",
  "instagram": "https://www.instagram.com/dreamora__decor/",
  "domain": "https://www.dreamora.qa",
  "updated": "19 October 2026",
}
C = CONFIG

NAV = [("index.html","Home"),("about.html","About"),("services.html","Décor Catalogue"),
       ("how-it-works.html","How to Book"),("faq.html","FAQ"),("contact.html","Contact")]
LEGAL = [("terms.html","Terms & Conditions"),("privacy.html","Privacy Policy"),
         ("refund.html","Refund & Cancellation"),("delivery.html","Delivery & Setup Policy"),
         ("payment.html","Payment & Security"),("complaints.html","Complaints & Consumer Rights")]

IG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>'
WA = '<svg width="28" height="28" viewBox="0 0 24 24" fill="#fff"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.2-.2-.5-.3z"/></svg>'

def head(title, desc, page):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Dreamora Decor Qatar</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{C['domain']}/{'' if page=='index.html' else page}">
<meta property="og:title" content="{title} | Dreamora Decor">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{C['domain']}/assets/img/logo-full.jpg">
<meta name="theme-color" content="#FEFBF6">
<link rel="icon" href="assets/img/logo-mark.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Great+Vibes&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"LocalBusiness","name":C['legal_name'],"alternateName":C['brand'],"url":C['domain'],"email":C['email'],"telephone":C['phone'],"address":{"@type":"PostalAddress","streetAddress":C['address'],"addressLocality":"Doha","addressCountry":"QA"},"sameAs":[C['instagram']],"priceRange":"QAR"})}</script>
</head>
<body>
<div class="topbar"><div class="container">
  <span>CR No. {C['cr']} · {C['legal_name']}</span>
  <span><a href="tel:{C['phone'].replace(' ','')}">{C['phone']}</a> / <a href="tel:{C['phone2'].replace(' ','')}">{C['phone2']}</a> · <a href="mailto:{C['email']}">{C['email']}</a></span>
</div></div>
<header class="site"><div class="container">
  <a class="brand" href="index.html" aria-label="Dreamora home"><img src="assets/img/logo-mark.jpg" alt="Dreamora butterfly logo"><span><span class="name">Dreamora</span><small>Interior Decoration W.L.L.</small></span></a>
  <nav class="main"><ul>
    {''.join(f'<li><a href="{h}" class="{"active" if h==page else ""}">{t}</a></li>' for h,t in NAV)}
    <li><a href="booking.html" class="cart-link {'active' if page=='booking.html' else ''}">Booking <span class="cart-count">0</span></a></li>
  </ul></nav>
  <button class="menu-btn" aria-label="Menu">☰ Menu</button>
</div></header>
<main>
'''

def foot():
    return f'''</main>
<footer class="site"><div class="container">
  <div class="f-grid">
    <div class="f-brand">
      <a href="index.html" style="display:inline-block;background:#FEFBF6;border-radius:16px;padding:10px 14px;margin-bottom:8px"><img src="assets/img/logo.jpg" alt="Dreamora Decor logo" style="width:150px;height:auto"></a>
      <p style="margin:6px 0 14px">Design your dreams. Bespoke event décor for birthdays, baby showers, ceremonies, weddings and celebrations across Qatar.</p>
      <a href="{C['instagram']}" target="_blank" rel="noopener" style="display:inline-flex;gap:8px;align-items:center">{IG} @dreamora__decor</a>
    </div>
    <div><h4>Explore</h4><ul>{''.join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV)}<li><a href="booking.html">Booking List</a></li></ul></div>
    <div><h4>Policies</h4><ul>{''.join(f'<li><a href="{h}">{t}</a></li>' for h,t in LEGAL)}</ul></div>
    <div><h4>Company</h4>
      <p><strong style="color:#fff">{C['legal_name']}</strong><br>Commercial Registration No. {C['cr']}<br>{C['address']}</p>
      <p style="margin-top:10px">Tel: <a href="tel:{C['phone'].replace(' ','')}">{C['phone']}</a> / <a href="tel:{C['phone2'].replace(' ','')}">{C['phone2']}</a><br>Email: <a href="mailto:{C['email']}">{C['email']}</a><br>{C['hours']}</p>
    </div>
  </div>
  <div class="f-legal">
    <span>© <span data-year></span> {C['legal_name']} · CR No. {C['cr']} · State of Qatar. All rights reserved.</span>
    <span>All prices are in Qatari Riyals (QAR). Governed by the laws of the State of Qatar.</span>
  </div>
</div></footer>
<a class="wa-float" href="https://wa.me/{''.join(ch for ch in C['whatsapp'] if ch.isdigit())}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{WA}</a>
<script>window.DREAMORA_CONFIG={json.dumps({"email":C['email'],"whatsapp":C['whatsapp'],"phone":C['phone']})};</script>
<script src="assets/js/catalogue.js"></script>
<script src="assets/js/main.js"></script>
</body></html>
'''

def page_head(eyebrow, title, sub, crumb):
    return f'''<section class="page-head"><div class="container">
<div class="crumbs"><a href="index.html">Home</a> / {crumb}</div>
<span class="eyebrow">{eyebrow}</span><h1>{title}</h1><p class="lead">{sub}</p></div></section>'''

def legal_meta():
    return f'''<div class="meta"><strong>{C['legal_name']}</strong> · Commercial Registration No. {C['cr']} · {C['address']}<br>
Email: <a href="mailto:{C['email']}">{C['email']}</a> · Tel: {C['phone']} / {C['phone2']} · Last updated: {C['updated']}</div>'''

ICON = {
 "cake":'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 21h16M5 21v-7a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v7M12 12V8M12 5.5c.8 0 1.2-.7 1.2-1.3S12 2 12 2s-1.2 1.6-1.2 2.2c0 .6.4 1.3 1.2 1.3zM5 16c1.5 1 3 1 4.5 0s3-1 4.5 0 3 1 5 0"/></svg>',
 "heart":'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>',
 "baby":'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="10" r="6"/><path d="M9.5 10h.01M14.5 10h.01M10 13c1.2.8 2.8.8 4 0M8 20h8"/></svg>',
 "ring":'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="14" r="6"/><path d="M9 4h6l-3 4z"/></svg>',
 "star":'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/></svg>',
 "flower":'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="9" r="2.5"/><path d="M12 6.5C12 4 10 3 9 4s0 4 3 5c3-1 4-4 3-5s-3 0-3 2.5zM12 11.5V21M12 16c-2 0-4-1-5-3M12 18c2 0 4-1 5-3"/></svg>',
}

SERVICES = [
 ("cake","Birthday Décor","Balloon arches, backdrops, neon signage, cake tables and number marquees for every age."),
 ("star","Themed Kids’ Parties","Character and storybook themes styled end-to-end — from welcome boards to plinths and props."),
 ("baby","Baby Shower & Valakappu","Traditional and modern ‘Mom to be’ celebrations with floral stages, bangle stations and drapes."),
 ("flower","Naming Ceremony & Noolukettu","Elegant, culturally inspired setups with brass lamps, jasmine strings and pastel florals."),
 ("ring","Weddings, Engagements & Bride-to-be","Stage décor, entrance styling and photo corners designed around your palette."),
 ("heart","Anniversaries & Holy Communion","Intimate, refined décor for milestone moments at home, halls, hotels and restaurants."),
]

def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f: f.write(html)

# ---------------- HOME ----------------
home = head("Event & Party Decoration in Qatar","Dreamora Interior Decoration W.L.L. – bespoke birthday, baby shower, valakappu, naming ceremony, wedding and themed party décor in Doha, Qatar. Book online.","index.html") + f'''
<section class="hero"><div class="container">
  <div>
    <span class="eyebrow">Event décor studio · Doha, Qatar</span>
    <h1 style="margin-top:12px">Design your <span class="script">dreams</span><br>into every celebration</h1>
    <p class="lead">From first birthdays to valakappu, naming ceremonies, bride-to-be and weddings — Dreamora creates balloon, floral and themed décor that turns your venue into a memory.</p>
    <div class="actions"><a class="btn" href="services.html">View Décor Catalogue</a><a class="btn ghost" href="booking.html">Book Your Event</a></div>
    <div class="badges"><div><strong>670+</strong>Setups shared</div><div><strong>All Qatar</strong>Delivery &amp; setup</div><div><strong>100%</strong>Custom themes</div></div>
  </div>
  <div class="hero-collage">
    <img src="assets/img/gallery/purple-magic.jpg" alt="Purple and silver balloon ring arch">
    <img src="assets/img/gallery/valakappu-stage.jpg" alt="Valakappu floral stage décor">
  </div>
</div></section>

<section><div class="container">
  <div class="section-head"><span class="eyebrow">What we do</span><h2>Décor for every <span class="script">milestone</span></h2><p class="muted">Every setup is designed, delivered, installed and dismantled by our team, so you can simply enjoy the day.</p></div>
  <div class="grid g3">{''.join(f'<div class="card"><div class="ic">{ICON[i]}</div><h3>{t}</h3><p>{d}</p></div>' for i,t,d in SERVICES)}</div>
</div></section>

<section class="alt"><div class="container">
  <div class="section-head"><span class="eyebrow">From our Instagram</span><h2>Featured <span class="script">setups</span></h2><p class="muted">A selection of recent work. Tap a photo to view it larger, or add a setup to your booking list.</p></div>
  <div class="grid g3" data-catalogue data-limit="6"></div>
  <p class="center" style="margin-top:36px"><a class="btn ghost" href="services.html">See the full catalogue</a></p>
</div></section>

<section><div class="container">
  <div class="section-head"><span class="eyebrow">Simple booking</span><h2>How it <span class="script">works</span></h2></div>
  <div class="grid g4 steps">
    <div class="card"><h3>Choose</h3><p>Browse the catalogue and add the setups you like — or tell us your own theme.</p></div>
    <div class="card"><h3>Request</h3><p>Send your event date, venue and details through our booking form.</p></div>
    <div class="card"><h3>Confirm</h3><p>Receive a written quotation in QAR and confirm with a secure advance payment.</p></div>
    <div class="card"><h3>Celebrate</h3><p>We deliver, set up before your guests arrive and dismantle afterwards.</p></div>
  </div>
</div></section>

<section style="padding-top:0"><div class="container">
  <div class="cta"><div><h2>Planning a celebration?</h2><p>Share your date and theme — we’ll reply with ideas and a quotation.</p></div>
  <div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn light" href="booking.html">Start Booking</a><a class="btn ghost" style="border-color:#fff;color:#fff" href="{C['instagram']}" target="_blank" rel="noopener">Follow on Instagram</a></div></div>
</div></section>
''' + foot()
write("index.html", home)

# ---------------- ABOUT ----------------
about = head("About Us","About Dreamora Interior Decoration W.L.L., a Qatar-registered event decoration company (CR No. 254750).","about.html") + page_head("Our story","About <span class='script'>Dreamora</span>","A Qatar-based décor studio dedicated to making every celebration feel personal, beautiful and effortless.","About") + f'''
<section><div class="container grid g2" style="align-items:center;gap:56px">
  <div><img src="assets/img/logo-full.jpg" alt="Dreamora Decor logo" style="border-radius:24px;box-shadow:var(--shadow);mix-blend-mode:multiply"></div>
  <div>
    <span class="eyebrow">Who we are</span>
    <h2 style="margin:10px 0 16px">Design your dreams</h2>
    <p class="muted">Dreamora Decor is the trading name of <strong>{C['legal_name']}</strong>, a limited liability company registered in the State of Qatar under Commercial Registration No. <strong>{C['cr']}</strong>.</p>
    <p class="muted" style="margin-top:12px">We design and install event décor for birthdays, baby showers and valakappu, naming ceremonies and noolukettu, bride-to-be events, engagements, weddings, anniversaries and holy communions. Our signature is soft, elegant styling — organic balloon garlands, fresh and faux florals, drapes, neon signage and custom printed elements — tailored to each family’s theme and culture.</p>
    <p class="muted" style="margin-top:12px">Like the butterflies in our logo, every Dreamora setup is made of many small details that come together into one beautiful moment.</p>
  </div>
</div></section>
<section class="alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Our promise</span><h2>Why families choose <span class="script">us</span></h2></div>
  <div class="grid g4">
    <div class="card"><h3>Personal design</h3><p>Every setup is adapted to your colours, names, theme and venue.</p></div>
    <div class="card"><h3>Transparent pricing</h3><p>Written quotations in QAR with no hidden charges.</p></div>
    <div class="card"><h3>On-time setup</h3><p>We arrive early, set up safely and leave the venue clean.</p></div>
    <div class="card"><h3>Licensed &amp; local</h3><p>A registered Qatari company serving Doha and all municipalities.</p></div>
  </div>
</div></section>
<section><div class="container legal">
  <h2>Company information</h2>
  <table class="t">
    <tr><th>Legal name</th><td>{C['legal_name']}</td></tr>
    <tr><th>Trading name</th><td>{C['brand']}</td></tr>
    <tr><th>Commercial Registration No.</th><td>{C['cr']}</td></tr>
    <tr><th>Legal form</th><td>Limited Liability Company (W.L.L.), State of Qatar</td></tr>
    <tr><th>Registered address</th><td>{C['address']}</td></tr>
    <tr><th>Telephone</th><td>{C['phone']}<br>{C['phone2']}</td></tr>
    <tr><th>Email</th><td>{C['email']}</td></tr>
    <tr><th>Working hours</th><td>{C['hours']}</td></tr>
  </table>
</div></section>
''' + foot()
write("about.html", about)

# ---------------- SERVICES / CATALOGUE ----------------
svc = head("Décor Catalogue","Browse Dreamora's event decoration catalogue – birthday, themed party, valakappu and ceremony setups in Qatar. Prices in QAR.","services.html") + page_head("Service catalogue","Décor <span class='script'>Catalogue</span>","Real setups from our Instagram. Add any design to your booking list — every setup can be customised in colour, size and name.","Décor Catalogue") + f'''
<section><div class="container">
  <div class="filters" data-filters></div>
  <div class="grid g3" data-catalogue></div>
  <div class="note" style="margin-top:36px">All prices are quoted in Qatari Riyals (QAR) and include design, delivery, installation and dismantling within Doha unless stated otherwise. Final pricing depends on size, venue and customisation and is confirmed in a written quotation before any payment. Photos show previous work; balloons, flowers and printed items may vary slightly in shade and availability.</div>
</div></section>
<section class="alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Also available</span><h2>Add-ons &amp; <span class="script">extras</span></h2></div>
  <div class="grid g4">
    <div class="card"><h3>Neon signs</h3><p>‘Happy Birthday’, ‘Oh Baby’ and custom name neons.</p></div>
    <div class="card"><h3>Welcome boards</h3><p>Printed easel boards with name, date and theme artwork.</p></div>
    <div class="card"><h3>Marquee numbers</h3><p>Balloon-filled or light-up numbers and letters.</p></div>
    <div class="card"><h3>Table styling</h3><p>Cake, dessert and gift tables with plinths and props.</p></div>
  </div>
  <p class="center" style="margin-top:32px"><a class="btn" href="booking.html">Request a quotation</a></p>
</div></section>
''' + foot()
write("services.html", svc)

# ---------------- HOW IT WORKS ----------------
how = head("How to Book","How to book Dreamora event decoration online in Qatar – steps, payment, delivery and setup.","how-it-works.html") + page_head("Booking guide","How to <span class='script'>book</span>","A clear, simple process from first idea to final setup.","How to Book") + '''
<section><div class="container">
  <div class="grid g3 steps">
    <div class="card"><h3>Browse &amp; select</h3><p>Explore the Décor Catalogue and tap “Add to booking” on any setup you like. You can also request a fully custom theme.</p></div>
    <div class="card"><h3>Submit your request</h3><p>On the Booking page, enter your event type, date, location and contact details, and accept our Terms and Refund &amp; Cancellation Policy.</p></div>
    <div class="card"><h3>Receive a quotation</h3><p>We confirm availability and send a written quotation in QAR with an itemised scope, normally within 24 hours.</p></div>
    <div class="card"><h3>Confirm with advance</h3><p>Your date is reserved once the advance payment is received through a secure payment link or bank transfer. You receive an electronic invoice/receipt.</p></div>
    <div class="card"><h3>Setup day</h3><p>Our team arrives at the agreed time, installs the décor and hands over to you before guests arrive.</p></div>
    <div class="card"><h3>Dismantling</h3><p>After the event we collect all rental items at the agreed time. The remaining balance is settled on or before the event day.</p></div>
  </div>
  <p class="center" style="margin-top:36px"><a class="btn" href="services.html">Start browsing</a></p>
</div></section>
''' + foot()
write("how-it-works.html", how)

# ---------------- BOOKING ----------------
book = head("Booking","Send a booking request to Dreamora Decor, Qatar.","booking.html") + page_head("Your booking","Booking <span class='script'>request</span>","Review your selected setups and send your event details. No payment is taken on this page.","Booking") + f'''
<section><div class="container cart-wrap">
  <div class="card">
    <h3 style="margin-bottom:6px">Selected setups</h3>
    <div data-cart></div>
    <div class="summary total"><span>Estimated total</span><span data-total>—</span></div>
    <p class="muted" style="font-size:.85rem;margin-top:8px">Prices in QAR. Final amount confirmed in your written quotation. <a href="services.html">+ Add more setups</a></p>
  </div>
  <div class="card">
    <h3 style="margin-bottom:16px">Event details</h3>
    <form id="bookingForm">
      <div class="f">
        <div><label for="n">Full name *</label><input id="n" name="name" required autocomplete="name"></div>
        <div><label for="p">Mobile (Qatar) *</label><input id="p" name="phone" required type="tel" placeholder="+974" autocomplete="tel"></div>
        <div class="full"><label for="e">Email *</label><input id="e" name="email" type="email" required autocomplete="email"></div>
        <div><label for="ev">Event type *</label><select id="ev" name="event" required><option value="">Select…</option><option>Birthday</option><option>Themed kids’ party</option><option>Baby shower / Valakappu</option><option>Naming ceremony / Noolukettu</option><option>Bride to be</option><option>Engagement / Wedding</option><option>Anniversary</option><option>Holy Communion</option><option>Corporate / Other</option></select></div>
        <div><label for="d">Event date *</label><input id="d" name="date" type="date" required></div>
        <div><label for="l">Venue / area *</label><input id="l" name="location" required placeholder="e.g. Home – Al Wakrah / Hotel hall"></div>
        <div><label for="g">Approx. guests</label><input id="g" name="guests" type="number" min="1"></div>
        <div class="full"><label for="no">Theme, colours, names &amp; notes</label><textarea id="no" name="notes" rows="4"></textarea></div>
        <div class="full"><label>Send request via</label>
          <div style="display:flex;gap:18px"><label class="check"><input type="radio" name="channel" value="whatsapp" checked> WhatsApp</label><label class="check"><input type="radio" name="channel" value="email"> Email</label></div></div>
        <div class="full"><label class="check"><input type="checkbox" required> I have read and agree to the <a href="terms.html" target="_blank">Terms &amp; Conditions</a>, <a href="refund.html" target="_blank">Refund &amp; Cancellation Policy</a> and <a href="privacy.html" target="_blank">Privacy Policy</a>.</label></div>
        <div class="full"><button class="btn" type="submit" style="width:100%">Send booking request</button></div>
      </div>
    </form>
    <div class="note" style="margin-top:16px">Submitting this form does not create a binding contract or charge you. A booking is confirmed only after you accept our written quotation and the advance payment is received.</div>
  </div>
</div></section>
''' + foot()
write("booking.html", book)

# ---------------- FAQ ----------------
faqs = [
 ("Which areas in Qatar do you cover?","We serve Doha and all municipalities of Qatar, including Al Wakrah, Al Rayyan, Lusail, Al Khor and Umm Salal. A transport charge may apply outside Doha and is shown in your quotation."),
 ("How far in advance should I book?","We recommend 7–14 days for standard setups and 3–4 weeks for weddings and large events. Online requests require at least 3 days’ notice; urgent requests are accepted subject to availability."),
 ("Can you customise colours, names and themes?","Yes. Every catalogue setup can be adapted in colour palette, size, signage and props, or we can design a completely new concept."),
 ("How much advance payment is required?","A 50% advance confirms your date. The balance is payable on or before the event day. Full details are in our Payment & Security Policy."),
 ("Can I cancel or change my date?","Yes, subject to the notice periods in our Refund & Cancellation Policy. Date changes are free once if requested at least 7 days in advance and subject to availability."),
 ("Do you set up at hotels and halls?","Yes. Please confirm the venue’s access time and any venue rules (e.g. no helium, no open flame) so we can plan accordingly."),
 ("Are the décor items mine to keep?","Backdrops, stands, plinths, neon signs, marquee numbers and props are rental items collected after the event. Balloons and personalised prints can be kept unless stated otherwise."),
 ("How do I pay?","Through a secure online payment link (Visa, Mastercard, debit cards) or bank transfer to our company account. All amounts are in Qatari Riyals (QAR)."),
]
faq = head("FAQ","Frequently asked questions about booking event decoration with Dreamora in Qatar.","faq.html") + page_head("Help centre","Frequently asked <span class='script'>questions</span>","Quick answers about booking, payments, delivery and setup.","FAQ") + '<section><div class="container legal">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs) + '<p class="center" style="margin-top:28px">Still have a question? <a href="contact.html">Contact us</a>.</p></div></section>' + foot()
write("faq.html", faq)

# ---------------- CONTACT ----------------
contact = head("Contact Us","Contact Dreamora Interior Decoration W.L.L. – phone, email, WhatsApp and address in Doha, Qatar.","contact.html") + page_head("Get in touch","Contact <span class='script'>us</span>","We’d love to hear about your celebration.","Contact") + f'''
<section><div class="container grid g2" style="gap:32px;align-items:start">
  <div class="card">
    <h3 style="margin-bottom:14px">{C['legal_name']}</h3>
    <table class="t">
      <tr><th>CR No.</th><td>{C['cr']}</td></tr>
      <tr><th>Address</th><td>{C['address']}</td></tr>
      <tr><th>Phone</th><td><a href="tel:{C['phone'].replace(' ','')}">{C['phone']}</a> / <a href="tel:{C['phone2'].replace(' ','')}">{C['phone2']}</a></td></tr>
      <tr><th>Email</th><td><a href="mailto:{C['email']}">{C['email']}</a></td></tr>
      <tr><th>Instagram</th><td><a href="{C['instagram']}" target="_blank" rel="noopener">@dreamora__decor</a></td></tr>
      <tr><th>Hours</th><td>{C['hours']}</td></tr>
    </table>
    <p class="muted" style="font-size:.9rem">For complaints, please see our <a href="complaints.html">Complaints &amp; Consumer Rights</a> page. We respond to all messages within 2 working days.</p>
  </div>
  <div class="card">
    <h3 style="margin-bottom:14px">Send a message</h3>
    <form id="contactForm"><div class="f">
      <div><label for="cn">Name *</label><input id="cn" name="name" required></div>
      <div><label for="cp">Phone *</label><input id="cp" name="phone" type="tel" required></div>
      <div class="full"><label for="ce">Email *</label><input id="ce" name="email" type="email" required></div>
      <div class="full"><label for="cs">Subject *</label><select id="cs" name="subject" required><option>General enquiry</option><option>Quotation</option><option>Existing booking</option><option>Complaint / feedback</option></select></div>
      <div class="full"><label for="cm">Message *</label><textarea id="cm" name="message" rows="5" required></textarea></div>
      <div class="full"><label class="check"><input type="checkbox" required> I agree to the processing of my details as described in the <a href="privacy.html">Privacy Policy</a>.</label></div>
      <div class="full"><button class="btn" style="width:100%">Send message</button></div>
    </div></form>
  </div>
</div></section>
''' + foot()
write("contact.html", contact)

# ---------------- LEGAL PAGES ----------------
def legal_page(fname, title, desc, body):
    write(fname, head(title, desc, fname) + page_head("Legal", title, f"{C['legal_name']} · CR No. {C['cr']}", title) + f'<section><div class="container legal">{legal_meta()}{body}</div></section>' + foot())

LN, CR = C['legal_name'], C['cr']

legal_page("terms.html","Terms &amp; Conditions","Terms and conditions for using the Dreamora website and booking event decoration services in Qatar.", f'''
<h2>1. About these terms</h2>
<p>These Terms &amp; Conditions (“Terms”) govern your use of {C['domain']} (the “Website”) and any booking of decoration services from <strong>{LN}</strong>, Commercial Registration No. {CR}, State of Qatar (“Dreamora”, “we”, “us”). By using the Website or placing a booking you agree to these Terms, our <a href="privacy.html">Privacy Policy</a>, <a href="refund.html">Refund &amp; Cancellation Policy</a>, <a href="delivery.html">Delivery &amp; Setup Policy</a> and <a href="payment.html">Payment &amp; Security Policy</a>.</p>
<h2>2. Eligibility</h2>
<p>You must be at least 18 years old and legally able to enter into contracts under the laws of the State of Qatar to place a booking.</p>
<h2>3. Services</h2>
<p>We provide event decoration services including design, supply, rental, delivery, installation and dismantling of décor. Catalogue photographs illustrate previous work; final colours, balloons, flowers and props may vary slightly due to availability and screen display. Substitutions of equal or higher value may be made with notice to you.</p>
<h2>4. Prices</h2>
<ul><li>All prices are displayed and charged in Qatari Riyals (QAR).</li><li>“Starting from” prices are indicative. The binding price is the one stated in your written quotation/invoice.</li><li>Quotations are valid for 7 days unless stated otherwise.</li><li>Transport outside Doha, venue fees, after-hours setup or late dismantling may incur additional charges, which will always be stated in advance.</li></ul>
<h2>5. Booking &amp; contract formation</h2>
<p>A booking request sent through the Website, WhatsApp or email is an invitation to quote. A binding contract is formed only when (a) you accept our written quotation and (b) we receive the advance payment and issue a confirmation. We may decline a booking where the date is unavailable or the request is unsafe or unlawful.</p>
<h2>6. Customer responsibilities</h2>
<ul><li>Provide accurate event details, venue address and access times.</li><li>Obtain any venue permissions required for decoration, helium balloons, neon signs or electrical connections.</li><li>Provide a safe working area and access to a power socket where needed.</li><li>Take reasonable care of rental items during the event.</li></ul>
<h2>7. Rental items &amp; damage</h2>
<p>Backdrops, stands, plinths, neon signs, marquee numbers, props and similar items remain the property of Dreamora and are collected after the event. Loss or damage beyond normal wear (other than by our staff) will be charged at repair or replacement cost, with supporting details provided to you.</p>
<h2>8. Personalised and custom items</h2>
<p>Printed name boards, custom signage and other personalised items are made to order. Please check spelling and dates in the proof we send; once approved, personalised items cannot be refunded except where defective.</p>
<h2>9. Photographs</h2>
<p>We may photograph our décor setups for our portfolio and social media. We will not publish photographs showing you or your guests without your consent. Please tell us if you prefer that your setup is not shared.</p>
<h2>10. Safety</h2>
<p>Children must be supervised around balloons, stands and electrical items. Uninflated or burst balloons are a choking hazard and must be kept away from children under 8.</p>
<h2>11. Limitation of liability</h2>
<p>Nothing in these Terms limits your rights under Qatar Law No. (8) of 2008 on Consumer Protection. Subject to that law, our total liability for any booking is limited to the amount you paid for that booking. We are not liable for delays or failure caused by events beyond our reasonable control (force majeure), including government restrictions, severe weather, road closures or venue decisions.</p>
<h2>12. Website use &amp; intellectual property</h2>
<p>All content on this Website, including the Dreamora name, butterfly logo, designs and photographs, belongs to {LN} and may not be copied or used commercially without written permission. You must not misuse the Website, attempt unauthorised access or submit false bookings.</p>
<h2>13. Electronic communications</h2>
<p>In accordance with the Electronic Commerce and Transactions Law (Law No. 16 of 2010), you agree that quotations, confirmations, invoices and notices may be provided electronically and have the same effect as written documents.</p>
<h2>14. Governing law &amp; disputes</h2>
<p>These Terms are governed by the laws of the State of Qatar. We will first try to resolve any complaint amicably (see <a href="complaints.html">Complaints</a>). Unresolved disputes fall under the jurisdiction of the competent courts of the State of Qatar, without prejudice to your right to contact the Ministry of Commerce and Industry.</p>
<h2>15. Changes</h2>
<p>We may update these Terms from time to time. The version published on the date of your booking applies to that booking.</p>
''')

legal_page("privacy.html","Privacy Policy","How Dreamora Interior Decoration W.L.L. collects, uses and protects personal data in line with Qatar's Personal Data Privacy Protection Law.", f'''
<p>{LN} (“we”) respects your privacy and processes personal data in accordance with Qatar Law No. (13) of 2016 on the Protection of Personal Data Privacy and related regulations.</p>
<h2>1. Data we collect</h2>
<ul><li><strong>Contact details:</strong> name, mobile number, email address.</li><li><strong>Event details:</strong> event type, date, venue/address, guest count, theme, names to be printed on décor.</li><li><strong>Payment records:</strong> amounts, dates and references. Card details are entered directly on our payment provider’s secure page and are never stored by us.</li><li><strong>Technical data:</strong> basic browser information and, if enabled, analytics cookies.</li><li><strong>Booking list:</strong> the setups you add are stored only in your own browser (local storage) until you send a request.</li></ul>
<h2>2. How we use your data</h2>
<ul><li>To respond to enquiries, prepare quotations and deliver your booking.</li><li>To issue invoices and meet legal, tax and accounting obligations.</li><li>To contact you about your booking (calls, WhatsApp, SMS, email).</li><li>To send offers only if you have opted in; you may opt out at any time.</li></ul>
<h2>3. Legal basis</h2>
<p>We process data to perform our contract with you, to comply with legal obligations, and with your consent where required.</p>
<h2>4. Sharing</h2>
<p>We do not sell your data. We share it only with service providers needed to deliver your booking (e.g. payment gateway, printing suppliers, delivery staff, email/WhatsApp providers) under confidentiality obligations, or when required by Qatari authorities.</p>
<h2>5. Children</h2>
<p>Our services are booked by adults. We may receive a child’s name or age for décor printing; this is used only for your event and is not published without your consent.</p>
<h2>6. Retention</h2>
<p>Booking and invoice records are kept for the period required by Qatari law; enquiry data that does not lead to a booking is deleted within 12 months.</p>
<h2>7. Security</h2>
<p>The Website uses HTTPS encryption. Access to customer data is limited to authorised staff.</p>
<h2>8. Your rights</h2>
<p>You may request access to, correction of, or deletion of your personal data, withdraw consent, or object to marketing by emailing <a href="mailto:{C['email']}">{C['email']}</a>. We respond within 30 days.</p>
<h2>9. Cookies</h2>
<p>We use essential browser storage to remember your booking list. If analytics cookies are added, you will be informed and can disable them in your browser settings.</p>
<h2>10. Contact</h2>
<p>Data enquiries: {LN}, {C['address']} · <a href="mailto:{C['email']}">{C['email']}</a> · {C['phone']} / {C['phone2']}.</p>
''')

legal_page("refund.html","Refund &amp; Cancellation Policy","Refund, return and cancellation policy for Dreamora event decoration bookings in Qatar.", f'''
<p>Because décor is planned, sourced and often personalised for a specific date, the following policy applies. It does not affect your statutory rights under Qatar Law No. (8) of 2008 on Consumer Protection.</p>
<h2>1. Cancellation by you</h2>
<table class="t"><tr><th>Notice before event date</th><th>Refund of amount paid</th></tr>
<tr><td>14 days or more</td><td>Full refund of the advance, less the cost of any personalised items already produced</td></tr>
<tr><td>7 – 13 days</td><td>50% of the advance refunded</td></tr>
<tr><td>3 – 6 days</td><td>25% of the advance refunded, or 100% credited to a future booking within 6 months</td></tr>
<tr><td>Less than 72 hours</td><td>No refund; advance may be credited to a future booking within 3 months at our discretion</td></tr></table>
<p>Cancellations must be sent in writing by email or WhatsApp. The notice period is calculated from the time we receive your message.</p>
<h2>2. Change of date or design</h2>
<ul><li>One date change is free if requested at least 7 days before the event, subject to availability.</li><li>Design changes are accepted up to 5 days before the event; any price difference will be quoted.</li></ul>
<h2>3. Cancellation by Dreamora</h2>
<p>If we must cancel for any reason within our control, you receive a <strong>100% refund</strong> of all amounts paid. If we cannot deliver due to force majeure, we will offer a new date or a full refund of amounts paid, less personalised items already delivered to you.</p>
<h2>4. Service issues &amp; returns</h2>
<p>As our services are delivered and installed on site, physical “returns” do not apply. If any part of the agreed setup is missing or materially different from your confirmed quotation, please inform our on-site team or contact us within <strong>24 hours</strong> of the event with photos. We will investigate and, where justified, provide a partial refund proportional to the affected items or a credit, at your choice.</p>
<h2>5. Purchased (non-rental) items</h2>
<p>Where you buy a décor item to keep, you may return it unused and in original condition within 7 days of delivery for a refund, unless it is personalised, perishable (fresh flowers, inflated balloons) or used. Defective items are replaced or refunded in full.</p>
<h2>6. How refunds are paid</h2>
<p>Approved refunds are made to the original payment method (card refunds via our payment provider, or bank transfer) in QAR within <strong>14 working days</strong> of approval. Your card issuer may take additional time to show the credit.</p>
<h2>7. Contact</h2>
<p>Refund and cancellation requests: <a href="mailto:{C['email']}">{C['email']}</a> · {C['phone']} / {C['phone2']}.</p>
''')

legal_page("delivery.html","Delivery &amp; Setup Policy","Delivery, installation and dismantling policy for Dreamora décor across Qatar.", f'''
<h2>1. Service area</h2>
<p>We deliver and install across the State of Qatar. Setups within Doha include delivery. Locations outside Doha (e.g. Al Khor, Dukhan, Mesaieed, Al Shamal) may carry a transport charge stated in your quotation.</p>
<h2>2. Setup timing</h2>
<ul><li>Setup time is agreed in your confirmation and depends on the design — typically 1 to 4 hours before the event.</li><li>Please ensure the venue is accessible at the agreed time. Waiting time caused by venue access delays beyond 30 minutes may be charged.</li><li>Setups between 11:00 PM and 7:00 AM are subject to availability and an after-hours fee.</li></ul>
<h2>3. Dismantling &amp; collection</h2>
<p>Rental items are collected after the event at the agreed time (same night or next day). Late collection requested by you may incur an additional fee.</p>
<h2>4. Delivery of purchased items</h2>
<p>Items you buy to keep are delivered within 2–5 working days in Doha, or collected from us by arrangement. You will be notified of the delivery window in advance.</p>
<h2>5. Venue requirements</h2>
<p>You are responsible for venue approval, parking/loading access and any venue restrictions. We follow venue safety rules and may adjust the design where a venue does not allow certain items.</p>
<h2>6. Handover</h2>
<p>Please inspect the setup at handover. Any concerns should be raised with our team on site so they can be fixed immediately.</p>
''')

legal_page("payment.html","Payment &amp; Security Policy","Accepted payment methods, payment terms and security for Dreamora bookings.", f'''
<h2>1. Currency</h2>
<p>All prices, quotations, invoices and payments are in <strong>Qatari Riyals (QAR)</strong>.</p>
<h2>2. Payment methods</h2>
<ul><li>Secure online payment link — Visa, Mastercard and local debit cards — processed by a licensed payment service provider in Qatar.</li><li>Bank transfer to the company account of {LN} (details on your invoice).</li><li>Cash or card on delivery for the balance, where agreed.</li></ul>
<h2>3. Payment terms</h2>
<ul><li><strong>Advance:</strong> 50% of the quotation to confirm the booking.</li><li><strong>Balance:</strong> due on or before the event day, prior to setup.</li><li>Bookings made less than 72 hours before the event require full payment.</li></ul>
<h2>4. Invoices &amp; receipts</h2>
<p>An electronic invoice/receipt showing our legal name and CR No. {CR} is issued for every payment.</p>
<h2>5. Card security</h2>
<p>Card payments are processed on the payment provider’s encrypted (HTTPS/TLS, 3-D Secure) page. Dreamora does not see or store your full card number or CVV. Never share card details by WhatsApp, phone or email — we will never ask you to.</p>
<h2>6. Failed or duplicate payments</h2>
<p>If a payment fails or you are charged twice, contact us with the transaction reference and any duplicate amount will be refunded in full to the original method within 14 working days.</p>
''')

legal_page("complaints.html","Complaints &amp; Consumer Rights","How to raise a complaint with Dreamora and your consumer rights in Qatar.", f'''
<h2>1. Our commitment</h2>
<p>We want every customer to be delighted. If something is not right, please tell us so we can fix it.</p>
<h2>2. How to complain</h2>
<ol><li>Contact us by email at <a href="mailto:{C['email']}">{C['email']}</a> or WhatsApp {C['phone']}, with your name, booking date, description and photos if possible.</li><li>We acknowledge your complaint within <strong>2 working days</strong>.</li><li>We aim to provide a resolution within <strong>7 working days</strong>.</li></ol>
<h2>3. Your consumer rights</h2>
<p>As a consumer in Qatar you are protected by Law No. (8) of 2008 on Consumer Protection and its implementing regulations, including the right to accurate information, clear prices in Qatari Riyals, an invoice for your purchase, and services that match what was agreed.</p>
<h2>4. Escalation</h2>
<p>If you are not satisfied with our response, you may contact the Consumer Protection Department of the Ministry of Commerce and Industry, State of Qatar, through its official channels.</p>
<h2>5. Business details</h2>
<p>{LN} · CR No. {CR} · {C['address']}.</p>
''')

# sitemap & robots
pages = [h for h,_ in NAV] + ["booking.html"] + [h for h,_ in LEGAL]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{C['domain']}/{'' if p=='index.html' else p}</loc></url>\n" for p in pages) + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {C['domain']}/sitemap.xml\n")
write("404.html", head("Page not found","Page not found","404.html") + page_head("Oops","Page not <span class='script'>found</span>","The page you’re looking for has flown away.","404") + '<section class="center"><a class="btn" href="index.html">Back to home</a></section>' + foot())
print("Built", len(pages)+1, "pages")
