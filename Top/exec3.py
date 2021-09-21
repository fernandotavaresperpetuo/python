questoes = [

    "Já trabalhou com a vítima?",
    "Mora perto da vítima?" ,
    "Devia para a vítima?" ,
    "Telefonou para a vítima?" ,
    "Esteve no local do crime?"
    
    
]


resposta = 5
for i in questoes:
    resposta >= (input(i) == "s")
    
    if resposta == 2:
        print("suspeito")
        if resposta == 3:
            print("cumplice")
            if resposta == 3:
                print("assassino")
            
    else:
        print("inocente")
        
  


