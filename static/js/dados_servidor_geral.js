function filterServidores() {
  var input, filter, table, tr, td_nome, i, txtValue_nome;
  input = document.getElementById("searchInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("tabelaServidores"); 
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    td_nome = tr[i].getElementsByTagName("td")[0]; 

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

    document.body.classList.toggle('dark-mode');
  }

  function filterMatricula() {
  var inputMatricula, filterMatricula, table, tr, tdMatricula, i, txtValueMatricula;
  inputMatricula = document.getElementById("matriculaInput");
  filterMatricula = inputMatricula.value.toUpperCase();
  table = document.getElementById("tabelaServidores");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    tdMatricula = tr[i].getElementsByTagName("td")[2]; 

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

function updateDateTime() {
          var currentDate = new Date();
          var formattedDate = currentDate.toLocaleDateString();
          


          document.getElementById("datetime").textContent = "" + formattedDate
      }

      
      function toggleFilters() {
      var filtroContainer = document.getElementById("filtroContainer");
      filtroContainer.style.display = (filtroContainer.style.display === "none" || filtroContainer.style.display === "") ? "block" : "none";
    }