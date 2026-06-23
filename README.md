# Python Packet Sniffer

> **Nota:** Este script foi desenvolvido exclusivamente para sistemas **Linux** e requer privilégios de superusuário (`sudo`).

## Como Executar

Certifique-se de estar no diretório do projeto antes de rodar os comandos:
```bash
cd Python-Packet-Sniffer
```

### 1. Execução Padrão (Sem Filtros)
Captura e exibe todos os pacotes em tempo real:
```bash
sudo python3 sniffer.py
```

### 2. Execução com Filtros (QUIC)

* **Filtrar pacotes QUIC (Long e Short Headers):**
  ```bash
  sudo python3 sniffer.py | grep -e "QUIC Packet (Long)" -e "QUIC Packet (Short)" -A5
  ```

* **Filtrar apenas QUIC Short Headers (Próximas 5 linhas):**
  ```bash
  sudo python3 sniffer.py | grep -A5 "QUIC Packet (Short)"
  ```

* **Filtrar apenas QUIC Long Headers (Próximas 5 linhas):**
  ```bash
  sudo python3 sniffer.py | grep -A5 "QUIC Packet (Long)"
  ```

### 3. Verificar Relatórios QUIC
  **Colar em outro terminal**
  ```bash
  watch -n 1 cat quic_stats.txt
  ```