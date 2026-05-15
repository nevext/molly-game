# 🦋 MOLLY GAME - Documentação Técnica

## 📋 Visão Geral

**Molly Game** é uma visual novel interativa em Flask que explora a ansiedade digital e o impacto das redes sociais em adolescentes. O jogador faz escolhas que alteram a barra de ansiedade de Molly (0-10), impactando o final.

**Status**: v2.0.0 (em desenvolvimento)
**Stack**: Python (Flask) + HTML/CSS/JS
**Tema**: Ansiedade digital, redes sociais, saúde mental

---

## 🏗️ Estrutura do Projeto

```
molly-game/
├── app.py                          # Flask principal + rotas
├── game_logic.py                   # Lógica do jogo (CAPITULOS, funções)
├── templates/
│   ├── index.html                  # Menu principal
│   ├── cena.html                   # Renderização de cenas
│   ├── fimdemo.html                # Telas de final
│   ├── transicao.html              # Transição dia/noite
├── static/
│   ├── css/style.css               # Estilos
│   ├── audio/                      # Trilhas + SFX
│   ├── jornada/                    # Imagens dos capítulos
│   └── [outros assets]
├── CLAUDE.md                       # Este arquivo
├── ROTEIRO_DO_JOGO.md              # Fluxo narrativo
├── MAPEAMENTO_DE_CENAS.md          # Detalhe de cada cena
└── AUDIT_CAMINHOS_ARQUIVOS.md      # Mapeamento de assets

```

---

## 🎮 Mecânicas Principais

### Sistema de Barra (0-10)

- **Barra 0-1**: Ansiedade CONTROLADA → **FINAL BOM**
- **Barra 2-10**: Ansiedade ALTA → **FINAL RUIM**
- Cada escolha tem um `delta` que altera a barra: `nova_barra = max(0, min(10, barra + delta))`

### Tipos de Capítulos

- **DIA** (`tipo: "dia"`): Narração linear sem escolhas
- **NOITE** (`tipo: "noite"`): Cenas com escolhas, mensagens dinâmicas
- **DEMO** (`tipo: "demo"`): Fim da demonstração

---

## 🔧 Componentes Principais

### app.py — Flask & Rotas

#### Rotas Principais

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Menu principal (index.html) |
| `/jogar` | GET | Inicia novo jogo, limpa session |
| `/cena` | GET | Renderiza a cena atual |
| `/avancar_frame` | GET | Próximo frame (dias) |
| `/transicao/<tipo>` | GET | Transição dia/noite |
| `/escolha/<opcao>` | GET | Processa escolha do jogador |
| `/avancar_data` | GET | Próximo JSON (noites) |
| `/escolha_data/<opcao>` | GET | Escolha JSON (noites) |
| `/fim_demo` | GET | Tela final |
| `/conquista/<nome>` | GET | Salva conquista na session |
| `/set_barra/<valor>` | GET | Debug: define barra manualmente |
| `/force_sleep` | GET | Debug: pula para cena de dormir |

#### Session Variables

```python
{
    "cap": "ato1_cap1_dia",           # Capítulo atual
    "frame": 0,                       # Frame do dia
    "cena": 1,                        # Número da cena noturna
    "barra": 3,                       # Ansiedade (0-10)
    "noite_count": 0,                 # Contador de noites (trilha rotativa)
    "contador_kelly": 0,              # Vezes que falou com Kelly
    "afinidade_kelly": 0,             # Afinidade com Kelly
    "humor_kelly": "animada",         # Humor de Kelly
    "dia_trilha": "...",              # Trilha do dia atual
    "dia_cap": "...",                 # Capítulo do dia atual
    "finais": {},                     # Finais vistos {"bom": True, ...}
    "finais_vistos": [],              # Lista de finais assistidos
    "conquistas": {},                 # Achievements desbloqueadas
    "descobriu_segredo_kelly": False, # Easter egg: flash vs luz
    "tipo_final": "aceitar"           # Escolha final (aceitar/lutar)
}
```

#### Funções Utilitárias

- `get_trilha_noite()`: Retorna trilha noturna rotativa (noite 1→night.mp3, noite 2→night_2.mp3, ...)
- `_build_conquistas()`: Monta dict de conquistas + easter eggs
- `preservar_progresso()`: Salva finais/conquistas antes de limpar session
- `restaurar_progresso()`: Restaura após clear()

### game_logic.py — Lógica do Jogo

#### Estrutura do CAPITULOS

```python
CAPITULOS = {
    "cap_id": {
        "tipo": "dia|noite|demo",
        "trilha": "audio/...",
        "proximo": "cap_id_proximo",
        "tem_escolhas": True/False,
        "frames": [...],              # Dias: lista de frames
        "cenas": {                    # Noites: dict de cenas
            1: {"titulo", "texto", "frame_idx", "opcoes": [...]}
        }
    }
}
```

#### Funções Principais

- `get_capitulo(cap_id)`: Retorna dict do capítulo
- `get_proximo_capitulo(cap_id)`: Retorna próximo capítulo
- `processar_escolha(cap_id, cena_num, opcao_index, barra)`: Aplica delta e retorna (nova_barra, acao)
- `get_flag_escolha(cap_id, cena_num, opcao_index)`: Retorna flags (ex: `{"humor": "insegura"}`)
- `molly_age_sozinha(cap_id, cena_num, barra)`: Retorna True se Molly envelhece
- `get_final(barra, tipo_forcado=None)`: Retorna final (bom/ruim/aceitar/lutar)
- `get_final_data(tipo)`: Retorna final especial (mae/amiga/etc)

#### Conquistas (19 totais)

```python
TODAS_CONQUISTAS = [
    'teve_sonho', 'entrou_pesadelo', 'sobreviveu_pesadelo', 'venceu_pesadelo',
    'morreu_pesadelo', 'sonho_bom', 'final_mae', 'melhor_amiga',
    'final_ruim', 'viu_frances', 'descobriu_segredo_kelly', 'relaxante',
    'ouvinte', 'viu_alucinacao', 'confiou_molly', 'confiou_narrador',
    'beta_tester', 'jogador_000', 'ela_agradece'
]
```

---

## 📖 Capítulos Implementados

### ATO 1 (Demos)

| Cap | ID | Tipo | Próximo | Escolhas | Descrição |
|-----|----|----|---------|---------|-----------|
| 1 | `ato1_cap1_dia` | dia | ato1_cap2_noite | ✗ | Molly posta foto (8 curtidas) |
| 2 | `ato1_cap2_noite` | noite | ato1_cap3_dia | ⚡ | Kelly manda SMS, escolha sobre comentário |
| 2 | `ato1_cap2_examinar` | noite | ato1_cap3_dia | ⚡ | Rota: investigar comentário |
| 2 | `ato1_cap2_naoligar` | noite | ato1_cap3_dia | ⚡ | Rota: ignorar e dormir |
| 2 | `ato1_cap2_curtidas` | noite | ato1_cap2_examinar | ⚡ | Sub-rota: ver 32 curtidas (easter egg: Frances Haugen) |
| 2 | `ato1_cap2_comentario` | noite | ato1_cap3_dia | ⚡ | Sub-rota: ver comentário "menor da zl" |
| 2 | `ato1_cap2_kelly` | noite | ato1_cap3_dia | ⚡ | Conversa com Kelly (-1 delta) |
| 3 | `ato1_cap3_dia` | dia | ato2_cap4_noite | ✗ | Molly tenta postar mas desiste |

### ATO 2 (Segundo Ato)

| Cap | ID | Tipo | Próximo | Escolhas | Descrição |
|-----|----|----|---------|---------|-----------|
| 4 | `ato2_cap4_noite` | noite | ato1_cap5_dia | ⚡ | Kelly manda novamente, ver/ignorar |
| 4 | `ato2_cap4_kelly` | noite | ato1_cap5_dia | ⚡ | Conversa dinâmica (muda por barra) |
| 5 | `ato1_cap5_dia` | dia | ato3_cap5_dia | ✗ | Molly tenta foto, frustração com filtros |

### ATO 3 (Plot Twist)

| Cap | ID | Tipo | Próximo | Escolhas | Descrição |
|-----|----|----|---------|---------|-----------|
| 5/7 | `ato3_cap5_dia` | dia | ato3_cap6_noite | ✗ | Molly acorda, quarto está "igual demais" |
| 6/8 | `ato3_cap6_noite` | noite | ato3_cap7_dia | ⚡ | Molly percebe repetição, conta para Kelly |
| 7/9 | `ato3_cap7_dia` | dia | ato3_cap8_dia | ✗ | PLOT TWIST: porta não abre, vê código |
| 8/10 | `ato3_cap8_dia` | dia | ato3_cap9_noite | ✗ | Narrador revela tudo (jogo meta) |
| 9/11 | `ato3_cap9_noite` | noite | None | ⚡ | **ESCOLHA FINAL**: aceitar ou lutar |

---

## 🎬 Finais Possíveis

### Final BOM (Barra 0-1)
```
São 23h. Você coloca o celular na gaveta e dorme cedo.
Pela primeira vez em semanas, descansa verdadeiramente.

Mensagem: "Desconectar não é fraqueza. É escolha. 
E escolhas pequenas mudam padrões grandes."
```

### Final RUIM (Barra 2-10)
```
São 2h da manhã. A foto tem 89 curtidas. 
Você dorme cansada. E acorda igual.

Mensagem: "Ansiedade digital não some sozinha. 
Se isso parece familiar, você não está sozinha. CVV: 188."
```

### Final ACEITAR (Ato 3, Escolha 1)
```
Molly aceitou o jogo. A mentira confortável.
Tudo se repete. Sempre igual.

Mensagem: "A paz da ignorância é uma escolha. 
Uma escolha que você pode fazer todos os dias. E fará."
```

### Final LUTAR (Ato 3, Escolha 2)
```
Molly gritou. As paredes começaram a piscar.
O código apareceu. Ela estava quebrando o jogo.

Mensagem: "Nem tudo que é real é confortável. 
Você escolheu acordar."
```

---

## 🎵 Sistema de Áudio

### Trilhas Musicais (Dias - Aleatórias)

```python
TRILHAS_DIA = [
    "audio/soundtrack/day.mp3",
    "audio/soundtrack/day_2.mp3",
    "audio/soundtrack/day_3.mp3",
]
```

### Trilhas Musicais (Noites - Rotativas)

```python
TRILHAS_NOITE = [
    "audio/soundtrack/night.mp3",       # Noite 1 (cap 2)
    "audio/soundtrack/night_2.mp3",     # Noites 2-3 (cap 4)
    "audio/soundtrack/night_3.mp3",     # Noite 4 (cap 9)
]
```

### Sound Effects

```
audio/sfx/
├── sfx_good_choice.mp3       # Escolha boa
├── sfx_bad_choice.mp3        # Escolha ruim
└── sfx_especial_choice.mp3   # Escolha especial
```

---

## 🖼️ Templates

### index.html — Menu Principal
- Botão "Jogar"
- Exibição de finais vistos
- Exibição de conquistas
- Tutorial (caneta, caderno)

### cena.html — Renderização de Cenas
- Frame da imagem
- Diálogo (narrador, Molly, SMS, conversa)
- Opções de escolha
- HUD (Ato, Capítulo)
- Trilha sonora

### fimdemo.html — Tela Final
- Imagem do final
- Texto descritivo
- Mensagem de reflexão
- Botão "Jogar de Novo"

### transicao.html — Transição
- Imagem de transição
- SFX de transição
- Botão continuar

---

## 🎯 Fluxos Principais

### Fluxo BOM (Barra 0-1)
```
Cap 1 → Cap 2 (Opção 1: -1)
      → Cap 2 Kelly → Cap 3 → Cap 4 → Cap 5
      → FIM BOM
```

### Fluxo RUIM (Barra 4+)
```
Cap 1 → Cap 2 (Opção 3: +1)
      → Cap 2 Examinar (Opção 3: +1)
      → Cap 2 Comentário (Opção 2: +2)
      → Cap 3 → Cap 4 → Cap 5 → Cap 6 (+1)
      → Cap 7-9 → Escolha Final
      → FIM RUIM / ACEITAR / LUTAR
```

---

## 🔄 Sistema de Conversa Dinâmica

Algumas conversas mudam conforme a **BARRA DE ANSIEDADE**:

### ato2_cap4_kelly — Cena 3

**BARRA ALTA (>= 2)**:
- Molly nega estar bem
- Cria desculpas ("estudos")
- Kelly fica preocupada

**BARRA BAIXA (< 2)**:
- Molly abre sobre estar cansada
- Kelly é solidária e amorosa
- Conversa mais profunda

---

## 🐛 Debug & Funções de Teste

### Rotas Debug (app.debug=True)

```
/set_barra/<valor>        # Define barra manualmente (0-10)
/force_sleep              # Pula direto para cena de dormir
```

### Variáveis Session para Debug

```python
session["barra"] = 5              # Teste final ruim
session["barra"] = 0              # Teste final bom
session["contador_kelly"] = 2     # Teste conversa Kelly
session["afinidade_kelly"] = 2    # Teste conquista "melhor_amiga"
```

---

## 📱 Recursos Especiais

### Easter Eggs

- **Frances Haugen** (ato1_cap2_curtidas, Cena 3): Menção a ativista que denunciou filtros do Instagram
  - URL: https://www.bbc.com/portuguese/articles/c3g1q1y1y1y1
- **Borboleta** (🦋): Símbolo recorrente (transformação, liberdade)
- **Reporter Perigosa**: Mencionada por Kelly, mistério não resolvido

### Propriedades Especiais de Cenas

| Propriedade | Efeito |
|-------------|--------|
| `ir_dormir: True` | Molly vai dormir, transição para dia |
| `fim_curtidas: True` | Volta para cena anterior |
| `volta_aqui: True` | Retorna após sub-rota |
| `cortar_musica: True` | Interrompe trilha sonora |
| `borboleta: True` | Elemento visual especial |
| `sumir_apos: True` | Opção desaparece após escolher |

---

## 🔐 Segurança

- **Secret Key**: Definida por variável de ambiente `SECRET_KEY` (padrão: "molly2026")
- **Session**: Tudo armazenado no cliente (Flask session)
- **Input Validation**: Opções checadas por índice

---

## 🚀 Como Executar

```bash
# Instalar dependências
pip install flask

# Executar (modo debug)
python app.py

# Acessar
http://localhost:5000
```

---

## 📝 Próximos Passos

- [ ] Implementar suporte a saves (banco de dados)
- [ ] Sistema de achievements real
- [ ] Mais variações de diálogo dinâmico
- [ ] Full game (capítulos 5-8 completos)
- [ ] Suporte a idiomas (i18n)
- [ ] Analytics de escolhas

---

## 📚 Documentação Relacionada

- **ROTEIRO_DO_JOGO.md**: Fluxo narrativo completo
- **MAPEAMENTO_DE_CENAS.md**: Detalhe de cada cena e escolha
- **AUDIT_CAMINHOS_ARQUIVOS.md**: Mapa de assets (imagens, áudio, etc)

---

**Versão**: 2.0.0
**Última atualização**: 2026-05-14
