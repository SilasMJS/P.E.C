#entrada de dados usuário informara o dado nesse caso o volume atual e o que deseja 
vol_atual=int(input("Digite o Volume Atual: "))
vol_desejado=int(input("Digite o Volume que Deseja: "))
#Processamento de dados com base nas informações passada  
difer=vol_desejado-vol_atual
#Saída de dados programa exibira a diferença que falta pra alcançar o volume desejado
print("A Diferença de Volume é ",difer)
