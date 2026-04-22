## Alterações e Correções Implementadas

### (`festival/urls.py`)
* **O que mudei:** Adicionei a rota dias/ que faltava para o menu funcionar.

### (`festival/views.py`)
* **O que mudei:** Importei os modelos todos, criei a função palcos_view e corrigi a query incompleta na concerto_view.

### (Interface Visual)

* **`festival/templates/festival/palcos.html`**
  * **O que mudei:** O link href="" estava vazio. Preenchi com o url correto do concerto.

* **`festival/templates/festival/dias.html`**
  * **O que mudei:** Este ficheiro não existia no meu projeto. Criei-o
* **`festival/templates/festival/concerto.html`**
  * **O que mudei:** Adicionei links no Dia e no Palco para voltar às páginas anteriores.