## Filtro
Adicionei uma classe CSS chamada book-section às seções de livros para identificá-las facilmente com JavaScript.

Adicionei um campo de busca no HTML, dentro de uma div com a classe search-container. Esse campo de busca permite ao usuário digitar o texto para filtrar as seções.

Adicionei um evento onkeyup ao campo de busca, que chama a função filterSections() toda vez que uma tecla for pressionada e solta. Dessa forma, a função de filtragem será acionada em tempo real enquanto o usuário digita.

A função filterSections() recebe o valor digitado no campo de busca como parâmetro (searchValue).

Usei o método querySelectorAll() para selecionar todas as seções de livros com a classe .book-section e armazená-las em uma variável chamada sections.

Usei o método forEach() para percorrer cada seção de livro.

Para cada seção, obtive o texto do título do livro (h2) usando querySelector("h2").textContent e armazenei-o na variável title.

Comparei o texto do título do livro com o valor de busca (convertidos ambos para minúsculas usando toLowerCase()) usando o método includes(). Se o valor de busca estiver contido no título, defini o estilo de exibição da seção como "block" (para mostrar a seção). Caso contrário, defini o estilo de exibição como "none" (para ocultar a seção).

Assim, as seções serão exibidas ou ocultadas de acordo com o valor digitado no campo de busca.

Essas modificações permitem que o usuário filtre as seções de acordo com o título do livro em tempo real, à medida que digita no campo de busca.