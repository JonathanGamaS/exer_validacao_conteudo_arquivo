# Teste

Baseado nas regras propostas, criei um arquivo .txt com várias entradas. A aplicação se encarrega de ler o arquivo, eliminar os registro que não são necessários e retornar uma lista com os registros no layout definido.

### Descrição do fluxo da aplicação

* O fluxo se inicia na "função verificando_arquivo_retornando_validos", ela quem vai receber o conteúdo do arquivo, e enviar para a função "verificador_dados";
* A função "verificador_dados" é a função principal, que vai guiar a outras funções que fazem cumprir as regras propostas no teste. Abaixo a descrição de cada função verificadora que está no fluxo de "verificar_dados":
* validando_numero_oferecido - Verifica se o numero de telefone é válido, verificando todas as regras propostas no teste. 
* verificador_tamanho_mensagem - Verifica se o tamanho da mensagem não é maior que o valor permitido.
* verificador_tempo - Verifica se o horário esta dentro do horário acertado para ser válido.
* verificar_retornar_id_broker - Verifica e retorna o nome da operadora vinculada a valor vindo do arquivo.
* verificador_black_list - Acessa o endpoint disponibilizado para averiguar se o número de telefone está na blacklist.
* Após as devidas verificações, os registros que retornam da função "verificador_dados" é enviado a função "verificando_duplicidade_mensagem", ela verifica mais de um registro para o mesmo número, e deixa somente um para cada numero, além de formatar para o layout final desejado e inserir os registros numa fila.

### Testes Unitários

* Desenvolvi dois testes unitários, um que verifica o fluxo da aplicação e se a saída esta vindo como uma lista. E outro que verifica se a aplicação lança uma exception caso o arquivo possua um conteúdo inválido para uso.


### Como executar

* Deixei adaptado o arquivo que criei para executar a aplicação, é necessário somente executar o arquivo orchestration na pasta code. 
* Lembrando que foi construido dessa maneira pois é uma execução local. No caso de um ambiente serverless Amazon por exemplo, seria necessário adaptar para receber o evento, se viria via front ou de um trigger do s3.


### Como executar os testes

* Os testes foram feitos com base no unnitest, sendo necessário somente executar o arquivo test_fluxo_verificador_dados_arquivo.py


### Descrição de linguagem, IDE, libs e etc

* A linguagem utilizada foi python, é a que possuo mais experiência para resolver o teste.
* IDE utilizada foi o Pycharm, é a IDE que utilizo a mais de dois anos, e atende todas minhas necessidades, principalmente para testes locais em aplicações serverless.
* Em questão de libs, utilizei datetime para comparar os horários. Requests para acessar o endpoint disponível que informa se o número de telefone esta na blacklist. E Unnitest para os testes unitários.


