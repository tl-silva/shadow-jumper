# Shadow Jumper - Platformer Game 🕹️

Este é um projeto de jogo de plataforma desenvolvido em **Python** utilizando a biblioteca **Pygame Zero (pgzero)**. O projeto demonstra conhecimentos em lógica de programação, animação de sprites, física básica de jogos e arquitetura orientada a objetos (POO).

## 📋 Requisitos do Projeto Atendidos

* **Gênero:** Platformer (Visão lateral com mecânicas de gravidade e saltos).
* **Módulos Utilizados:** `pgzero`, `math`, `random` e a classe `Rect` do `pygame`.
* **Menu Principal:** Interface com botões clicáveis para iniciar, alternar áudio e fechar o jogo.
* **Sons e Música:** Sistema de música de fundo em loop e efeitos sonoros para ações (pulo e dano).
* **Inimigos:** Patrulhas automatizadas que se movem em territórios definidos e oferecem perigo ao herói.
* **Animação de Sprites:** Implementação de animação cíclica para todos os personagens (parados e em movimento), garantindo fluidez visual.
* **Código Limpo:** Nomenclatura em inglês, estrutura organizada e aderência às boas práticas de programação (PEP8).

---

## 🎮 Como Executar

1.  **Instale o Pygame Zero:**
    Abra o seu terminal ou prompt de comando e instale a biblioteca necessária:
    ```bash
    pip install pgzero
    ```

2.  **Organize os Arquivos:**
    Certifique-se de que o seu código esteja em um arquivo (ex: `main.py`) e que as pastas `images` e `sounds` estejam no mesmo local.

3.  **Inicie o Jogo:**
    No terminal, dentro da pasta do projeto, execute:
    ```bash
    pgzrun main.py
    ```

### ⌨️ Controles:
* **Setas Esquerda/Direita:** Movimentação lateral do herói.
* **Espaço ou Seta para Cima:** Pular.
* **Mouse:** Utilizado para clicar nos botões do Menu Principal.

---

## 🛠️ Destaques da Implementação

* **Arquitetura POO:** Uso de herança com a classe `AnimatedSprite` para gerenciar animações de forma genérica.
* **Máquina de Estados:** Gerenciamento de fluxo entre `MENU` e `GAME`.
* **Física de Plataforma:** Implementação de gravidade e detecção de colisão precisa utilizando `Rect`.
* **Animação Direcional:** Sistema que alterna entre estados de 'andando' e 'parado' mantendo a última direção do herói.

---

## 📂 Estrutura de Pastas

Para o funcionamento correto do motor **Pygame Zero**, os arquivos devem estar organizados da seguinte forma:

```text
📁 shadow_jumper/
│
├── 📄 main.py              # Código fonte do jogo
├── 📁 images/              # Pasta de ativos gráficos
│   ├── background.png      # Fundo (800x600)
│   ├── hero_idle_r1.png, hero_idle_r2.png (e versões _l1, _l2)
│   ├── hero_walk_r1.png, hero_walk_r2.png (e versões _l1, _l2)
│   └── enemy_walk_right1.png, enemy_walk_left1.png (frames do inimigo)
└── 📁 sounds/              # Pasta de ativos de áudio
    ├── background_theme.wav # Música de fundo
    ├── jump.wav            # Efeito de pulo
    └── hit.wav             # Efeito de colisão/dano
