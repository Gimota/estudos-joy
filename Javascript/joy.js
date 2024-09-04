// Capturando os elementos
const titulo = document.getElementById('titulo');
const ul = document.querySelector('ul');
const link = document.querySelector('a');
const listaOrdenada = document.getElementById('lista-ordenada');

// Adicionando conteúdo ao elemento h1
titulo.innerText = "Bem-vindo ao Projeto!";

// Adicionando conteúdo ao elemento a
link.innerText = "Visite ProZ Educação";

// Adicionando itens à lista não ordenada (ul) com innerHTML
ul.innerHTML = `
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
`;

// Adicionando itens à lista ordenada (ol) com links
listaOrdenada.innerHTML = `
    <li><a href="https://google.com">Google</a></li>
    <li><a href="https://youtube.com">YouTube</a></li>
    <li><a href="https://github.com">GitHub</a></li>
`;
