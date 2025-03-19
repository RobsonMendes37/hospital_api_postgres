# Hospital Persistência

Este projeto implementa a configuração e a criação de tabelas em um banco de dados PostgreSQL para um sistema hospitalar. A aplicação utiliza Python com FastApi e a biblioteca psycopg2 para conectar e interagir com o banco de dados, criando as tabelas necessárias para gerenciar informações de pacientes, sintomas, médicos, remédios e receitas.






### Descrição das Tabelas

- *paciente*: Armazena informações dos pacientes (id, nome, idade)
- *sintoma*: Registra sintomas e seus tratamentos (id, nome, tratamento)
- *paciente_sintoma*: Tabela de relacionamento entre pacientes e sintomas
- *medico*: Armazena informações dos médicos (id, nome, idade)
- *remedio*: Registra informações sobre medicamentos (id, nome, data_fabricacao, data_validade, prescricao)
- *receita*: Relaciona médicos, remédios e pacientes (id, medico_id, remedio_id, paciente_id)

### Tecnologias Utilizadas

- Python
- PostgreSQL
- psycopg2
- FastAPI para rotas
- SQLAlchemy 

## Estrutura do Projeto
![Imagem do WhatsApp de 2025-03-19 à(s) 06 18 39_f7248890](https://github.com/user-attachments/assets/df38ec52-7f8a-4e0d-8445-9dce3370444d)
![Imagem do WhatsApp de 2025-03-19 à(s) 06 19 14_6c3e04ef](https://github.com/user-attachments/assets/553e5d62-91e8-428d-b61e-2ecf94811547)
![Imagem do WhatsApp de 2025-03-19 à(s) 06 19 32_a97fae8e](https://github.com/user-attachments/assets/8a58ba0b-555f-4fe2-8878-456f17601dac)



### Próximos Passos

- Implementar models com SQLAlchemy
- Criar rotas para cada entidade
- Adicionar validações de dados
- Implementar testes unitários e de integração

## Pré-requisitos

- Python 3.x
- PostgreSQL instalado e configurado
- Biblioteca psycopg2 para Python

## Configuração do Banco de Dados

Antes de executar o script, certifique-se que:
- O PostgreSQL está instalado e em execução.
- Você possui um banco de dados chamado hospital.
- As credenciais de acesso (usuário: postgres, senha: postgres, host: localhost, porta: 5432) estejam corretas. Caso necessário, ajuste esses valores no arquivo db.py.

## Executando o Script

Para criar as tabelas no banco de dados, basta executar o script:

bash
uvicorn main:app --reload


Se a conexão for realizada com sucesso, as tabelas serão criadas e uma mensagem de confirmação será exibida no terminal.




## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
