# Projeto Web e Mobile em Django e Kivy
Este projeto consiste em um sistema web e um aplicativo mobile, ambos compartilhando a mesma API desenvolvida em Django. O objetivo deste projeto é demonstrar algumas habilidades em Django e Kivy, bem como mostrar a capacidade de desenvolver uma aplicação que possa ser adaptada para produção.

## Instalação
Antes de iniciar a instalação do projeto, certifique-se de ter o Python e o pip instalados em sua máquina. Além disso, é recomendável a criação de um ambiente virtual para isolar as bibliotecas deste projeto das bibliotecas globais.

1 - Clone este repositório em sua máquina:

``` git clone https://github.com/Luksmito/SistemaDeAgendamento```

Acesse o diretório raiz do projeto:

```cd SistemaDeAgendamento```

Instale as dependências do projeto:

```pip install -r requirement.txt```

##Uso
Após a instalação das dependências, você pode executar o sistema web e o aplicativo mobile seguindo as instruções abaixo.

### Sistema Web
Acesse o diretório webapp:

```cd webapp```

Execute as migrações do banco de dados:

```python manage.py migrate```

Inicie o servidor de desenvolvimento:

```python manage.py runserver```

Acesse o endereço http://localhost:8000 em seu navegador para visualizar a aplicação.

### Aplicativo Mobile

Acesse o diretório mobileapp:

```cd mobileapp```

Execute o aplicativo em um emulador ou dispositivo físico:

```python main.py```

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Se você deseja corrigir um bug, implementar uma nova funcionalidade ou melhorar a documentação, siga os passos abaixo:

Faça um fork deste repositório.

Crie um novo branch com suas modificações:


```git checkout -b minha-modificacao```

Faça o commit das suas modificações:

```git commit -am "Minha modificação"```

Faça o push para o seu fork:

```git push origin minha-modificacao```

Crie um novo pull request para este repositório.
## Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
