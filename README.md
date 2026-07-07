# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

## Objetivo

Este projeto tem como objetivo realizar o ciclo completo de engenharia e avaliação de prompts utilizando LangChain e LangSmith.

O desafio consiste em:

- Fazer pull de prompts de baixa qualidade disponíveis no LangSmith Prompt Hub;
- Refatorar e otimizar esses prompts utilizando técnicas avançadas de Prompt Engineering;
- Fazer push dos prompts otimizados para o LangSmith;
- Avaliar os prompts utilizando métricas automáticas;
- Atingir pontuação mínima de 0.8 em todas as métricas definidas pelo projeto.

O prompt utilizado neste trabalho transforma relatos de bugs em User Stories estruturadas para uso em processos ágeis de desenvolvimento.

---

# Técnicas Aplicadas (Fase 2)

## 1. Role Prompting

Foi definida a seguinte persona:

> Product Manager Sênior

### Justificativa

Essa abordagem permite que o modelo assuma um contexto profissional alinhado à transformação de bugs em User Stories orientadas ao negócio.

### Benefícios

- Maior consistência das respostas;
- Melhor alinhamento com práticas Scrum e Agile;
- Maior foco no impacto ao usuário final;
- Melhor contextualização dos requisitos funcionais.

---

## 2. Few-shot Learning

Foram adicionados exemplos completos de entrada e saída.

### Como foi aplicado

O prompt contém exemplos reais de:

- Erro de Login Google;
- Erro 500 ao salvar formulário;
- Perda de dados ao atualizar página.

### Benefícios

- Maior aderência ao formato esperado;
- Redução de ambiguidades;
- Melhor consistência entre as respostas;
- Aumento da precisão.

---

## 3. Chain of Thought (CoT)

Foi incorporado um fluxo de raciocínio explícito para orientar a análise do bug antes da geração da User Story.

### Etapas utilizadas

1. Identificar o erro relatado;
2. Identificar o usuário impactado;
3. Avaliar o impacto causado;
4. Determinar o comportamento esperado;
5. Construir a User Story;
6. Gerar critérios de aceitação testáveis.

### Benefícios

- Melhor interpretação do problema;
- Aumento da corretude;
- Melhor alinhamento com os exemplos do dataset;
- Maior qualidade dos critérios de aceitação.

---

## 4. Estruturação de Saída

Foi definido um formato obrigatório com:

- Título;
- Contexto;
- User Story;
- Critérios de Aceitação.

### Benefícios

- Respostas mais padronizadas;
- Maior clareza;
- Melhor desempenho nas métricas automáticas;
- Facilidade de leitura por Product Owners e equipes de desenvolvimento.

---

# Prompt Otimizado

Prompt desenvolvido:

```text
prompts/bug_to_user_story_v2.yml
```

Técnicas utilizadas:

- Role Prompting
- Few-shot Learning
- Chain of Thought
- Estruturação de Saída
- Tratamento de Edge Cases

---

# Resultados Finais

Após as iterações de refinamento e avaliação, o prompt atingiu os requisitos mínimos definidos pelo desafio.

## Métricas Obtidas

| Métrica | Resultado |
|----------|----------|
| Helpfulness | 0.89 |
| Correctness | 0.84 |
| F1-Score | 0.80 |
| Clarity | 0.89 |
| Precision | 0.89 |

## Média Geral

```text
0.8615
```

## Status Final

```text
✅ APROVADO
```

Todas as métricas ficaram iguais ou superiores ao limite mínimo de 0.80.

---

## Resultado da Avaliação

```text
Métricas Derivadas:
- Helpfulness: 0.89 ✓
- Correctness: 0.84 ✓

Métricas Base:
- F1-Score: 0.80 ✓
- Clarity: 0.89 ✓
- Precision: 0.89 ✓

Média Geral: 0.8615

STATUS: APROVADO
```

---

# Comparação v1 x v2

| Aspecto | Prompt v1 | Prompt v2 |
|----------|----------|----------|
| Persona definida | Não | Sim |
| Few-shot Learning | Não | Sim |
| Chain of Thought | Não | Sim |
| Critérios de Aceitação | Básicos | Detalhados |
| Edge Cases | Não | Sim |
| Estrutura de Saída | Inconsistente | Padronizada |
| Clareza | Baixa | Alta |
| Resultado Final | Reprovado | Aprovado |

---

# Evidências no LangSmith

## Dashboard LangSmith

**https://smith.langchain.com/prompts/bug_to_user_story_v2?organizationId=9831f73f-775f-44dc-9eb5-7715cb661cc8**

Ou utilizar screenshots das execuções conforme solicitado.


# Estrutura do Projeto

```text
mba-ia-pull-evaluation-prompt/
│
├── prompts/
│   ├── bug_to_user_story_v1.yml
│   └── bug_to_user_story_v2.yml
│
├── datasets/
│   └── bug_to_user_story.jsonl
│
├── src/
│   ├── pull_prompts.py
│   ├── push_prompts.py
│   ├── evaluate.py
│   ├── metrics.py
│   └── utils.py
│
├── tests/
│   └── test_prompts.py
│
├── requirements.txt
├── README.md
└── .env
```

---

# Como Executar

## 1. Criar ambiente virtual

```bash
python -m venv venv
```

## 2. Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

---

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 4. Fazer Pull do Prompt

```bash
python src/pull_prompts.py
```

---

## 5. Fazer Push do Prompt Otimizado

```bash
python src/push_prompts.py
```

---

## 6. Executar Avaliação

```bash
python src/evaluate.py
```

---

# Conclusão

O prompt original foi completamente refatorado utilizando técnicas avançadas de Prompt Engineering.

A combinação de Role Prompting, Few-shot Learning e Chain of Thought possibilitou elevar significativamente a qualidade das User Stories geradas.

O resultado final atingiu todos os critérios mínimos estabelecidos no desafio, superando a meta de 0.80 em todas as métricas avaliadas e alcançando média geral de 0.8615.