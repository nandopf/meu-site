# Arquitetura do Projeto - Monitoramento de Temperatura

Este documento descreve o fluxo de dados e a estrutura técnica do sistema de monitoramento de temperatura.

## 🏗️ Estrutura Geral

O projeto é baseado em uma arquitetura **Serverless** utilizando o Supabase como Backend as a Service (BaaS) e um Frontend estático.

### 1. Camada de Dados (Backend)
- **Provedor:** Supabase (PostgreSQL).
- **Tabela:** `temperatura_quarto`.
- **Campos:**
  - `id` (int8, Primary Key)
  - `created_at` (timestamp, default: now())
  - `temperatura` (float8)
  - `humidade` (float8)
  - `cpu_temp` (float8)
- **Segurança:** RLS (Row Level Security) habilitado com política de leitura pública para usuários `anon`.

### 2. Camada de Apresentação (Frontend)
- **Tecnologias:** HTML5, CSS3, JavaScript (ES6+).
- **Bibliotecas Externas:**
  - `supabase-js`: Comunicação com o banco de dados.
  - `Chart.js`: Renderização de gráficos multi-eixo.
- **Componentes:**
  - **Tabs de Filtro:** Diária, Semanal, Mensal e Total.
  - **Summary Cards:** Temp. Ambiente, Humidade e Saúde do Sistema (CPU Temp).
  - **Smart Insights:** Motor de análise lógica que gera diagnósticos técnicos automáticos baseados nas métricas do período.
  - **Gráfico de Linha Triplo:** Visualização simultânea de temperatura ambiente, humidade e temperatura da CPU.

## 🔄 Fluxo de Dados (Workflow)

1.  **Ingestão (Arduino/Simulação):** Os dados são inseridos na tabela `temperatura_quarto` no Supabase via API REST.
2.  **Requisição:** Ao abrir o site ou trocar de aba, o JavaScript dispara uma query filtrada para o Supabase.
3.  **Processamento:** O Frontend recebe o JSON de resposta e calcula as métricas (min/max/avg).
4.  **Renderização:** 
    - O `Chart.js` desenha a curva de temperatura.
    - O DOM é atualizado com os novos valores nos cartões e na tabela.
5.  **Atualização:** Um timer (`setInterval`) repete esse fluxo a cada 60 segundos automaticamente.

## 📂 Organização de Arquivos

- `index.html`: Página inicial com menu de navegação.
- `sensor1.html`: Dashboard principal com gráficos e filtros.
- `style.css`: Estilização global e componentes UI modernos.
- `teste_bd.html`: Ferramenta de diagnóstico para testar conectividade.
- `ARCHITECTURE.md`: Este documento de documentação.

## 🚀 Escalabilidade
A arquitetura foi projetada para ser modular. Novos projetos (como o Fermentador, Hidroponia e Irrigação de Lúpulo) utilizarão o mesmo ecossistema Supabase, apenas criando novas tabelas e painéis frontend específicos, mantendo a centralização dos dados.

---
*Atualizado em: 01 de Maio de 2026*
