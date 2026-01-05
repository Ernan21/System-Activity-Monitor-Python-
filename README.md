# 🕵️‍♂️ System Activity Monitor (Python)

## 📌 Descrição

Este projeto é um **monitor de atividades do sistema**, desenvolvido em Python, capaz de registrar em tempo real:

* ⌨️ Teclas pressionadas
* 🖥️ Processos iniciados e encerrados
* 📁 Alterações em arquivos e diretórios
* 📸 Captura periódica de telas (opcional)

O objetivo do projeto é **auditoria, estudo de comportamento do sistema e automação**, sendo indicado para **ambientes controlados**, **laboratórios**, **pesquisa** ou **uso educacional**.

---

## 🚀 Funcionalidades

### ⌨️ Monitoramento de Teclado

* Registra teclas pressionadas
* Diferencia teclas normais e especiais
* Log com data e hora

### 🖥️ Monitoramento de Processos

* Detecta processos iniciados
* Detecta processos encerrados
* Baseado em varredura periódica do sistema

### 📁 Monitoramento de Arquivos

* Detecta:

  * Criação
  * Modificação
  * Exclusão
  * Movimentação de arquivos
* Pode monitorar diretórios de forma recursiva

### 📸 Captura de Tela (Opcional)

* Capturas automáticas em intervalos definidos
* Salvamento organizado por timestamp
* Função desativada por padrão (comentada)

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.9+**
* `pynput` — captura de teclado
* `psutil` — monitoramento de processos
* `pyautogui` — captura de tela
* `watchdog` — monitoramento de sistema de arquivos
* `threading` — execução paralela
* `datetime` — controle de tempo

---

## 📁 Estrutura do Projeto

```text
📦 system-activity-monitor
 ┣ 📄 main.py
 ┣ 📄 activity_log.txt
 ┣ 📁 screenshots/
 ┗ 📄 README.md
```

---

## ⚙️ Configurações

No código, é possível ajustar os intervalos:

```python
screenshot_timer = 1   # segundos entre screenshots
logfile_timer = 5      # intervalo de logs de processos
```

Para ativar a captura de tela, basta **descomentar**:

```python
Thread(target=capture_screenshots, daemon=True).start()
```

---

## 📦 Instalação

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/system-activity-monitor.git
cd system-activity-monitor
```

### 2️⃣ Instale as dependências

```bash
pip install pynput psutil pyautogui watchdog
```

---

## ▶️ Como Executar

```bash
python main.py
```

O script irá:

* Criar o arquivo `activity_log.txt`
* Criar a pasta `screenshots/` (se não existir)
* Iniciar o monitoramento em segundo plano

---

## ⚠️ Aviso Legal

> ⚠️ **Uso Responsável**
>
> Este projeto **não deve ser utilizado sem o consentimento explícito do usuário ou administrador do sistema**.
>
> O autor **não se responsabiliza** por uso indevido, ilegal ou antiético deste software.
>
> Recomendado apenas para:
>
> * Estudos
> * Ambientes controlados
> * Auditoria autorizada
> * Aprendizado de Python e automação

---

## 📌 Possíveis Melhorias Futuras

* [ ] Logs estruturados (JSON)
* [ ] Interface gráfica
* [ ] Configuração via arquivo `.env`
* [ ] Criptografia dos logs
* [ ] Serviço em segundo plano (Windows/Linux)

---

## 👨‍💻 Autor

**Ernando Freitas**
💻 Python • Automação • Sistemas 📍 Brasil

