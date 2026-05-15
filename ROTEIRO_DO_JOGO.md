# 🦋 ROTEIRO DO JOGO MOLLY - FLUXO NARRATIVO

## Sistema de Barra (0-10)
- **Barra 0-1**: Final BOM ✓
- **Barra 2-10**: Final RUIM ✗
- Cada escolha altera a barra com um `delta` (positivo = pior, negativo = melhor)

---

## 📍 ATO 1 - CAPÍTULO 1 (Dia)
**ato1_cap1_dia** → *SEM ESCOLHAS*
- Molly volta da escola
- Posta foto no Instagram
- Fica ansiosinha vendo 8 curtidas
- **Próximo**: ato1_cap2_noite

---

## 🌙 ATO 1 - CAPÍTULO 2 (Noite) - **PRIMEIRA ESCOLHA**
**ato1_cap2_noite**
- Molly está deitada, recebe mensagem de Kelly sobre um comentário ruim no post

### ⚡ ESCOLHA:
1. **"Responder 'Não ligo pra essas coisas'"** `delta: -1` 
   - ✓ Reduz ansiedade
   - → vai para **ato1_cap2_kelly** (conversa com Kelly)
   - Kelly incentiva ("vc é linda do jeito que é")
   - Kelly fala sobre uma "Reporter perigosa" sendo procurada
   - Molly vai dormir + **ir_dormir: True**

2. **"Deixar pra depois e tentar dormir"** `delta: 0`
   - acao: "naoligar"
   - → vai para **ato1_cap2_naoligar** (rota curta)
   - Molly vira o celular de cabeça para baixo
   - Dorme sem responder
   - Mantém a barra

3. **"Examinar que comentário é esse"** `delta: +1` 🔴 SFX ruim
   - ✗ Aumenta ansiedade
   - → vai para **ato1_cap2_examinar** (rota de investigação)

---

## 🔍 ATO 1 - CAPÍTULO 2 (Examinar) - ROTA SECUNDÁRIA
**ato1_cap2_examinar** → *Molly está investigando o comentário*

### ⚡ ESCOLHA:
1. **"Deixar pra lá e ir dormir"** `delta: -1`
   - ✓ Reduz ansiedade
   - → vai dormir

2. **"Ver as curtidas"** `delta: +1`
   - → vai para **ato1_cap2_curtidas** (sub-rota)
   - Molly vê 32 curtidas (não 8!)
   - Easter egg: Menciona Frances Haugen (ativista que denunciou Instagram)
   - Volta para **ato1_cap2_examinar**

3. **"Ver o comentário"** `delta: +1`
   - → vai para **ato1_cap2_comentario** (sub-rota)

---

## 💬 ATO 1 - CAPÍTULO 2 (Comentário) - SUB-ROTA
**ato1_cap2_comentario** → *Molly vê o comentário: "menor da zl"*

### ⚡ ESCOLHA:
1. **"Ignorar e ir dormir"** `delta: -1`
   - ✓ Reduz ansiedade
   - → vai dormir

2. **"Apagar o post"** `delta: +2` 🔴 SFX ruim + Borboleta
   - ✗✗ MUITO NEGATIVO (maior delta)
   - Molly apaga o post
   - → vai dormir

---

## ☀️ ATO 1 - CAPÍTULO 3 (Dia)
**ato1_cap3_dia** → *SEM ESCOLHAS*
- Dia seguinte, Molly ainda insegura
- Kelly manda SMS incentivando a postar mais
- Molly tenta tirar nova foto mas se frustra
- Abandona a ideia: "Estou cansada disso"
- **Próximo**: ato2_cap4_noite

---

## 🌙 ATO 2 - CAPÍTULO 4 (Noite) - **SEGUNDA ESCOLHA**
**ato2_cap4_noite**
- Molly deitada, recebe notificação
- Kelly manda mensagem

### ⚡ ESCOLHA (primeira cena):
1. **"Ver a mensagem"** `delta: 0`
   - → vai para **ato2_cap4_kelly** (conversa)

2. **"Ir dormir"** `delta: 0`
   - → vai direto para **fim_demo**

3. **"Ficar olhando para o teto"** `delta: 0`
   - Molly ignora primeira vez
   - Kelly manda outra mensagem: "Molly? Tá acordada?"
   - **Nova escolha**:
     - **"Ver a mensagem"** → **ato2_cap4_kelly**
     - **"Continuar ignorando"** `delta: +1` → **fim_demo**

---

## 💬 ATO 2 - CAPÍTULO 4 (Kelly) - CONVERSA DECISIVA
**ato2_cap4_kelly** → *Molly conversa com Kelly*

**IMPORTANTE**: A conversa muda baseada na barra!

### SE BARRA ALTA (>=2 - ansiedade alta):
```
Molly nega estar bem
Kelly pergunta o que aconteceu
Molly responde "Não tava dormindo"
Molly diz que tá cansada
Kelly pergunta se quer conversar
Molly admite cansaço
```

### SE BARRA BAIXA (<2 - ansiedade controlada):
```
Molly diz que estava ocupada/estudando
Kelly insiste que é mentira
Molly abre sobre estar cansada
Kelly pergunta sobre a foto
Molly abre o jogo sobre sentimentos
Kelly reafirma que Molly é bonita sem filtro
```

**Depois da conversa**:
- Molly fica pensativa
- Vai dormir

**Próximo**: transicao_sono (que leva para ato3)

---

## ⚠️ ATO 3 - CAPÍTULO 5 (Dia) - A REALIDADE COMEÇA A FALHAR
**ato3_cap5_dia** → *SEM ESCOLHAS*
- Molly ACORDA em seu quarto
- Tudo parece... exatamente igual ao passado
- Ela sente que algo está errado
- O quarto está "igual demais"
- **Monólogo**: "Como se nada tivesse mudado. Como se eu tivesse voltado"
- **Próximo**: ato3_cap6_noite

---

## 🌙 ATO 3 - CAPÍTULO 6 (Noite) - **TERCEIRA ESCOLHA**
**ato3_cap6_noite** → *Molly percebe a repetição*

### ⚡ ESCOLHA:
1. **"Contar tudo para Kelly"** `delta: -2` ✓✓
   - ✓ Reduz muito a ansiedade
   - Molly abre sobre a repetição
   - Kelly fica preocupada

2. **"Fingir que está tudo bem"** `delta: +1` 🔴
   - ✗ Aumenta ansiedade
   - Molly nega que algo está errado
   - Kelly insiste
   - Molly segue fingindo

3. **"Não responder"** `delta: +1` 🔴
   - ✗ Aumenta ansiedade (isolamento)
   - Molly vai direto dormir

**Próximo**: ato3_cap7_dia

---

## ☀️ ATO 3 - CAPÍTULO 7 (Dia) - A REVELAÇÃO
**ato3_cap7_dia** → *SEM ESCOLHAS* 🎮 PLOT TWIST
- Molly tenta abrir a porta
- **A PORTA NÃO ABRE**
- Ela pega o celular e vê na câmera:
  - Linhas de código
  - Glitches piscando
  - **Realização**: "Eu não sou real. Nenhum disso é real."
- O NARRADOR fala:
  - "Você finalmente descobriu. Bem-vinda ao jogo, Molly."

**Próximo**: ato3_cap8_dia

---

## ☀️ ATO 3 - CAPÍTULO 8 (Dia) - O NARRADOR EXPLICA
**ato3_cap8_dia** → *SEM ESCOLHAS* 🎤 REVELAÇÃO TOTAL
- Narrador revela quem é Molly:
  - 16 anos
  - Lutando contra ansiedade das redes sociais
- Narrador pergunta: "Você sabia que cada escolha deixava cicatrizes?"
- Narrador revela a meta-verdade:
  - "Alguns passos pioraram. Outros ajudaram. Mas sempre volta ao mesmo ponto."
- **FINAL DO ATO 3**: "Porque você chegou ao fim. E agora... você tem uma última escolha."

**Próximo**: ato3_cap9_noite

---

## 🌙 ATO 3 - CAPÍTULO 9 (Noite) - **A ESCOLHA FINAL** 🎯
**ato3_cap9_noite** → *A VERDADEIRA ESCOLHA DO JOGO*

### ⚡ ESCOLHA FINAL (Sem delta, escolha narrativa):

1. **"Aceitar. Vou ficar aqui."**
   - `acao: "final_aceitar"`
   - 🎬 **FINAL: ACEITAR**
   ```
   Molly respirou fundo. Aceitou o jogo.
   Aceitou a mentira confortável.
   Tudo ficou... normal? Não. Familiar.
   Ela conhece esse padrão agora.
   Tudo se repete. Sempre igual.
   
   Mensagem: "A paz da ignorância é uma escolha. 
   Uma escolha que você pode fazer todos os dias. E fará."
   ```

2. **"Lutar. Preciso escapar."**
   - `acao: "final_lutar"`
   - 🎬 **FINAL: LUTAR**
   ```
   Molly gritou. Pediu para sair. Para parar.
   As paredes começaram a piscar.
   O código apareceu.
   Ela estava quebrando o jogo.
   
   Mensagem: "Nem tudo que é real é confortável.
   Nem tudo que é mentira é pacífico.
   Você escolheu acordar."
   ```

---

## 📊 FINAIS POSSÍVEIS (Baseado na barra)

### FINAL BOM ✓ (Barra 0-1)
```
São 23h. O celular está na mão.
Você olha para ele por um segundo e coloca na gaveta.
Não checou as curtidas uma última vez.
Não abriu o feed. Só fechou a gaveta.
A tela apaga.
Pela primeira vez em semanas, você dorme antes da meia noite.

MENSAGEM: "Desconectar não é fraqueza. É escolha.
E escolhas pequenas mudam padrões grandes."
```

### FINAL RUIM ✗ (Barra 2-10)
```
São 2h da manhã.
Você ainda está checando.
A foto tem 89 curtidas agora.
Parece pouco. Parece sempre pouco.
Você dorme às 3h.
No dia seguinte acorda cansada. No outro também.

MENSAGEM: "Ansiedade digital não some sozinha.
Se isso parece familiar, você não está sozinha.
CVV: 188."
```

### FINAL ACEITAR 🔄 (Ato 3 - escolha)
```
Molly respirou fundo. Aceitou o jogo.
Aceitou a mentira confortável.
E de repente, tudo ficou... normal? Não. Familiar.
Ela conhece esse padrão agora.
Tudo se repete. Sempre igual.

MENSAGEM: "A paz da ignorância é uma escolha.
Uma escolha que você pode fazer todos os dias. E fará."
```

### FINAL LUTAR ⚔️ (Ato 3 - escolha)
```
Molly gritou. Pediu para sair. Para parar. Para acordar.
As paredes começaram a piscar.
O código apareceu.
Ela estava quebrando o jogo.
E ninguém poderia pará-la agora.

MENSAGEM: "Nem tudo que é real é confortável.
Nem tudo que é mentira é pacífico.
Você escolheu acordar."
```

---

## 🗺️ MAPA DE FLUXO RESUMIDO

```
ATO 1
  └─ Cap 1 (dia) ✗ escolhas
      └─ Cap 2 (noite) ⚡ ESCOLHA 1
          ├─ Opção 1: Kelly (-1) → Cap 2 Kelly → Cap 3
          ├─ Opção 2: Não Ligar (0) → Cap 2 Não Ligar → Cap 3
          └─ Opção 3: Examinar (+1) → Cap 2 Examinar
              ├─ Sub: Deixar (-1) → dormir
              ├─ Sub: Curtidas (+1) → Ver 32 curtidas → voltar
              └─ Sub: Comentário (+1) → Ver "menor da zl"
                  ├─ Ignorar (-1) → dormir
                  └─ Apagar (+2) → dormir
      └─ Cap 3 (dia) ✗ escolhas

ATO 2
  └─ Cap 4 (noite) ⚡ ESCOLHA 2
      ├─ Opção 1: Ver (0) → Cap 4 Kelly → Fim Demo
      ├─ Opção 2: Dormir (0) → Fim Demo
      └─ Opção 3: Teto (0) → Kelly manda de novo
          ├─ Ver (0) → Cap 4 Kelly → Fim Demo
          └─ Ignorar (+1) → Fim Demo
      └─ Cap 4 Kelly (conversa adaptada pela barra)

ATO 3
  └─ Cap 5 (dia) ✗ escolhas (porta não abre)
      └─ Cap 6 (noite) ⚡ ESCOLHA 3
          ├─ Contar pra Kelly (-2) → continua
          ├─ Fingir (+1) → continua
          └─ Não responder (+1) → continua
      └─ Cap 7 (dia) ✗ escolhas (REVELAÇÃO)
      └─ Cap 8 (dia) ✗ escolhas (narrador explica)
      └─ Cap 9 (noite) ⚡ ESCOLHA FINAL (sem delta)
          ├─ Aceitar → FINAL ACEITAR
          └─ Lutar → FINAL LUTAR

FINAL BOM (barra 0-1) OU FINAL RUIM (barra 2-10)
```

---

## 📝 RESUMO DAS MUDANÇAS DE TRAJETÓRIA

| Escolha | Opção | Delta | Efeito | Próxima Cena |
|---------|-------|-------|--------|-------------|
| 1️⃣ Cap 2 | Responder Kelly | -1 | ✓ Reduz ansiedade | Cap 2 Kelly |
| 1️⃣ Cap 2 | Deixar pra depois | 0 | Neutro | Cap 2 Não Ligar |
| 1️⃣ Cap 2 | Examinar | +1 | ✗ Aumenta | Cap 2 Examinar |
| 🔍 Examinar | Deixar | -1 | ✓ Reduz | Dormir |
| 🔍 Examinar | Ver Curtidas | +1 | ✗ Aumenta | Sub-rota curtidas |
| 🔍 Examinar | Ver Comentário | +1 | ✗ Aumenta | Sub-rota comentário |
| 💬 Comentário | Ignorar | -1 | ✓ Reduz | Dormir |
| 💬 Comentário | Apagar | +2 | ✗✗ MUITO NEG | Dormir |
| 2️⃣ Cap 4 | Ver mensagem | 0 | Neutro | Cap 4 Kelly |
| 2️⃣ Cap 4 | Dormir | 0 | Neutro | Fim Demo |
| 2️⃣ Cap 4 | Teto → Ver | 0 | Neutro | Cap 4 Kelly |
| 2️⃣ Cap 4 | Teto → Ignorar | +1 | ✗ Aumenta | Fim Demo |
| 3️⃣ Cap 6 | Contar Kelly | -2 | ✓✓ REDUZ MUITO | Continua ato 3 |
| 3️⃣ Cap 6 | Fingir | +1 | ✗ Aumenta | Continua ato 3 |
| 3️⃣ Cap 6 | Não Responder | +1 | ✗ Aumenta | Continua ato 3 |
| 🎯 Cap 9 | Aceitar | - | Narrativo | FINAL ACEITAR |
| 🎯 Cap 9 | Lutar | - | Narrativo | FINAL LUTAR |

---

## 🎬 CHECKPOINT DO SISTEMA DE BARRA

```
Barra 0-1
  └─ Molly com ansiedade CONTROLADA
      → FINAL BOM (dorme cedo, saudável)

Barra 2-10
  └─ Molly com ansiedade ALTA
      → FINAL RUIM (2h da manhã, dependência digital)

ATO 3 (Override)
  └─ Viagem para fora da realidade
      └─ Escolha Final
          ├─ ACEITAR → Paz da ignorância
          └─ LUTAR → Confronto com realidade
```

---

**Observação Meta**: O jogo é sobre ESCOLHAS PEQUENAS que criam PADRÕES GRANDES. 
Cada decisão importa. Mas o sistema também sugere que, sem consciência real, sempre voltaremos ao mesmo ponto. 🦋
