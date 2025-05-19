# 📌 Sistema de Recuperação de Informações usando VectorDB e RetrievalQA
Esse repositório é referente a AV5 da matéria de TASI 1, contendo um script Python que utiliza embenddings e um VectorDB para responder perguntas. Esse sitema integra a biblioteca LangChain e o módulo RetrivalQA.
- Lembrar de retirar as aspas simples '' na execução dos codigos no terminal.

## 😭 Observação importante!
Professor, eu simplesmente não consegui executar meu código pois meu PC não tem memória RAM suficiente pra isso, aparece essa mensagem:
ollama._types.ResponseError: model requires more system memory (5.6 GiB) than is available (4.3 GiB) (status code: 500)
Eu testei 4 modelos diferentes (llama3, mistral, nomic/mini e phi3:mini) mas meu PC não tanka nenhum deles, então não tenho nenhum vídeo de demonstração e não sei quais erros tem na execução do script... Mas como eu tive muita dificuldade em fazer essa atividade e ralei muito, estou entregando aqui!
Espero que entenda D=


## 🔧 Pré-requisitos!
- Ollama instalado (https://ollama.com/download)
- Ter o modelo LLM "phi3:mini" instalado na máquina (rode no terminal 'ollama pull phi3:mini').
- Modelo 'nomic-embed-text' baixado (rode no terminal 'ollama pull nomic-embed-text').
- Bibliotecas do langchain, faiss e pypdf baixados (rode no terminal 'pip install langchain langchain-community langchain-ollama faiss-cpu pypdf').
- Python 3 + pip.


## 🚀 Como executar?
1. Quando instalamos o Ollama ele começa a rodar em segundo plano automaticamente, para verificar execute no seu terminal 'ollama list', deve aparecer informações como o nome do modelo, a memória utilizada e a última modificação feita. Caso não apareça nenhuma dessas informações, inicie o Ollama executando no seu terminal 'ollama serve'.
Baixe o arquivo 'av3_script.py'.
2. Baixe o arquivo 'av5_script.py'.
3. Abra no terminal o diretório onde o arquivo .py está localizado: 'cd C:/Users/seu_user/.........'.
4. Execute o arquivo .py no terminal: 'python av5_script.py'.