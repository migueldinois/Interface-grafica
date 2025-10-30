# Projeto 31: Log de Manutenção de Veículo

## Descrição

Este projeto tem como objetivo criar um sistema para controle de manutenção de veículos, permitindo o cadastro dos veículos e o registro de todos os serviços realizados em cada um. A proposta inclui a organização das informações em duas tabelas interligadas: uma para veículos e outra para os serviços associados a cada veículo.

---

## Funcionalidades obrigatórias

- **Cadastro de veículos**
  - Informar marca, modelo, ano e matrícula/placa.
  - Permitir incluir, editar e remover veículos.

- **Listagem de veículos**
  - Exibir todos os veículos em uma tabela ou lista.

- **Cadastro de serviços**
  - Associar serviços a um veículo específico.
  - Registrar tipo do serviço (exemplo: troca de óleo, revisão), data e quilometragem.

- **Histórico de serviços**
  - Exibir apenas os serviços do veículo selecionado, em uma segunda tabela.
  - Permitir incluir, editar e remover serviços.

---

## Estrutura sugerida

- **Tabela 1 (Veículos):**
  - Marca
  - Modelo
  - Ano
  - Matrícula/Placa

- **Tabela 2 (Serviços):**
  - Tipo de serviço
  - Data
  - Quilometragem
  - ID do veículo (para vincular o serviço ao veículo)

---

## Fluxo de uso

1. Cadastro dos veículos pelo usuário.
2. Seleção de um veículo na primeira tabela.
3. Exibição automática do histórico de serviços desse veículo na segunda tabela.
4. Cadastro, edição e exclusão de serviços diretamente vinculados ao veículo selecionado.

---

## Requisitos técnicos

- Interface com duas tabelas (veículos e serviços).
- Funcionalidades de CRUD para veículos e para serviços.
- Relacionamento correto entre veículos e seus respectivos serviços.
- Fácil navegação e visualização dos dados.

---

## Observações

- O sistema pode ser implementado com a tecnologia de sua preferência (ex: Python com Tkinter, JavaScript com Electron, etc).
- O foco está na lógica de relacionamento entre veículos e serviços e na experiência do usuário.
- Documente como instalar e utilizar o sistema, caso necessário.

---

Projeto educacional para prática de lógica, CRUD e interface gráfica.