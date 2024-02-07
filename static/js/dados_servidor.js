function filterServidores() {
    var input, filter, table, tr, td_nome, i, txtValue_nome;
    input = document.getElementById("searchInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("tabelaServidores"); // Seleciona a tabela de servidores
    tr = table.getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
      td_nome = tr[i].getElementsByTagName("td")[0]; // Assume que o nome do servidor está na primeira coluna

      if (td_nome) {
        txtValue_nome = td_nome.textContent || td_nome.innerText;

        if (txtValue_nome.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }

    function toggleDarkMode() {
      // Adiciona ou remove a classe 'dark-mode' do corpo da página
      document.body.classList.toggle('dark-mode');
    }


    function filterData() {
    var inputDate, filterDate, table, tr, tdDate, i, txtValueDate;
    inputDate = document.getElementById("dateInput");
    filterDate = inputDate.value;
    table = document.getElementById("tabelaServidores");
    tr = table.getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
        tdDate = tr[i].getElementsByTagName("td")[10]; // Assumindo que a data está na 11ª coluna (índice 10)

        if (tdDate) {
            txtValueDate = tdDate.textContent || tdDate.innerText;

            // Tentar extrair a data usando uma expressão regular
            var match = /(\d{1,2}) de ([a-zA-Z]+) de (\d{4})/.exec(txtValueDate);

            if (match) {
                // Formatar a data para "DD/MM/YYYY"
                var monthNames = [
                    "Janeiro", "Fevereiro", "Março",
                    "Abril", "Maio", "Junho", "Julho",
                    "Agosto", "Setembro", "Outubro",
                    "Novembro", "Dezembro"
                ];

                var monthIndex = monthNames.indexOf(match[2]);
                var formattedDate = match[1].padStart(2, '0') + "/" + (monthIndex + 1).toString().padStart(2, '0') + "/" + match[3];

                // Formatar a data de filtro para o mesmo formato
                var datePartsFilter = filterDate.split("-");
                var formattedFilterDate = datePartsFilter[2] + "/" + datePartsFilter[1] + "/" + datePartsFilter[0];

                if (formattedDate === formattedFilterDate || filterDate === "") {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    }
}




function filterMatricula() {
    var inputMatricula, filterMatricula, table, tr, tdMatricula, i, txtValueMatricula;
    inputMatricula = document.getElementById("matriculaInput");
    filterMatricula = inputMatricula.value.toUpperCase();
    table = document.getElementById("tabelaServidores");
    tr = table.getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
      tdMatricula = tr[i].getElementsByTagName("td")[3]; // Assumindo que a matrícula está na 4ª coluna (índice 3)

      if (tdMatricula) {
        txtValueMatricula = tdMatricula.textContent || tdMatricula.innerText;

        if (txtValueMatricula.toUpperCase().indexOf(filterMatricula) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }


  function toggleFilters() {
        var filtroContainer = document.getElementById("filtroContainer");
        filtroContainer.style.display = (filtroContainer.style.display === "none" || filtroContainer.style.display === "") ? "block" : "none";
      }
