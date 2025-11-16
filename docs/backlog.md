# 📅 Backlog do Produto
Lista de histórias de usuário e critérios de aceitação do projeto *Exoplanet Detector System*.

| ID   | História do Usuário | Critérios de Aceitação | Prioridade |
|------|----------------------|-------------------------|------------|
| US01 | Como pesquisador, quero enviar ou baixar curvas de luz, para analisá-las. | O sistema deve carregar a curva e mostrar um preview. | Alta |
| US02 | Como analista, quero pré-processar curvas de luz, para deixá-las limpas e normalizadas. | Os dados devem ser salvos em `data/processed/` e sem ruídos óbvios. | Alta |
| US03 | Como cientista, quero aplicar o algoritmo BLS, para identificar possíveis trânsitos. | O sistema deve gerar lista de períodos candidatos e gráfico BLS. | Alta |
| US04 | Como cientista, quero classificar possíveis trânsitos com ML, para automatizar a análise. | O modelo deve retornar uma confiança ou label. | Média |
| US05 | Como usuário, quero visualizar gráficos claros, para interpretar os resultados facilmente. | Gráficos devem ser exibidos em notebooks. | Média |
| US06 | Como usuário, quero uma interface simples (opcional), para usar o sistema sem precisar de código. | Uma interface mínima deve permitir upload e análise. | Baixa |

## Épicos

- **EP01 — Coleta e Organização de Dados**
- **EP02 — Pré-processamento**
- **EP03 — Detecção de Trânsitos (BLS)**
- **EP04 — Classificação com Machine Learning**
- **EP05 — Visualização dos Resultados**
- **EP06 — Interface do Usuário (Opcional)**