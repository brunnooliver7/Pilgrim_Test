# PilgrimTest

Disponível em https://pilgrim-test.herokuapp.com

## Uso comum
1. Acesse o site https://pilgrim-test.herokuapp.com, onde se encontra a Api Root
2. Acesse a página de contribuidores (contributors) ou de livros (books)
3. Na página de contribuidores, é possível adicionar dados dos contribuidores (por meio do método POST), tais como 'Name', 'Email' e 'Country'. Observação: os campos 'Author', 'Editor' e 'Reviewer' só podem ser adicionados no ambiente de administrador. É possível ainda, acessar os dados de um contribuidor específico por meio da forma '/contributors/id', sendo poossível acionar as ações de DELETE, PUT e GET.
4. Na página de livros, é possível adicionar dados dos livros (por meio do método POST), tais como "Title", "Language" e "Contributor". É possível ainda, acessar os dados de um livro específico por meio da forma ''/books/id', sendo possível acionar as ações de DELETE, PUT e GET.

## Uso do administrador
1. Acesse https://pilgrim-test.herokuapp.com/admin
2. Acesse o ambiente de administrador com o login 'usuario' e a senha 'senha123'.
3. Gerencie os usuários existentes, assim como suas permissões no campo 'AUTHENTICATION AND AUTHORIZATION'
4. Adicione dados de livros em 'Books'.
5. Adicione dados de contribuidores em 'Contributors'.
