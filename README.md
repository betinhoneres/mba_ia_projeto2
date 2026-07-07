# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

Este repositório contém a implementação completa do desafio de automação, refatoração e avaliação de prompts utilizando o **LangChain** e o **LangSmith Prompt Hub**. O principal objetivo deste projeto é otimizar um prompt inicial de baixa qualidade (`v1`), responsável por transformar relatos brutos de bugs em **User Stories** altamente estruturadas e prontas para o desenvolvimento ágil, atingindo uma pontuação mínima de **0.8 (80%)** em todas as métricas estabelecidas pelo PRD.

---

## Técnicas Aplicadas (Fase 2)

Para elevar a qualidade das respostas e mitigar ambiguidades ou alucinações de formato do modelo original (`v1`), a versão otimizada em `prompts/bug_to_user_story_v2.yml` incorporou as seguintes técnicas avançadas de Engenharia de Prompts:

1. **Role Prompting (Definição de persona)**
   * *Justificativa*: São personas que tem conhecimento tecnico e do negocio, esse contexto garante um vocabulario técnico apropriado do framework Scrum e garante foco no valor de negócio e no impacto ao usuário final.

2. **Few-shot Learning (Aprendizado com exemplos)**
   * *Como foi aplicado*: Foram incluídos dois exemplos detalhados de exemplos reais de entradas (relato de bug bruto) e saídas idealmente esperadas.
   * *Justificativa*: Com essa técnica busquei fixar o formato exato da resposta esperado, e guiar o LLM em relação à densidade de detalhes exigida nos critérios de aceite.

3. **Chain of Thought (CoT - Cadeia de Raciocínio)**
   * *Como foi aplicado*: O prompt força o modelo a preencher a seção `# Análise do Bug (Pensamento Passo a Passo)` identificando explicitamente o problema real por trás do sintoma e medindo o impacto no negócio antes de gerar a User Story.
   * *Justificativa*: Decompor o problema logicamente antes de escrever a solução melhora drasticamente as métricas de corretude (*Correctness*) e precisão (*Precision*), simulando o fluxo de pensamento real de um analista humano.

4. **Markdown Formatting (Estruturação Rigorosa)**
   * *Como foi aplicado*: Definição estrita das seções obrigatórias (`# Análise do Bug`, `# User Story`, `# Critérios de Aceite`) e do padrão Gherkin BDD (*Dado-Quando-Então*).
   * *Justificativa*: Garante previsibilidade na saída estruturada, facilitando o consumo posterior das informações e elevando o índice de clareza (*Clarity*).

---

## 📊 Resultados Finais

* **Link Público do Dashboard LangSmith**: *[Insira aqui o link público que você gerará ao final da execução]*

### Tabela Comparativa de Desempenho

Abaixo está o comparativo entre o comportamento esperado/obtido entre o prompt inicial (`v1`) e o prompt refatorado (`v2`):

| Métrica | Prompt Base (v1) | Prompt Otimizado (v2) | Meta Mínima | Status Final |
| :--- | :---: | :---: | :---: | :---: |
| **Helpfulness** | ~0.45 ✗ | *[Preencher]* | 0.80 | **Aguardando Run** |
| **Correctness** | ~0.52 ✗ | *[Preencher]* | 0.80 | **Aguardando Run** |
| **F1-Score** | ~0.48 ✗ | *[Preencher]* | 0.80 | **Aguardando Run** |
| **Clarity** | ~0.50 ✗ | *[Preencher]* | 0.80 | **Aguardando Run** |
| **Precision** | ~0.46 ✗ | *[Preencher]* | 0.80 | **Aguardando Run** |
| **MÉDIA GERAL** | ~0.48 ✗ | *[Preencher]* | 0.80 | **Aguardando Run** |

> **Nota de Validação**: *As notas definitivas do prompt v2 serão atualizadas nesta tabela assim que o script `src/evaluate.py` concluir a rodada de avaliação atual contra os 15 cenários de teste.*

---

## 💻 Como Executar

### Pré-requisitos
* Python 3.9 ou superior instalado.
* Conta ativa na OpenAI (com créditos para API) ou Google AI Studio.
* Conta configurada no LangSmith.

### 1. Configuração do Ambiente e Instalação
Clone o seu repositório, configure e ative o ambiente virtual (`venv`), instalando as dependências obrigatórias: