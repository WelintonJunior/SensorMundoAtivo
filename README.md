
# Exoesqueleto Humano - Detecção de Pose e Limite de Ângulos

Este projeto utiliza a biblioteca **MediaPipe** para detecção de pose humana em tempo real, com o objetivo de monitorar os ângulos das articulações e alertar visualmente quando esses ângulos ultrapassarem limites definidos.

## Funcionalidades

- **Detecção de Pose**: A detecção de pontos articulares, como ombro, cotovelo, punho, quadril, joelho e tornozelo, em tempo real utilizando a câmera do computador.
- **Cálculo de Ângulo**: Cálculo do ângulo entre três pontos articulares (ex: ombro, cotovelo e punho) e verificação se o ângulo está dentro dos limites definidos.
- **Notificação Visual**: Caso o ângulo ultrapasse o limite, o código altera a cor da linha conectando os pontos para um alerta visual.
- **Ajuste de Parâmetros de Imagem**: A imagem da câmera pode ser ajustada em termos de brilho e nitidez para melhorar a visualização.

## Requisitos

Antes de executar o código, é necessário instalar as dependências. Crie um ambiente virtual (opcional, mas recomendado) e instale as dependências listadas abaixo.

### Instalação das Dependências

1. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    ```

2. Ative o ambiente virtual:
    - Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - Linux/Mac:
      ```bash
      source venv/bin/activate
      ```

3. Instale as dependências necessárias:
    ```bash
    pip install opencv-python mediapipe numpy
    ```

### Arquivo de Configuração `conf.json`

O código requer um arquivo de configuração **`conf.json`** para definir os limites angulares das articulações.

Exemplo de `conf.json`:

```json
{
    "braco_direito": 160,
    "braco_esquerdo": 160
}
```

### Parâmetros Configuráveis

- **ALPHA**: Fator de ajuste de brilho da imagem.
- **BETA**: Fator de ajuste de contraste da imagem.
- **SHARPEN_KERNEL**: Filtro de nitidez aplicado à imagem.

Estes parâmetros estão definidos no código e podem ser ajustados conforme a necessidade.

## Como Executar

1. Certifique-se de que a câmera do seu computador esteja funcionando corretamente.
2. Certifique-se de ter o arquivo `conf.json` no mesmo diretório que o script Python.
3. Execute o script Python:

    ```bash
    python app.py
    ```

### Controle de Execução

- O programa irá exibir uma janela com a captura de vídeo da sua webcam.
- A qualquer momento, pressione a tecla **`q`** para sair do programa.

## Como Funciona

- O código utiliza a biblioteca **MediaPipe** para capturar os pontos articulares do corpo humano. Ele calcula o ângulo formado entre três pontos selecionados (por exemplo, entre o ombro, cotovelo e punho) e verifica se esse ângulo ultrapassa os limites definidos no arquivo `conf.json`.
- Se o ângulo ultrapassar o limite, o código alterará a cor da linha conectando os pontos articulares para **vermelho**, indicando que o movimento ultrapassou o limite.
- A cada quadro, a taxa de **FPS (Frames por Segundo)** é calculada e exibida na tela.
- Os pontos articulares são desenhados na tela com a numeração correspondente a cada ponto, para facilitar a visualização e depuração.

## Personalização

Você pode facilmente personalizar o código para:
- **Adicionar mais articulações e ângulos** para monitoramento, basta adicionar mais entradas no arquivo `conf.json` e ajustar os pontos de conexão no código.
- **Ajustar os limites angulares** para cada articulação, alterando os valores no arquivo `conf.json`.

## Exemplo de Execução

![Exemplo de Execução](./screenshots/exemplo.jpg) (adicionar captura de tela, se necessário)

