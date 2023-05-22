import csv
# Nossa fábrica de software ficou especializada em trabalhar com arquivos. Desta maneira, nos foi enviado um arquivo
# CSV para leitura e verificação de um dado. Os clientes desejam saber qual o filme com maior público no ano de exibição.

with open('filmes.csv', 'r', encoding='utf-8') as file:
    publico = {
        2019: 0,
        2018: 0,
        2017: 0,
        2016: 0,
        2015: 0,
        2014: 0,
        2013: 0,
        2012: 0,
        2011: 0,
        2010: 0,
        2009: 0,
    }
    filmes = {
        2019: '',
        2018: '',
        2017: '',
        2016: '',
        2015: '',
        2014: '',
        2013: '',
        2012: '',
        2011: '',
        2010: '',
        2009: '',
    }
    reader = csv.reader(file, delimiter=',')
    for i, linha in enumerate(reader):
        if i == 0:
            pass
        else:
            ano_exibicao = int(linha[1])
            titulo_filme = linha[2]
            qtd_exibicao = float(linha[8])
            # print(f'Ano {ano_exibicao} filme {titulo_filme} público {qtd_exibicao}')

            if ano_exibicao == 2019:
                if qtd_exibicao > publico[2019]:
                    publico[2019] = qtd_exibicao
                    filmes[2019] = titulo_filme
                else:
                    pass

            if ano_exibicao == 2018:
                if qtd_exibicao > publico[2018]:
                    publico[2018] = qtd_exibicao
                    filmes[2018] = titulo_filme
                else:
                    pass

            if ano_exibicao == 2017:
                if qtd_exibicao > publico[2017]:
                    publico[2017] = qtd_exibicao
                    filmes[2017] = titulo_filme
                else:
                    pass

            if ano_exibicao == 2016:
                if qtd_exibicao > publico[2016]:
                    publico[2016] = qtd_exibicao
                    filmes[2016] = titulo_filme
                else:
                    pass

            if ano_exibicao == 2015:
                if qtd_exibicao > publico[2015]:
                    publico[2015] = qtd_exibicao
                    filmes[2015] = titulo_filme
                else:
                    pass

            if ano_exibicao == 2014:
                if qtd_exibicao > publico[2014]:
                    publico[2014] = qtd_exibicao
                    filmes[2014] = titulo_filme
                else:
                    pass

            if ano_exibicao == 2013:
                if qtd_exibicao > publico[2013]:
                    publico[2013] = qtd_exibicao
                    filmes[2013] = titulo_filme
                else:
                    pass

            if ano_exibicao == 2012:
                if qtd_exibicao > publico[2012]:
                    publico[2012] = qtd_exibicao
                    filmes[2012] = titulo_filme
                else:
                    pass

            if ano_exibicao == 2011:
                if qtd_exibicao > publico[2011]:
                    publico[2011] = qtd_exibicao
                    filmes[2011] = titulo_filme
                else:
                    pass

            if ano_exibicao == 2010:
                if qtd_exibicao > publico[2010]:
                    publico[2010] = qtd_exibicao
                    filmes[2010] = titulo_filme
                else:
                    pass

            if ano_exibicao == 2009:
                if qtd_exibicao > publico[2009]:
                    publico[2009] = qtd_exibicao
                    filmes[2009] = titulo_filme
                else:
                    pass

    print('\nResumo:')
    print(f'Em 2019 o filme {filmes[2019]} teve {publico[2019]} exibições.')
    print(f'Em 2018 o filme {filmes[2018]} teve {publico[2018]} exibições.')
    print(f'Em 2017 o filme {filmes[2017]} teve {publico[2017]} exibições.')
    print(f'Em 2016 o filme {filmes[2016]} teve {publico[2016]} exibições.')
    print(f'Em 2015 o filme {filmes[2015]} teve {publico[2015]} exibições.')
    print(f'Em 2014 o filme {filmes[2014]} teve {publico[2014]} exibições.')
    print(f'Em 2013 o filme {filmes[2013]} teve {publico[2013]} exibições.')
    print(f'Em 2012 o filme {filmes[2012]} teve {publico[2012]} exibições.')
    print(f'Em 2011 o filme {filmes[2011]} teve {publico[2011]} exibições.')
    print(f'Em 2010 o filme {filmes[2010]} teve {publico[2010]} exibições.')
    print(f'Em 2009 o filme {filmes[2009]} teve {publico[2009]} exibições.')
