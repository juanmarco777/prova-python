mensagem = str(input("msg: "))
  
  
conversion_code = { 
    
#orig = "abcdefghijklmnopqrstuvwxyz"
#dest = "nvxkrgpszdeailyuhfbocqjmwt"
    
    'a': 'n', 'b': 'v', 'c': 'x', 'd': 'k', 'e': 'r', 'f': 'g', 
    'g': 'p', 'h': 's', 'i': 'z', 'j': 'd', 'k': 'e', 'l': 'a', 
    'm': 'i', 'n': 'l', 'o': 'y', 'p': 'u', 'q': 'h', 'r': 'f', 
    's': 'b', 't': 'o', 'u': 'c', 'v': 'q', 'w': 'j', 'x': 'm', 
    'y': 'w', 'z': 't'
} 
converted_data = "" 
  
  
for i in range(0, len(mensagem)): 
    if mensagem[i] in conversion_code.keys(): 
        converted_data += conversion_code[mensagem[i]] 
    else: 
        converted_data += mensagem[i] 
print(converted_data) 
