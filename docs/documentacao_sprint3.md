# Sprint 3 – Implementação do BLS com dados TCE

Nesta sprint foi implementado o algoritmo Box Least Squares (BLS) aplicado a estrelas que possuem eventos TCE registrados pela missão Kepler.

O objetivo é verificar se o BLS reproduz o período encontrado pelo pipeline automático da NASA.

Etapas:
1. Seleção de um TCE com período válido
2. Download da curva de luz correspondente usando Lightkurve
3. Execução do BLS em um intervalo próximo ao período do TCE
4. Comparação entre:
   - período do catálogo (TCE Period)
   - período detectado pelo BLS
5. Geração do gráfico da força do sinal (BLS Power)

Resultados esperados:
- Confirmar que o BLS encontra um período próximo ao do TCE
- Detectar discrepâncias que indiquem ruído ou falsos positivos
- Visualizações que demonstrem claramente o sinal
