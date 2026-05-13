# 📂 AUDIT DE CAMINHOS DE ARQUIVOS — MOLLY GAME

## Resumo
Este documento mapeia TODOS os caminhos de arquivo referenciados no código (Python e Templates) que se referem à pasta `static/`. Indica:
- Onde o caminho é referenciado
- Qual é o caminho ATUAL no código
- Onde o arquivo deveria estar / está realmente

---

## 📊 ESTATÍSTICAS

- **Total de referências encontradas**: 129 (Python) + 63 (Templates) = 192 referências
- **Arquivos únicos referenciados**: ~85
- **Categorias**: Imagens (JPG/PNG), Áudio (MP3), Vídeos (MP4), Fontes (OTF/TTF), CSS

---

## 🎵 ÁUDIO — TRILHAS MUSICAIS (Music/)

### App.py — TRILHAS_NOITE (Referências em app.py:7-9)
```
Arquivo: app.py (linhas 7-9)
Caminho no código: journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night).mp3
Status: ✓ Usado em rotação noturna
Localização esperada: static/journey/ato_1/Cap_2(noite)/Music/

Arquivo: app.py (linhas 7-9)
Caminho no código: journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3
Status: ✓ Trilha noturna alternativa
Localização esperada: static/journey/ato_1/Cap_2(noite)/Music/

Arquivo: app.py (linhas 7-9)
Caminho no código: journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_3).mp3
Status: ✓ Terceira trilha noturna
Localização esperada: static/journey/ato_1/Cap_2(noite)/Music/
```

### Game Logic — CAPITULOS TRILHAS (game_logic.py)

| Capítulo ID | Caminho no Código | Localização | Linhas |
|-----------|-----------------|-----------|-------|
| ato1_cap1_dia | journey/ato_1/Cap_1(dia)/Music/Molly_Original_Soundtrack(Day).mp3 | static/journey/ato_1/Cap_1(dia)/Music/ | 8 |
| ato1_cap2_noite | journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3 | static/journey/ato_1/Cap_2(noite)/Music/ | 33 |
| ato1_cap2_examinar | journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3 | static/journey/ato_1/Cap_2(noite)/Music/ | 130 |
| ato1_cap2_curtidas | journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3 | static/journey/ato_1/Cap_2(noite)/Music/ | 210 |
| ato1_cap2_comentario | journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3 | static/journey/ato_1/Cap_2(noite)/Music/ | 258 |
| ato1_cap2_kelly | journey/ato_1/Cap_2(noite)/Music/Molly_Original_Soundtrack(Night_2).mp3 | static/journey/ato_1/Cap_2(noite)/Music/ | 316 |
| ato1_cap3_dia | journey/ato_1/Cap_1(dia)/Music/Molly_Original_Soundtrack(Day).mp3 | static/journey/ato_1/Cap_1(dia)/Music/ | 367 |
| ato2_cap4_noite | journey/ato_2/Cap_4(noite)/Music/Molly_Original_Soundtrack(Night).mp3 | static/journey/ato_2/Cap_4(noite)/Music/ | 388 |
| ato2_cap4_kelly | journey/ato_2/Cap_4(noite)/Music/Molly_Original_Soundtrack(Night).mp3 | static/journey/ato_2/Cap_4(noite)/Music/ | 479 |
| ato1_cap5_dia | journey/ato_2/Cap_5(dia)/Music/Molly_Original_Soundtrack(Day).mp3 | static/journey/ato_2/Cap_5(dia)/Music/ | 629 |
| ato3_cap5_dia | journey/ato_3/Cap_7(dia)/Music/Molly_Original_Soundtrack(Day).mp3 | static/journey/ato_3/Cap_7(dia)/Music/ | 644 |
| ato3_cap6_noite | journey/ato_3/Cap_8(dia)/Music/Molly_Original_Soundtrack(Night_2).mp3 | static/journey/ato_3/Cap_8(dia)/Music/ | 678 |
| ato3_cap7_dia | journey/ato_3/Cap_9(noite)/Music/Molly_Original_Soundtrack(Day).mp3 | static/journey/ato_3/Cap_9(noite)/Music/ | 726 |
| ato3_cap8_dia | journey/ato_3/Cap_9(noite)/Music/Molly_Original_Soundtrack(Day).mp3 | static/journey/ato_3/Cap_9(noite)/Music/ | 743 |
| ato3_cap9_noite | journey/ato_3/Cap_9(noite)/Music/Molly_Original_Soundtrack(Night_3).mp3 | static/journey/ato_3/Cap_9(noite)/Music/ | 760 |

### Menu — Áudio (Templates/index.html)

```
Arquivo: templates/index.html (linha 32)
Caminho no código: menu/Mr_Magic_Remix(Molly).mp3
Referência: {{ url_for('static', filename='menu/Mr_Magic_Remix(Molly).mp3') }}
Localização esperada: static/menu/
Status: ✓ Trilha do menu
```

### Sound Effects (Transições - Templates)

```
Arquivo: templates/transicao_sonho_bom.html (linha 183)
Caminho no código: audio/Sound_Effects/sfx_dream_cool.mp3
Referência: {{ url_for('static', filename='audio/Sound_Effects/sfx_dream_cool.mp3') }}
Localização esperada: static/audio/Sound_Effects/
Status: ✓ SFX de sonho bom

Arquivo: templates/transicao_sonho_bom.html (linha 214)
Caminho no código: audio/Sound_Effects/sfx_suspense(Molly).mp3
Referência: {{ url_for('static', filename='audio/Sound_Effects/sfx_suspense(Molly).mp3') }}
Localização esperada: static/audio/Sound_Effects/
Status: ✓ SFX de suspense

Arquivo: templates/transicao_pesadelo.html (linha 152)
Caminho no código: audio/Sound_Effects/sfx_nightmare.mp3
Referência: {{ url_for('static', filename='audio/Sound_Effects/sfx_nightmare.mp3') }}
Localização esperada: static/audio/Sound_Effects/
Status: ✓ SFX de pesadelo

Arquivo: templates/transicao_pesadelo.html (linha 176)
Caminho no código: audio/Sound_Effects/sfx_suspense(Molly).mp3
Referência: {{ url_for('static', filename='audio/Sound_Effects/sfx_suspense(Molly).mp3') }}
Localização esperada: static/audio/Sound_Effects/
Status: ✓ SFX de suspense (pesadelo)

Arquivo: templates/transicao.html (linha 142)
Caminho no código: journey/ato_1/Cap_2(noite)/Sound/sfx_day_night.mp3
Status: ✓ Transição dia → noite
Localização esperada: static/journey/ato_1/Cap_2(noite)/Sound/

Arquivo: templates/transicao.html (linha 142)
Caminho no código: journey/ato_1/Cap_2(noite)/Sound/sfx_night_day.mp3
Status: ✓ Transição noite → dia
Localização esperada: static/journey/ato_1/Cap_2(noite)/Sound/
```

### Sound Effects — Game Logic (game_logic.py)

| Arquivo | Linha | Caminho | Status |
|---------|-------|---------|--------|
| game_logic.py | 3 | journey/ato_1/Cap_2(noite)/Sound/ | Base SFX |

---

## 🖼️ IMAGENS — Capítulos/Cenas (journey/ato_X/...)

### Ato 1 - Cap 1 (Dia)

```
Arquivo: game_logic.py (linhas 13-27)
Caminhos referenciados:
- journey/ato_1/Cap_1(dia)/Molly_1.png (5 referências)
- journey/ato_1/Cap_1(dia)/Molly_2.png (3 referências)
- journey/ato_1/Cap_1(dia)/Molly_3.png (2 referências)
- journey/ato_1/Cap_1(dia)/Molly_4.png (2 referências)
- journey/ato_1/Cap_1(dia)/Molly_5.png (2 referências)
- journey/ato_1/Cap_1(dia)/Molly_6.png (3 referências)

Localização esperada: static/journey/ato_1/Cap_1(dia)/
Status: ✓ Frames do capítulo 1
```

### Ato 1 - Cap 2 (Noite - Principal)

```
Arquivo: game_logic.py (linhas 38-43)
Caminhos referenciados em frames:
- journey/ato_1/Cap_2(noite)/Molly_1.png
- journey/ato_1/Cap_2(noite)/Molly_2.png
- journey/ato_1/Cap_2(noite)/Molly_3.png
- journey/ato_1/Cap_2(noite)/Molly_4.png
- journey/ato_1/Cap_2(noite)/Molly_5.png
- journey/ato_1/Cap_2(noite)/Molly_6.png

Localização esperada: static/journey/ato_1/Cap_2(noite)/
Status: ✓ Frames principais cap 2 noite
```

### Ato 1 - Cap 2 (Noite - Examinar Route)

```
Arquivo: game_logic.py (linhas 135-143)
Caminhos em frames de Clicou_Examinar:
- journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_1.png
- journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_2.png
- journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_3.png
- journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_4.png
- journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_5.png
- journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_6.png
- journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_8.png
- journey/ato_1/Cap_2(noite)/Clicou_Examinar/Molly_9.png

Localização esperada: static/journey/ato_1/Cap_2(noite)/Clicou_Examinar/
Status: ✓ Frames da rota "examinar comentário"
```

### Ato 1 - Cap 3 (Dia)

```
Arquivo: game_logic.py (linhas 371-382)
Caminhos referenciados:
- journey/ato_1/Cap_3(dia)/Molly_1.png (2 referências)
- journey/ato_1/Cap_3(dia)/Molly_2.png (3 referências)
- journey/ato_1/Cap_3(dia)/Molly_3.png (1 referência)
- journey/ato_1/Cap_3(dia)/Molly_4.png (2 referências)
- journey/ato_1/Cap_3(dia)/Molly_5.png (2 referências)
- journey/ato_1/Cap_3(dia)/Molly_6.png (2 referências)

Localização esperada: static/journey/ato_1/Cap_3(dia)/
Status: ✓ Frames cap 3 dia
```

### Ato 2 - Cap 4 (Noite)

```
Arquivo: game_logic.py (linhas 393-396, 484-489)
Caminhos referenciados:
- journey/ato_2/Cap_4(noite)/Molly_1.png (2 referências)
- journey/ato_2/Cap_4(noite)/Molly_2.png (2 referências)
- journey/ato_2/Cap_4(noite)/Molly_3.png (2 referências)
- journey/ato_2/Cap_4(noite)/Molly_4.png (2 referências)
- journey/ato_2/Cap_4(noite)/Molly_5.png (1 referência)
- journey/ato_2/Cap_4(noite)/Molly_6.png (1 referência)

Localização esperada: static/journey/ato_2/Cap_4(noite)/
Status: ✓ Frames cap 4 noite
```

### Ato 2 - Cap 5 (Dia)

```
Arquivo: game_logic.py (linhas 633-638)
Caminhos referenciados:
- journey/ato_2/Cap_5(dia)/Molly_1.png
- journey/ato_2/Cap_5(dia)/Molly_2.png
- journey/ato_2/Cap_5(dia)/Molly_3.png
- journey/ato_2/Cap_5(dia)/Molly_4.png
- journey/ato_2/Cap_5(dia)/Molly_5.png
- journey/ato_2/Cap_5(dia)/Molly_6.png

Localização esperada: static/journey/ato_2/Cap_5(dia)/
Status: ✓ Frames cap 5 dia
```

### Ato 3 - Cap 7 (Dia - Cap 5 numeração)

```
Arquivo: game_logic.py (linhas 649-672)
Caminhos referenciados:
- journey/ato_3/Cap_7(dia)/Molly_1.png (3 referências)
- journey/ato_3/Cap_7(dia)/Molly_2.png (3 referências)
- journey/ato_3/Cap_7(dia)/Molly_3.png (3 referências)
- journey/ato_3/Cap_7(dia)/Molly_4.png (3 referências)
- journey/ato_3/Cap_7(dia)/Molly_5.png (3 referências)
- journey/ato_3/Cap_7(dia)/Molly_6.png (3 referências)

Localização esperada: static/journey/ato_3/Cap_7(dia)/
Status: ✓ Frames cap 7 dia (ato 3 cap 1)
```

### Ato 3 - Cap 8 (Dia - Background)

```
Arquivo: game_logic.py (linha 682)
Caminho referenciado:
- journey/ato_3/Cap_8(dia)/Fundo_Noite.png

Localização esperada: static/journey/ato_3/Cap_8(dia)/
Status: ✓ Background para cena noite
```

### Ato 3 - Cap 9 (Noite - Plot Twist)

```
Arquivo: game_logic.py (linhas 730-737, 747-754)
Caminhos referenciados:
- journey/ato_3/Cap_9(noite)/Molly_1.png (2 referências)
- journey/ato_3/Cap_9(noite)/Molly_2.png (2 referências)
- journey/ato_3/Cap_9(noite)/Molly_3.png (2 referências)
- journey/ato_3/Cap_9(noite)/Molly_4.png (2 referências)
- journey/ato_3/Cap_9(noite)/Molly_5.png (2 referências)
- journey/ato_3/Cap_9(noite)/Molly_6.png (2 referências)
- journey/ato_3/Cap_9(noite)/Molly_7.png (2 referências)
- journey/ato_3/Cap_9(noite)/Molly_8.png (2 referências)
- journey/ato_3/Cap_9(noite)/Fundo_Noite_Final.png (linha 764)

Localização esperada: static/journey/ato_3/Cap_9(noite)/
Status: ✓ Frames finais noite
```

### Finais (Final Screens)

```
Arquivo: game_logic.py (linhas 870-894)
Caminhos de final referenciados:

FINAL BOM:
- journey/ato_1/Cap_2(noite)/Molly_1.png (linha 870)

FINAL RUIM:
- journey/ato_1/Cap_2(noite)/Molly_6.png (linha 876)

FINAL ACEITAR:
- journey/final/ruim/Molly_1.png (linha 882)

FINAL LUTAR:
- journey/final/ruim/Molly_6.png (linha 888)

FINAL SONHO_MAE:
- journey/final/ruim/Molly_2.png (linha 894)

Localização esperada: static/journey/final/ruim/
Status: ✓ Personagens para telas finais
```

---

## 🎨 IMAGENS — UI/HUD (Static/box, pen, fly, etc)

### Box - Molly Name Box

```
Arquivo: templates/cena.html (linhas 180, 229)
Caminho: box/box_molly/Molly_Name_Box.png
Referência: {{ url_for('static', filename='box/box_molly/Molly_Name_Box.png') }}
Localização esperada: static/box/box_molly/
Status: ✓ Nome da Molly em cena
Ocorrências: 2x em cena.html
```

### Box - Molly Speech Box

```
Arquivo: templates/cena.html (linhas 182, 231)
Caminho: box/box_molly/box_molly_v2.png
Referência: {{ url_for('static', filename='box/box_molly/box_molly_v2.png') }}
Localização esperada: static/box/box_molly/
Status: ✓ Caixa de diálogo da Molly
Ocorrências: 2x em cena.html + 2x em JavaScript constantes
```

### Borboleta (Butterfly Animation)

```
Arquivo: templates/index.html (linhas 319-322)
Caminhos:
- fly/BORBOLETA_1.png
- fly/BORBOLETA_2.png
- fly/BORBOLETA_3.png
- fly/BORBOLETA_4.png

Arquivo: templates/cena.html (linhas 165, 319-322)
Caminhos: (repetidos)
- fly/BORBOLETA_1.png
- fly/BORBOLETA_2.png
- fly/BORBOLETA_3.png
- fly/BORBOLETA_4.png

Localização esperada: static/fly/
Status: ✓ Animação de borboleta (4 frames)
Ocorrências: index.html (4x) + cena.html (5x)
```

### Caneta (Pen)

```
Arquivo: templates/index.html (linha 93)
Caminho: pen/CANETA.png
Referência: {{ url_for('static', filename='pen/CANETA.png') }}
Localização esperada: static/pen/
Status: ✓ Caneta no tutorial
Ocorrências: 1x em tutorial index.html
```

---

## 📖 IMAGENS — Caderno (Notebook/Diary)

```
Arquivo: templates/index.html (linhas 313-316)
Caminhos:
- book/CADERNO_FECHADO.png
- book/CADERNO_SEMLACRE.png
- book/CADERNO_SEMIABERTO.png
- book/CADERNO_ABERTO_TOTALMENTE.png

Localização esperada: static/book/
Status: ✓ 4 estados do caderno para animação
Ocorrências: 1 set em index.html (tutorial)
```

---

## 🎬 VÍDEOS (Video/)

### Abertura/Opening

```
Arquivo: templates/index.html (linha 145)
Caminho: video/Abertura/Opening_Game.mp4
Referência: {{ url_for('static', filename='video/Abertura/Opening_Game.mp4') }}
Localização esperada: static/video/Abertura/
Status: ✓ Vídeo de abertura
```

### Molly GIFs

```
Arquivo: templates/index.html (linha 236)
Caminho: video/molly/Molly_gif(5s).gif
Referência: {{ url_for('static', filename='video/molly/Molly_gif(5s).gif') }}
Localização esperada: static/video/molly/
Status: ✓ GIF animado de Molly (5s)

Arquivo: templates/index.html (linha 246)
Caminho: video/molly/Molly_gif_timida.gif
Referência: {{ url_for('static', filename='video/molly/Molly_gif_timida.gif') }}
Localização esperada: static/video/molly/
Status: ✓ GIF de Molly tímida
```

---

## 🎨 CSS

```
Arquivo: templates/index.html (linha 24)
Caminho: css/style.css
Referência: {{ url_for('static', filename='css/style.css') }}
Localização esperada: static/css/
Status: ✓ Folha de estilos principal
```

---

## 🔤 FONTES (Fonts)

### Glassure Font

```
Arquivos referenciados:
- templates/index.html (linha 11)
- templates/cena.html (linha 10)
- templates/final.html (linha 11)
- templates/fimdemo.html (linha 11)
- templates/transicao.html (linha 11)
- templates/transicao_pesadelo.html (não encontrado)
- templates/transicao_sonho_bom.html (não encontrado)

Caminho: menu/Glassure.otf
Referência: {{ url_for('static', filename='menu/Glassure.otf') }}
Localização esperada: static/menu/
Status: ✓ Fonte decorativa (serif)
Ocorrências: 5 arquivos
```

### DM Sans Font (Regular)

```
Arquivos referenciados:
- templates/index.html (linha 15)
- templates/cena.html (linha 11)
- templates/final.html (linha 15)
- templates/fimdemo.html (linha 15)
- templates/transicao.html (linha 15)

Caminho: menu/DMSans-VariableFont_opsz,wght.ttf
Referência: {{ url_for('static', filename='menu/DMSans-VariableFont_opsz,wght.ttf') }}
Localização esperada: static/menu/
Status: ✓ Fonte variável (sans-serif)
Ocorrências: 5 arquivos
```

### DM Sans Font (Italic)

```
Arquivo: templates/index.html (linha 20)
Caminho: menu/DMSans-Italic-VariableFont_opsz,wght.ttf
(TRUNCADO NO CÓDIGO: DMSans-Italic-VariableFont_opsz,wgh....ttf)
Referência: {{ url_for('static', filename='menu/DMSans-Italic-VariableFont_opsz,wgh....ttf') }}
Localização esperada: static/menu/
Status: ⚠️ TRUNCADO/POSSÍVEL ERRO
Nota: Nome do arquivo está incompleto no código
```

---

## 🖼️ IMAGENS — Menu & Demo

### Menu Fundo

```
Arquivo: templates/index.html (linha 28)
Caminho: menu/menu_fundo.png
Referência: {{ url_for('static', filename='menu/menu_fundo.png') }}
Localização esperada: static/menu/
Status: ✓ Fundo do menu principal
```

### Dream Demo Test

```
Arquivo: templates/index.html (linha 121)
Caminho: journey/dream/dream_initial/dream_demo_test.png
Referência: {{ url_for('static', filename='journey/dream/dream_initial/dream_demo_test.png') }}
Localização esperada: static/journey/dream/dream_initial/
Status: ✓ Imagem de teste para sonho (demo)
Nota: Referenciado 2x no mesmo arquivo
```

---

## 📋 RESUMO POR CATEGORIA

### 📂 Pastas Principais Usadas

| Pasta | Quantidade | Tipo | Localização |
|-------|-----------|------|------------|
| journey/ato_1/Cap_1(dia) | 6 | Imagens (frames) | static/journey/ |
| journey/ato_1/Cap_2(noite) | 6 + 8 sub | Imagens + Music + Sound | static/journey/ |
| journey/ato_1/Cap_3(dia) | 6 | Imagens | static/journey/ |
| journey/ato_2/Cap_4(noite) | 6 | Imagens + Music | static/journey/ |
| journey/ato_2/Cap_5(dia) | 6 | Imagens + Music | static/journey/ |
| journey/ato_3/Cap_7(dia) | 6 | Imagens + Music | static/journey/ |
| journey/ato_3/Cap_8(dia) | 1 background | Imagens | static/journey/ |
| journey/ato_3/Cap_9(noite) | 8 + background | Imagens + Music | static/journey/ |
| journey/final/ruim | 3 | Imagens finais | static/journey/ |
| journey/dream/dream_initial | 1 | Teste | static/journey/ |
| menu | 5 | Fontes + fundo + audio | static/menu/ |
| box/box_molly | 2 | UI boxes | static/box/ |
| fly | 4 | Animação borboleta | static/fly/ |
| pen | 1 | Caneta | static/pen/ |
| book | 4 | Estados caderno | static/book/ |
| audio/Sound_Effects | 4 | SFX | static/audio/ |
| video/Abertura | 1 | Vídeo MP4 | static/video/ |
| video/molly | 2 | GIFs | static/video/ |
| css | 1 | Folha estilos | static/css/ |

---

## ⚠️ PROBLEMAS IDENTIFICADOS

### 1. ⚠️ Font Truncada
**Arquivo**: templates/index.html (linha 20)
**Problema**: Nome da fonte está truncado/cortado
```
Referenciado como: menu/DMSans-Italic-VariableFont_opsz,wgh....ttf
Esperado: menu/DMSans-Italic-VariableFont_opsz,wght.ttf
```

### 2. 🔍 Caminhos não verificados no servidor
Os seguintes caminhos não foram fisicamente verificados:
- `static/audio/Sound_Effects/` — Arquivos SFX
- `static/video/Abertura/` — Vídeo de abertura
- `static/video/molly/` — GIFs de Molly
- `static/journey/final/ruim/` — Imagens finais
- `static/journey/dream/` — Imagens de sonho

### 3. ✓ Estrutura esperada vs. atual
Todos os caminhos seguem o padrão esperado:
```
static/journey/ato_X/Cap_Y(tipo)/
static/menu/
static/box/box_molly/
static/fly/
static/pen/
static/book/
static/audio/Sound_Effects/
static/video/Abertura/
static/video/molly/
static/css/
```

---

## 📊 CONTAGEM FINAL

| Categoria | Quantidade |
|-----------|-----------|
| Imagens de Capítulos (PNG) | ~60 |
| Trilhas Musicais (MP3) | 15 |
| Sound Effects (MP3) | 4 |
| Vídeos/GIFs | 3 |
| Fontes (OTF/TTF) | 3 |
| CSS | 1 |
| Outros (UI elements) | ~8 |
| **TOTAL** | **~94 arquivos** |

---

## 📝 NOTAS

1. Todos os caminhos começam com `journey/`, `menu/`, `box/`, `fly/`, `pen/`, `book/`, `audio/`, `video/` ou `css/`
2. O prefixo `static/` é adicionado pelo Flask via `url_for('static', filename='...')`
3. Não há caminhos absolutos `/static/` no HTML (todos usam `url_for`)
4. Em JavaScript, alguns caminhos usam `/static/...` diretamente
5. Os sounds de transição também usam `/static/journey/ato_1/Cap_2(noite)/Sound/`
6. O `SFX_BASE` em game_logic.py é `journey/ato_1/Cap_2(noite)/Sound/`

---

## 🎯 PRÓXIMOS PASSOS (Sugestões)

1. ✓ Verificar físicamente os arquivos em `static/audio/Sound_Effects/`
2. ✓ Verificar se os vídeos em `static/video/` existem
3. ✓ Corrigir a font truncada em `templates/index.html` linha 20
4. ✓ Considerar consolidar os SFX paths (atualmente espalhados)
5. ✓ Documentar a estrutura de arquivos esperada

