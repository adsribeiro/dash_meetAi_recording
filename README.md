# Aplicativo Web de Gravação e Resumo de Reuniões

Este é um projeto de um aplicativo web desenvolvido em Python utilizando o framework Dash. O objetivo do aplicativo é gravar o áudio de reuniões, converter o áudio em texto utilizando inteligência artificial e, em seguida, processar o texto para gerar um resumo da reunião em tópicos. Além disso, o aplicativo permite gravar o arquivo de áudio original e o resumo em formato PDF em um banco de dados NoSQL.

## Funcionalidades

### 1. Gravar Áudio das Reuniões

O aplicativo permite iniciar e parar a gravação do áudio das reuniões. Os usuários podem iniciar a gravação antes do início da reunião e pará-la quando a reunião for concluída.

### 2. Conversão de Áudio em Texto

Após a gravação do áudio, o aplicativo utiliza inteligência artificial para converter o áudio em texto. Isso permite que o conteúdo da reunião seja processado de forma mais eficiente.

### 3. Resumo da Reunião em Tópicos

O texto resultante da conversão do áudio é processado para gerar um resumo da reunião em tópicos. O resumo destaca os principais pontos discutidos durante a reunião, facilitando a revisão e o entendimento do conteúdo.

### 4. Armazenamento em Banco de Dados NoSQL

Tanto o arquivo de áudio original quanto o resumo da reunião em formato PDF são armazenados em um banco de dados NoSQL. Isso permite que os usuários acessem e visualizem facilmente o conteúdo das reuniões anteriores.

## Tecnologias Utilizadas

- Python
- Dash (framework web)
- PyAudio (gravação de áudio)
- API de reconhecimento de fala (para conversão de áudio em texto)
- Inteligência Artificial (para processamento de texto e geração de resumo)
- Banco de dados NoSQL (para armazenamento de arquivos de áudio e resumos)

