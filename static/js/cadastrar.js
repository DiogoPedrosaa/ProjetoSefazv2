$(document).ready(function () {


    // Função para verificar se os campos obrigatórios estão preenchidos
    function validarFormulario() {
      var nome = $('#id_nome').val();
      var matricula = $('#id_matricula').val();
    
      // Verifica se os campos obrigatórios estão preenchidos
      if (nome.trim() === '' || matricula.trim() === '') {
        alert('Por favor, preencha todos os campos obrigatórios.');
        return false;  // Impede o envio do formulário
      }
    
      return true;  // Permite o envio do formulário se os campos estiverem preenchidos
    }
    
    $('#formularioCadastro').submit(function () {
      // Chama a função de validação antes de enviar o formulário
      return validarFormulario();
    })
    });
      $(document).ready(function () {
    
        $('#id_nome').on('input', function () {
          var inputNome = $(this).val().toLowerCase();
    
         
          if (inputNome.trim() === '') {
            
            $('#sugestoes-container').hide();
            return;
          }
    
         
          $.ajax({
            url: '/api/api-pessoas/',  
            success: function (nomes) {
              var sugestoes = nomes.filter(function (pessoa) {
                return pessoa.nome.toLowerCase().includes(inputNome);
              });
    
             
              var sugestoesContainer = $('#sugestoes-container');
              sugestoesContainer.empty();
    
              if (sugestoes.length > 0) {
                sugestoesContainer.show();
              } else {
                sugestoesContainer.hide(); 
              }
    
              sugestoes.forEach(function (pessoa) {
                var sugestaoDiv = $('<div class="sugestao-nome">' + pessoa.nome + '</div>');
                sugestaoDiv.click(function () {
    
                  $('#id_nome').val(pessoa.nome);
           
                  $('#id_matricula').val(pessoa.pessoa_mat);
                  
                  sugestoesContainer.empty().hide();
                });
                sugestoesContainer.append(sugestaoDiv);
              });
            }
          });
        });
      });
    
    
      $(document).ready(function () {
        $('select').change(function () {
            calcularTotalPontos();
        });
    
        function calcularTotalPontos() {
            var totalPontos = 0;
    
            // Mapear os campos de escolha para as suas pontuações correspondentes
            var pontuacoes = {
                '30': 30,
                '20': 20,
                '15': 15,
                '10': 10,
                '05': 5,
                '08': 8,
                '04': 4,
                '02': 2,
                
            };
    
            // Iterar sobre os campos de escolha e somar as pontuações
            $('select').each(function () {
                var escolha = $(this).val();
                totalPontos += pontuacoes[escolha] || 0;
            });
    
            // Atualizar o elemento HTML que exibe o total de pontos
            $('#pontos-total').text(totalPontos);
        }
    
        // Chamar a função para calcular os pontos iniciais
        calcularTotalPontos();
    });
    
    