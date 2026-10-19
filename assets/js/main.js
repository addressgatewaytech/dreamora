/* Dreamora Interior Decoration W.L.L. – site script */
(function(){
  const CFG = window.DREAMORA_CONFIG || {};
  const KEY = "dreamora_booking";
  const $ = (s,c=document)=>c.querySelector(s);
  const $$ = (s,c=document)=>[...c.querySelectorAll(s)];

  // storage helpers (safe)
  const load = ()=>{ try{ return JSON.parse(localStorage.getItem(KEY))||[] }catch(e){ return [] } };
  const save = v=>{ try{ localStorage.setItem(KEY,JSON.stringify(v)) }catch(e){} };
  const fmt = p => p==null ? "Price on request" : "QAR " + Number(p).toLocaleString("en-QA",{minimumFractionDigits:2});

  // mobile menu
  const btn=$(".menu-btn"), nav=$("nav.main");
  if(btn&&nav) btn.addEventListener("click",()=>nav.classList.toggle("open"));

  // year
  $$("[data-year]").forEach(e=>e.textContent=new Date().getFullYear());

  // cart count
  function count(){ const n=load().length; $$(".cart-count").forEach(e=>e.textContent=n); }
  count();

  function toast(msg){
    let t=$(".toast"); if(!t){ t=document.createElement("div"); t.className="toast"; document.body.appendChild(t); }
    t.textContent=msg; t.classList.add("show"); setTimeout(()=>t.classList.remove("show"),2200);
  }

  function addItem(id){
    const list=load(); if(list.includes(id)){ toast("Already in your booking list"); return; }
    list.push(id); save(list); count(); toast("Added to your booking list");
  }

  // catalogue render
  const cat=window.DREAMORA_CATALOGUE||[];
  const grid=$("[data-catalogue]");
  if(grid){
    const limit=+grid.dataset.limit||0;
    const filt=$("[data-filters]");
    let current="all";
    function render(){
      let items=cat.filter(i=>current==="all"||i.cat===current);
      if(limit) items=items.slice(0,limit);
      grid.innerHTML=items.map(i=>`
        <article class="item">
          <div class="ph" data-zoom="assets/img/gallery/${i.img}">
            <img src="assets/img/gallery/${i.img}" alt="${i.title} – Dreamora event decoration in Qatar" loading="lazy">
            <span class="tag">${(window.DREAMORA_CATEGORIES||{})[i.cat]||""}</span>
          </div>
          <div class="body">
            <span class="ref">Ref. ${i.id}</span>
            <h3>${i.title}</h3>
            <p>${i.desc}</p>
            <div class="row">
              <div class="price">${i.price==null?'<small>Starting price</small>On request':'<small>Starting from</small>'+fmt(i.price)}</div>
              <button class="btn small" data-add="${i.id}">Add to booking</button>
            </div>
          </div>
        </article>`).join("");
    }
    if(filt){
      const cats=window.DREAMORA_CATEGORIES||{all:"All"};
      filt.innerHTML=Object.entries(cats).map(([k,v])=>`<button data-f="${k}" class="${k==="all"?"on":""}">${v}</button>`).join("");
      filt.addEventListener("click",e=>{ const b=e.target.closest("[data-f]"); if(!b) return;
        current=b.dataset.f; $$("button",filt).forEach(x=>x.classList.toggle("on",x===b)); render(); });
      const h=location.hash.replace("#",""); if(cats[h]){ current=h; $$("button",filt).forEach(x=>x.classList.toggle("on",x.dataset.f===h)); }
    }
    render();
  }
  document.addEventListener("click",e=>{
    const a=e.target.closest("[data-add]"); if(a){ addItem(a.dataset.add); return; }
    const z=e.target.closest("[data-zoom]"); if(z){ openLb(z.dataset.zoom); }
  });

  // lightbox
  function openLb(src){
    let lb=$(".lb"); if(!lb){ lb=document.createElement("div"); lb.className="lb"; lb.innerHTML='<button aria-label="Close">×</button><img alt="">'; document.body.appendChild(lb);
      lb.addEventListener("click",ev=>{ if(ev.target.tagName!=="IMG") lb.classList.remove("open") }); }
    $("img",lb).src=src; lb.classList.add("open");
  }

  // booking page
  const cartBox=$("[data-cart]");
  if(cartBox){
    function drawCart(){
      const ids=load(); const items=ids.map(id=>cat.find(c=>c.id===id)).filter(Boolean);
      if(!items.length){ cartBox.innerHTML='<p class="muted">Your booking list is empty. <a href="services.html">Browse our décor catalogue</a> and add the setups you love.</p>'; $("[data-total]").textContent="—"; return; }
      cartBox.innerHTML=items.map(i=>`<div class="cart-item"><img src="assets/img/gallery/${i.img}" alt="${i.title}">
        <div class="grow"><strong>${i.title}</strong><br><span class="muted" style="font-size:.85rem">Ref. ${i.id} · ${fmt(i.price)}</span></div>
        <button data-rm="${i.id}">Remove</button></div>`).join("");
      const priced=items.filter(i=>i.price!=null); const sum=priced.reduce((a,b)=>a+b.price,0);
      $("[data-total]").textContent = priced.length===items.length ? fmt(sum) : (priced.length? fmt(sum)+" + items on request":"Quotation to follow");
    }
    cartBox.addEventListener("click",e=>{ const r=e.target.closest("[data-rm]"); if(!r) return; save(load().filter(x=>x!==r.dataset.rm)); count(); drawCart(); });
    drawCart();

    const form=$("#bookingForm");
    form.addEventListener("submit",e=>{
      e.preventDefault();
      const d=Object.fromEntries(new FormData(form).entries());
      const items=load().map(id=>cat.find(c=>c.id===id)).filter(Boolean);
      const lines=[
        "*New Booking Request – Dreamora Decor*","",
        "Name: "+d.name,"Phone: "+d.phone,"Email: "+d.email,
        "Event: "+d.event,"Date: "+d.date,"Location: "+d.location,"Guests: "+(d.guests||"-"),"",
        "Selected setups:", ...(items.length?items.map(i=>"• "+i.id+" – "+i.title):["• Custom design (no catalogue item selected)"]),"",
        "Notes: "+(d.notes||"-"),"",
        "I have read and agree to the Terms & Conditions and Refund & Cancellation Policy."
      ];
      const msg=encodeURIComponent(lines.join("\n"));
      const wa=(CFG.whatsapp||"").replace(/\D/g,"");
      if(d.channel==="email"||!wa){
        location.href="mailto:"+(CFG.email||"")+"?subject="+encodeURIComponent("Booking Request – "+d.event+" – "+d.date)+"&body="+msg;
      }else{
        window.open("https://wa.me/"+wa+"?text="+msg,"_blank");
      }
      toast("Thank you! Your request is ready to send.");
    });
  }

  // contact form
  const cf=$("#contactForm");
  if(cf) cf.addEventListener("submit",e=>{
    e.preventDefault(); const d=Object.fromEntries(new FormData(cf).entries());
    location.href="mailto:"+(CFG.email||"")+"?subject="+encodeURIComponent("Website enquiry – "+d.subject)+"&body="+encodeURIComponent("Name: "+d.name+"\nPhone: "+d.phone+"\nEmail: "+d.email+"\n\n"+d.message);
  });

  // min date = today + 3 days (advance booking)
  $$('input[type="date"]').forEach(i=>{ const t=new Date(Date.now()+3*864e5); i.min=t.toISOString().slice(0,10); });
})();
