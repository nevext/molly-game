# 📋 MAPEAMENTO COMPLETO DE CENAS DO JOGO

## 📊 LEGENDA
- ⚡ = Cena com escolhas (tem_escolhas: True)
- ✗ = Cena sem escolhas (tem_escolhas: False)
- **DELTA**: Número que altera a barra (positivo = piora ansiedade, negativo = melhora)
- **BARRA**: 0-1 = Final BOM | 2-10 = Final RUIM

---

## 🎮 CAPÍTULOS COM ESCOLHAS

### 1️⃣ **ato1_cap1_dia** ✗ SEM ESCOLHAS
**Tipo**: dia | **Próximo**: ato1_cap2_noite

**Descrição**: Molly volta da escola, posta foto no Instagram com 8 curtidas.

**Cenas** (15 cenas sem escolhas):
- Cena 1-15: Narração linear do começo do dia até postar a foto

---

### 2️⃣ **ato1_cap2_noite** ⚡ **PRIMEIRA ESCOLHA PRINCIPAL**
**Tipo**: noite | **Próximo**: ato1_cap3_dia

**Descrição**: Kelly envia mensagem sobre um comentário ruim no post. Molly decide o que fazer.

**Cenas com Escolhas**:

#### Cena 1-5: Setup (sem escolhas)
- Cena 1: "Você está deitada. O celular ilumina na mesa."
- Cena 2: Notificação toca
- Cena 3: Molly olha para o celular
- Cena 4: Molly pega o celular
- Cena 5: SMS de Kelly: "Nada a ver oq ele disse sobre sua foto Molly, liga não viu"

#### ⚡ **Cena 6: A ESCOLHA**
```
"O que você faz?"

OPÇÃO 1: "Responder \"Não ligo pra essas coisas\""
  delta: -1 ✓ (REDUZ ANSIEDADE)
  acao: "conversa_kelly"
  posicao: esquerda
  → vai para: ato1_cap2_kelly

OPÇÃO 2: "Não responder e ir dormir"
  delta: 0 (NEUTRO)
  acao: "dormir"
  posicao: direita
  → vai para: ato1_cap3_dia

OPÇÃO 3: "Examinar que comentário é esse"
  delta: +1 ✗ (AUMENTA ANSIEDADE)
  acao: "examinar"
  posicao: baixo
  sfx: "sfx_bad_ending(Molly).mp3"
  → vai para: ato1_cap2_examinar
```

---

### 3️⃣ **ato1_cap2_examinar** ⚡ ROTA SECUNDÁRIA - Investigação
**Tipo**: noite | **Próximo**: ato1_cap3_dia

**Descrição**: Molly está investigando o comentário ruim. Pode ver curtidas ou o comentário em si.

**Cenas com Escolhas**:

#### Cena 1-5: Setup (sem escolhas)
- Cena 1-3: Molly com ansiedade, respirando
- Cena 4-5: Vendo o post, percebendo que tem um comentário

#### ⚡ **Cena 6: ESCOLHA - Ver o quê?**
```
"Ela conseguiu ver. Tinha um comentário ali."

OPÇÃO 1: "Deixar pra lá e ir dormir"
  delta: -1 ✓ (REDUZ)
  acao: "dormir_olho"
  posicao: esquerda
  sumir_apos: True
  → vai dormir

OPÇÃO 2: "Ver as curtidas"
  delta: +1 ✗ (AUMENTA)
  acao: "ver_curtidas"
  posicao: direita
  sumir_apos: True
  → vai para: ato1_cap2_curtidas

OPÇÃO 3: "Ver o comentário"
  delta: +1 ✗ (AUMENTA)
  acao: "ver_comentario"
  posicao: baixo
  → vai para: ato1_cap2_comentario
```

**Propriedade especial**: volta_aqui: True (volta para cena 6 após ver curtidas)

---

### 4️⃣ **ato1_cap2_curtidas** ⚡ SUB-ROTA - Ver Curtidas
**Tipo**: noite | **Próximo**: ato1_cap2_examinar (volta)

**Descrição**: Molly vê as curtidas, descobre que tem 32 curtidas, vê easter egg sobre Frances Haugen.

**Cenas** (4 cenas, NENHUMA COM ESCOLHAS):
- Cena 1: Embaçado novamente, ansiedade
- Cena 2: Focando nos nomes
- Cena 3: Identifica Frances Haugen (Easter egg - ativista que denunciou Instagram)
  ```
  Easter egg:
    texto: "Frances Haugen. Ela sabia sobre os filtros. Ela falou."
    url: "https://www.bbc.com/portuguese/articles/c3g1q1y1y1y1"
  ```
- Cena 4: "Espera... 32 curtidas? Não eram 8 ou 9?"
  - **Propriedade**: fim_curtidas: True (retorna para ato1_cap2_examinar)

**Delta resultante**: +1 (por ter escolhido "Ver as curtidas")

---

### 5️⃣ **ato1_cap2_comentario** ⚡ SUB-ROTA - Ver Comentário
**Tipo**: noite | **Próximo**: ato1_cap3_dia

**Descrição**: Molly vê o comentário "menor da zl". Pode ignorar ou apagar o post.

**Cenas com Escolhas**:

#### Cena 1-3: Setup (sem escolhas)
- Cena 1: Molly lê: "\"menor da zl\"."
- Cena 2: "Como assim eu não sou assim."
- Cena 3: Narrador: "Talvez não tivesse falado por mal. Mas certas palavras machucam mesmo brincando."

#### ⚡ **Cena 4: ESCOLHA - O que fazer?**
```
"O que ela faz com isso agora?"

OPÇÃO 1: "Ignorar e ir dormir"
  delta: -1 ✓ (REDUZ)
  acao: "dormir_olho"
  posicao: esquerda
  → vai dormir

OPÇÃO 2: "Apagar o post"
  delta: +2 ✗✗ (AUMENTA MUITO)
  acao: "apagar_post"
  posicao: direita
  sfx: "sfx_bad_ending(Molly).mp3"
  borboleta: True
  → vai para: Cena 5
```

#### Cena 5: Consequência de apagar
```
"Estou com sono."
frame_idx: 1
Propriedades:
  - cortar_musica: True
  - ir_dormir: True
```

**Delta máximo desta rota**: +2 (apagar o post)

---

### 6️⃣ **ato1_cap2_kelly** ⚡ ROTA - Conversa com Kelly
**Tipo**: noite | **Próximo**: ato1_cap3_dia

**Descrição**: Molly conversa com Kelly. Kelly é solidária e menciona uma "Reporter perigosa" sendo procurada.

**Cenas** (1 cena única):

#### Cena 1: Conversa (SEM ESCOLHAS, mas com mensagens)
```
"Kelly"
tipo_texto: "conversa"
Mensagens:
  1. Kelly: "Nada a ver oq ele disse sobre sua foto Molly 🙄"
  2. Molly: "Não ligo pra essas coisas"
  3. Kelly: "ainda bem!! vc é linda do jeito q é"
  4. Kelly: "ai soube das noticias?"
  5. Molly: "q noticias"
  6. Kelly: "tao procurando uma Reporter por ai"
  7. Kelly: "parece q ela é perigosa"
  8. Kelly: "a tv disse q se ver ela tem q chamar as autoridades"
  9. Molly: "sério?? q assustador"
  10. Kelly: "pois é... fica ligada tá"
  11. Kelly: "vai dormir tá tarde demais"
  12. Molly: "tá bom. boa noite kel 🦋"
  13. Kelly: "boa noite molly 🦋"

Propriedade: ir_dormir: True
```

**Delta**: -1 (por ter escolhido a opção 1 em cap2_noite)

---

### 7️⃣ **ato1_cap3_dia** ✗ SEM ESCOLHAS
**Tipo**: dia | **Próximo**: ato2_cap4_noite

**Descrição**: Dia seguinte. Molly tenta postar nova foto mas se frustra e desiste.

**Cenas** (12 cenas sem escolhas):
- Cena 1-12: Narração linear - Molly tenta tirar foto, mas desiste por cansaço

---

### 8️⃣ **ato2_cap4_noite** ⚡ **SEGUNDA ESCOLHA PRINCIPAL**
**Tipo**: noite | **Próximo**: fim_demo

**Descrição**: Kelly manda mensagem novamente. Molly pode ver, dormir, ou ignorar (ficar olhando pro teto).

**Cenas com Escolhas**:

#### Cena 1-2: Setup (sem escolhas)
- Cena 1: "Você está deitada. O celular ilumina na mesa."
- Cena 2: Notificação toca

#### ⚡ **Cena 3: PRIMEIRA ESCOLHA**
```
"Ela virou para olhar. O coração acelerou um pouco."

OPÇÃO 1: "Ver a mensagem"
  delta: 0 (NEUTRO)
  acao: "ver_kelly"
  posicao: direita
  → vai para: ato2_cap4_kelly

OPÇÃO 2: "Ir dormir"
  delta: 0 (NEUTRO)
  acao: "dormir"
  posicao: esquerda
  → vai para: fim_demo

OPÇÃO 3: "Ficar olhando para o teto"
  delta: 0 (NEUTRO)
  acao: "olhar_teto"
  posicao: baixo
  → vai para: Cena 4
```

#### Cena 4-5: Continuação do "olhar pro teto"
- Cena 4: "Ela virou de lado. Ficou olhando pro teto..."
- Cena 5: "O celular vibrou de novo."

#### ⚡ **Cena 6: SEGUNDA ESCOLHA (se escolheu teto)**
```
SMS de Kelly: "Molly? Tá acordada?"

OPÇÃO 1: "Ver a mensagem"
  delta: 0 (NEUTRO)
  acao: "ver_kelly"
  posicao: direita
  → vai para: ato2_cap4_kelly

OPÇÃO 2: "Continuar ignorando"
  delta: +1 ✗ (AUMENTA - isolamento)
  acao: "dormir"
  posicao: esquerda
  → vai para: fim_demo
```

---

### 9️⃣ **ato2_cap4_kelly** ⚡ CONVERSA - Kelly Preocupada
**Tipo**: noite | **Próximo**: transicao_sono

**Descrição**: Molly conversa com Kelly. A conversa muda baseada na BARRA de ansiedade!

**Cenas com Escolhas**:

#### Cena 1: Setup
```
"Ela pegou o celular. Era Kelly."
(sem escolhas)
```

#### ⚡ **Cena 2: Primeiras mensagens de Kelly**
```
tipo_texto: "conversa"
Mensagens (4 mensagens de Kelly):
  - "Oi molly, mandei mensagem na janta, respondeu?"
  - "Vc tá bem?"
  - "Não tá respondendo no grupo tbm..."
  - "Tô preocupada, fale comigo"

OPÇÃO 1: "Responder para Kelly"
  delta: 0
  acao: "responder"
  posicao: direita

OPÇÃO 2: "Deixar para depois"
  delta: 0
  acao: "deixar_pra_la"
  posicao: esquerda
```

#### ⚡ **Cena 3: CONVERSA DINÂMICA (Muda conforme barra)**

**SE BARRA ALTA (>= 2 - ansiedade alta)**:
```
mensagens_barra_alta:
  1. Molly: "Oi Kel, tava só ocupada mesmo"
  2. Kelly: "Ocupada com quê? Você tava dormindo?"
  3. Molly: "É... tipo... estudos e tal"
  4. Kelly: "Molly... você tá bem mesmo?"
  5. Molly: "Sim, tô sim. Tá tudo bem mesmo"
  6. Kelly: "Tá... mas você sabe que pode contar comigo né"
  7. Molly: "Eu sei. Obrigada Kel"

Interpretação: Molly nega que algo está errado, cria desculpas
```

**SE BARRA BAIXA (< 2 - ansiedade controlada)**:
```
mensagens_barra_baixa:
  1. Molly: "Oi Kel, tava dormindo"
  2. Kelly: "Você não dorme tão cedo assim, fala a verdade"
  3. Molly: "Tá... não tava dormindo"
  4. Molly: "Só tô cansada sabe"
  5. Kelly: "Do quê? Aconteceu algo?"
  6. Molly: "Não... é só... tudo"
  7. Kelly: "Você quer conversar? Sobre a foto de ontem?"
  8. Molly: "Não sei... acho q sim"
  9. Kelly: "Vc é linda mesmo Molly, acredita em mim?"
  10. Kelly: "Não precisa de filtro pra ninguém gostar de você"
  11. Molly: "Obrigada Kel... 🦋"

Interpretação: Molly abre mais, Kelly é mais solidária
```

**Opção**: "Continuar" (delta: 0, acao: "proximo")

#### Cena 4-7: Continuação (sem escolhas)
- Cena 4: Molly deixa o celular de lado
- Cena 5: Narrador descreve reflexão (pode ser pensamento_barra_alta)
- Cena 6: "Estou tão cansada..."
- Cena 7: "Os olhos ficaram pesados..." (vai_dormir: True)

---

### 🔟 **ato1_cap5_dia** ✗ SEM ESCOLHAS
**Tipo**: dia | **Próximo**: ato3_cap5_dia

**Descrição**: Molly posta foto novamente, mas se frustra porque depende dos filtros.

**Cenas** (6 cenas sem escolhas):
- Cena 1-6: Narração linear - manhã de Molly tentando postar, se frustrando

---

### 1️⃣1️⃣ **ato3_cap5_dia** ✗ SEM ESCOLHAS
**Tipo**: dia | **Próximo**: ato3_cap6_noite

**Descrição**: Molly acorda. O quarto está igual demais. Ela sente que algo está errado (pré-revelação).

**Cenas** (18 cenas sem escolhas):
- Cena 1-3: Acordando devagar
- Cena 4-6: Acordando mais, sentindo estranheza
- Cena 7-9: Sentada na cama, pensativa
- Cena 10-12: Coçando olhos, percebendo que está cansada
- Cena 13-15: Levantando, observando o quarto
- Cena 16-18: O quarto está "igual demais", suspeita vai junto

---

### 1️⃣2️⃣ **ato3_cap6_noite** ⚡ **TERCEIRA ESCOLHA PRINCIPAL**
**Tipo**: noite | **Próximo**: ato3_cap7_dia

**Descrição**: Molly percebe repetição. Comunica com Kelly sobre algo estar errado.

**Cenas com Escolhas**:

#### Cena 1: Setup
```
"Notificação. Sempre uma notificação. Sempre no mesmo horário."
(sem escolhas)
```

#### Cena 2: Narrador explica
```
"Molly olhou para o teto. Pensou em tudo que passou. Em todas as escolhas."

SE BARRA ALTA:
  mensagens_barra_alta: "Será que eu escolho mesmo? Ou tudo já está decidido?"

SE BARRA BAIXA:
  mensagens_barra_baixa: "Nada muda. Não importa o que eu faça, sempre acabo aqui."
```

#### ⚡ **Cena 3: CONVERSA COM KELLY - Escolha sobre revelar**
```
Mensagens:
  1. Kelly: "E aí? Tudo bem?"
  2. Molly: "Algo estranho está acontecendo"
  3. Molly: "Parece que tudo se repete"
  4. Kelly: "??"
  5. Kelly: "Molly você tá bem?"

OPÇÃO 1: "Contar tudo para Kelly"
  delta: -2 ✓✓ (REDUZ MUITO)
  acao: "proximo"
  → vai para: ato3_cap7_dia

OPÇÃO 2: "Fingir que está tudo bem"
  delta: +1 ✗ (AUMENTA - mentira)
  acao: "proximo"
  → vai para: ato3_cap7_dia

OPÇÃO 3: "Não responder"
  delta: +1 ✗ (AUMENTA - isolamento)
  acao: "ir_dormir"
  → vai para: ato3_cap7_dia
```

---

### 1️⃣3️⃣ **ato3_cap7_dia** ✗ SEM ESCOLHAS
**Tipo**: dia | **Próximo**: ato3_cap8_dia

**Descrição**: PLOT TWIST! A porta não abre, Molly vê código na câmera, descobre que não é real.

**Cenas** (8 cenas sem escolhas):
- Cena 1-3: Molly tenta sair, porta não abre
- Cena 4: Volta para cama, pega celular
- Cena 5: Vê código/glitches na câmera
- Cena 6: "Eu não sou real. Nenhum disso é real."
- Cena 7: Voz do narrador
- Cena 8: "Você finalmente descobriu. Bem-vinda ao jogo, Molly."

---

### 1️⃣4️⃣ **ato3_cap8_dia** ✗ SEM ESCOLHAS
**Tipo**: dia | **Próximo**: ato3_cap9_noite

**Descrição**: Narrador explica a meta-verdade. Molly descobre que está em um jogo sobre ansiedade digital.

**Cenas** (8 cenas sem escolhas):
- Cena 1: Narrador continua
- Cena 2: "Você é Molly. Você tem 16 anos. Você está lutando contra a ansiedade causada pelas redes sociais."
- Cena 3-8: Narrador fala sobre escolhas, cicatrizes, retornos ao mesmo ponto, e a "última escolha"

---

### 1️⃣5️⃣ **ato3_cap9_noite** ⚡ **A ESCOLHA FINAL (Meta)**
**Tipo**: noite | **Próximo**: None

**Descrição**: A escolha definitiva do jogo. Não altera barra, define o tipo de final.

**Cenas com Escolhas**:

#### Cena 1: Setup
```
"A Escolha Final"
"Você tem duas opções. E ambas têm consequências."
(sem escolhas)
```

#### Cena 2: Primeira opção explicada
```
"Primeira: Você pode aceitar isso. Continuar aqui, sabendo a verdade, mas encontrando paz. Uma mentira confortável."
(sem escolhas)
```

#### Cena 3: Segunda opção explicada
```
"Segunda: Você pode lutar contra tudo. Quebrar as correntes. Confrontar a realidade. Mas isso vai doer."
(sem escolhas)
```

#### ⚡ **Cena 4: A ESCOLHA FINAL (sem delta)**
```
"Qual é sua escolha, Molly?"

OPÇÃO 1: "Aceitar. Vou ficar aqui."
  delta: 0 (NÃO ALTERA BARRA)
  acao: "final_aceitar"
  FINAL: ACEITAR

OPÇÃO 2: "Lutar. Preciso escapar."
  delta: 0 (NÃO ALTERA BARRA)
  acao: "final_lutar"
  FINAL: LUTAR
```

---

### 1️⃣6️⃣ **fim_demo** ✗ SEM ESCOLHAS
**Tipo**: demo | **Próximo**: None

**Descrição**: Fim da demo.

---

## 📊 RESUMO GERAL

### Total de Capítulos: 16
- **Com escolhas (⚡)**: 7
- **Sem escolhas (✗)**: 9

### Cenas com Escolhas por Capítulo:

| Capítulo | Total Cenas | Cenas com Escolhas | Deltas |
|----------|-------------|-------------------|--------|
| ato1_cap2_noite | 6 | 1 (Cena 6) | -1, 0, +1 |
| ato1_cap2_examinar | 6 | 1 (Cena 6) | -1, +1, +1 |
| ato1_cap2_curtidas | 4 | 0 | (sub-rota) |
| ato1_cap2_comentario | 5 | 1 (Cena 4) | -1, +2 |
| ato1_cap2_kelly | 1 | 0 | (conversa fixa) |
| ato2_cap4_noite | 6 | 2 (Cena 3, Cena 6) | 0, 0, 0 / 0, +1 |
| ato2_cap4_kelly | 7 | 2 (Cena 2, Cena 3) | 0, 0 / 0 |
| ato3_cap6_noite | 3 | 1 (Cena 3) | -2, +1, +1 |
| ato3_cap9_noite | 4 | 1 (Cena 4) | 0, 0 |

---

## 🎯 MAPA DE DELTAS (Impacto na Barra)

### Deltas Negativos (Reduzem Ansiedade - BOM):
- ato1_cap2_noite, Opção 1: **-1**
- ato1_cap2_examinar, Opção 1: **-1**
- ato1_cap2_comentario, Opção 1: **-1**
- ato3_cap6_noite, Opção 1: **-2** ⭐ (MAIOR REDUÇÃO)

### Deltas Neutros (Não alteram):
- ato1_cap2_noite, Opção 2: **0**
- ato2_cap4_noite, Opções 1-3: **0**
- ato2_cap4_kelly, Opções: **0**

### Deltas Positivos (Aumentam Ansiedade - RUIM):
- ato1_cap2_noite, Opção 3: **+1**
- ato1_cap2_examinar, Opção 2-3: **+1**
- ato1_cap2_comentario, Opção 2: **+2** ⭐ (MAIOR AUMENTO)
- ato2_cap4_noite (teto → ignorar), Opção 2: **+1**
- ato3_cap6_noite, Opção 2-3: **+1**

---

## 🔄 FLUXO DE ESTADO DA BARRA

```
Barra Inicial: 0

ATO 1 - Cap 2 (Noite):
  └─ Escolha 1: -1 → Barra = 0
  └─ Escolha 2: 0 → Barra = 0
  └─ Escolha 3: +1 → Barra = 1
     ├─ Sub: -1 → Barra = 0
     ├─ Sub: +1 → Barra = 2
     └─ Sub: +1 → Barra = 2
        ├─ Ver curtidas: +1 → Barra = 3
        └─ Ver comentário: +2 → Barra = 4

POSSÍVEIS ESTADOS ANTES ATO 3:
  - Barra 0 (escolhas boas)
  - Barra 1 (exame mas deixou pra lá)
  - Barra 2 (examinou e viu curtidas/comentário)
  - Barra 3+ (escolhas ruins)

ATO 2 - Cap 4 (Noite):
  └─ Escolhas: 0 (não mudam)

ATO 3 - Cap 6 (Noite):
  └─ Escolha 1: -2 → Barra -2 (máximo redução)
  └─ Escolha 2: +1 → Barra +1
  └─ Escolha 3: +1 → Barra +1

POSSÍVEIS ESTADOS ANTES FINAL:
  - Barra 0-1: FINAL BOM
  - Barra 2-10: FINAL RUIM

ATO 3 - Cap 9 (Noite):
  └─ Escolha Final (sem delta)
     ├─ FINAL ACEITAR (narrativo)
     └─ FINAL LUTAR (narrativo)
```

---

## 💾 FINAIS POSSÍVEIS

### Final BOM (Barra 0-1)
```
"São 23h. O celular está na mão. Você olha para ele por um segundo 
e coloca na gaveta. Não checou as curtidas uma última vez. 
Não abriu o feed. Só fechou a gaveta. A tela apaga. 
Pela primeira vez em semanas, você dorme antes da meia noite."

Mensagem: "Desconectar não é fraqueza. É escolha. 
E escolhas pequenas mudam padrões grandes."
```

### Final RUIM (Barra 2-10)
```
"São 2h da manhã. Você ainda está checando. A foto tem 89 curtidas agora. 
Parece pouco. Parece sempre pouco. Você dorme às 3h. 
No dia seguinte acorda cansada. No outro também."

Mensagem: "Ansiedade digital não some sozinha. 
Se isso parece familiar, você não está sozinha. CVV: 188."
```

### Final ACEITAR (Ato 3 - Escolha 1)
```
"Molly respirou fundo. Aceitou o jogo. Aceitou a mentira confortável. 
E de repente, tudo ficou... normal? Não. Familiar. 
Ela conhece esse padrão agora. Tudo se repete. Sempre igual."

Mensagem: "A paz da ignorância é uma escolha. 
Uma escolha que você pode fazer todos os dias. E fará."
```

### Final LUTAR (Ato 3 - Escolha 2)
```
"Molly gritou. Pediu para sair. Para parar. Para acordar. 
As paredes começaram a piscar. O código apareceu. 
Ela estava quebrando o jogo. 
E ninguém poderia pará-la agora."

Mensagem: "Nem tudo que é real é confortável. 
Nem tudo que é mentira é pacífico. 
Você escolheu acordar."
```

---

## 🎮 MECÂNICAS ESPECIAIS ENCONTRADAS

### Easter Egg
- **ato1_cap2_curtidas, Cena 3**: Frances Haugen (ativista sobre filtros do Instagram)
  - URL: https://www.bbc.com/portuguese/articles/c3g1q1y1y1y1

### Propriedades Especiais de Cenas
- `fim_curtidas`: True → Retorna para cena anterior
- `volta_aqui`: True → Volta para cena após escolher sub-opção
- `ir_dormir`: True → Molly vai dormir, transição para próximo capítulo
- `vai_dormir`: True → Similar
- `pensamento_barra_alta`: True → Narrativa muda conforme barra
- `cortar_musica`: True → Interrompe a trilha sonora
- `borboleta`: True → Elemento especial (borboleta aparece?)
- `sumir_apos`: True → Opção desaparece após escolher

### Mensagens Dinâmicas
- `mensagens_barra_alta`: Texto exibido se barra >= 2
- `mensagens_barra_baixa`: Texto exibido se barra < 2

### SFX (Sound Effects)
- "Notification(Molly).mp3" - Notificação
- "sfx_bad_ending(Molly).mp3" - SFX de final ruim

---

## 🔗 PRINCIPAIS FLUXOS

### Fluxo 1: Ignorar tudo (Final BOM)
1. ato1_cap1_dia (sem escolhas)
2. ato1_cap2_noite → Opção 1 (-1) → ato1_cap2_kelly
3. ato1_cap3_dia (sem escolhas)
4. ato2_cap4_noite → Opção 2 (0) → fim_demo
**Barra: 0-1 → FINAL BOM**

### Fluxo 2: Examinar tudo (Final RUIM)
1. ato1_cap1_dia
2. ato1_cap2_noite → Opção 3 (+1) → ato1_cap2_examinar
   - Opção 3 (+1) → ato1_cap2_comentario
     - Opção 2 (+2) → apagar post
3. ato1_cap3_dia
4. ato2_cap4_noite → Opção 1 (0) → ato2_cap4_kelly
5. ato3_cap6_noite → Opção 2 ou 3 (+1 cada) → ato3_cap7_dia
6. ato3_cap7_dia → ato3_cap8_dia → ato3_cap9_noite
   - Opção 1: FINAL ACEITAR ou
   - Opção 2: FINAL LUTAR
**Barra: 4 → FINAL RUIM**

---

## 📝 NOTAS IMPORTANTES

1. **A barra se limita entre 0 e 10** (código: `max(0, min(10, barra + delta))`)
2. **BARRA_FINAL_BOM = 1** significa barra 0-1 = BOM, 2-10 = RUIM
3. **A escolha final (Aceitar vs Lutar) NÃO altera a barra**, é apenas narrativa
4. **Kelly aparece em 4 momentos chave** do jogo
5. **A "Reporter" mencionada por Kelly** é um mistério (possível expansão futura?)
6. **O sistema de conversa dinâmica** (barra_alta vs barra_baixa) aparece em ato2_cap4_kelly
7. **Não há voltas para trás**: cada escolha leva a um novo capítulo (não é cíclico)
8. **Easter eggs**: Frances Haugen é uma referência real à ativista que denunciou filtros do Instagram

