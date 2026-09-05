'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const inquest = 'https://www.eleceng.adelaide.edu.au/personal/dabbott/wiki/index.php/The_Taman_Shud_Case_Coronial_Inquest';
  const places = [
    {id:'adelaide',name:'Adelaide railway station',lat:-34.9212,lng:138.5964,status:'documented',type:'Ticket and luggage evidence',short:'Ticket sales and the cloakroom place central Adelaide in the case.',detail:'The Henley Beach ticket and suitcase evidence concern this station. The suitcase stamp places deposit in an 11:00–noon interval; the depositor was not identified. The bus fare was issued somewhere in the city zone from the station to West/South Terrace.',source:inquest,sourceName:'Read the inquest transcription'},
    {id:'henley',name:'Henley Beach',lat:-34.9215,lng:138.4935,status:'documented',type:'Unused ticket destination',short:'A ticket destination; a completed journey is not established.',detail:'An unused Henley Beach railway ticket was found among the belongings. Its purchase cannot be tied to an exact time or intended train. This marker locates the district approximately; it does not mark a verified 1948 station platform.',source:inquest,sourceName:'Read the transport testimony'},
    {id:'leonards',name:'St Leonard’s',lat:-34.967,lng:138.514,status:'documented',type:'Ticketed service direction',short:'The 11:15 service is documented; the alighting stop is unknown.',detail:'Ticket CB88708 was a 7d fare associated with the 11:15 St Leonard’s run. It was issued in the city zone. The conductor did not identify the deceased, and the ticket does not establish where its holder got off. This district marker is not a stop reconstruction.',source:inquest,sourceName:'Read the bus-ticket evidence'},
    {id:'somerton',name:'Somerton Beach',lat:-34.993,lng:138.5124,status:'documented',type:'Body-discovery district',short:'The final approach to the beach remains unknown.',detail:'The body was found on Somerton Beach on 1 December 1948. The marker shows the vicinity only. The evidence does not establish a continuous route from the ticketed bus service to the body-discovery point.',source:inquest,sourceName:'Read the inquest transcription'},
    {id:'queenstown',name:'Queenstown',lat:-34.865,lng:138.51,status:'candidate',type:'Proposed Q locality',short:'Named on the environs map; a 1948 connection still needs a source.',detail:'Queenstown is printed on the undated Adelaide Environs raster. It is not a stopping-place label on the inspected 1938 SAR metropolitan inset. The old Albert Park tram corridor closed in 1934; a 1948 bus or other connection must be established separately.',source:'https://www.trammuseumadelaide.com/port-adelaide',sourceName:'Read the tramway history'},
    {id:'quarantine',name:'Torrens Island quarantine station',lat:-34.805,lng:138.52,status:'candidate',type:'Proposed AQS expansion',short:'A historical name lead, with a necessary water crossing.',detail:'The phrase Adelaide Quarantine Station appears in an 1887 newspaper, but the acronym AQS and its use in 1948 are not established. Torrens Island was reached by launch or barge before the 1962 bridge. This is a broad location marker, not a verified landing point or evidence of a visit.',source:'https://www.naa.gov.au/help-your-research/fact-sheets/torrens-island-quarantine-station-south-australia',sourceName:'Explore the National Archives leads'},
    {id:'glenelg',name:'Glenelg',lat:-34.98,lng:138.512,status:'candidate',type:'Proposed G expansion',short:'A plausible place initial; the code does not confirm it.',detail:'Glenelg is one possible expansion of G. Reading GAB as Glenelg–Adelaide–Brighton is an interpretation among alternatives. The location of a known case clue cannot independently confirm a decoding constructed around that clue.',source:'https://github.com/idorunning/Somerton-man/blob/review/itinerary-audit-2026-09-05/HYPOTHESIS.md',sourceName:'Read the revised hypothesis'},
    {id:'brighton',name:'Brighton',lat:-35.019,lng:138.516,status:'candidate',type:'Proposed B expansion',short:'One of several B candidates; no visit is established.',detail:'Brighton is a possible B destination, but other B places have also been used in the project. A test must state whether repeated letters always identify the same place. No route distance or journey time is calculated from this marker.',source:'https://github.com/idorunning/Somerton-man/blob/review/itinerary-audit-2026-09-05/HYPOTHESIS.md',sourceName:'Read the revised hypothesis'}
  ];
  let currentFilter='all', selected='adelaide', map=null, layer=null;
  const visiblePlaces=()=>places.filter(p=>currentFilter==='all'||p.status===currentFilter);
  function selectPlace(id,pan=true){
    const p=places.find(x=>x.id===id);if(!p)return;selected=id;
    $('place-select').value=id;$('detail-name').textContent=p.name;
    $('detail-type').textContent=p.type;$('detail-type').className='tag '+(p.status==='candidate'?'candidate':'');
    $('detail-text').textContent=p.detail;$('detail-source').href=p.source;$('detail-source').textContent=p.sourceName+' ↗';
    $('detail-coords').textContent=`Approximate: ${Math.abs(p.lat).toFixed(3)}° S, ${p.lng.toFixed(3)}° E`;
    document.querySelectorAll('.evidence-item').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.place===id)));
    if(map&&pan)map.setView([p.lat,p.lng],Math.max(map.getZoom(),12),{animate:false});
  }
  function refreshPlaces(){
    const shown=visiblePlaces();const list=$('evidence-list');const select=$('place-select');list.replaceChildren();select.replaceChildren();
    shown.forEach(p=>{
      const option=document.createElement('option');option.value=p.id;option.textContent=p.name;select.append(option);
      const button=document.createElement('button');button.className='evidence-item';button.dataset.place=p.id;button.type='button';
      const tag=document.createElement('span');tag.className='tag '+(p.status==='candidate'?'candidate':'');tag.textContent=p.status==='candidate'?'Candidate interpretation':'Documented context';
      const title=document.createElement('strong');title.textContent=p.name;const text=document.createElement('small');text.textContent=p.short;
      button.append(tag,title,text);button.addEventListener('click',()=>selectPlace(p.id));list.append(button);
    });
    if(!shown.some(p=>p.id===selected))selected=shown[0].id;
    selectPlace(selected,false);
    if(map){
      layer.clearLayers();shown.forEach(p=>{
        const marker=L.marker([p.lat,p.lng],{icon:L.divIcon({className:'place-marker '+(p.status==='candidate'?'candidate':''),iconSize:[15,15],iconAnchor:[7,7]}),title:p.name,alt:p.name+' — '+p.status,keyboard:true});
        marker.bindTooltip(p.name,{direction:'top',offset:[0,-9]});marker.on('click',()=>selectPlace(p.id,false));marker.addTo(layer);
      });
      map.fitBounds(shown.map(p=>[p.lat,p.lng]),{padding:[35,35],maxZoom:12,animate:false});
    }
    $('place-count').textContent=shown.length+' locations shown';
  }
  document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{
    currentFilter=b.dataset.filter;document.querySelectorAll('[data-filter]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));refreshPlaces();
  }));
  $('place-select').addEventListener('change',e=>selectPlace(e.target.value));
  refreshPlaces();

  // Modern coordinates are a locator only. No historical route polyline is inferred.
  function initialiseMap(){
    if(!window.L||map)return;
    map=L.map('map',{scrollWheelZoom:false,preferCanvas:true}).setView([-34.923,138.548],11);
    const tiles=L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:18,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);
    let tileSeen=false;
    tiles.on('tileload',()=>{tileSeen=true;$('basemap-status').textContent='Modern basemap · approximate locations';});
    tiles.on('tileerror',()=>{if(!tileSeen)$('basemap-status').textContent='Basemap unavailable · approximate markers and evidence remain accessible';});
    layer=L.layerGroup().addTo(map);document.querySelector('.map-canvas').classList.add('map-ready');refreshPlaces();
  }
  const mapCss=document.createElement('link');mapCss.rel='stylesheet';mapCss.href='https://unpkg.com/leaflet@1.9.4/dist/leaflet.css';mapCss.integrity='sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=';mapCss.crossOrigin='anonymous';document.head.append(mapCss);
  const mapScript=document.createElement('script');mapScript.src='https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';mapScript.integrity='sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=';mapScript.crossOrigin='anonymous';mapScript.onload=initialiseMap;
  mapScript.onerror=()=>{$('map-fallback-text').textContent='The online basemap could not load. Select any location below to read its evidence and approximate coordinates.';$('basemap-status').textContent='Offline evidence view';};document.head.append(mapScript);

  function updateCode(){
    const lines=[$('glyph-one').value+'RGOABABD',$('glyph-three').value+'TBIMPANETP','MLIABOAIAQ'+$('glyph-four').value,'ITTMTSAMSTGAB'];
    [1,3,4,5].forEach((n,i)=>$('code-line-'+n).textContent=lines[i]);
    $('unique-count').textContent=new Set(lines.join('')).size;
    $('variant-label').textContent=$('glyph-one').value+'/'+$('glyph-three').value+'/'+$('glyph-four').value;
    $('code-feedback').textContent='Current reading '+$('variant-label').textContent+': 44 retained characters, '+new Set(lines.join('')).size+' distinct letters. No complete line matches the four tested corridor strings.';
  }
  ['glyph-one','glyph-three','glyph-four'].forEach(id=>$(id).addEventListener('change',updateCode));updateCode();

  const scans=JSON.parse($('scan-data').textContent);let scanKey='environs',zoom=1,rotation=0;
  const img=$('scan-image');
  function layoutScan(){
    if(!img.naturalWidth)return;
    const quarter=((rotation%180)+180)%180===90;
    const naturalW=quarter?img.naturalHeight:img.naturalWidth;
    const naturalH=quarter?img.naturalWidth:img.naturalHeight;
    const fit=Math.min(1,Math.max(240,$('scan-scroll').clientWidth-24)/naturalW);
    const factor=fit*zoom;const width=naturalW*factor,height=naturalH*factor;
    $('scan-stage').style.width=width+'px';$('scan-stage').style.height=height+'px';
    img.style.width=img.naturalWidth*factor+'px';img.style.height=img.naturalHeight*factor+'px';img.style.left=(width-img.naturalWidth*factor)/2+'px';img.style.top=(height-img.naturalHeight*factor)/2+'px';img.style.transform=`rotate(${rotation}deg)`;
    $('scan-zoom').textContent=Math.round(zoom*100)+'%';$('zoom-out').disabled=zoom<=1;$('zoom-in').disabled=zoom>=4;
  }
  function chooseScan(){
    scanKey=$('scan-select').value;const s=scans[scanKey];zoom=1;rotation=s.rotation||0;
    img.src=s.src;img.alt=s.alt;$('scan-caption').textContent=s.caption;$('scan-original').href=s.src;
    $('scan-scroll').scrollTop=0;$('scan-scroll').scrollLeft=0;
  }
  img.addEventListener('load',layoutScan);$('scan-select').addEventListener('change',chooseScan);
  $('zoom-in').addEventListener('click',()=>{zoom=Math.min(4,zoom+.5);layoutScan();});$('zoom-out').addEventListener('click',()=>{zoom=Math.max(1,zoom-.5);layoutScan();});
  $('rotate-scan').addEventListener('click',()=>{rotation=(rotation+90)%360;layoutScan();});
  $('reset-scan').addEventListener('click',()=>{zoom=1;rotation=scans[scanKey].rotation||0;layoutScan();$('scan-scroll').scrollTo(0,0);});
  window.addEventListener('resize',layoutScan);chooseScan();
  $('view-code-scan').addEventListener('click',()=>{$('scan-select').value='code';chooseScan();});
  let reportWasOpen=false;window.addEventListener('beforeprint',()=>{reportWasOpen=$('full-report').open;$('full-report').open=true;});window.addEventListener('afterprint',()=>{$('full-report').open=reportWasOpen;});
})();
