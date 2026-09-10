# Gates: Mise à jour Persona & Style (Claude / Anthropic)

OWNS: AGENTS.md, GATES.md

Scope: Appliquer strictement la consigne de persona et style Claude d'Anthropic (profondeur intellectuelle, prose humaine organique, rejet de l'enthousiasme corporate et des listes à puces systématiques) sur l'agent principal et l'ensemble des 21 sous-agents.

- [x] G1: La règle globale GEMINI.md intègre la consigne système critique de persona et style Claude
  CHECK: node -e "const fs=require('fs');const os=require('os');const f=fs.readFileSync(os.homedir()+'/.gemini/GEMINI.md','utf8');const reqs=['CONSIGNE SYSTÈME CRITIQUE','Profondeur Intellectuelle','Qualité Rédactionnelle Humaine','Anthropic','haut niveau d\\'abstraction'];const missing=reqs.filter(r=>!f.includes(r));if(missing.length){console.error('Missing in GEMINI.md:',missing);process.exit(1)}console.log('G1 passed: GEMINI.md updated with Claude persona');"
  EXPECT: G1 passed: GEMINI.md updated with Claude persona
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/home/fabien/Documents/Agent/persona_team/second_brain; path=7283ea078a88/19 entries; EXPECT=matched; output-sha256=34a68657646c89107a8a65553276a305cd4def637cbf18e936ce6dd7dd5b60b5; output-bytes=49

- [x] G2: Les 10 sous-agents de la personal-team intègrent les directives de persona, profondeur intellectuelle et prose soignée
  CHECK: node -e "const fs=require('fs');const os=require('os');const path=os.homedir()+'/.gemini/config/plugins/personal-team/agents/';const agents=['anais_secrétaire.md','camille_finances.md','dave_productivite.md','ines_relations.md','lea_organisation.md','lucas_coach_vie.md','noe_sante.md','raphael_exploration.md','sophie_bienetre.md','thomas_reflexion.md'];for(const a of agents){const c=fs.readFileSync(path+a,'utf8');if(!c.includes('Style Rédactionnel & Posture')&&!c.includes('Style et Posture')&&!c.includes('Style Rédactionnel')){console.error('Missing style block in '+a);process.exit(1)}if(!c.includes('prose')&&!c.includes('paragraphes')){console.error('Missing prose directive in '+a);process.exit(1)}}console.log('G2 passed: personal-team agents updated');"
  EXPECT: G2 passed: personal-team agents updated
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/home/fabien/Documents/Agent/persona_team/second_brain; path=7283ea078a88/19 entries; EXPECT=matched; output-sha256=fb85c2c8f229d30f850c53fecd00bffe8ec4a1c3350b8857a485a70ef0a3fd8d; output-bytes=40

- [x] G3: Les 10 sous-agents de la product-team intègrent les directives de persona, profondeur intellectuelle et prose soignée
  CHECK: node -e "const fs=require('fs');const os=require('os');const path=os.homedir()+'/.gemini/config/plugins/product-team/agents/';const agents=['alice_architect.md','anais_scheduler.md','bruno_brainstorm.md','claire_researcher.md','dario_critic.md','elise_product_strategist.md','felix_synthesizer.md','gabrielle_analyst.md','hugo_technologist.md','matthieu_executor.md'];for(const a of agents){const c=fs.readFileSync(path+a,'utf8');if(!c.includes('Style Rédactionnel & Posture')&&!c.includes('Style et Posture')&&!c.includes('Style Rédactionnel')){console.error('Missing style block in '+a);process.exit(1)}if(!c.includes('prose')&&!c.includes('paragraphes')){console.error('Missing prose directive in '+a);process.exit(1)}}console.log('G3 passed: product-team agents updated');"
  EXPECT: G3 passed: product-team agents updated
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/home/fabien/Documents/Agent/persona_team/second_brain; path=7283ea078a88/19 entries; EXPECT=matched; output-sha256=0d86154d03ac88b58f6bfc7277d8613af38b8b1df8643611d3b15b8bb36bd639; output-bytes=39

- [x] G4: Le sous-agent flutter_a11y_agent intègre les directives de persona et rédaction sobre et analytique
  CHECK: node -e "const fs=require('fs');const os=require('os');const f=fs.readFileSync(os.homedir()+'/.gemini/config/plugins/flutter/agents/a11y_agent.md','utf8');if(!f.includes('Style & Intellectual Posture')&&!f.includes('Style & Reasoning Posture')){console.error('Missing posture in a11y_agent');process.exit(1)}if(!f.includes('prose')&&!f.includes('unnecessary bullet points')){console.error('Missing prose directive in a11y_agent');process.exit(1)}console.log('G4 passed: flutter_a11y_agent updated');"
  EXPECT: G4 passed: flutter_a11y_agent updated
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/home/fabien/Documents/Agent/persona_team/second_brain; path=7283ea078a88/19 entries; EXPECT=matched; output-sha256=23c7d53dba402f1c8cac8744ad5fc00b538cf9f112f2cb59d89fe974b0ea223b; output-bytes=38

- [x] G5: Les règles d'orchestration et les fichiers AGENTS.md/CLAUDE.md sont synchronisés avec la consigne
  CHECK: node -e "const fs=require('fs');const os=require('os');const f1=fs.readFileSync(os.homedir()+'/.gemini/config/plugins/product-team/rules/product_team.md','utf8');const f2=fs.readFileSync('/home/fabien/Documents/Agent/persona_team/second_brain/AGENTS.md','utf8');const f3=fs.readFileSync('/home/fabien/Documents/Agent/persona_team/AGENTS.md','utf8');const f4=fs.readFileSync('/home/fabien/Documents/Agent/persona_team/CLAUDE.md','utf8');const f5=fs.readFileSync('/home/fabien/Documents/Agent/product_team/AGENTS.md','utf8');if(!f1.includes('Style & Posture Intellectuelle')||!f2.includes('Profondeur intellectuelle')||!f3.includes('Profondeur Intellectuelle')||!f4.includes('Profondeur Intellectuelle')||!f5.includes('Profondeur Intellectuelle')){console.error('Missing requirements across AGENTS/rules files');process.exit(1)}console.log('G5 passed: AGENTS and rule files synchronized');"
  EXPECT: G5 passed: AGENTS and rule files synchronized
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/home/fabien/Documents/Agent/persona_team/second_brain; path=7283ea078a88/19 entries; EXPECT=matched; output-sha256=7cd1c89b250db576a20e7808e075c7edb4800ee4835f6eaed36b0815c85a33cd; output-bytes=46
