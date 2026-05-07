# Molly

Jogo narrativo interativo desenvolvido em Python com Flask, criado como projeto de prática extensionista do curso de Ciência da Computação do CIESA.

O jogador acompanha Molly, uma jovem de 16 anos, ao longo de sua rotina digital. As escolhas feitas e as que a própria Molly faz sozinha determinam como a história termina.

---

## Tecnologias utilizadas

- Python 3.x
- Flask
- HTML / CSS
- JavaScript

---

## Como rodar o projeto

Clone o repositório:

```bash
git clone https://github.com/nevext/molly-game.git
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Rode o servidor:

```bash
python app.py
```

Acesse em: `http://localhost:5000`

---

## Estrutura do projeto

```
molly-game/
├── static/
│   ├── images/
│   │   ├── characters/   → expressões da Molly
│   │   └── backgrounds/  → cenários do jogo
│   ├── audio/            → trilhas sonoras
│   └── css/
│       └── style.css
├── templates/
│   ├── index.html        → menu principal
│   ├── cena.html         → engine das cenas
│   └── final.html        → tela de final
├── app.py                → rotas Flask
├── game_logic.py         → lógica do jogo
├── requirements.txt
└── README.md
```

---

## Rotas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Menu principal |
| GET | `/jogar` | Inicia o jogo e sorteia a abertura |
| GET | `/cena` | Exibe a cena atual |
| GET | `/escolha/<opcao>` | Processa a escolha do jogador |
| GET | `/final` | Exibe o final baseado na barra de ansiedade |
| GET | `/reiniciar` | Limpa a sessão e volta ao menu |

---

## Como o jogo funciona

O jogo possui 6 aberturas diferentes sorteadas aleatoriamente a cada jogatina. Cada abertura tem 7 cenas com escolhas de múltipla opção. Uma barra de ansiedade invisível acumula ao longo das cenas quando ultrapassa certos níveis, a própria Molly toma decisões sem esperar o jogador. O valor final da barra determina se o jogador recebe o final bom ou ruim.

---

## Progresso

- [x] Repositório criado
- [x] Estrutura base do projeto
- [x] Roteiro completo — 6 aberturas, 42 cenas, 12 finais
- [x] Arte da Molly — expressões criadas
- [ ] Cenários criados
- [ ] Menu principal
- [ ] Backend Flask
- [ ] Sistema de barra de ansiedade
- [ ] Cenas implementadas
- [ ] Finais implementadas
- [ ] Easter eggs implementados
- [ ] Som adicionado
- [ ] Testes
- [ ] Hospedagem

---

## Desenvolvedor

**David Neves de Figueiredo** — Ciência da Computação, CIESA