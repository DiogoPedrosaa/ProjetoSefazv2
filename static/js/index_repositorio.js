document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("searchButton").addEventListener("click", function() {
        // Obtenha o valor do campo de entrada de pesquisa
        var searchTerm = document.getElementById("searchInput").value.toLowerCase();
    
        // Selecione todos os links
        var links = document.querySelectorAll(".link a");
    
        // Itere sobre cada link
        links.forEach(function(link) {
            // Verifique se o texto do link contém o termo de pesquisa
            var linkText = link.textContent.toLowerCase();
            if (linkText.includes(searchTerm)) {
                // Se o termo de pesquisa estiver presente no texto do link, exiba o link
                link.parentElement.style.display = "block";
            } else {
                // Caso contrário, oculte o link
                link.parentElement.style.display = "none";
            }
        });
    });
});