# 🌡️ Lab Environmental & System Monitor

Sistema avançado de monitoramento ambiental e de saúde de hardware integrado com **Supabase**, **Chart.js** e **Análise Automática de Dados**.

## 🚀 Funcionalidades Principais

- **Monitoramento Ambiental:** Temperatura (°C) e Humidade (%) em tempo real.
- **Saúde do Sistema:** Monitoramento da temperatura da CPU do Raspberry Pi.
- **💡 Insights Inteligentes:** Motor de análise que gera diagnósticos automáticos sobre o clima e a segurança do hardware.
- **Gráficos Multi-Eixo:** Visualização de 3 variáveis simultâneas com escalas independentes.
- **Filtros Temporais:** Alternância dinâmica entre visões Diária, Semanal e Mensal.

## 🛠️ Arquitetura do Sistema

```mermaid
graph TD
    A[Raspberry Pi + Sensores] -->|Temp + Hum + CPU| B(Supabase DB)
    B -->|Real-time API| C[Site / GitHub Pages]
    subgraph Frontend - Análise
        C --> D[Chart.js - 3 Variáveis]
        C --> E[Smart Insights - Diagnóstico]
        C --> F[Dashboard de Métricas]
    end
    subgraph Períodos
        G[Diário] --- C
        H[Semanal] --- C
        I[Mensal] --- C
    end
```

## 📋 Como Configurar

1. **Banco de Dados:**
   - Configure a tabela `temperatura_quarto` no Supabase (ver `ARCHITECTURE.md`).
   - Aplique as políticas de RLS para acesso público.

2. **Frontend:**
   - Configure sua `SUPABASE_URL` e `ANON_KEY` no arquivo `sensor1.html`.
   - Hospede no GitHub Pages para acesso remoto.

3. **Raspberry Pi:**
   - Utilize o script Python (exemplo em `ARCHITECTURE.md`) para enviar os dados.

---
Desenvolvido por **Fernando** | 2026
