Este projeto é um (RPA) feito em Python que automatiza o processo de login e cadastro de produtos em um sistema web. A ideia inicial era simples, mas ele evoluiu para se tornar um laboratório completo para aplicar conceitos modernos de DevOps, como containerização e automação segura.

O script lê os dados de um arquivo .csv, navega até a página de login, preenche as credenciais, acessa o formulário de cadastro e insere produto por produto, até o final da lista.

Tecnologias Utilizadas

    Python: A linguagem que dá vida ao projeto.

    Selenium: Para uma automação web robusta e profissional, que interage diretamente com os elementos da página, sem depender de coordenadas de tela.

    Pandas: Para a leitura e manipulação eficiente dos dados do arquivo .csv.

    Docker: Para empacotar toda a aplicação e suas dependências em um container, garantindo que ela rode da mesma forma em qualquer ambiente.

    python-dotenv: Para gerenciar as credenciais de forma segura, sem nunca expor senhas e logins no código-fonte.
    