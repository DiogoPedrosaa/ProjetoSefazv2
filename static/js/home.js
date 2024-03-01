var mensagemSucessoForm = $('#mensagem-sucesso-form');

    function configurarSugestaoNomes() {
      $('#id_nome').on('input', function () {
        var inputNome = $(this).val().toLowerCase();
      

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
    }

    function inicializarCalculoPontos() {
      $('#formularioCadastro select').change(function () {
        calcularTotalPontos();
      });
    }

    function calcularTotalPontos() {
      var totalPontos = 0;

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

      $('#formularioCadastro select').each(function () {
        var escolha = $(this).val();
        totalPontos += pontuacoes[escolha] || 0;
      });

      $('#pontos-total').text(totalPontos);
    }

    $(document).ready(function () {
      configurarSugestaoNomes();

      var conteudoAberto = false;
      document.getElementById('btnSistemaLancamento').addEventListener('click', function () {
        if (conteudoAberto) {
          document.getElementById('conteudo').innerHTML = '';
          conteudoAberto = false;
        } else {
          var xhttp = new XMLHttpRequest();
          xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
              document.getElementById('conteudo').innerHTML = this.responseText;
              document.getElementById('conteudo').style.padding = '5px';
              document.getElementById('conteudo').style.fontSize = '14px';
              conteudoAberto = true;
              configurarSugestaoNomes();
              inicializarCalculoPontos();

              var form = document.getElementById('formularioCadastro');
              form.addEventListener('submit', function (event) {
                event.preventDefault();
                var formData = new FormData(form);
                var xhttpForm = new XMLHttpRequest();
                xhttpForm.onreadystatechange = function () {
                  if (this.readyState == 4 && this.status == 200) {
                 
                    mensagemSucessoForm.html('Lançamento Realizado com sucesso!').show();
                    console.log(this.responseText);
                    form.reset();
                    $('#pontos-total').text('0');
                    mensagemSucessoForm.fadeOut(4000);
                  }
                };
                xhttpForm.open('POST', '/cadastrar/', true);
                xhttpForm.send(formData);
              });


              $('#formularioCadastro #limpar-opcoes').click(function () {

                $('#formularioCadastro')[0].reset();


                $('#pontos-total').text('0');
              });
            }
          };
          xhttp.open('GET', 'cadastrar', true);
          xhttp.send();
        }
      });
    });