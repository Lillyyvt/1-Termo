Copiar código
╔══════════════════════════════════════════════════════╗
║  🎵 REQUIREMENTS SUNSET SYMPHONY - FULL EDITION 🎵  ║
║  Funcional + Não Funcional + Ágil + Prototipagem     ║
║        Diagramas + Brainstorm + Entrevistas          ║
╚══════════════════════════════════════════════════════╝

🎯 REQUISITOS FUNCIONAIS (RF)
✅ O QUE O SISTEMA FAZ 🎵 Exemplo App Pedidos

├── RF01: Cadastrar usuário
├── RF02: Fazer pedido online  
├── RF03: Pagar com PIX/Cartão
├── RF04: Rastrear entrega
├── RF05: Consultar histórico pedidos
└── RF06: Avaliar entregas
📝 FORMATO :RF-ID + Verbo + Objeto

#  　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

⚡ REQUISITOS NÃO FUNCIONAIS (RNF)
🚀 COMO O SISTEMA FUNCIONA

├── RNF01: Resposta < 2s (performance)
├── RNF02: 99,9% uptime (disponibilidade)
├── RNF03: Suporta 10 mil usuários simultâneos
├── RNF04: HTTPS + JWT (segurança)
├── RNF05: Responsivo mobile-first (UX)
└── RNF06: Acessibilidade WCAG 2.1 (inclusão)

#  　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

🧠 TÉCNICAS DE LEVANTAMENTO DE REQUISITOS
🎤 ENTREVISTAS

👥 PERFIS ENTREVISTADOS:
├── Cliente Final (5 pessoas)
├── Gerente Restaurante (2 pessoas)  
├── Entregador (3 pessoas)
└── Administrador (1 pessoa)

📋 PERGUNTAS TÍPICAS:
"Qual maior dor no pedido atual?"
"Como prefere acompanhar entrega?"
"O que falta no app concorrente?"

#  　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

💡 BRAINSTORMING

🎯 RESULTADOS TOP 5:
1. Notificação push tempo real
2. Cupom de desconto inteligente
3. Chat com suporte no app
4. Mapa interativo entregador
5. Recomendação por histórico

#  　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

📐 DIAGRAMAS
📊 CASO DE USO (UML)

Copiar código
Cliente ──(autentica)──> Sistema
         ──(faz pedido)──┤
         ──(paga)───────┤
         ──(rastreia)───

#  　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

🔄 PRINCIPAL DO FLUXOGRAMA

[Login] → [Catálogo] → [Carrinho] 
     ↓
[Pagamento] → [Confirmação] → [Rastreio]

#  　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

📱 WIREFRAMES (Prototipagem)

Tela 1: Login (Email/Senha/Google)
Tela 2: Catálogo (Grid + Filtros)
Tela 3: Carrinho (Qtd + Cupom)
Tela 4: Pagamento (PIX/Cartão)
Tela 5: Rastreio (Mapa + ETA)

#  　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

🥁 METODOLOGIAS ÁGEIS

📋 SCRUM (2 semanas/sprint)
├── 📅 Planejamento Sprint (2h)
├── ✅ Daily (15min 10h)
├── 📈 Review (1h sexta)
├── 🔄 Retrospectiva (1h)
└── 📋 Backlog Produto (Jira/Trello)

#  　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

🎯 KANBAN
┌─────────────┬──────────┬──────────┐
│   To Do     │  Doing   │   Done   │
├─────────────┼──────────┼──────────┤
│ RF01 Login  │ RF03 Pix │ RF01 ✓   │
│ RF02 Cat.   │ RF04 Map │ RF02 ✓   │
└─────────────┴──────────┴──────────┘

#  　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

🎸 GERAÇÃO DE PROJETO


👑 PAPÉIS:
├── 🧑‍💼 Product Owner (define prioridade)
├── 🤹 Scrum Master (remove impedimentos)
└── 👨‍💻 Dev Team (3 Frontend + 2 Backend)

📊 ARTEFATOS:
├── 📋 Product Backlog (MoSCoW priorizado)
├── 🎯 Sprint Backlog (tarefas 1-8h)
└── 📈 Burndown Chart (progresso diário)

#  　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

⏱️ CERIMÔNIAS:
- Daily: Seg-Ven 10h (15min)
- Planning: Seg 9h (2h)
- Review: Sex 16h (1h)
- Retro: Sex 17h (1h)

#  　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

📚 DOCUMENTAÇÃO ÁGIL
📄 HISTÓRIAS DE USUÁRIOS COMPLETAS

Como [CLIENTE] quero [FUNÇÃO] para [BENEFÍCIO]

✅ RF01: Como cliente quero me cadastrar para acessar histórico
✅ RF02: Como cliente quero ver catálogo para escolher rápido
✅ RF03: Como cliente quero pagar PIX para receber instantâneo
✅ RF04: Como cliente quero rastrear para saber hora exata

#  　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

📊 DEFINIÇÃO DE PRONTA (INVESTIR)

✅ I - Independente (funciona sozinho)
✅ N - Negociável (pode ajustar)
✅ V - Valioso (traz benefício)
✅ E - Estimável (Story Points: 1,2,3,5,8)
✅ S - Pequeno (máx 8h esforço)
✅ T - Testável (criterios aceitação)

#  　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ　ﾟ･｡･ﾟ

🎨 PROTOTIPAGEM & VALIDAÇÃO
o
🔍 FERRAMENTAS:
├── Figma (Wireframes Hi-Fi)
├── MarvelApp (Protótipo clicável)
└── UserTesting (Validação 5 users)

📊 MVP (Minimum Viable Product):
Sprint 1: RF01 + RF02 + Login
Sprint 2: RF03 + RF04 Pagamento
Sprint 3: RF05 + RF06 Histórico


╔══════════════════════════════════════════════════════╗
║  🎵 SUNSET SYMPHONY - REQUIREMENTS COMPLETE 🎵      ║
║ ☀️Funcional + Não Funcional + Ágil + Prototipagem ☀️║
║  Diagramas + Brainstorm + Entrevistas + Docs Prontas ║
╚══════════════════════════════════════════════════════║