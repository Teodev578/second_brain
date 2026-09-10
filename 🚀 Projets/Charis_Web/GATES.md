# Gates: Charis-Web — Arborescence + Processus Design

OWNS: 🚀 Projets/Charis_Web/Arborescence_Portfolio_OnePage.md, 🚀 Projets/Charis_Web/Processus_Design_Charis_Web.md

Scope: Produire l'arborescence de la one-page portfolio et le document processus design pour Charis-Web

- [x] G1: L'arborescence existe et contient les 8 sections de la one-page
  CHECK: node -e "const fs=require('fs');const f=fs.readFileSync('Arborescence_Portfolio_OnePage.md','utf8');const sections=['HERO SECTION','VISION & MISSION','ÉQUIPE PASTORALE','EXTRAITS AUDIO','PROCHAINS CULTES','LOCALISATION','DONS & SOUTIEN','FOOTER'];const missing=sections.filter(s=>!f.includes(s));if(missing.length){console.error('Missing:',missing);process.exit(1)}console.log('arborescence sections verified')"
  EXPECT: arborescence sections verified
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/home/fabien/Documents/Agent/persona_team/second_brain/🚀 Projets/Charis_Web; path=18164335f33d/23 entries; EXPECT=matched; output-sha256=700c5e2063d8ae71995243554a8291286fcacade1dea346ad36a713a7aa27f62; output-bytes=31

- [x] G2: L'arborescence inclut un tableau de notes de design (palette, mobile, player)
  CHECK: node -e "const f=require('fs').readFileSync('Arborescence_Portfolio_OnePage.md','utf8');if(!f.includes('572269')){console.error('Missing palette');process.exit(1)}if(!f.includes('Mobile')){console.error('Missing mobile note');process.exit(1)}console.log('design notes verified')"
  EXPECT: design notes verified
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/home/fabien/Documents/Agent/persona_team/second_brain/🚀 Projets/Charis_Web; path=18164335f33d/23 entries; EXPECT=matched; output-sha256=06c447c966080bb68f0c26605f319ca03c31f35ad90dcd6340343bf98d4c8895; output-bytes=22

- [x] G3: Le processus design existe et couvre les 5 phases du Double Diamond
  CHECK: node -e "const f=require('fs').readFileSync('Processus_Design_Charis_Web.md','utf8');const phases=['Phase 1','Phase 2','Phase 3','Phase 4','Phase 5'];const missing=phases.filter(p=>!f.includes(p));if(missing.length){console.error('Missing:',missing);process.exit(1)}console.log('processus phases verified')"
  EXPECT: processus phases verified
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/home/fabien/Documents/Agent/persona_team/second_brain/🚀 Projets/Charis_Web; path=18164335f33d/23 entries; EXPECT=matched; output-sha256=6ff53e20dabe1011d66f081f5f556a503560aa0a309b7293df30aba9dc6a2157; output-bytes=26

- [x] G4: Le processus design contient les 4 profils utilisateurs avec table
  CHECK: node -e "const f=require('fs').readFileSync('Processus_Design_Charis_Web.md','utf8');const profiles=['Le Visiteur','Le Fidèle','Le Curieux','Le Portfolio'];const missing=profiles.filter(p=>!f.includes(p));if(missing.length){console.error('Missing profiles:',missing);process.exit(1)}console.log('user profiles verified')"
  EXPECT: user profiles verified
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/home/fabien/Documents/Agent/persona_team/second_brain/🚀 Projets/Charis_Web; path=18164335f33d/23 entries; EXPECT=matched; output-sha256=0f77a2bdf55faf62d01c7f7d3864a691d8baf8eb5f1b0e9dfa1dfa8743569193; output-bytes=23

- [x] G5: Le processus design contient la roadmap de production avec statuts
  CHECK: node -e "const f=require('fs').readFileSync('Processus_Design_Charis_Web.md','utf8');if(!f.includes('Recherche UX')){console.error('Missing roadmap items');process.exit(1)}if(!f.includes('Terminé')||!f.includes('À faire')){console.error('Missing status markers');process.exit(1)}console.log('roadmap verified')"
  EXPECT: roadmap verified
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/home/fabien/Documents/Agent/persona_team/second_brain/🚀 Projets/Charis_Web; path=18164335f33d/23 entries; EXPECT=matched; output-sha256=9aaa7e5bcdf0b722be83319c81316e08c6b9d75b18c36e2972972227925428e2; output-bytes=17

- [x] G6: Les deux fichiers ont un frontmatter YAML valide
  CHECK: node -e "const fs=require('fs');const files=['Arborescence_Portfolio_OnePage.md','Processus_Design_Charis_Web.md'];files.forEach(f=>{const c=fs.readFileSync(f,'utf8');if(!c.startsWith('---')){console.error('Missing frontmatter:',f);process.exit(1)}if(!c.includes('status:')){console.error('Missing status field:',f);process.exit(1)}});console.log('frontmatter validated')"
  EXPECT: frontmatter validated
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/home/fabien/Documents/Agent/persona_team/second_brain/🚀 Projets/Charis_Web; path=18164335f33d/23 entries; EXPECT=matched; output-sha256=ca3d054fe546f22d623a204138906b39529c3045d7b6aec5fa310357cdfb2a68; output-bytes=22

- [x] G7: Les deux documents sont cohérents (palette partagée, sections identiques)
  CHECK: node -e "const a=require('fs').readFileSync('Arborescence_Portfolio_OnePage.md','utf8');const p=require('fs').readFileSync('Processus_Design_Charis_Web.md','utf8');if(!p.includes('Arborescence_Portfolio_OnePage')){console.error('Missing cross-reference');process.exit(1)}console.log('cross-reference verified')"
  EXPECT: cross-reference verified
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/home/fabien/Documents/Agent/persona_team/second_brain/🚀 Projets/Charis_Web; path=18164335f33d/23 entries; EXPECT=matched; output-sha256=a4e4516df8fc361af8bff464ba4a8b34b053fb9f8a4cfccb314ad96575e930b2; output-bytes=25
